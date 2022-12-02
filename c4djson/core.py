from typing import Optional, Union
import c4d, re
from c4djson.bl import *

setattr(c4d, "ID_BASELIST", c4d.Tbaselist2d)


class Atom:
    def __init__(self, value, dummy=None, ident: Optional[str] = None):
        self.value, self.dummy, self.ident = value, dummy, ident

    def __repr__(self):
        """Priority: `ident` > `dummy` > `value`"""
        if self.ident is not None:
            return self.ident
        if self.dummy is not None:
            return repr(self.dummy)
        return repr(self.value)

    def __eq__(self, other: object):
        if isinstance(other, Atom):
            return hash(self) == hash(other)
        return False

    def __hash__(self):
        """
        For `c4d.DescID`, only referring the id for each level.
        """
        if hasattr(self.value, "GetHashCode"):
            return getattr(self.value, "GetHashCode")()
        try:
            return hash(self.value)
        except TypeError:
            return id(self.value)


class Key(Atom):
    ...


class Val(Atom):
    def __hash__(self):
        return super().__hash__()

    def __eq__(self, other: object):
        if not isinstance(other, Atom):
            return False
        if isinstance(self.value, (c4d.FieldList, c4d.InExcludeData, c4d.BaseTime, c4d.FontData, c4d.PriorityData)):
            # TODO
            return self.dummy == other.dummy
        if isinstance(self.value, c4d.SplineData) and isinstance(other.value, c4d.SplineData):
            spline1, spline2 = self.value, other.value
            if spline1.GetKnotCount() != spline2.GetKnotCount():
                return False
            for knot1, knot2 in zip(spline1.GetKnots(), spline2.GetKnots()):
                for key in ["vPos", "lFlagsSettings", "vTangentLeft", "vTangentRight", "interpol"]:
                    if knot1[key] != knot2[key]:
                        return False
            return True

        return hash(self) == hash(other)


class Comment(Key):
    def __init__(self, ident=""):
        super().__init__(None, None, ident)

    def __hash__(self):
        return super(object).__hash__()


JSON = dict[Union[Key, int], Union[Val, "JSON"]]


class Param:
    def __init__(self, descid: c4d.DescID, bl: BL):
        self.descid, self.bl = descid, bl
        if descid[0].dtype == 0:
            description = bl.obj.GetDescription(c4d.DESCFLAGS_DESC_0)
            descid = description.CheckDescID(descid, [bl.obj])
            self.descid = descid or self.descid

    @property
    def description(self):
        return self.bl.obj.GetDescription(c4d.DESCFLAGS_DESC_0)

    @property
    def bc(self):
        return self.description.GetParameter(self.descid)

    def __getitem__(self, key: int):
        return self.bc[key]


class Tree:
    doc = c4d.documents.GetActiveDocument()
    database = {}

    def __init__(self, data: Optional[dict] = None):
        Tree.doc = c4d.documents.GetActiveDocument()
        self.objects: dict[tuple[int, str], c4d.BaseList2D] = {}
        self.data = {} if data is None else data
        self.ParseObjects(self.data)
        self.ParseParams(self.data)

    def __getitem__(self, bl: BL):
        return self.objects[bl.link]

    def ParseObjects(self, data: dict, parent: Optional[BL] = None):
        for key, val in data.items():
            if isinstance(key, BL):
                bl: BL = key
                if parent is not None:
                    bl.SetParent(parent)
                self.objects[bl.link] = bl.obj
                val = self.ParseObjects(val, bl)

    def ParseParams(self, data: dict, bl: Optional[BL] = None):
        for key, val in data.items():
            if isinstance(key, BL):
                bl: BL = key
                self.ParseParams(val, bl)
            else:
                assert bl is not None
                if type(key) == int:
                    key = (key,)
                param = Param(DescID(*key), bl)
                # When param is c4d.FIELDS
                # When param is a button
                if param[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_BUTTON:
                    c4d.CallButton(bl.obj, param.descid[-1].id)
                    continue
                # When param value is [] (means animated)
                if type(val) == list and any(type(item) == tuple for item in val):
                    self.ParseTrack(param, val)
                    continue
                # When param is USERDATA
                if param.descid == c4d.DESCID_DYNAMICSUB:
                    LoadUserData(val, self, bl)
                    continue
                paramkey = tuple(param.descid[i].id for i in range(param.descid.GetDepth()))
                val = LoadValue(val, param.bc, self)
                if val is not None:
                    try:
                        bl.obj[paramkey] = val
                    except (TypeError, AttributeError):
                        import traceback
                        print(traceback.format_exc(), end="")
                        print("Object:", bl)
                        print("Param:", param.descid)
                        print("Value:", val)

    def ParseTrack(self, param: Param, data: list[Union[tuple, dict]]):
        track = param.bl.obj.FindCTrack(param.descid)
        if track is not None:
            track.Remove()
        track = c4d.CTrack(param.bl.obj, param.descid)
        curve = track.GetCurve()
        trackCategory = track.GetTrackCategory()
        fps = Tree.doc.GetFps()
        descid = param.descid
        obj = param.bl.obj

        def AddKeyframe(frame: int, value, interpolation=c4d.CINTER_SPLINE):
            keyDict = curve.AddKey(c4d.BaseTime(frame, fps))
            key: c4d.CKey = keyDict["key"]
            keyIndex = keyDict["nidx"]
            value = LoadValue(value, param.bc, self)
            if trackCategory == c4d.CTRACK_CATEGORY_DATA:
                key.SetGeData(curve, value)
            else:
                key.SetValue(curve, value)
            curve.SetKeyDefault(Tree.doc, keyIndex)
            key.SetInterpolation(curve, interpolation)

        for item in data:
            if type(item) == tuple:
                AddKeyframe(*item)
            if type(item) == dict:
                self.ParseParams({BL.FromObj(track): item})
        obj.InsertTrackSorted(track)
        firstValue = LoadValue(data[0][1], param.bc, self)
        if descid.GetDepth() == 1:
            # `SetData` can transfer basic types (e.g. int -> float) implicitly.
            # This can avoid some weird behaviours.
            obj.GetDataInstance().SetData(descid[0].id, firstValue)
        else:
            obj[descid] = firstValue
        return track

    def load(self, replace=True, dumpWhenLoaded=True):
        self.doc.StartUndo()
        for bl in reversed([i for i in self.data if isinstance(i, BL)]):
            if isinstance(bl.obj, c4d.BaseObject):
                if replace:
                    for old in self.doc.GetObjects():
                        if old.GetName() == bl.obj.GetName() and old.GetType() == bl.type.value:
                            old.Remove()
                self.doc.InsertObject(bl.obj)
                self.doc.SetSelection(bl.obj, c4d.SELECTION_ADD)
                self.doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, bl.obj)
            if isinstance(bl.obj, c4d.BaseMaterial):
                if replace:
                    old = self.doc.SearchMaterial(bl.name)
                    if old is not None and old.GetType() == bl.type.value:
                        old.Remove()
                # When there's no mat in mat manager, the insert operation may lose it's name
                name = bl.name
                self.doc.InsertMaterial(bl.obj)
                self.doc.SetSelection(bl.obj, c4d.SELECTION_ADD)
                bl.obj.SetName(name)  # Restore it's name
                self.doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, bl.obj)
        self.doc.EndUndo()
        c4d.EventAdd()
        Command.UnFoldAll()
        if dumpWhenLoaded:
            print(Dict2Str(DumpSelected()))
        return self


