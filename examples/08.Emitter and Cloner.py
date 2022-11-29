from c4djson.core import *

doc.Flush()

if __name__ == "__main__":
    tree = Tree({
        O.particle @ 'Source': {
            # Birthrate Viewport
            c4d.PARTICLEOBJECT_BIRTHEDITOR: 20,
            # Birthrate Renderer
            c4d.PARTICLEOBJECT_BIRTHRAYTRACER: 20,
            c4d.PARTICLEOBJECT_SPEED: 0,
            # X-Size
            c4d.PARTICLEOBJECT_SIZEX: 10,
            # Y-Size
            c4d.PARTICLEOBJECT_SIZEY: 10,
            # Angle Horizontal
            c4d.PARTICLEOBJECT_ANGLEH: 360,
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.particle @ 'Source',
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgrandom @ 'Random Effector'],
            # Random Effector
            1500: 1,
            T.dynamicsbody: {
                # Follow Position
                c4d.RIGID_BODY_LINEAR_FOLLOW_STRENGTH: 10,
            },
            O.sphere: {
                # Radius
                c4d.PRIM_SPHERE_RAD: 10,
                c4d.PRIM_SPHERE_TYPE: c4d.PRIM_SPHERE_TYPE_HEXA,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
        },
        O.mgrandom @ 'Random Effector': {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
            c4d.ID_MG_BASEEFFECTOR_USCALE: 0.5,
            # Color Mode: Effector Color
            c4d.ID_MG_BASEEFFECTOR_COLOR_MODE: c4d.ID_MG_BASEEFFECTOR_COLOR_MODE_EFFECTOR,
            # Use Alpha/Strength
            c4d.ID_MG_BASEEFFECTOR_COLOR_ALPHA: True,
            # Blending Mode: Add
            c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND: c4d.ID_MG_BASEEFFECTOR_COLOR_BLEND_ADD,
        },
    })
    tree.load()
