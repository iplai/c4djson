from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.extrude: {
            c4d.CAPSANDBEVELS_STARTBEVEL_OFFSET: 1,
            T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            O.connector: {
                O.splinerectangle: {
                    c4d.PRIM_RECTANGLE_WIDTH: 260,
                    c4d.PRIM_RECTANGLE_HEIGHT: 260,
                    c4d.PRIM_PLANE: c4d.PRIM_PLANE_XZ,
                },
                O.mgcloner: {
                    c4d.MG_GRID_RESOLUTION: (10, 1, 10),
                    c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
                    c4d.MG_GRID_SIZE: (25,),
                    O.splinecircle: {
                        c4d.PRIM_CIRCLE_RADIUS: 10,
                        c4d.PRIM_PLANE: c4d.PRIM_PLANE_XZ,
                    },
                },
            },
        },
        O.mgcloner: {
            c4d.ID_BASEOBJECT_REL_POSITION: (0, -100, 0),
            c4d.MG_GRID_RESOLUTION: (10, 1, 10),
            c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
            c4d.MG_GRID_SIZE: (25,),
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgshader],
            T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            O.sphere: {c4d.PRIM_SPHERE_RAD: 8},
        },
        O.mgshader: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: True,
            (c4d.ID_MG_BASEEFFECTOR_POSITION, c4d.VECTOR_Y): 200,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_COLOR_ALPHA: True,
            c4d.ID_MG_SHADER_SHADER: X.noise,
            X.noise: {
                c4d.SLA_NOISE_ANI_SPEED: 2,
                c4d.SLA_NOISE_TIMEPERIOD: 3,
            },
        },
    })
    doc.Flush()
    tree.load().print()
    Command.unfoldall()