class Command:
    def PlayForward():
        playForward = 12412
        if not c4d.IsCommandChecked(playForward):
            c4d.CallCommand(playForward)

    def UnFoldAll():
        c4d.CallCommand(100004748)

    def ClearConsole():
        c4d.CallCommand(13957)


excludeParamMappings = {
    c4d.Tbaselist2d: [c4d.ID_BASELIST_NAME],
    c4d.Obase: [
        c4d.ID_BASEOBJECT_GLOBAL_POSITION,
        c4d.ID_BASEOBJECT_ABS_POSITION,
        c4d.ID_BASEOBJECT_GLOBAL_ROTATION,
        c4d.ID_BASEOBJECT_ABS_ROTATION,
        c4d.ID_BASEOBJECT_ABS_SCALE
    ],
    c4d.CTbase: [c4d.ID_CTRACK_FCURVE_COLOR],
    c4d.Ofield: [c4d.FIELD_PREVIEW],
    c4d.Mbase: [c4d.ID_MATERIALASSIGNMENTS, 526340, 525828],
    c4d.FLbase: [c4d.FIELD_PREVIEW],
}


def DumpParams(obj: c4d.BaseList2D, excludes: dict[int, list[int]] = excludeParamMappings):
    result: dict[Key, Val] = {}
    description = obj.GetDescription(c4d.DESCFLAGS_DESC_0)

    def FilterParams(descid: c4d.DescID):
        if descid.GetDepth() == 0:
            return True
        for baseType in excludes:
            if obj.IsInstanceOf(baseType):
                if descid[0].id in excludes[baseType]:
                    return True
        return False

    bc: c4d.BaseContainer
    descid: c4d.DescID
    for bc, descid, _ in description:
        if not c4d.DESCID_DYNAMICSUB.IsPartOf(descid)[0]:  # Not a userdata
            if descid[-1].dtype in [c4d.DTYPE_GROUP, c4d.DTYPE_SEPARATOR]:
                continue
        if FilterParams(descid):
            continue
        try:
            value = obj[descid]
        except AttributeError:
            # The value can't access
            value = None
            if descid != c4d.DESCID_DYNAMICSUB:
                continue
        key = Key(descid, DumpDescID(descid, description))
        val = Val(value, DumpValue(value, descid, bc))
        if repr(key) in ["c4d.OPYTHON_CODE", "c4d.TPYTHON_CODE"]:
            val.ident = "code"
        result[key] = val
    return result


def DumpParamDescids(obj: c4d.BaseList2D, excludes: dict[int, list[int]] = excludeParamMappings):
    result = DumpParams(obj, excludes)
    for key in result:
        result[key] = Val(key.value)
    return result


