from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.extrude: {
            c4d.EXTRUDEOBJECT_EXTRUSIONOFFSET: 0,
            c4d.CAPSANDBEVELS_CAP_TYPE: c4d.CAPSANDBEVELS_CAP_TYPE_REGULAR,
            c4d.CAPSANDBEVELS_CAP_REGULAR_SIZE: 5,
            c4d.CAPSANDBEVELS_CAP_DELAUNAY_QUAD: True,
            T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            O.splinecircle: {
                c4d.PRIM_CIRCLE_RADIUS: 200,
                c4d.PRIM_PLANE: c4d.PRIM_PLANE_XZ,
            },
            O.cacollision: {
                c4d.ID_CA_COLLISION_DEFORMER_OBJECT_COLLIDERS: [O.mgcloner],
                c4d.ID_CA_COLLISION_DEFORMER_OBJECT_SIZE: 2,
            },
            O.cajiggle: {},
        },
        O.null @ 'Bubbles': {
            O.particle: {
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): -100,
                (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y): 90,
                c4d.PARTICLEOBJECT_SPEED: 120,
                c4d.PARTICLEOBJECT_SIZEX: 200,
                c4d.PARTICLEOBJECT_SIZEY: 200,
            },
            O.turbulence: {c4d.TURBULENCEOBJECT_STRENGTH: 20},
            O.mgcloner: {
                c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
                c4d.MG_OBJECT_LINK: O.particle,
                c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgrandom],
                O.sphere: {
                    c4d.PRIM_SPHERE_RAD: 20,
                    c4d.PRIM_SPHERE_TYPE: c4d.PRIM_SPHERE_TYPE_HEXA,
                    T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
                },
            },
            O.mgrandom: {
                c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
                c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
                c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
                c4d.ID_MG_BASEEFFECTOR_USCALE: 0.2,
                c4d.ID_MG_BASEEFFECTOR_COLOR_MODE: c4d.ID_MG_BASEEFFECTOR_COLOR_MODE_EFFECTOR,
                c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND: c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND_ADD,
            },
        },
    })
    tree.load().print()
    Command.unfoldall()
