from c4djson.core import *


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
            # Viewport Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
            # Renderer Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
            O.mgtext: {
                # Position.Y
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): 100,
                # Animated Text Spline
                c4d.PRIM_TEXT_TEXT: [
                    (i * (t1 + t2), str(n - 1 - i)) for i in range(n)
                ],
                c4d.PRIM_TEXT_ALIGN: c4d.PRIM_TEXT_ALIGN_MIDDLE,
            }
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.connector,
            # Distribution: Volume
            c4d.MG_POLY_MODE_: c4d.MG_POLY_MODE_VOLUME,
            c4d.MG_POLYVOLUME_COUNT: 160,
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgrandom],
            T.dynamicsbody: {
                # Animated Follow Position
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
            # Color Mode: Effector Color
            c4d.ID_MG_BASEEFFECTOR_COLOR_MODE: c4d.ID_MG_BASEEFFECTOR_COLOR_MODE_EFFECTOR,
            # Use Alpha/Strength
            c4d.ID_MG_BASEEFFECTOR_COLOR_ALPHA: True,
            # Blending Mode: Add
            c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND: c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND_ADD,
        },
        O.plane: {
            T.dynamicsbody: {c4d.RIGID_BODY_DYNAMIC: c4d.RIGID_BODY_DYNAMIC_OFF}
        }
    }).load()
    doc.SetMaxTime(c4d.BaseTime(time, doc.GetFps()))
    # Bullet steps per frame
    doc.FindSceneHook(180000100)[c4d.WORLD_SUBSTEPS] = 15