def DumpParamDetails(obj: c4d.BaseList2D, descid: c4d.DescID):
    result: dict[Key, Val] = {}
    # creator = descid[-1].creator
    # result[Key("creator", ident="creator")] = Val(creator, ident=FindIdent(creator))
    description = obj.GetDescription(c4d.DESCFLAGS_DESC_0)
    descid = description.CheckDescID(descid, [obj])
    dtype = descid[-1].dtype
    dtypeIdent = FindIdent(dtype, "^(DTYPE_|CUSTOMDATATYPE_)|_DATA$")
    result[Key(c4d.DTYPE_, ident="c4d.DTYPE_")] = Val(dtype, ident=dtypeIdent)
    bc = description.GetParameter(descid)
    details = DumpBaseContainer(bc)
    generalMappings = {
        c4d.DESC_VERSION: "^DESC_VERSION_",
        c4d.DESC_ANIMATE: "^DESC_ANIMATE_",
        c4d.DESC_UNIT: "^DESC_UNIT_",
        c4d.DESC_CUSTOMGUI: "^CUSTOMGUI_",
    }
    for key, val in details.items():
        key.ident = FindIdent(key.value, "DESC_")
        if key.value in generalMappings:
            val.ident = FindIdent(val.value, generalMappings[key.value])
    if Key(c4d.DESC_CUSTOMGUI) in details:
        if details[Key(c4d.DESC_CUSTOMGUI)].value in [c4d.CUSTOMGUI_BOOL, c4d.CUSTOMGUI_BITMAPBOOL]:
            for key, val in details.items():
                if key.ident is None:
                    key.ident = FindIdent(key.value, f"^BITMAPBOOL_")
                    if key.ident is not None:
                        val.ident = FindIdent(val.value, "^RESOURCEIMAGE_")
        guiSuffix = details[Key(c4d.DESC_CUSTOMGUI)].ident.split("_")[-1]
    for key, val in details.items():
        if key.ident is None:
            key.ident = FindIdent(key.value, f"^{guiSuffix}")
            key.ident = key.ident or FindIdent(key.value, guiSuffix)
        if key.value in [c4d.DESC_MIN, c4d.DESC_MAX, c4d.DESC_DEFAULT, c4d.DESC_STEP]:
            val.dummy = DumpValue(val.value, descid, bc)
    result |= details
    return result


def DumpUserDataDetails(obj: c4d.BaseList2D, descid: c4d.DescID):
    result: dict[Key, Val] = {}
    dtype = descid[-1].dtype
    dtypeIdent = FindIdent(dtype, "^(DTYPE_|CUSTOMDATATYPE_)|_DATA$")
    result[Key(c4d.DTYPE_, ident="c4d.DTYPE_")] = Val(dtype, ident=dtypeIdent)
    bc = None
    for descid2, bc in obj.GetUserDataContainer():
        if descid.GetHashCode() == descid2.GetHashCode():
            break
    assert isinstance(bc, c4d.BaseContainer)
    details = DumpBaseContainer(bc)
    generalMappings = {
        c4d.DESC_VERSION: "^DESC_VERSION_",
        c4d.DESC_ANIMATE: "^DESC_ANIMATE_",
        c4d.DESC_UNIT: "^DESC_UNIT_",
        c4d.DESC_CUSTOMGUI: "^CUSTOMGUI_",
    }
    for key, val in details.items():
        key.ident = FindIdent(key.value, "DESC_")
        if key.value in generalMappings:
            val.ident = FindIdent(val.value, generalMappings[key.value])
    if Key(c4d.DESC_CUSTOMGUI) in details:
        if details[Key(c4d.DESC_CUSTOMGUI)].value in [c4d.CUSTOMGUI_BOOL, c4d.CUSTOMGUI_BITMAPBOOL]:
            for key, val in details.items():
                if key.ident is None:
                    key.ident = FindIdent(key.value, f"^BITMAPBOOL_")
                    if key.ident is not None:
                        val.ident = FindIdent(val.value, "^RESOURCEIMAGE_")
        guiSuffix = details[Key(c4d.DESC_CUSTOMGUI)].ident.split("_")[-1]
    for key, val in details.items():
        if key.ident is None:
            key.ident = FindIdent(key.value, f"^{guiSuffix}")
            key.ident = key.ident or FindIdent(key.value, guiSuffix)
    for key, val in details.items():
        valueKeys = [c4d.DESC_DEFAULT, c4d.DESC_MIN, c4d.DESC_MAX, c4d.DESC_MINSLIDER, c4d.DESC_MAXSLIDER]
        if dtype != c4d.DTYPE_BOOL:
            valueKeys.append(c4d.DESC_STEP)
        if key.value in valueKeys:
            val.dummy = DumpValue(val.value, descid, bc)
    result |= {key: val for key, val in details.items() if key.value not in [
        c4d.DESC_REMOVEABLE, c4d.DESC_EDITABLE, c4d.DESC_VERSION, c4d.DESC_ANIMATE]}
    return result


def DumpUserData(data: dict[Key, dict[Key, Val]]):
    # TODO
    result: dict[Key, Val] = {}
    for key, val in data.items():
        if val[Key(c4d.DESC_PARENTGROUP)].value in [c4d.DescID(0), c4d.DESCID_DYNAMICSUB]:
            result[Key(key.value, val[Key(c4d.DESC_NAME)].value)] = val
    return result


