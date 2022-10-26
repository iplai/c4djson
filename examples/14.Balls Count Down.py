from c4djson import *


if __name__ == "__main__":
    doc.Flush()
    t1 = 30  # frames balls down
    t2 = 15  # frames balls up
    n = 11  # Count down n - 1
    keyframes = []
    time = 0
    for i in range(n):
        keyframes.append((time, 10))
        time += t1
        if i != n - 1:
            keyframes.append((time, 0, c4d.CINTERPOLATION_STEP))
        time += t2

    tree = Tree({
        O.connector: {
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.MODE_OFF,
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.MODE_OFF,
            O.mgtext: {
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): 100,
                c4d.PRIM_TEXT_ALIGN: c4d.PRIM_TEXT_ALIGN_MIDDLE,
                c4d.PRIM_TEXT_TEXT: [
                    (i * (t1 + t2), str(n - 1 - i)) for i in range(n)
                ],
            }
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.connector,
            c4d.MG_POLY_MODE_: c4d.MG_POLY_MODE_VOLUME,
            c4d.MG_POLYVOLUME_COUNT: 160,
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgrandom],
            T.dynamicsbody: {
                c4d.RIGID_BODY_LINEAR_FOLLOW_STRENGTH: keyframes
            },
            O.sphere: {
                c4d.PRIM_SPHERE_RAD: 5,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            }
        },
        O.mgrandom: {  # Random scale with color
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
            c4d.ID_MG_BASEEFFECTOR_USCALE: 0.2,
            c4d.ID_MG_BASEEFFECTOR_COLOR_MODE: c4d.ID_MG_BASEEFFECTOR_COLOR_MODE_EFFECTOR,
            c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND: c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND_ADD,
        },
        O.plane: {
            T.dynamicsbody: {c4d.RIGID_BODY_DYNAMIC: c4d.RIGID_BODY_DYNAMIC_OFF}
        }
    }).load().print()
    Command.unfoldall()
    doc.SetMaxTime(c4d.BaseTime(time, doc.GetFps()))
    # Bullet steps per frame
    doc.FindSceneHook(180000100)[c4d.WORLD_SUBSTEPS] = 15
