import c4d, enum

__all__ = [
    "c4d", "Tree", "O", "T", "X", "F", "FL", "CT", "VP", "M", "Doc", "Command", "database", "dump", "Node", "Param", "find_ident"
]

database = {}


class Type(enum.Enum):
    """This is a Fake definition.
    Use pylance to color the node as Enum Member in vscode
    ```
    "editor.semanticTokenColorCustomizations": {
        "enabled": true,
        "rules": {
            "enumMember": "#bae02d",
        }
    }
    ```
    """


from c4djson.nodetype import Type


class Node:
    raws: dict[int, c4d.BaseList2D] = {}

    def __init__(self, type: Type):
        self.type = type
        if type.value not in self.raws:
            self.raws[type.value] = c4d.BaseList2D(type.value)
        self.obj = c4d.BaseList2D(type.value)
        self._raw: c4d.BaseList2D = None
        self.default_name = self.obj.GetName()
        self.parent: Node = None

    def __repr__(self):
        if self.default_name == self.name:
            return str(self.type)
        return f"{self.type} @ '{self.name}'"

    def __matmul__(self, name: str):
        self.name = name
        return self

    @classmethod
    def from_obj(cls, obj: c4d.BaseList2D):
        nodetype: Type = Type.find(obj.GetType())
        if nodetype is None:
            return None
        try:
            node = cls(nodetype)
        except BaseException:
            return None
        node.obj = obj
        return node

    @property
    def name(self):
        if self.obj.IsAlive():
            return self.obj.GetName().replace(" . ", ".")
        else:
            return self.default_name

    @name.setter
    def name(self, name: str):
        self.obj.SetName(name)

    @property
    def link(self):
        return self.type.value, self.name

    @property
    def raw(self):
        return self._raw or self.raws[self.type.value]

    def is_track(self):
        return self.type.value == c4d.CTbase

    def create_special_track(self, parent: c4d.BaseList2D):
        tid = self.type.value
        self.obj = c4d.CTrack(parent, c4d.DescID(tid, tid, 0))
        parent.InsertTrackSorted(self.obj)

    def set_parent(self, parent: "Node"):
        self.parent = parent
        if isinstance(self.obj, c4d.BaseObject) and isinstance(parent.obj, c4d.BaseObject):
            self.obj.InsertUnderLast(parent.obj)
        if isinstance(self.obj, c4d.BaseTag) and isinstance(parent.obj, c4d.BaseObject):
            parent.obj.InsertTag(self.obj, pred=parent.obj.GetLastTag())
        if isinstance(self.obj, c4d.BaseShader) and isinstance(parent.obj, c4d.BaseList2D):
            parent.obj.InsertShader(self.obj)
        if isinstance(self.obj, c4d.CTrack) and isinstance(parent.obj, c4d.BaseList2D):
            if self.type.value != c4d.CTbase:
                self.create_special_track(parent.obj)
        if isinstance(self.obj, c4d.modules.mograph.FieldLayer):
            # if isinstance(parent.obj, c4d.modules.mograph.FieldLayer):
            if isinstance(parent.obj, c4d.BaseList2D):
                self.obj.InsertUnderLast(parent.obj)


class Param:
    def __init__(self, descid: c4d.DescID, node: Node):
        self.descid = descid
        self.node = node

    def __repr__(self):
        return str(self.ident or self.name or self.descid)

    def __str__(self):
        return str(self.name or self.ident or self.descid)

    def __getitem__(self, key: int):
        return self.bc[key]

    @property
    def description(self):
        try:
            return self.node.obj.GetDescription(c4d.DESCFLAGS_DESC_0)
        except ReferenceError:
            obj = c4d.BaseList2D(self.node.type.value)
            return obj.GetDescription(c4d.DESCFLAGS_DESC_0)

    @property
    def bc(self):
        return self.description.GetParameter(self.descid)

    @property
    def name(self):
        name = self.bc[c4d.DESC_NAME] or self.bc[c4d.DESC_SHORT_NAME] or ""
        return str(name).replace(" . ", ".")

    @property
    def ident(self):
        if self.descid.GetDepth() == 2:
            descid = c4d.DescID(self.descid[0])
            bc = self.description.GetParameter(descid)
            ident = self.bc[c4d.DESC_IDENT]
            ident = f"c4d.{ident}" if ident else self.descid[1].id
            return f"(c4d.{bc[c4d.DESC_IDENT]}, {ident})"
        ident = self.bc[c4d.DESC_IDENT]
        return f"c4d.{ident}" if ident else ""


class CycleVal:
    def __init__(self, param: Param, value):
        self.param, self.value = param, value

    def __str__(self):
        name = self.param[c4d.DESC_CYCLE][self.value]
        return f"{name}" if name else self.value

    def __repr__(self):
        if self.param[c4d.DESC_CYCLESYMBOLS] is not None:
            ident = self.param[c4d.DESC_CYCLESYMBOLS][self.value]
            return f"c4d.{ident}" if ident else str(self.value)
        else:
            return str(self.value)


class Userdata(Param):
    def __init__(self, name: str, dtype: int, node: Node):
        bc = c4d.GetCustomDataTypeDefault(dtype)
        bc[c4d.DESC_NAME] = bc[c4d.DESC_SHORT_NAME] = name
        descid = node.obj.AddUserData(bc)
        super().__init__(descid, node)

    def __setitem__(self, key, val):
        bc = self.bc.GetClone(c4d.COPYFLAGS_NONE)
        bc[key] = val
        self.node.obj.SetUserDataContainer(self.descid, bc)

    def __repr__(self):
        return repr(super().__str__())


class UserdataDump(Param):
    def __repr__(self):
        return repr(super().__str__())


class UserdataKey:
    cycle_keys = {
        c4d.DESC_UNIT: {"prefix": "DESC_UNIT_"},
        c4d.DESC_CUSTOMGUI: {"prefix": "CUSTOMGUI_"},
    }
    value_keys = [c4d.DESC_MINSLIDER, c4d.DESC_MAXSLIDER, c4d.DESC_STEP, c4d.DESC_DEFAULT]

    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        if self.value == c4d.DTYPE_:
            return "c4d.DTYPE_"
        return find_ident(self.value, "DESC_") or self.value

    def generate(self, val):
        if self.value == c4d.DTYPE_:
            return UserdataVal(val, find_ident(val, "DTYPE_"))
        if self.value in self.cycle_keys:
            prefix = self.cycle_keys[self.value]["prefix"]
            return UserdataVal(val, find_ident(val, prefix))
        return UserdataVal(val)