def LoadUserData(data: dict[tuple[int, int], dict[int]], tree: Tree, bl: BL):
    for item in data.values():
        dtype = item[c4d.DTYPE_]
        bc = c4d.GetCustomDataTypeDefault(dtype)
        valueKeys = [
            c4d.DESC_DEFAULT, c4d.DESC_MIN, c4d.DESC_MAX, c4d.DESC_MINSLIDER, c4d.DESC_MAXSLIDER
        ]
        if dtype != c4d.DTYPE_BOOL:
            valueKeys.append(c4d.DESC_STEP)
        for key, val in item.items():
            if key == c4d.DTYPE_:
                continue
            if key == c4d.DESC_PARENTGROUP:
                bc[key] = DescID(*val)
            elif key in [c4d.DESC_CYCLE, c4d.DESC_CYCLEICONS]:
                bc[key] = LoadBaseContainer(val)
            elif key not in valueKeys:
                bc[key] = val
        for key, val in item.items():
            if key in valueKeys:
                bc[key] = LoadValue(val, bc, tree)
        descid = bl.obj.AddUserData(bc)
        if bc[c4d.DESC_DEFAULT] is not None:
            bl.obj[descid] = bc[c4d.DESC_DEFAULT]


def DumpDirtyParams(obj: c4d.BaseList2D, comment=True):
    result: JSON = {}
    params = DumpParams(obj)
    desc = obj.GetDescription(c4d.DESCFLAGS_DESC_0)
    trackData = DumpTracks(obj)
    # raw = BL.GetRaw(obj.GetType())
    raw = c4d.BaseList2D(obj.GetType())
    if isinstance(raw, c4d.BaseObject):
        Tree.doc.InsertObject(raw)
    effectorStrengthParamIds = []
    effectorKey = Key(c4d.DescID(c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST))
    if effectorKey in params:
        effectors: c4d.InExcludeData = params[effectorKey].value
        for i in range(effectors.GetObjectCount()):
            effectorStrengthParamIds.append(1500 + i)
    for key, val in params.items():
        descid: c4d.DescID = key.value
        if "CACHE" in repr(key):
            # TODO
            continue
        try:
            rawValue = raw[descid]
        except AttributeError:
            rawValue = object() if val.value is None else None
        bc = desc.GetParameter(descid)
        rawDummy = None
        if rawValue is not None:
            rawDummy = DumpValue(rawValue, descid, desc.GetParameter(descid))
        # if descid == DescID((11010, 22, 180000102)):
        #     print(isinstance(rawValue, object))
        #     print(val, rawValue.GetFrame(Tree.doc.GetFps()))
        if Val(rawValue, rawDummy) == val:
            if descid not in [DescID((1204, 15, 1018583))]:  # c4d.MG_GRID_MODE
                continue
        if bc[c4d.DESC_DEFAULT] is not None and val.value == bc[c4d.DESC_DEFAULT]:
            if descid[0].id != 700:
                continue
        if descid[0].id in effectorStrengthParamIds and val.value == 1:
            continue
        try:
            raw[descid] = val.value
            raw.Message(c4d.MSG_CHANGE)
        except (AttributeError, TypeError):
            ...
        if descid == c4d.DESCID_DYNAMICSUB:  # UserData
            val = {}
        if descid[0].id == 700 and descid.GetDepth() == 2:  # UserData details
            userdataDetails = DumpUserDataDetails(obj, descid)
            result[Key(c4d.DESCID_DYNAMICSUB)][key] = userdataDetails
        if descid[-1].dtype in [c4d.DTYPE_GROUP, c4d.DTYPE_SEPARATOR]:
            continue
        # Parse vector params who has only one dirty channel
        if descid[-1].dtype == c4d.DTYPE_VECTOR:
            assert isinstance(val.value, c4d.Vector)
            assert isinstance(rawValue, c4d.Vector)
            x, y, z = val.value.x, val.value.y, val.value.z
            a, b, c = rawValue.x, rawValue.y, rawValue.z
            if (x == a, y == b, z == c).count(True) == 2:
                for i, v in enumerate((x, y, z)):
                    if v != (a, b, c)[i]:
                        subid = [c4d.VECTOR_X, c4d.VECTOR_Y, c4d.VECTOR_Z][i]
                        desclevel = c4d.DescLevel(subid, c4d.DTYPE_REAL, c4d.DTYPE_VECTOR)
                        descid.PushId(desclevel)
                        key.value, key.dummy = descid, DumpDescID(descid, desc)
                        val.value, val.dummy, val.ident = v, val.dummy[i].value, val.dummy[i].ident
                        bc = desc.GetParameter(descid)
        name: str = bc[c4d.DESC_NAME] or bc[c4d.DESC_SHORT_NAME]
        cycle = bc[c4d.DESC_CYCLE]
        cycleName = cycle[val.value] if cycle else None
        if comment and name:
            keyRepr = repr(key)
            if name.replace(" ", "_").upper() not in keyRepr and name.replace(" ", "").upper() not in keyRepr:
                name = name.replace(" . ", ".")
                re.sub
                if cycleName:
                    result[Comment(f"# {name}: {cycleName}")] = None
                else:
                    animated = "Animated " if key in trackData else ""
                    result[Comment(f"# {animated}{name}")] = None
        result[key] = trackData.get(key) or val
    for key, val in trackData.items():
        if key not in result:
            bc = desc.GetParameter(key.value)
            name: str = bc[c4d.DESC_NAME] or bc[c4d.DESC_SHORT_NAME]
            if name and comment:
                name = name.replace(" . ", ".")
                result[Comment(f"# Animated {name}")] = None
            result[key] = val
    # if Key(c4d.DESCID_DYNAMICSUB) in result:
    #     result[Key(c4d.DESCID_DYNAMICSUB)] = DumpUserData(result[Key(c4d.DESCID_DYNAMICSUB)])
    raw.Remove()
    return result


