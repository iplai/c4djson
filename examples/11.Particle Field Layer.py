from c4djson.core import *

if __name__ == "__main__":
    tree = Tree({
        O.plane: {
            # Position.Y
            (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): -5,
            T.dynamicsbody: {c4d.RIGID_BODY_DYNAMIC: c4d.RIGID_BODY_DYNAMIC_OFF},
        },
        O.particle: {
            # Rotation.P
            (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y): 270,
            # Birthrate Viewport
            c4d.PARTICLEOBJECT_BIRTHEDITOR: 2,
            # Birthrate Renderer
            c4d.PARTICLEOBJECT_BIRTHRAYTRACER: 2,
            # Start Emission
            c4d.PARTICLEOBJECT_START: 25,
            # Stop Emission
            c4d.PARTICLEOBJECT_STOP: 300,
            c4d.PARTICLEOBJECT_SPEED: 0,
            # X-Size
            c4d.PARTICLEOBJECT_SIZEX: 220,
            # Y-Size
            c4d.PARTICLEOBJECT_SIZEY: 220,
        },
        O.particle @ 'Emitter Dummy': {
            # Position.Y
            (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): 100,
            # Rotation.P
            (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y): 270,
            # Birthrate Viewport
            c4d.PARTICLEOBJECT_BIRTHEDITOR: 2,
            # Birthrate Renderer
            c4d.PARTICLEOBJECT_BIRTHRAYTRACER: 2,
            # Stop Emission
            c4d.PARTICLEOBJECT_STOP: 300,
            c4d.PARTICLEOBJECT_SPEED: 100,
            # X-Size
            c4d.PARTICLEOBJECT_SIZEX: 220,
            # Y-Size
            c4d.PARTICLEOBJECT_SIZEY: 220,
        },
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
            c4d.ID_MG_BASEEFFECTOR_USCALE: 1,
            # Use Alpha/Strength
            c4d.ID_MG_BASEEFFECTOR_COLOR_ALPHA: True,
            # Modify Clone
            c4d.ID_MG_BASEEFFECTOR_CLONE: 0.8,
            c4d.FIELDS: {
                FL.particleobject: {
                    # Particle Object
                    c4d.FIELDLAYER_PARTICLE_OBJECT: O.particle,
                    # Color Mode: Color
                    c4d.FIELD_COLOR_MODE: c4d.FIELD_COLOR_MODE_COLOR,
                    c4d.FIELD_COLOR: (100, 200, 20),
                },
            },
        },
        O.mgcloner: {
            # Clones: Sort
            c4d.MGCLONER_MODE: c4d.MGCLONER_MODE_SORT,
            # Instance Mode: Multi-Instance
            c4d.MGCLONER_VOLUMEINSTANCES_MODE: c4d.MGCLONER_VOLUMEINSTANCES_MODE_RENDERMULTIINSTANCE,
            # Count
            c4d.MG_GRID_RESOLUTION: (20, 1, 20),
            c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
            c4d.MG_GRID_SIZE: (12,),
            c4d.ID_MG_TRANSFORM_COLOR: (182, 80, 128),
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain],
            T.dynamicsbody: {},
            O.cube: {
                # Size
                c4d.PRIM_CUBE_LEN: (10,),
                # Separate Surfaces
                c4d.PRIM_CUBE_SEP: True,
                c4d.PRIM_CUBE_DOFILLET: True,
                # Fillet Radius
                c4d.PRIM_CUBE_FRAD: 1,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
            O.platonic: {
                # Radius
                c4d.PRIM_PLATONIC_RAD: 8,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
                O.bevel: {
                    # Offset
                    c4d.O_BEVEL_RADIUS: 0.5,
                },
            },
        },
    })
    doc.Flush()
    tree.load()
