"""
Author: Dale Chan
Name-en-US: Dump Document
Description-en-US: Dump and print json from doc with selected active object (in hierarchy) and selected meterials
"""
import c4d
from c4djson.node import Node, Param
from c4djson.nodetype import Type
from c4djson.tree import dict2str, get_ident


def dump(ident=True):
    """Dump and print json from doc with selected object(in hierarchy) and selected meterials"""
    data = {}
    doc = c4d.documents.GetActiveDocument()
    op = doc.GetActiveObject()
    materials = doc.GetActiveMaterials()
    if op is not None:
        data |= parse_node(op, doc)
    for mat in materials:
        data |= parse_material(mat, doc)
    data = collapse_branches(data)
    print(dict2str(data, ident=ident))


#  DataTag in Cloner, VariableTag in Particle Emitter
_tids_not_to_parse = [
    c4d.ID_MOTAGDATA, c4d.Tparticle, c4d.Tcacheproxytagpolyselection, c4d.Tcacheproxytagedgeselection,
    c4d.Tpoint, c4d.Ttangent
]


def parse_node(obj: c4d.BaseList2D, doc):
    if obj.GetType() in _tids_not_to_parse:
        return {}
    nodetype = Type.find(obj.GetType())
    if nodetype is None:
        return {}
    node = Node(nodetype)
    if node.raw is None:
        return {}
    node.obj, node.name = obj, obj.GetName().replace(" . ", ".")
    data = {node: parse_params(node, doc)}
    data[node] |= parse_userdata(node, doc)
    if node.type.value == c4d.CTbase:
        data = parse_track(node, doc) | data
        if not data[node]:  # if a track node has no param to set, delete it
            data.pop(node)
            return data
    branches = obj.GetBranchInfo(c4d.GETBRANCHINFO_ONLYWITHCHILDREN) or []
    branchdata: dict
    for branchdata in branches:
        gelisthead: c4d.GeListHead = branchdata.get("head")
        branchid: int = branchdata.get("id")
        branchname: str = branchdata.get("name", f"Branch:{branchid}")
        child = gelisthead.GetDown()
        if child is None:
            continue
        data[node][branchname] = {}
        while child is not None:
            if isinstance(child, c4d.BaseTag):  # reverse the sequence for tags
                data[node][branchname] = parse_node(child, doc) | data[node][branchname]
            else:
                data[node][branchname] |= parse_node(child, doc)
            child = child.GetNext()
        if len(data[node][branchname]) == 0:
            data[node].pop(branchname, None)
    if isinstance(obj, c4d.BaseObject):
        for child in obj.GetChildren():
            data[node] |= parse_node(child, doc)
    return data


interpolation_dict = {
    c4d.CINTERPOLATION_SPLINE: str("c4d.CINTERPOLATION_SPLINE"),
    c4d.CINTERPOLATION_LINEAR: str("c4d.CINTERPOLATION_LINEAR"),
    c4d.CINTERPOLATION_STEP: "c4d.CINTERPOLATION_STEP",
}


def parse_material(mat: c4d.BaseMaterial, doc):
    return parse_node(mat, doc)


def _descid_d1(*args):
    return c4d.DescID(c4d.DescLevel(*args))


_black_list = [
    _descid_d1(900, 130, 110050),               # c4d.ID_BASELIST_NAME,
    _descid_d1(1041671, 3, 110050),             # c4d.ID_BASELIST_ICON_COLOR,
    _descid_d1(910, 23, 5155),                  # c4d.ID_BASEOBJECT_GLOBAL_POSITION,
    _descid_d1(925, 23, 5155),                  # c4d.ID_BASEOBJECT_ABS_POSITION,
    _descid_d1(911, 23, 5155),                  # c4d.ID_BASEOBJECT_GLOBAL_ROTATION,
    _descid_d1(926, 23, 5155),                  # c4d.ID_BASEOBJECT_ABS_ROTATION,
    _descid_d1(1204, 19, 1000988),              # c4d.PRIM_REGULARWIDTH,
    _descid_d1(901, 3, 5350),                   # c4d.ID_CTRACK_FCURVE_COLOR
    _descid_d1(200000029, 200000027, 1001074),  # c4d.ID_MATERIALASSIGNMENTS,
    _descid_d1(1204, 400006001, 431000028),     # c4d.O_BEVELL_SHAPING_CONSTANT,
]
_white_list = [  # No matter whether the param is same as it's default, dump it.
    _descid_d1(1204, 15, 1018583),              # c4d.MG_GRID_MODE,
]
_dynamic_defaults = [
    (_descid_d1(1016, 400006001, 1018740), 1),  # c4d.MG_OBJECT_ALIGN
    (_descid_d1(1102, 15, 1018571), 6),         # c4d.MG_POLY_UPVECTOR
    (_descid_d1(1106, 19, 1018571), 1),         # c4d.MG_POLY_SCALEONPOLY_AMOUNT
    (_descid_d1(1122, 19, 1018573), 0.5),       # c4d.MG_POLYEDGE_OFFSET
    (_descid_d1(1121, 19, 1018573), 0.5),       # c4d.MG_POLYEDGE_SCALE
    (_descid_d1(1104, 400006001, 1018571), 1),  # c4d.MG_POLY_SELECTION_ACTIVE
]


def check_dynamic_default(descid: c4d.DescID, node: Node):
    for id, val in _dynamic_defaults:
        if descid == id and node.obj[descid] == val:
            return True
    return False