def DumpTracks(obj: c4d.BaseList2D):
    result: dict[Key, list] = {}
    tracks = obj.GetCTracks()
    doc = Tree.doc
    fps = doc.GetFps()
    desc = obj.GetDescription(c4d.DESCFLAGS_DESC_0)
    for track in tracks:
        trackCategory = track.GetTrackCategory()
        descid = track.GetDescriptionID()
        bc = desc.GetParameter(descid)
        keyFrames = []
        curve = track.GetCurve()
        for i in range(curve.GetKeyCount()):
            curveKey = curve.GetKey(i)
            frame = curveKey.GetTime().GetFrame(fps)
            value = curveKey.GetGeData() if trackCategory == c4d.CTRACK_CATEGORY_DATA else curveKey.GetValue()
            val = Val(value, DumpValue(value, descid, bc))
            interpolation = curveKey.GetInterpolation()
            if interpolation != c4d.CINTER_SPLINE:
                keyFrames.append((frame, val, Val(interpolation, ident=FindIdent(interpolation, "^CINTER_"))))
            else:
                keyFrames.append((frame, val))
        trackDetails = DumpDirtyParams(track)
        if trackDetails:
            keyFrames.append(trackDetails)
        result[Key(descid, DumpDescID(descid, desc))] = keyFrames
    return result


_tids_not_to_parse = [
    c4d.ID_MOTAGDATA, c4d.Tparticle,
    c4d.Tcacheproxytagpolyselection, c4d.Tcacheproxytagedgeselection,
    c4d.Tpoint, c4d.Tpolygon, c4d.Ttangent
]


def DumpBaseList(obj: c4d.BaseList2D):
    result: JSON = {}
    if obj.GetType() in _tids_not_to_parse:
        return result
    bl = BL.FromObj(obj)
    if bl is None:
        return {}
    key = Key(obj, bl)
    result[key] = DumpDirtyParams(obj)
    shader = obj.GetFirstShader()
    while shader is not None:
        result[key] |= DumpBaseList(shader)
        shader = shader.GetNext()
    if isinstance(obj, c4d.BaseObject):
        for tag in obj.GetTags():
            result[key] |= DumpBaseList(tag)
        for child in obj.GetChildren():
            result[key] |= DumpBaseList(child)
    return result


def DumpSelected():
    result: JSON = {}
    doc = Tree.doc
    objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE)
    materials = doc.GetActiveMaterials()
    for obj in objects:
        result |= DumpBaseList(obj)
    for mat in materials:
        result |= DumpBaseList(mat)
    if not result:
        tags = doc.GetActiveTags()
        for tag in tags:
            result |= DumpBaseList(tag)
    return result


def DumpDoc():
    result: JSON = {}
    doc = Tree.doc
    objects = doc.GetObjects()
    materials = doc.GetMaterials()
    for obj in objects:
        result |= DumpBaseList(obj)
    for mat in materials:
        result |= DumpBaseList(mat)
    if not result:
        tags = doc.GetActiveTags()
        for tag in tags:
            result |= DumpBaseList(tag)
    return result


def DumpDescID(descid: c4d.DescID, desc: c4d.Description):
    if descid == c4d.DESCID_ROOT:
        return Atom(descid, ident="c4d.DESCID_ROOT")
    levels: list[Atom] = []
    for i in range(descid.GetDepth()):
        subcid = c4d.DescID(*[descid[j] for j in range(i + 1)])
        subbc = desc.GetParameter(subcid)
        ident = subbc[c4d.DESC_IDENT]
        ident = "ID_BASELIST" if ident == "Obaselist" else ident
        ident = f"c4d.{ident}" if ident else None
        if subcid[0].id != 700:
            ident = ident or FindIdent(descid[-1].id, "ID_BASELIST")
        # if ident is None and subcid[-1].creator == c4d.Tbaselist2d:
        #     ident = FindIdent(subcid[-1].id, "^ID_BASELIST")
        levels.append(Atom(subcid[-1].id, ident=ident))
    if len(levels) == 1:
        return levels[0]
    return tuple(levels)


def LoadDescID(obj: c4d.BaseList2D, cid: Union[int, tuple[int]]):
    descid: c4d.DescID
    for bc, descid, _ in obj.GetDescription(c4d.DESCFLAGS_DESC_0):
        if type(cid) == int and descid[0].id == cid:
            return descid
        if type(cid) == tuple:
            if cid[0] == descid[0].id:
                assert cid[1] in [c4d.VECTOR_X, c4d.VECTOR_Y, c4d.VECTOR_Z]
                desclevel = c4d.DescLevel(cid[1], c4d.DTYPE_REAL, c4d.DTYPE_VECTOR)
                descid.PushId(desclevel)
                return descid
    raise ValueError(f"Can't find parameter <{cid}> in {obj}")


