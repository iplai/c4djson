from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.particle @ "Source": {
            c4d.PARTICLEOBJECT_BIRTHEDITOR: 20,
            c4d.PARTICLEOBJECT_BIRTHRAYTRACER: 20,
            c4d.PARTICLEOBJECT_SPEED: 0,
            c4d.PARTICLEOBJECT_SIZEX: 10,
            c4d.PARTICLEOBJECT_SIZEY: 10,
            c4d.PARTICLEOBJECT_ANGLEH: 360,
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.particle @ "Source",
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgrandom @ "Random Effector"],
            T.dynamicsbody: {
                c4d.RIGID_BODY_LINEAR_FOLLOW_STRENGTH: 10,
            },
            O.sphere: {
                c4d.PRIM_SPHERE_RAD: 10,
                c4d.PRIM_SPHERE_TYPE: c4d.PRIM_SPHERE_TYPE_HEXA,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
        },
        O.mgrandom @ "Random Effector": {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
            c4d.ID_MG_BASEEFFECTOR_USCALE: 0.5,
            c4d.ID_MG_BASEEFFECTOR_COLOR_MODE: c4d.ID_MG_BASEEFFECTOR_COLOR_MODE_EFFECTOR,
            c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND: c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND_ADD,
        },
    })
    tree.load().print()
    Command.unfoldall()
    # Command.playforward()
