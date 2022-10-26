from c4djson import *


if __name__ == "__main__":
    n = 12
    sep_max = 20
    sep_min = 6
    tree = Tree({
        O.null @ "Fold Door": {
                T.expresso: {
                    # Xpresso graph content not supported yet
                },
                c4d.ID_USERDATA: {
                    "Fold Door": {
                        "Offset": {
                            c4d.DTYPE_: c4d.DTYPE_REAL,
                            c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                            c4d.DESC_UNIT: c4d.DESC_UNIT_REAL,
                            c4d.DESC_DEFAULT: sep_max * (n - 1),
                            c4d.DESC_MINSLIDER: sep_min * (n - 1),
                            c4d.DESC_MAXSLIDER: sep_max * (n - 1),
                            c4d.DESC_STEP: 0.01,
                        },
                    },
                },
                O.null @ "Points": {
                    O.null @ f"Point {i}": {
                        (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Z): i * sep_max,
                        c4d.NULLOBJECT_DISPLAY: c4d.NULLOBJECT_DISPLAY_CIRCLE,
                        c4d.NULLOBJECT_RADIUS: 2,
                        c4d.ID_BASEOBJECT_USECOLOR: c4d.ID_BASEOBJECT_USECOLOR_AUTOMATIC,
                        c4d.ID_BASEOBJECT_COLOR: (255, 0, 0),
                    } for i in range(n)
                },
                },
    })
    doc.Flush()
    tree.load().print()
    Command.unfoldall()

    root: c4d.BaseObject = tree[O.null @ "Fold Door"]
    # xpressoTag = c4d.modules.graphview.XPressoTag()
    # root.InsertTag(xpressoTag)
    xpressoTag: c4d.modules.graphview.XPressoTag = root.GetTag(c4d.Texpresso)
    gvNodeMaster = xpressoTag.GetNodeMaster()
    gvRoot = gvNodeMaster.GetRoot()
    gvnode_object_root = gvNodeMaster.CreateNode(gvRoot, c4d.ID_OPERATOR_OBJECT, x=10, y=30)

    port_userdata_slider = gvnode_object_root.AddPort(
        c4d.GV_PORT_OUTPUT, root.GetUserDataContainer()[1][0], message=True)

    gvnode_object_last_point = gvNodeMaster.CreateNode(gvRoot, c4d.ID_OPERATOR_OBJECT, x=160, y=30)
    gvnode_object_last_point[c4d.GV_OBJECT_OBJECT_ID] = tree[O.null @ f"Point {n-1}"]
    port_last_point_pos_z = gvnode_object_last_point.AddPort(
        c4d.GV_PORT_INPUT, c4d.DescID(*[c4d.DescLevel(i) for i in (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Z)]), message=True)

    port_userdata_slider.Connect(port_last_point_pos_z)

    node_iteration = gvNodeMaster.CreateNode(gvRoot, c4d.ID_OPERATOR_ITERATE, x=10, y=130)
    node_iteration[c4d.GV_ITERATE_INPUT_UPPER] = n - 2

    node_linklist_up = gvNodeMaster.CreateNode(gvRoot, c4d.ID_OPERATOR_LINK, x=240, y=130)
    container = c4d.InExcludeData()
    for point in tree[O.null @ f"Points"].GetChildren()[-1:0:-1]:
        container.InsertObject(point, 1)
    node_linklist_up[c4d.GV_LINK_LIST] = container

    node_iteration.GetOutPort(0).Connect(node_linklist_up.GetInPort(0))

    node_linklist_down = gvNodeMaster.CreateNode(gvRoot, c4d.ID_OPERATOR_LINK, x=240, y=230)
    container = c4d.InExcludeData()
    for point in tree[O.null @ f"Points"].GetChildren()[-2::-1]:
        container.InsertObject(point, 1)
    node_linklist_down[c4d.GV_LINK_LIST] = container

    node_iteration.GetOutPort(0).Connect(node_linklist_down.GetInPort(0))

    node_object_iterated_point = gvNodeMaster.CreateNode(gvRoot, c4d.ID_OPERATOR_OBJECT, x=450, y=230)
    node_object_iterated_point[c4d.GV_OBJECT_OBJECT_ID] = tree[O.null @ f"Point 0"]
    port_iterated_point_object = node_object_iterated_point.AddPort(
        c4d.GV_PORT_INPUT, c4d.GV_OBJECT_OPERATOR_OBJECT_IN, message=True)
    port_iterated_point_pos_z = node_object_iterated_point.AddPort(
        c4d.GV_PORT_INPUT, c4d.DescID(*[c4d.DescLevel(i) for i in (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Z)]), message=True)

    node_linklist_down.GetOutPort(0).Connect(port_iterated_point_object)

    node_python = gvNodeMaster.CreateNode(gvRoot, c4d.GVpython, x=400, y=130)
    node_python.RemoveUnusedPorts()
    node_python[
        c4d.GV_PYTHON_CODE
    ] = """
from typing import Optional
import c4d, math

def main() -> None:
    global z2, mid_z, mid_x
    z1 = Input1[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z]
    z2 = Input2[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z]
    d = z1 - z2
    if d < 6:
        z2 = z1 - 6
    if d > 20:
        z2 = z1 - 20
    mid_z = (z1 + z2) / 2
    mid_x = math.sqrt(200 - (z1 -mid_z) ** 2)
    """
    port_python_link_1 = node_python.AddPort(
        1, c4d.DescID(c4d.DescLevel(c4d.IN_LINK, c4d.DTYPE_BASELISTLINK, c4d.GVpython)), message=True)
    port_python_link_1.SetName("Input1")
    port_python_link_2 = node_python.AddPort(
        1, c4d.DescID(c4d.DescLevel(c4d.IN_LINK, c4d.DTYPE_BASELISTLINK, c4d.GVpython)), message=True)
    port_python_link_2.SetName("Input2")
    node_linklist_up.GetOutPort(0).Connect(port_python_link_1)
    node_linklist_down.GetOutPort(0).Connect(port_python_link_2)

    port_python_z2 = node_python.AddPort(2, c4d.DescID(c4d.DescLevel(
        c4d.OUT_REAL, c4d.ID_GV_DATA_TYPE_REAL, c4d.GVpython)), message=True)
    port_python_z2.SetName("z2")

    port_python_z2.Connect(port_iterated_point_pos_z)