def DumpValue(value, descid: c4d.DescID, bc: c4d.BaseContainer):
    dtype = descid[-1].dtype
    if dtype == c4d.DTYPE_BASELISTLINK:
        if value is None:
            return None
        return BL.FromObj(value)
    if dtype == c4d.DTYPE_BOOL:
        return bool(value)
    if dtype == c4d.DTYPE_REAL:
        if bc[c4d.DESC_UNIT] == c4d.DESC_UNIT_DEGREE:
            value = c4d.utils.RadToDeg(value)
            return Atom(value, ident=Float2Str(value))
        return Atom(value, ident=Float2Str(value))
    if dtype == c4d.DTYPE_COLOR:
        return DumpColor(value)
    if dtype == c4d.DTYPE_VECTOR:
        if bc[c4d.DESC_UNIT] == c4d.DESC_UNIT_DEGREE:
            x, y, z = map(c4d.utils.RadToDeg, (value.x, value.y, value.z))
            value = c4d.Vector(x, y, z)
        return DumpVector(value)
    if dtype == c4d.DTYPE_LONG:
        if descid[-1].id == c4d.FIELD_TYPE:
            return Atom(value, ident=FindIdent(value, "^F"))
        if (cyclesymbols := bc[c4d.DESC_CYCLESYMBOLS]):
            ident = None
            if cyclesymbols[value] is not None:
                ident = f"c4d.{cyclesymbols[value]}"
            return Atom(value, ident=ident)
    if dtype == c4d.DTYPE_TIME:
        assert isinstance(value, c4d.BaseTime)
        return value.GetFrame(Tree.doc.GetFps())
    if dtype == c4d.CUSTOMDATATYPE_SPLINE:
        return DumpSplineData(value)
    if dtype == c4d.CUSTOMDATATYPE_GRADIENT:
        return DumpGradient(value)
    if dtype == c4d.CUSTOMDATATYPE_FIELDLIST:
        return DumpFieldList(value)
    if dtype == c4d.CUSTOMDATATYPE_INEXCLUDE_LIST:
        return DumpInExcludeData(value)
    if dtype == c4d.FONTCHOOSER_DATA:
        return DumpFontData(value)
    if dtype == c4d.CUSTOMGUI_PRIORITY_DATA:
        return DumpPriorityData(value)
    if dtype == 0:
        if isinstance(value, c4d.Vector):
            return DumpVector(value)
    return None