class UserdataVal:
    def __init__(self, value, ident: str = None):
        self.value, self.ident = value, ident

    def __repr__(self) -> str:
        return self.ident or repr(self.value)


class KeyFrame:
    def __init__(self, value: tuple):
        self.value = value

    def __repr__(self) -> str:
        frame, val = self.value[:2]
        if len(self.value) > 2:
            ident = find_ident(self.value[2], "CINTERPOLATION_")
            return f"({frame}, {val!r}, {ident})"
        return f"({frame}, {val!r})"


class Tree:
    def __init__(self, data: dict = None):
        self.doc = c4d.documents.GetActiveDocument()
        self.objects: dict[tuple[int, str], c4d.BaseList2D] = {}
        self.data = {} if data is None else data
        self.data = self.parse_nodes(self.data)
        self.parse_params(self.data)

    def __getitem__(self, node: Node):
        return self.objects[node.link]

    def parse_nodes(self, data: dict, parent: Node = None):
        result = {}
        for key, val in data.items():
            if isinstance(key, Node):
                node: Node = key
                if parent is not None:
                    node.set_parent(parent)
                self.objects[node.link] = node.obj
                val = self.parse_nodes(val, node)
            elif isinstance(key, int):
                assert parent is not None
                param = Param(c4d.DescID(key), parent)
                key = param
            elif isinstance(key, tuple) and all(type(i) == int for i in key):
                assert parent is not None
                assert 1 < len(key) < 3
                descid = c4d.DescID(*[c4d.DescLevel(i) for i in key])
                param = Param(descid, parent)
                key = param
            if isinstance(key, Param) and type(val) == dict:
                val = self.parse_nodes(val, parent)
            result[key] = val
        return result

    def parse_params(self, data: dict):
        for node in [i for i in data if isinstance(i, Node)]:
            node_data: dict = data[node]
            track: c4d.CTrack = None
            for key, val in node_data.items():
                # Bind track object
                if isinstance(key, Node) and key.is_track() and track:
                    key.obj = track
                    track = None
                if not isinstance(key, Param):
                    continue
                param = key
                # When param is c4d.FIELDS
                if param[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_FIELDLIST:
                    val: dict
                    self.parse_params(val)
                    fieldlist = c4d.FieldList()
                    fieldlayer_nodes = [i for i in val if isinstance(i, Node)]
                    for fieldlayer_node in reversed(fieldlayer_nodes):
                        fieldlist.InsertLayer(fieldlayer_node.obj)
                    val = fieldlist
                # When param is a button
                if param[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_BUTTON:
                    c4d.CallButton(node.obj, param.descid[0].id)
                    continue
                # When param value is [] (means animated)
                if type(val) == list and all(type(i) == tuple for i in val):
                    node_data[param] = [KeyFrame(i) for i in val]
                    track = self.set_track(param, val)
                    continue
                # When param is USERDATA
                if param.descid == c4d.DescID(c4d.ID_USERDATA):
                    node_data[param] = self.parse_userdata(node, val)
                    continue
                if param[c4d.DESC_CYCLE] is not None:
                    node_data[param] = CycleVal(param, val)
                paramkey = tuple(param.descid[i].id for i in range(param.descid.GetDepth()))
                try:
                    node.obj[paramkey] = self.convert_value(param, val)
                except (TypeError, AttributeError) as e:
                    import traceback
                    print(traceback.format_exc(), end="")
                    print("Node:", node)
                    print("Param:", param, param.descid)
                    print("Value:", val)
            self.parse_params(node_data)

    def convert_value(self, param: Param, val):
        if isinstance(val, (list, tuple)):
            if all(isinstance(i, (int, float)) for i in val) and 1 <= len(val) <= 3:
                val = c4d.Vector(*val)
        if param[c4d.DESC_UNIT] == c4d.DESC_UNIT_DEGREE:
            if isinstance(val, c4d.Vector):
                x, y, z = map(c4d.utils.DegToRad, (val.x, val.y, val.z))
                val = c4d.Vector(x, y, z)
            elif isinstance(val, (int, float)):
                val = c4d.utils.DegToRad(val)
        if param[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_TIME:
            fps = self.doc.GetFps()
            if isinstance(val, c4d.Vector):
                x, y, z = map(c4d.BaseTime, (val.x, val.y, val.z), (fps, fps, fps))
                val = c4d.Vector(x, y, z)
            elif isinstance(val, (int, float)):
                val = c4d.BaseTime(val, fps)
        if param[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_COLOR:
            x, y, z = map(lambda i: i / 255, (val.x, val.y, val.z))
            val = c4d.Vector(x, y, z)
        if isinstance(val, Node):
            val = self.objects[val.link]
        if isinstance(val, (tuple, list)) and all(isinstance(i, Node) for i in val):
            container = c4d.InExcludeData()
            item: Node
            for item in val:
                container.InsertObject(self.objects[item.link], 7)
            val = container
        return val

    def parse_params_post(self, data: dict):
        """Once inserted to doc, change it's description by send message to c4d"""
        for node in [i for i in data if isinstance(i, Node)]:
            node_data: dict = data[node]
            for param in [i for i in node_data if isinstance(i, Param)]:
                val = node_data[param]
                if not param.name:
                    node.obj.Message(c4d.MSG_CHANGE)  # Update the description
                    if param[c4d.DESC_CYCLE] and type(val) == int:
                        node_data[param] = CycleVal(param, val)
            self.parse_params_post(node_data)

    def parse_userdata(self, node: Node, data: dict[str, dict], parent=c4d.DescID(0)):
        result = {}
        for uname, udata in data.items():
            dtype = udata.get(c4d.DTYPE_, c4d.DTYPE_GROUP)
            userdata = Userdata(uname, dtype, node)
            userdata[c4d.DESC_PARENTGROUP] = parent
            if dtype == c4d.DTYPE_GROUP:
                userdata[c4d.DESC_TITLEBAR] = True
                result[userdata] = self.parse_userdata(node, udata, userdata.descid)
                continue
            result[userdata] = {}
            for key, val in udata.items():
                userdata_key = UserdataKey(key)
                result[userdata][userdata_key] = userdata_key.generate(val)
                if key == c4d.DTYPE_:
                    continue
                if key in UserdataKey.value_keys:
                    val = self.convert_value(userdata, val)
                if key == c4d.DESC_CYCLE:
                    val = dict2bc(val)
                userdata[key] = val
            if userdata[c4d.DESC_DEFAULT] is not None:
                node.obj[userdata.descid] = userdata[c4d.DESC_DEFAULT]
        return result

    def set_track(self, param: Param, val: list[tuple]):
        track = c4d.CTrack(param.node.obj, param.descid)
        curve = track.GetCurve()
        track_cate = track.GetTrackCategory()
        fps = self.doc.GetFps()

        def addKeyframe(frame: int, value, interpolation=c4d.CINTERPOLATION_SPLINE):
            keyDict = curve.AddKey(c4d.BaseTime(frame, fps))
            key: c4d.CKey = keyDict["key"]
            keyIndex = keyDict["nidx"]
            value = self.convert_value(param, value)
            if track_cate == c4d.CTRACK_CATEGORY_DATA:
                key.SetGeData(curve, value)
            else:
                key.SetValue(curve, value)
            curve.SetKeyDefault(self.doc, keyIndex)
            key.SetInterpolation(curve, interpolation)

        for keyframe in val:
            addKeyframe(*keyframe)
        param.node.obj.InsertTrackSorted(track)
        param.node.obj[param.descid] = self.convert_value(param, val[0][1])
        return track

    def load(self, replace=True):
        self.doc.StartUndo()
        for node in reversed([i for i in self.data if isinstance(i, Node)]):
            if isinstance(node.obj, c4d.BaseObject):
                if replace:
                    for old in self.doc.GetObjects():
                        if old.GetName() == node.name and old.GetType() == node.type.value:
                            old.Remove()
                self.doc.InsertObject(node.obj)
                self.doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, node.obj)
            if isinstance(node.obj, c4d.BaseMaterial):
                if replace:
                    old = self.doc.SearchMaterial(node.name)
                    if old is not None and old.GetType() == node.type.value:
                        old.Remove()
                # When there's no mat in mat manager, the insert operation may lose it's name
                name = node.name
                self.doc.InsertMaterial(node.obj)
                node.name = name  # Restore it's name
                self.doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, node.obj)
        self.doc.EndUndo()
        c4d.EventAdd()
        self.parse_params_post(self.data)
        return self

    def print(self, indent=2, ident=False):
        print(dict2str(self.data, indent=indent, ident=ident))
        return self

##############   Tree End    ###############

############## DocTree Start ###############


#  DataTag in Cloner, VariableTag in Particle Emitter
_tids_not_to_parse = [
    c4d.ID_MOTAGDATA, c4d.Tparticle, c4d.Tcacheproxytagpolyselection, c4d.Tcacheproxytagedgeselection,
    c4d.Tpoint, c4d.Tpolygon, c4d.Ttangent
]


def _descid_d1(*args):
    return c4d.DescID(c4d.DescLevel(*args))


_black_list = [
    _descid_d1(900, 130, 110050),                 # c4d.ID_BASELIST_NAME,
    _descid_d1(1041671, 3, 110050),               # c4d.ID_BASELIST_ICON_COLOR,
    _descid_d1(910, 23, 5155),                    # c4d.ID_BASEOBJECT_GLOBAL_POSITION,
    _descid_d1(925, 23, 5155),                    # c4d.ID_BASEOBJECT_ABS_POSITION,
    _descid_d1(911, 23, 5155),                    # c4d.ID_BASEOBJECT_GLOBAL_ROTATION,
    _descid_d1(926, 23, 5155),                    # c4d.ID_BASEOBJECT_ABS_ROTATION,
    _descid_d1(1204, 19, 1000988),                # c4d.PRIM_REGULARWIDTH,
    _descid_d1(901, 3, 5350),                     # c4d.ID_CTRACK_FCURVE_COLOR
    _descid_d1(200000029, 200000027, 1001074),    # c4d.ID_MATERIALASSIGNMENTS,
    _descid_d1(1204, 400006001, 431000028),       # c4d.O_BEVELL_SHAPING_CONSTANT,
    _descid_d1(440000308, 400006001, 440000249),  # c4d.ID_FIELDLAYER_ENABLE_DIRECTION,
]
_white_list = [  # No matter whether the param is same as it's default, dump it.
    _descid_d1(1204, 15, 1018583),              # c4d.MG_GRID_MODE,
]
_dynamic_defaults = [
    (_descid_d1(1016, 400006001, 1018740), 1),  # c4d.MG_OBJECT_ALIGN
]


def check_dynamic_default(descid: c4d.DescID, node: Node):
    for id, val in _dynamic_defaults:
        if descid == id and node.obj[descid] == val:
            return True
    return False


class DocTree:
    def __init__(self) -> None:
        self.doc = c4d.documents.GetActiveDocument()
        data = {}
        objects = self.doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE)  # | c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER
        materials = self.doc.GetActiveMaterials()
        for obj in objects:
            data |= self.parse_node(obj)
        for mat in materials:
            data |= self.parse_material(mat)
        data = collapse_branches(data)
        self.data = data

    def parse_node(self, obj: c4d.BaseList2D):
        if obj.GetType() in _tids_not_to_parse:
            return {}
        node = Node.from_obj(obj)
        if node is None:
            return {}
        data = {node: self.parse_params(node)}
        data[node] |= self.parse_userdata(node)
        if node.type.value == c4d.CTbase:
            data = self.parse_track(node) | data
            if not data[node]:  # if a track node has no param to set, delete it
                data.pop(node)
                return data
        branches = obj.GetBranchInfo(c4d.GETBRANCHINFO_ONLYWITHCHILDREN) or []
        for branchdata in branches:
            gelisthead: c4d.GeListHead = branchdata.get("head")
            branchid: int = branchdata.get("id")
            branchname: str = branchdata.get("name", f"Branch:{branchid}")
            child = gelisthead.GetDown()
            if child is None:
                continue
            data[node][branchname] = {}
            while child is not None:
                # if isinstance(child, c4d.BaseTag):  # reverse the sequence for tags
                #     data[node][branchname] = self.parse_node(child) | data[node][branchname]
                # else:
                #     data[node][branchname] |= self.parse_node(child)
                data[node][branchname] |= self.parse_node(child)
                child = child.GetNext()
            if len(data[node][branchname]) == 0:
                data[node].pop(branchname, None)
        if isinstance(obj, (c4d.BaseObject, c4d.BaseShader)):
            for child in obj.GetChildren():
                data[node] |= self.parse_node(child)
        return data

    def parse_material(self, mat: c4d.BaseMaterial):
        return self.parse_node(mat)

    def parse_params(self, node: Node):
        data = {}
        if node.type.value == 1018544:  # c4d.Omgcloner
            if node.obj[c4d.ID_MG_MOTIONGENERATOR_MODE] == c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT:
                param = Param(c4d.DescID(c4d.ID_MG_MOTIONGENERATOR_MODE), node)
                data[param] = CycleVal(param, c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT)
                node._raw = c4d.BaseObject(1018544)
                node._raw[c4d.ID_MG_MOTIONGENERATOR_MODE] = c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT
                obj = node.obj[c4d.MG_OBJECT_LINK]
                param = Param(c4d.DescID(c4d.MG_OBJECT_LINK), node)
                data[param] = Node.from_obj(obj) if obj else None
                node._raw[c4d.MG_OBJECT_LINK] = obj
                node._raw.Message(c4d.MSG_CHANGE)
        bc: c4d.BaseContainer
        descid: c4d.DescID
        for bc, descid, _ in node.obj.GetDescription(c4d.DESCFLAGS_DESC_NONE):
            if descid.GetDepth() == 0:
                continue
            # if descid[0].id == c4d.ID_FIELDLAYER_ENABLE_DIRECTION:
            #     print(bc[c4d.DESC_NAME], descid)
            if any(descid == id for id in _black_list):
                continue
            if not any(descid == id for id in _white_list):
                try:
                    if node.obj[descid] == node.raw[descid]:
                        continue
                except AttributeError:
                    continue
            # if check_dynamic_default(descid, node):
            #     continue
            param = Param(descid, node)
            if not param.ident:
                continue
            val = self.convert_value(param, node.obj[descid])
            val = self.parse_prs(param, val)
            if param[c4d.DESC_CYCLE] is not None:
                val = CycleVal(param, val)
            if val is not None:
                data[param] = val
        return data

    def convert_value(self, param: Param, val):
        doc = self.doc
        if param[c4d.DESC_UNIT] == c4d.DESC_UNIT_DEGREE:
            if isinstance(val, c4d.Vector):
                x, y, z = map(c4d.utils.RadToDeg, (val.x, val.y, val.z))
                val = x, y, z
            elif isinstance(val, (int, float)):
                val = c4d.utils.RadToDeg(val)
        if isinstance(val, c4d.BaseTime):
            val = val.GetFrame(doc.GetFps())
        if param[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_COLOR:
            assert isinstance(val, c4d.Vector)
            x, y, z = map(lambda i: round(i * 255), (val.x, val.y, val.z))
            val = x, y, z
        if param[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_BOOL:
            val = bool(val)
        if isinstance(val, c4d.Vector):
            x, y, z = map(lambda i: round(i) if round(i) == i else i, (val.x, val.y, val.z))
            val = x, y, z
        if isinstance(val, c4d.BaseList2D):
            val = Node.from_obj(val) or val
        if isinstance(val, c4d.FontData):
            bc = val.GetFont()
            val = {k: v for k, v in bc} or None
            if val is not None:
                val = {"CustomDataType": "FontData"} | val
        if isinstance(val, c4d.SplineData):
            val = None
        if isinstance(val, c4d.BitmapButtonStruct):
            val = None
        if isinstance(val, c4d.PriorityData):
            val = None
        if isinstance(val, c4d.InExcludeData):
            container = val
            val = []
            for i in range(container.GetObjectCount()):
                obj = container.ObjectFromIndex(doc, i)
                val.append(Node.from_obj(obj) or obj)
            val = val or None
        if isinstance(val, c4d.Gradient):
            val = None
        if isinstance(val, c4d.FieldList):
            fieldlist = val
            val = fieldlist if fieldlist.HasContent() else None
            if val is not None:
                result = {}
                child = fieldlist.GetLayersRoot().GetDown()
                while child is not None:
                    result |= self.parse_node(child)
                    child = child.GetNext()
                val = result
        if isinstance(val, tuple) and all(isinstance(i, (int, float)) for i in val):
            if param[c4d.DESC_UNIT] == c4d.DESC_UNIT_REAL:
                if param[c4d.DESC_STEP] == c4d.Vector(1, 1, 1):
                    val = tuple(round(i) for i in val)
            if val.count(val[0]) == len(val):
                val = (val[0],)
            val = tuple(round(i) if abs(i - round(i)) < 1e-14 else i for i in val)
        if isinstance(val, float) and abs(val - round(val)) < 1e-14:
            val = round(val)
        return val

    def parse_prs(self, param: Param, val: tuple):
        if param.descid[0].id in [
            c4d.ID_BASEOBJECT_REL_POSITION, c4d.ID_BASEOBJECT_REL_POSITION, c4d.ID_BASEOBJECT_REL_POSITION
        ]:
            if val.count(0) == 2:
                for i, v in enumerate(val):
                    if v != 0:
                        desclevel = c4d.DescLevel([c4d.VECTOR_X, c4d.VECTOR_Y, c4d.VECTOR_Z][i])
                        param.descid.PushId(desclevel)
                        return v
        return val

    def parse_track(self, node: Node):
        doc = self.doc
        fps = doc.GetFps()
        track: c4d.CTrack = node.obj
        track_cate = track.GetTrackCategory()
        descid = track.GetDescriptionID()
        host_node = Node.from_obj(track.GetObject())
        assert host_node is not None
        param = Param(descid, host_node)
        val = []
        curve = track.GetCurve()
        for i in range(curve.GetKeyCount()):
            key = curve.GetKey(i)
            frame = key.GetTime().GetFrame(fps)
            value = key.GetGeData() if track_cate == c4d.CTRACK_CATEGORY_DATA else key.GetValue()
            value = self.convert_value(param, value)
            interpolation = key.GetInterpolation()
            if interpolation != c4d.CINTERPOLATION_SPLINE:
                val.append(KeyFrame((frame, value, interpolation)))
            else:
                val.append(KeyFrame((frame, value)))
        return {param: val}

    def parse_userdata(self, node: Node):
        if not node.obj.GetUserDataContainer():
            return {}
        param = Param(c4d.DescID(c4d.ID_USERDATA), node)
        data = {param: {}}
        descid: c4d.DescID
        for descid, bc in node.obj.GetUserDataContainer():
            userdata = UserdataDump(descid, node)
            parent = self.find_parent(data[param], bc[c4d.DESC_PARENTGROUP])
            parent[userdata] = {}
            if descid[1].dtype != c4d.DTYPE_GROUP:
                userdata_key = UserdataKey(c4d.DTYPE_)
                parent[userdata][userdata_key] = userdata_key.generate(descid[1].dtype)
                descid_tem = node.obj.AddUserData(c4d.GetCustomDataTypeDefault(descid[1].dtype))
                bc_tem = node.obj.GetDescription(c4d.DESCFLAGS_DESC_0).GetParameter(descid_tem)
                for key, val in bc:
                    if bc_tem[key] == val:
                        continue
                    if key in [c4d.DESC_NAME, c4d.DESC_PARENTGROUP]:
                        continue
                    if key == c4d.DESC_SHORT_NAME:
                        if val == bc[c4d.DESC_NAME]:
                            continue
                    userdata_key = UserdataKey(key)
                    if key in UserdataKey.value_keys:
                        val = self.convert_value(userdata, val)
                    if key == c4d.DESC_CYCLE:
                        val = bc2dict(val)
                    parent[userdata][userdata_key] = userdata_key.generate(val)
                node.obj.RemoveUserData(descid_tem)
        return data

    def find_parent(self, data: dict[Param, dict], descid: c4d.DescID):
        if descid == c4d.DescID(0):
            return data
        for param, pdata in data.items():
            if param.descid == descid:
                return pdata
            else:
                return self.find_parent(pdata, descid)
        return {}

    def print(self, indent=2, ident=False):
        print(dict2str(self.data, indent=indent, ident=ident))
        return self


def dump(indent=2, ident=True):
    """Dump and print json from doc with selected object(in hierarchy) and selected meterials"""
    tree = DocTree()
    tree.print(indent, ident)

############## DocTree End ###############


def find_ident(value: int, prefix=""):
    for key, val in c4d.__dict__.items():
        if val == value and key.startswith(prefix):
            return f"c4d.{key}"


def dict2str(data: dict, indent=2, depth=0, ident=False):
    newline = any(isinstance(v, (dict, list)) for v in data.values())
    newline = newline or len(data.keys()) > 1
    output = "{\n" if newline else "{"
    for key, val in data.items():
        s = " " * indent * (depth + 1) if newline else " "
        e = ",\n" if newline else " "
        if type(val) == str:
            val = repr(val)
        if isinstance(key, Param):
            if "PYTHON_CODE" in key.ident:
                val = "<PYTHON CODE>"
            if isinstance(val, list) and any(isinstance(i, KeyFrame) for i in val):
                if ident and key.name:
                    output += f"{s}# Animate {key.name}\n"
        if isinstance(val, UserdataVal) and type(val.value) == dict:
            val = dict2str(val.value, indent, depth + 1, ident)
        if type(val) == dict:
            val = dict2str(val, indent, depth + 1, ident)
        if isinstance(val, list):
            val = list2str(val, indent, depth + 1)
        if ident:
            if type(val) != str:
                val = repr(val)
            output += f"{s}{key!r}: {val}{e}"
        else:
            output += f"{s}{key!s}: {val}{e}"
    s = " " * indent * depth if newline else ""
    output += s + "}"
    return output


def list2str(data: list, indent=2, depth=0):
    newline = any(isinstance(v, (tuple, list)) and len(v) > 2 for v in data)
    newline = any(isinstance(v, KeyFrame) and len(v.value) > 2 for v in data)
    newline = newline or len(data) > 3
    output = "[\n" if newline else "[ "
    for i, item in enumerate(data):
        s = " " * indent * (depth + 1) if newline else ""
        e = ",\n" if newline else (", " if i < len(data) - 1 else " ")
        if isinstance(item, tuple):
            item = ", ".join(str(i) for i in item)
            item = f"({item})"
        output += f"{s}{item!s}{e}"
    s = " " * indent * depth if newline else ""
    output += s + "]"
    return output


def dict2bc(data: dict):
    bc = c4d.BaseContainer()
    for key, val in data.items():
        bc[key] = val
    return bc


def bc2dict(bc: c4d.BaseContainer):
    data = {}
    for key, val in bc:
        data[key] = val
    return data


def collapse_branches(data: dict):
    result = {}
    for key, val in data.items():
        if key in ["Tags", "Shaders", "Tracks"] and type(val) == dict:
            result |= collapse_branches(val)
            continue
        if type(val) == dict:
            result[key] = collapse_branches(val)
            continue
        result[key] = val
    return result


class Command:
    def playforward():
        playforward = 12412
        if not c4d.IsCommandChecked(playforward):
            c4d.CallCommand(playforward)

    def unfoldall():
        c4d.CallCommand(100004748)


class O(Type):
    array = c4d.Oarray
    atomarray = c4d.Oatomarray
    attractor = c4d.Oattractor
    background = c4d.Obackground
    base = c4d.Obase
    basedeform = c4d.Obasedeform
    baseeffector = c4d.Obaseeffector
    basemogen = c4d.Obasemogen
    bend = c4d.Obend
    bevel = c4d.Obevel
    bezier = c4d.Obezier
    bodycapture = c4d.Obodycapture
    bone_ex = c4d.Obone_EX
    boole = c4d.Oboole
    bulge = c4d.Obulge
    cacameraspacedeform = c4d.Ocacameraspacedeform
    cacluster = c4d.Ocacluster
    cacollision = c4d.Ocacollision
    cacomponent = c4d.Ocacomponent
    cacorrection = c4d.Ocacorrection
    cajiggle = c4d.Ocajiggle
    camera = c4d.Ocamera
    camesh = c4d.Ocamesh
    camorph = c4d.Ocamorph
    camuscle = c4d.Ocamuscle
    capointcache = c4d.Ocapointcache
    capsule = c4d.Ocapsule
    caskin = c4d.Ocaskin
    casmooth = c4d.Ocasmooth
    casquash = c4d.Ocasquash
    castep = c4d.Ocastep
    casurface = c4d.Ocasurface
    character = c4d.Ocharacter
    cloth = c4d.Ocloth
    cmotion = c4d.Ocmotion
    cone = c4d.Ocone
    connector = c4d.Oconnector
    connectorconstraint = c4d.Oconnectorconstraint
    cube = c4d.Ocube
    cylinder = c4d.Ocylinder
    datacapture = c4d.Odatacapture
    deflector = c4d.Odeflector
    destructor = c4d.Odestructor
    disc = c4d.Odisc
    displacer = c4d.Odisplacer
    doodle = c4d.Odoodle
    environment = c4d.Oenvironment
    explosion = c4d.Oexplosion
    explosionfx = c4d.Oexplosionfx
    extrude = c4d.Oextrude
    facecapture = c4d.Ofacecapture
    falloff = c4d.Ofalloff
    feathers = c4d.Ofeathers
    ffd = c4d.Offd
    field = c4d.Ofield
    fieldremapper = c4d.Fieldremapper
    figure = c4d.Ofigure
    floor = c4d.Ofloor
    force = c4d.Oforce
    foreground = c4d.Oforeground
    formula = c4d.Oformula
    fractal = c4d.Ofractal
    friction = c4d.Ofriction
    fur = c4d.Ofur
    gravitation = c4d.Ogravitation
    guide = c4d.Oguide
    instance = c4d.Oinstance
    joint = c4d.Ojoint
    lathe = c4d.Olathe
    layer = c4d.Olayer
    light = c4d.Olight
    line = c4d.Oline
    lod = c4d.Olod
    loft = c4d.Oloft
    melt = c4d.Omelt
    metaball = c4d.Ometaball
    mgcloner = c4d.Omgcloner
    mgcoffee = c4d.Omgcoffee
    mgdelay = c4d.Omgdelay
    mgeffectortarget = c4d.Omgeffectortarget
    mgextrude = c4d.Omgextrude
    mgformula = c4d.Omgformula
    mgfracture = c4d.Omgfracture
    mginheritance = c4d.Omginheritance
    mginstance = c4d.Omginstance
    mgmatrix = c4d.Omgmatrix
    mgplain = c4d.Omgplain
    mgpolyfx = c4d.Omgpolyfx
    mgpushapart = c4d.Omgpushapart
    mgpython = c4d.Omgpython
    mgrandom = c4d.Omgrandom
    mgreeffector = c4d.Omgreeffector
    mgroup = c4d.Omgroup
    mgshader = c4d.Omgshader
    mgsound = c4d.Omgsound
    mgspline = c4d.Omgspline
    mgsplinemask = c4d.Omgsplinemask
    mgsplinewrap = c4d.Omgsplinewrap
    mgstep = c4d.Omgstep
    mgtext = c4d.Omgtext
    mgtime = c4d.Omgtime
    mgtracer = c4d.Omgtracer
    mgvolume = c4d.Omgvolume
    mgvoronoifracture = c4d.Omgvoronoifracture
    mospline = 440000054
    motionclip = c4d.Omotionclip
    motiontracker = c4d.Omotiontracker
    motor = c4d.Omotor
    null = c4d.Onull
    objecttracker = c4d.Oobjecttracker
    oiltank = c4d.Ooiltank
    particle = c4d.Oparticle
    particlemodifier = c4d.Oparticlemodifier
    pivot = c4d.Opivot
    pivotmanipulator = c4d.Opivotmanipulator
    plane = c4d.Oplane
    planemanipulator = c4d.Oplanemanipulator
    platonic = c4d.Oplatonic
    plugin = c4d.Oplugin
    pluginpolygon = c4d.Opluginpolygon
    point = c4d.Opoint
    polygon = c4d.Opolygon
    polyreduction = c4d.Opolyreduction
    polyreduxgenerator = c4d.Opolyreduxgenerator
    pyramid = c4d.Opyramid
    python = c4d.Opython
    relief = c4d.Orelief
    remesh = c4d.Oremesh
    rotation = c4d.Orotation
    rsbakeset = c4d.Orsbakeset
    rsenvironment = c4d.Orsenvironment
    rsproxy = c4d.Orsproxy
    rssky = c4d.Orssky
    rsvolume = c4d.Orsvolume
    scatterobject = c4d.Oscatterobject
    scatterplacement = c4d.OScatterPlacement
    sds = c4d.Osds
    selection = c4d.Oselection
    shatter = c4d.Oshatter
    shear = c4d.Oshear
    showdisplacement = c4d.Oshowdisplacement
    shrinkwrap = c4d.Oshrinkwrap
    simulationscene = c4d.Osimulationscene
    singlepoly = c4d.Osinglepoly
    skin = c4d.Oskin
    sky = c4d.Osky
    sphere = c4d.Osphere
    spherify = c4d.Ospherify
    spline = c4d.Ospline
    spline4side = c4d.Ospline4side
    splinearc = c4d.Osplinearc
    splinecircle = c4d.Osplinecircle
    splinecissoid = c4d.Osplinecissoid
    splinecogwheel = c4d.Osplinecogwheel
    splinecontour = c4d.Osplinecontour
    splinecycloid = c4d.Osplinecycloid
    splinedeformer = c4d.Osplinedeformer
    splineflower = c4d.Osplineflower
    splineformula = c4d.Osplineformula
    splinehelix = c4d.Osplinehelix
    splinenside = c4d.Osplinenside
    splineprimitive = c4d.Osplineprimitive
    splineprofile = c4d.Osplineprofile
    splinerail = c4d.Osplinerail
    splinerectangle = c4d.Osplinerectangle
    splinestar = c4d.Osplinestar
    splinetext = c4d.Osplinetext
    spring = c4d.Ospring
    stage = c4d.Ostage
    sweep = c4d.Osweep
    symmetry = c4d.Osymmetry
    taper = c4d.Otaper
    torus = c4d.Otorus
    tube = c4d.Otube
    turbulence = c4d.Oturbulence
    twist = c4d.Otwist
    vectorimport = c4d.Ovectorimport
    volume = c4d.Ovolume
    volumebuilder = c4d.Ovolumebuilder
    volumecachelayer = c4d.Ovolumecachelayer
    volumefilter = c4d.Ovolumefilter
    volumeloader = c4d.Ovolumeloader
    volumemesher = c4d.Ovolumemesher
    volumeset = c4d.Ovolumeset
    voronoipointgenerator = c4d.Ovoronoipointgenerator
    wave = c4d.Owave
    weighteffector = c4d.Oweighteffector
    wind = c4d.Owind
    winddeform = c4d.Owinddeform
    workplane = c4d.Oworkplane
    wrap = c4d.Owrap
    xref = c4d.Oxref
    xrefsimple = c4d.Oxrefsimple


class T(Type):
    alembicmorphtag = c4d.Talembicmorphtag
    aligntopath = c4d.Taligntopath
    aligntospline = c4d.Taligntospline
    annotation = c4d.Tannotation
    archigrass = c4d.Tarchigrass
    bakeparticle = c4d.Tbakeparticle
    baketexture = c4d.Tbaketexture
    base = c4d.Tbase
    cacheproxytag = c4d.Tcacheproxytag
    cacheproxytagedgeselection = c4d.Tcacheproxytagedgeselection
    cacheproxytagpointselection = c4d.Tcacheproxytagpointselection
    cacheproxytagpolyselection = c4d.Tcacheproxytagpolyselection
    cacomponent = c4d.Tcacomponent
    caconstraint = c4d.Tcaconstraint
    caik = c4d.Tcaik
    caikspline = c4d.Tcaikspline
    cameracalibrator = c4d.Tcameracalibrator
    cameraorrientation = c4d.Tcameraorrientation
    capointcache = c4d.Tcapointcache
    catension = c4d.Tcatension
    cavisualselector = c4d.Tcavisualselector
    chardefinition = c4d.Tchardefinition
    charmotiontransfer = c4d.Tcharmotiontransfer
    cloth = c4d.Tcloth
    clothbelt = c4d.Tclothbelt
    collider = c4d.Tcollider
    compositing = c4d.Tcompositing
    connector = c4d.Tconnector
    corner = c4d.Tcorner
    crane = c4d.Tcrane
    display = c4d.Tdisplay
    doodleimage = c4d.Tdoodleimage
    driver = c4d.Tdriver
    dynamicsbody = c4d.Tdynamicsbody
    edgeselection = c4d.Tedgeselection
    expresso = c4d.Texpresso
    grouppriority = c4d.Tgrouppriority
    interaction = c4d.Tinteraction
    line = c4d.Tline
    lookatcamera = c4d.Tlookatcamera
    maskconstraint = c4d.Tmaskconstraint
    meshattribute = c4d.Tmeshattribute
    metaball = c4d.Tmetaball
    mgcolor = c4d.Tmgcolor
    mgdependence = c4d.Tmgdependence
    mgselection = c4d.Tmgselection
    mgtracer = c4d.Tmgtracer
    mgweight = c4d.Tmgweight
    morphcam = c4d.Tmorphcam
    motionblur = c4d.Tmotionblur
    motioncam = c4d.Tmotioncam
    motionsystem = c4d.Tmotionsystem
    moveseye = c4d.Tmoveseye
    movesposemorph = c4d.Tmovesposemorph
    normal = c4d.Tnormal
    particle = c4d.Tparticle
    phong = c4d.Tphong
    planarconstraint = c4d.Tplanarconstraint
    plugin = c4d.Tplugin
    point = c4d.Tpoint
    pointselection = c4d.Tpointselection
    polygon = c4d.Tpolygon
    polygonselection = c4d.Tpolygonselection
    posemorph = c4d.Tposemorph
    positionconstraint = c4d.Tpositionconstraint
    protection = c4d.Tprotection
    python = c4d.Tpython
    render = c4d.Trender
    restriction = c4d.Trestriction
    retarget = c4d.Tretarget
    rope = c4d.Trope
    ropebelt = c4d.Tropebelt
    rscamera = c4d.Trscamera
    rsobject = c4d.Trsobject
    savetemp = c4d.Tsavetemp
    scenenodes = c4d.Tscenenodes
    sculpt = c4d.Tsculpt
    sds = c4d.Tsds
    sdsdata = c4d.Tsdsdata
    segment = c4d.Tsegment
    sketchrender = c4d.Tsketchrender
    sketchstyle = c4d.Tsketchstyle
    softselection = c4d.Tsoftselection
    splinenormal = c4d.Tsplinenormal
    sticktexture = c4d.Tsticktexture
    stop = c4d.Tstop
    sunexpression = c4d.Tsunexpression
    tangent = c4d.Ttangent
    targetexpression = c4d.Ttargetexpression
    texture = c4d.Ttexture
    todo = c4d.Ttodo
    userdata = c4d.Tuserdata
    uvw = c4d.Tuvw
    variable = c4d.Tvariable
    vectorconstraint = c4d.Tvectorconstraint
    vertexcolor = c4d.Tvertexcolor
    vertexmap = c4d.Tvertexmap
    vibrate = c4d.Tvibrate
    weights = c4d.Tweights


class X(Type):
    ambientocclusion = c4d.Xambientocclusion
    art = c4d.Xart
    base = c4d.Xbase
    bitmap = c4d.Xbitmap
    brick = c4d.Xbrick
    cel = c4d.Xcel
    chanlum = c4d.Xchanlum
    checkerboard = c4d.Xcheckerboard
    cloud = c4d.Xcloud
    color = c4d.Xcolor
    colorizer = c4d.Xcolorizer
    colorstripes = c4d.Xcolorstripes
    cyclone = c4d.Xcyclone
    distorter = c4d.Xdistorter
    earth = c4d.Xearth
    falloff = c4d.Xfalloff
    filter = c4d.Xfilter
    fire = c4d.Xfire
    flame = c4d.Xflame
    formula = c4d.Xformula
    fresnel = c4d.Xfresnel
    fusion = c4d.Xfusion
    galaxy = c4d.Xgalaxy
    gradient = c4d.Xgradient
    hatch = c4d.Xhatch
    layer = c4d.Xlayer
    lensdistortion = c4d.Xlensdistortion
    lumas = c4d.Xlumas
    marble = c4d.Xmarble
    metal = c4d.Xmetal
    mgbeat = c4d.Xmgbeat
    mgcamera = c4d.Xmgcamera
    mgcolor = c4d.Xmgcolor
    mgmultishader = c4d.Xmgmultishader
    mosaic = c4d.Xmosaic
    movesface = c4d.Xmovesface
    noise = c4d.Xnoise
    normaldirection = c4d.Xnormaldirection
    normalizer = c4d.Xnormalizer
    objectcolor = c4d.Xobjectcolor
    pavement = c4d.Xpavement
    planet = c4d.Xplanet
    polygonhair = c4d.Xpolygonhair
    posterizer = c4d.Xposterizer
    projector = c4d.Xprojector
    proximal = c4d.Xproximal
    rainsampler = c4d.Xrainsampler
    ripple = c4d.Xripple
    rust = c4d.Xrust
    simplenoise = c4d.Xsimplenoise
    simpleturbulence = c4d.Xsimpleturbulence
    spectral = c4d.Xspectral
    spline = c4d.Xspline
    spots = c4d.Xspots
    sss = c4d.Xsss
    star = c4d.Xstar
    starfield = c4d.Xstarfield
    sunburst = c4d.Xsunburst
    terrainmask = c4d.Xterrainmask
    thinfilm = c4d.Xthinfilm
    tiles = c4d.Xtiles
    translucency = c4d.Xtranslucency
    variation = c4d.Xvariation
    venus = c4d.Xvenus
    vertexmap = c4d.Xvertexmap
    water = c4d.Xwater
    wood = c4d.Xwood
    xmbsubsurface = c4d.Xxmbsubsurface


class F(Type):
    box = c4d.Fbox
    capsule = c4d.Fcapsule
    cone = c4d.Fcone
    cylinder = c4d.Fcylinder
    formula = c4d.Fformula
    group = c4d.Fgroup
    linear = c4d.Flinear
    python = c4d.Fpython
    radial = c4d.Fradial
    random = c4d.Frandom
    shader = c4d.Fshader
    sound = c4d.Fsound
    spherical = c4d.Fspherical
    torus = c4d.Ftorus


class FL(Type):
    base = c4d.FLbase
    clamp = c4d.FLclamp
    colorize = c4d.FLcolorize
    curve = c4d.FLcurve
    decay = c4d.FLdecay
    delay = c4d.FLdelay
    descid = c4d.FLdescid
    field = c4d.FLfield
    folder = c4d.FLfolder
    formula = c4d.FLformula
    gradient = c4d.FLgradient
    invert = c4d.FLinvert
    mograph = c4d.FLmograph
    noise = c4d.FLnoise
    particleobject = c4d.FLparticleobject
    plugin = c4d.FLplugin
    polygonobject = c4d.FLpolygonobject
    proximity = c4d.FLproximity
    python = c4d.FLpython
    quantize = c4d.FLquantize
    rangemap = c4d.FLrangemap
    remap = c4d.FLremap
    solid = c4d.FLsolid
    spline = c4d.FLspline
    step = c4d.FLstep
    time = c4d.FLtime
    volumeobject = c4d.FLvolumeobject
    weight = c4d.FLweight


class CT(Type):
    base = c4d.CTbase
    ct2d = c4d.CT2d
    doodle = c4d.CTdoodle
    mask = c4d.CTMask
    morph = c4d.CTmorph
    pla = c4d.CTpla
    sound = c4d.CTsound
    time = c4d.CTtime


class VP(Type):
    ambientocclusion = c4d.VPambientocclusion
    birender = c4d.VPbirender
    bloom = c4d.VPbloom
    colorcorrection = c4d.VPcolorcorrection
    colormapping = c4d.VPcolormapping
    comic = c4d.VPcomic
    cylindricallens = c4d.VPcylindricallens
    demowatermark = c4d.VPdemowatermark
    globalillumination = c4d.VPglobalillumination
    gpurenderer = c4d.VPGPURenderer
    hlensdistortion = c4d.VPPhLensDistortion
    lenseffects = c4d.VPlenseffects
    magicbulletlooks = c4d.VPMagicBulletLooks
    medianfilter = c4d.VPmedianfilter
    normalpass = c4d.VPnormalpass
    objectglow = c4d.VPobjectglow
    opticsuite_depthoffield = c4d.VPopticsuite_depthoffield
    opticsuite_glow = c4d.VPopticsuite_glow
    opticsuite_highlights = c4d.VPopticsuite_highlights
    positionpass = c4d.VPpositionpass
    remote = c4d.VPremote
    rsposteffects = c4d.VPrsposteffects
    rsrenderer = c4d.VPrsrenderer
    scenemotionblur = c4d.VPscenemotionblur
    sharpenfilter = c4d.VPsharpenfilter
    softfilter = c4d.VPsoftfilter
    tonemapping = c4d.VPToneMapping
    toons = c4d.VPtoons
    vectormotionblur = c4d.VPvectormotionblur
    watermark = c4d.VPwatermark
    xmbsampler = c4d.VPxmbsampler


class M(Type):
    banji = c4d.Mbanji
    banzi = c4d.Mbanzi
    base = c4d.Mbase
    cgfx = c4d.MCgFX
    cheen = c4d.Mcheen
    danel = c4d.Mdanel
    fog = c4d.Mfog
    mabel = c4d.Mmabel
    material = c4d.Mmaterial
    nukei = c4d.Mnukei
    outline = c4d.Moutline
    plugin = c4d.Mplugin
    pyroobject = c4d.Mpyroobject
    pyrovolume = c4d.Mpyrovolume
    rsgraph = c4d.Mrsgraph
    shadowcatcher = c4d.Mshadowcatcher
    sketch = c4d.Msketch
    terrain = c4d.Mterrain


class Doc(Type):
    base = c4d.Tbasedocument


if __name__ == "__main__":
    import importlib, c4djson.main, c4djson
    importlib.reload(c4djson.main)
    importlib.reload(c4djson)
