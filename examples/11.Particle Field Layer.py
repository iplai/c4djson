from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.plane: {
            (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): -5,
            T.dynamicsbody: {c4d.RIGID_BODY_DYNAMIC: c4d.RIGID_BODY_DYNAMIC_OFF},
        },
        O.particle: {
            (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y): 90,
            c4d.PARTICLEOBJECT_STOP: 300,
            c4d.PARTICLEOBJECT_SPEED: 0.0,
            c4d.PARTICLEOBJECT_SIZEX: 200.0,
            c4d.PARTICLEOBJECT_SIZEY: 200.0,
        },
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
            c4d.ID_MG_BASEEFFECTOR_USCALE: 1.0,
            c4d.ID_MG_BASEEFFECTOR_COLOR_ALPHA: True,
            c4d.ID_MG_BASEEFFECTOR_CLONE: 0.8,
            c4d.FIELDS: {
                FL.particleobject: {
                    c4d.FIELDLAYER_PARTICLE_OBJECT: O.particle,
                    c4d.FIELD_COLOR_MODE: c4d.FIELD_COLOR_MODE_COLOR,
                    c4d.FIELD_COLOR: (100, 200, 20),
                },
            },
        },
        O.mgcloner: {
            c4d.MGCLONER_MODE: c4d.MGCLONER_MODE_SORT,
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain],
            c4d.MG_GRID_RESOLUTION: (20, 1, 20),
            c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
            c4d.MG_GRID_SIZE: (12, 12, 12),
            c4d.ID_MG_TRANSFORM_COLOR: (182, 80, 128),
            T.dynamicsbody: {},
            O.cube: {
                c4d.PRIM_CUBE_LEN: (10, 10, 10),
                c4d.PRIM_CUBE_FRAD: 0.2,
                c4d.PRIM_CUBE_DOFILLET: True,
                c4d.PRIM_CUBE_SEP: True,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
            O.platonic: {
                c4d.PRIM_PLATONIC_RAD: 8,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
                O.bevel: {c4d.O_BEVEL_RADIUS: 0.1, },
            },
        },
    })
    doc.Flush()
    tree.load().print()
    Command.unfoldall()
    # Command.playforward()()