def LoadValue(value, bc: c4d.BaseContainer, tree: Tree):
    val = value
    if isinstance(val, tuple):
        if all(isinstance(i, (int, float)) for i in val) and 1 <= len(val) <= 3:
            val = c4d.Vector(*val)
    if bc[c4d.DESC_UNIT] == c4d.DESC_UNIT_DEGREE:
        if isinstance(val, c4d.Vector):
            x, y, z = map(c4d.utils.DegToRad, (val.x, val.y, val.z))
            val = c4d.Vector(x, y, z)
        elif isinstance(val, (int, float)):
            val = c4d.utils.DegToRad(val)
    if isinstance(val, BL):
        val = tree[val]

    if bc[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_TIME:
        fps = Tree.doc.GetFps()
        if isinstance(val, c4d.Vector):
            x, y, z = map(c4d.BaseTime, (val.x, val.y, val.z), (fps, fps, fps))
            val = c4d.Vector(x, y, z)
        elif isinstance(val, (int, float)):
            val = c4d.BaseTime(val, fps)
    elif bc[c4d.DESC_CUSTOMGUI] in [c4d.CUSTOMGUI_REAL, c4d.CUSTOMGUI_REALSLIDER]:
        val = float(val)
    elif bc[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_COLOR:
        x, y, z = map(lambda i: i / 255, (val.x, val.y, val.z))
        val = c4d.Vector(x, y, z)
    elif bc[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_FONTCHOOSER:
        font = c4d.FontData()
        font.SetFont(LoadBaseContainer(val))
        val = font
    elif bc[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_INEXCLUDE_LIST:
        val = LoadInExcludeData(val, tree)
    elif bc[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_FIELDLIST:
        val = LoadFieldList(val, tree)
    elif bc[c4d.DESC_CUSTOMGUI] == c4d.CUSTOMGUI_GRADIENT:
        val = LoadGradient(val)
    return val


def Float2Str(value: float):
    if abs(value) < 65536 and value == (integer := round(value)):
        return str(integer)
    else:
        return f"{value:.5}"


def DumpVector(value: c4d.Vector):
    x, y, z = value.x, value.y, value.z
    if x == y == z and len(str(x)) > 3:
        return (Atom(x, ident=Float2Str(x)),)
    return tuple(map(lambda i: Atom(i, ident=Float2Str(i)), (x, y, z)))


def DumpColor(value: c4d.Vector):
    x, y, z = value.x, value.y, value.z
    try:
        x, y, z = map(lambda i: round(i * 255), (x, y, z))
    except OverflowError:
        if x > 0:
            return (float("inf"), float("inf"), float("inf"))
        else:
            return (float("-inf"), float("-inf"), float("-inf"))
    return (x, y, z)


def LoadColor(value: tuple):
    x, y, z = value
    return c4d.Vector(x / 255, y / 255, z / 255)


def DumpBaseContainer(bc: c4d.BaseContainer):
    result: JSON = {}
    for key, val in bc:
        key = Key(key)
        # TODO: BaseContainer items can have same key!
        while key in result:
            key = Key(key.value + 1)
        if isinstance(val, c4d.BaseContainer):
            result[key] = DumpBaseContainer(val)
        elif isinstance(val, c4d.Vector):
            result[key] = Val(val, DumpVector(val))
        else:
            result[key] = Val(val)
    return result


def LoadBaseContainer(data: dict):
    bc = c4d.BaseContainer()
    for key, val in data.items():
        bc[key] = val
    return bc


def DumpFieldList(fieldlist: c4d.FieldList):
    result: JSON = {}
    child = fieldlist.GetLayersRoot().GetDown()
    while child is not None:
        result |= DumpBaseList(child)
        child = child.GetNext()
    return result


def LoadFieldList(data: dict[BL, dict[int]], tree: Tree):
    tree.ParseObjects(data)
    tree.ParseParams(data)
    fieldlist = c4d.FieldList()
    for fieldlayerBL in reversed(data):
        fieldlist.InsertLayer(fieldlayerBL.obj)
    return fieldlist


def DumpFontData(fontData: c4d.FontData):
    return DumpBaseContainer(fontData.GetFont())


def DumpPriorityData(priorityData: c4d.PriorityData):
    result = {}
    keys = [
        Key(c4d.PRIORITYVALUE_MODE, ident="c4d.PRIORITYVALUE_MODE"),
        Key(c4d.PRIORITYVALUE_PRIORITY, ident="c4d.PRIORITYVALUE_PRIORITY"),
        Key(c4d.PRIORITYVALUE_CAMERADEPENDENT, ident="c4d.PRIORITYVALUE_CAMERADEPENDENT"),
    ]
    for key in keys:
        val = Val(priorityData.GetPriorityValue(key.value))
        if key.value == c4d.PRIORITYVALUE_MODE:
            val.ident = FindIdent(val.value, "^CYCLE_")
        result[key] = val
    return result


def DumpInExcludeData(inExclude: c4d.InExcludeData):
    result: dict[tuple[int, int], BL] = {}
    for i in range(inExclude.GetObjectCount()):
        obj = inExclude.ObjectFromIndex(Tree.doc, i)
        if obj is not None:
            result[(i, inExclude.GetFlags(i))] = BL.FromObj(obj)
    if all(key[1] == 7 for key in result.keys()):
        return [bl for bl in result.values()]
    return result


def LoadInExcludeData(data: Union[dict[tuple[int, int], BL], list[BL]], tree: Tree):
    container = c4d.InExcludeData()
    if type(data) == dict:
        for key, val in data.items():
            _, flag = key
            if isinstance(val, BL):
                container.InsertObject(tree[val], flag)
    if type(data) == list:
        for item in data:
            container.InsertObject(tree[item], 7)
    return container


def DumpSplineData(splinedata: c4d.SplineData):
    result: dict[int, dict[Key, Val]] = {}
    for data in splinedata.GetKnots():
        i = ((data["lFlagsSettings"] >> 16) & 0x0000ffff)  # start from 1
        result[i] = {}
        for key, value in data.items():
            dummy = ident = None
            if key == "lFlagsSettings":
                ident = bin(value)
            elif key == "interpol":
                ident = FindIdent(value, "^CustomSplineKnotInterpolation")
            elif isinstance(value, c4d.Vector):
                dummy = DumpVector(value)
            result[i][Key(key)] = Val(value, dummy, ident)
    return result


def DumpGradient(gradient: c4d.Gradient):
    result: JSON = {}
    key = Key(c4d.GRADIENT_KNOT, ident="c4d.GRADIENT_KNOT")
    result[key] = {}
    knotsContainer = gradient.GetData(key.value)
    for _, bc in knotsContainer:
        knotsDict = DumpBaseContainer(bc)
        for k, v in knotsDict.items():
            k.ident = FindIdent(k.value, "^GRADIENTKNOT_")
            if k.value == c4d.GRADIENTKNOT_COLOR:
                v.dummy = DumpColor(v.value)
            if k.value == c4d.GRADIENTKNOT_INTERPOLATION:
                v.ident = FindIdent(v.value, "^GRADIENT_INTERPOLATION_")
        result[key][bc[c4d.GRADIENTKNOT_ID]] = knotsDict
    key = Key(c4d.GRADIENT_MODE, ident="c4d.GRADIENT_MODE")
    val = Val(gradient.GetData(key.value))
    val.ident = FindIdent(val.value, "GRADIENTMODE_")
    result[key] = val
    key = Key(c4d.GRADIENT_UNCLAMPED, ident="c4d.GRADIENT_UNCLAMPED")
    val = Val(gradient.GetData(key.value))
    val.dummy = bool(val.value)
    result[key] = val
    return result


def LoadGradient(data: dict[int, Union[dict, int, bool]]):
    gradient = c4d.Gradient()
    knotsContainer = c4d.BaseContainer()
    for knotData in data[c4d.GRADIENT_KNOT].values():
        knotData[c4d.GRADIENTKNOT_COLOR] = LoadColor(knotData[c4d.GRADIENTKNOT_COLOR])
        knotsContainer.InsData(0, LoadBaseContainer(knotData))
    gradient.SetData(c4d.GRADIENT_KNOT, knotsContainer)
    gradient.SetData(c4d.GRADIENT_MODE, data[c4d.GRADIENT_MODE])
    gradient.SetData(c4d.GRADIENT_UNCLAMPED, data[c4d.GRADIENT_UNCLAMPED])
    return gradient


def DumpDescription(desc: c4d.Description):
    result = {}
    descid: c4d.DescID
    for bc, descid, groupId in desc:
        details = DumpBaseContainer(bc)
        dtype = descid[-1].dtype
        dtypeIdent = FindIdent(dtype, "^(DTYPE_|CUSTOMDATATYPE_)|_DATA$")
        details = {Key(c4d.DTYPE_, ident="c4d.DTYPE_"): Val(dtype, ident=dtypeIdent)} | details
        generalMappings = {
            c4d.DESC_VERSION: "^DESC_VERSION_",
            c4d.DESC_ANIMATE: "^DESC_ANIMATE_",
            c4d.DESC_UNIT: "^DESC_UNIT_",
            c4d.DESC_CUSTOMGUI: "^CUSTOMGUI_",
        }
        for key, val in details.items():
            key.ident = FindIdent(key.value, "DESC_") if key.ident is None else key.ident
            if key.value in generalMappings:
                val.ident = FindIdent(val.value, generalMappings[key.value])
        if Key(c4d.DESC_CUSTOMGUI) in details:
            customgui = details[Key(c4d.DESC_CUSTOMGUI)]
            if customgui.value in [c4d.CUSTOMGUI_BOOL, c4d.CUSTOMGUI_BITMAPBOOL]:
                for key, val in details.items():
                    if key.ident is None:
                        key.ident = FindIdent(key.value, f"^BITMAPBOOL_")
                        if key.ident is not None:
                            val.ident = FindIdent(val.value, "^RESOURCEIMAGE_")
            try:
                guiSuffix = customgui.ident.split("_")[-1]
            except AttributeError:
                guiSuffix = None
                import sys
                print(f"File \"{__file__}\", line {sys._getframe().f_lineno}:")
                print("  Found Unrecognized c4d.DESC_CUSTOMGUI:", customgui.value)
        for key, val in details.items():
            if key.ident is None and guiSuffix is not None:
                key.ident = FindIdent(key.value, f"^{guiSuffix}")
                key.ident = key.ident or FindIdent(key.value, guiSuffix)
            if key.value in [c4d.DESC_MIN, c4d.DESC_MAX, c4d.DESC_DEFAULT, c4d.DESC_STEP]:
                val.dummy = DumpValue(val.value, descid, bc)
        result[Key(descid, DumpDescID(descid, desc))] = Val(bc, details)
    return result


def DescID(*args: Union[int, tuple[int]]):
    if all(type(i) == int for i in args):
        return c4d.DescID(*[c4d.DescLevel(i) for i in args])
    if all(type(i) == tuple for i in args):
        return c4d.DescID(*[c4d.DescLevel(0) if i == () else c4d.DescLevel(*i) for i in args])


def FindIdent(value: int, pattern: Optional[str] = None):
    for key, val in c4d.__dict__.items():
        if val != value:
            continue
        if pattern and re.search(pattern, key):
            return f"c4d.{key}"
        if pattern is None:
            return f"c4d.{key}"


def Dict2Str(data: dict, indent=2, depth=0):
    newline = any(isinstance(v, (dict, list)) for v in data.values())
    newline = newline or any(isinstance(v, Val) and type(v.dummy) == dict for v in data.values())
    newline = newline or len(data.keys()) > 1
    output = "{\n" if newline else "{"
    for key, val in data.items():
        s = " " * indent * (depth + 1) if newline else " "
        e = ",\n" if newline else " "
        if type(val) == dict:
            val = Dict2Str(val, indent, depth + 1)
        elif isinstance(val, Val) and type(val.dummy) == dict:
            val = Dict2Str(val.dummy, indent, depth + 1)
        elif isinstance(val, Val) and type(val.dummy) == list:
            val = List2Str(val.dummy, indent, depth + 1)
        elif isinstance(val, list):
            val = List2Str(val, indent, depth + 1)
        elif type(val) == str:
            val = repr(val)
        if isinstance(key, Comment):
            output += f"{s}{key}\n"
            continue
        output += f"{s}{key!r}: {val}{e}"
    s = " " * indent * depth if newline else ""
    output += s + "}"
    return output


def List2Str(data: list, indent=2, depth=0):
    newline = any(isinstance(v, (tuple, list)) and len(v) > 2 for v in data)
    newline = any(isinstance(v, dict) for v in data)
    newline = newline or len(repr(data)) > 50
    output = "[\n" if newline else "["
    for i, item in enumerate(data):
        s = " " * indent * (depth + 1) if newline else ""
        e = ",\n" if newline else (", " if i < len(data) - 1 else "")
        if isinstance(item, dict):
            item = Dict2Str(item, indent, depth + 1)
        if isinstance(item, tuple):
            item = ", ".join(str(i) for i in item)
            item = f"({item})"
        output += f"{s}{item!s}{e}"
    s = " " * indent * depth if newline else ""
    output += s + "]"
    return output


if __name__ == "__main__":
    import importlib, c4djson.core
    importlib.reload(c4djson.core)
