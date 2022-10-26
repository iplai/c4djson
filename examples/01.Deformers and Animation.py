from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.null @ "Deformed Cylinder": {
            O.sds: {
                c4d.SDSOBJECT_TYPE: c4d.SDSOBJECT_TYPE_OSD_BILINEAR,
                c4d.SDSOBJECT_SUBEDITOR_CM: 1,
                c4d.SDSOBJECT_SUBRAY_CM: 1,
                O.cylinder: {
                    c4d.PRIM_CYLINDER_RADIUS: 20,
                    c4d.PRIM_CYLINDER_HEIGHT: 200,
                    c4d.PRIM_CYLINDER_HSUB: 20,
                    c4d.PRIM_CYLINDER_SEG: 3,
                    c4d.PRIM_CYLINDER_CAPS: False,
                    # Animate H Rotation
                    (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_X): [(0, 0), (90, 360)],
                    T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
                },
            },
            O.twist: {
                c4d.DEFORMOBJECT_SIZE: (40, 200, 40),
                c4d.DEFORMOBJECT_ANGLE: 360,
            },
            O.bend: {
                c4d.DEFORMOBJECT_SIZE: (40, 200, 40),
                c4d.DEFORMOBJECT_STRENGTH: 360,
            },
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.sds,
            c4d.MG_POLY_MODE_: c4d.MG_POLY_MODE_EDGE,
            O.sphere: {
                c4d.PRIM_SPHERE_RAD: 5,
                c4d.PRIM_SPHERE_SUB: 24,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
        },
    })
    doc.Flush()
    tree.load().print()
    doc.SetSelection(tree[O.cylinder])
    Command.unfoldall()
