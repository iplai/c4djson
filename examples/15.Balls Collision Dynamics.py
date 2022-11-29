from c4djson.core import *


if __name__ == "__main__":
    tree = Tree({
        O.mgcloner: {
            # Count
            c4d.MG_GRID_RESOLUTION: (10, 3, 3),
            c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
            c4d.MG_GRID_SIZE: (20, 10, 10),
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain],
            T.dynamicsbody: {
                # Follow Position
                c4d.RIGID_BODY_LINEAR_FOLLOW_STRENGTH: 10,
            },
            O.sphere: {
                # Radius
                c4d.PRIM_SPHERE_RAD: 1,
                # Segments
                c4d.PRIM_SPHERE_SUB: 24,
                c4d.PRIM_SPHERE_TYPE: c4d.PRIM_SPHERE_TYPE_HEXA,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
        },
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
            c4d.ID_MG_BASEEFFECTOR_USCALE: 20,
            c4d.FIELDS: {
                FL.field: {c4d.ID_FIELDLAYER_LINK: F.spherical},
            },
            F.spherical: {
                # Viewport Visibility: Off
                c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
                # Renderer Visibility: Off
                c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
                c4d.SPHERICAL_SIZE: 120,
                c4d.FIELD_INNER_OFFSET: 0,
            },
        },
        O.sphere: {
            # Animated Position.X
            (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X): [
                (0, -200),
                (30, 200),
                {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OSCILLATE},
            ],
            # Radius
            c4d.PRIM_SPHERE_RAD: 60,
            # Segments
            c4d.PRIM_SPHERE_SUB: 36,
            c4d.PRIM_SPHERE_TYPE: c4d.PRIM_SPHERE_TYPE_HEXA,
            T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            T.dynamicsbody: {c4d.RIGID_BODY_DYNAMIC: c4d.RIGID_BODY_DYNAMIC_OFF},
        },
    })
    doc.Flush()
    tree.load()