def parse_params(node: Node, doc):
    data = {}
    bc: c4d.BaseContainer
    descid: c4d.DescID
    for bc, descid, _ in node.obj.GetDescription(c4d.DESCFLAGS_DESC_NONE):
        if descid.GetDepth() == 0:
            continue
        # if descid[0].id == c4d.MG_GRID_MODE:
        #     print(bc[c4d.DESC_NAME], descid)
        if any(descid == id for id in _black_list):
            continue
        if not any(descid == id for id in _white_list):
            try:
                if node.obj[descid] == node.raw[descid]:
                    continue
            except AttributeError:
                continue
        if check_dynamic_default(descid, node):
            continue
        param = Param(descid, bc)
        if not param.ident:
            continue
        val = convert_value(param, node.obj[descid], doc)
        if val is not None:
            data[param] = val
    return data


def convert_value(param: Param, val, doc: c4d.documents.BaseDocument):
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
        val = val.x, val.y, val.z
    if isinstance(val, c4d.BaseList2D):
        nodetype = Type.find(val.GetType())
        if nodetype is not None:
            node = Node(nodetype)
            node.obj, node.name = val, val.GetName()
            val = node
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
            nodetype = Type.find(obj.GetType())
            if nodetype is not None:
                node = Node(nodetype)
                node.obj, node.name = obj, obj.GetName()
                val.append(node)
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
                result |= parse_node(child, doc)
                child = child.GetNext()
            val = result
    if isinstance(val, tuple) and all(isinstance(i, (int, float)) for i in val):
        if param[c4d.DESC_UNIT] == c4d.DESC_UNIT_REAL:
            if param[c4d.DESC_STEP] == c4d.Vector(1, 1, 1):
                val = tuple(round(i) for i in val)
        if val.count(val[0]) == len(val):
            val = (val[0],)
    return val


def parse_track(node: Node, doc: c4d.documents.BaseDocument):
    fps = doc.GetFps()
    track: c4d.CTrack = node.obj
    track_cate = track.GetTrackCategory()
    descid = track.GetDescriptionID()
    bc = track.GetObject().GetDescription(c4d.DESCFLAGS_DESC_NONE).GetParameter(descid)
    param = Param(descid, bc)
    if descid.GetDepth() == 2:
        descid_0 = c4d.DescID(descid[0].id)
        bc_0 = track.GetObject().GetDescription(c4d.DESCFLAGS_DESC_NONE).GetParameter(descid_0)
        if not param.ident:
            param.ident = descid[1].id
        param.ident = f"(c4d.{bc_0[c4d.DESC_IDENT]}, {param.ident})"
    val = []
    curve = track.GetCurve()
    for i in range(curve.GetKeyCount()):
        key = curve.GetKey(i)
        frame = key.GetTime().GetFrame(fps)
        value = key.GetGeData() if track_cate == c4d.CTRACK_CATEGORY_DATA else key.GetValue()
        value = convert_value(param, value, doc)
        interpolation = key.GetInterpolation()
        if interpolation != c4d.CINTERPOLATION_SPLINE:
            interpolation = interpolation_dict[interpolation]
            val.append((frame, value, interpolation))
        else:
            val.append((frame, value))
    return {param: val}


def find_parent(data: dict[Param, dict], descid: c4d.DescID):
    if descid == c4d.DescID(0):
        return data
    for param, pdata in data.items():
        if param.descid == descid:
            return pdata
        else:
            return find_parent(pdata, descid)


def parse_userdata(node: Node, doc: c4d.documents.BaseDocument):
    if not node.obj.GetUserDataContainer():
        return {}
    data = {"c4d.ID_USERDATA": {}}
    descid: c4d.DescID
    for descid, bc in node.obj.GetUserDataContainer():
        param = Param(descid, bc)
        parent = find_parent(data["c4d.ID_USERDATA"], bc[c4d.DESC_PARENTGROUP])
        parent[param] = {}
        if param[c4d.DTYPE_] != c4d.DTYPE_GROUP:
            parent[param]["c4d.DTYPE_"] = get_ident(descid[1].dtype, "DTYPE_")
            for key, val in bc:
                ident = get_ident(key, "DESC_")
                if key == c4d.DESC_UNIT:
                    parent[param][ident] = get_ident(val, "DESC_UNIT_") or val
                elif key == c4d.DESC_CUSTOMGUI:
                    parent[param][ident] = get_ident(val, "CUSTOMGUI_") or val
                elif key == c4d.DESC_MINSLIDER:
                    parent[param][ident] = convert_value(param, val, doc)
                elif key == c4d.DESC_MAXSLIDER:
                    parent[param][ident] = convert_value(param, val, doc)
                elif key == c4d.DESC_STEP:
                    parent[param][ident] = convert_value(param, val, doc)
                elif key == c4d.DESC_DEFAULT:
                    parent[param][ident] = convert_value(param, val, doc)
                elif key == c4d.DESC_CYCLE:
                    val: c4d.BaseContainer
                    parent[param][ident] = {k: v for k, v in val}
                else:
                    parent[param][ident or key] = val
    return userdata2dict(data)


def userdata2dict(data: dict):
    """Convert param to repr(param.name)"""
    result = {}
    for key, val in data.items():
        if isinstance(key, Param):
            key = repr(key.name)
        if isinstance(val, dict):
            val = userdata2dict(val)
        result[key] = val
    return result


def collapse_branches(data: dict):
    result = {}
    for key, val in data.items():
        # if key in ["Tracks"]:
        #     continue
        if key in ["Tags", "Shaders", "Tracks"] and type(val) == dict:
            result |= collapse_branches(val)
            continue
        if type(val) == dict:
            result[key] = collapse_branches(val)
            continue
        result[key] = val
    return result


if __name__ == "__main__":
    dump(ident=True)
