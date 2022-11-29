from c4djson.core import *


if __name__ == "__main__":
    tree = Tree({
        O.mgcloner: {
            # Clones: Blend
            c4d.MGCLONER_MODE: c4d.MGCLONER_MODE_BLEND,
            # Count
            c4d.MG_GRID_RESOLUTION: (20, 20, 1),
            c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
            c4d.MG_GRID_SIZE: (30, 20, 0),
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain],
            O.splinetext: {
                # Text Spline
                c4d.PRIM_TEXT_TEXT: '0',
                c4d.PRIM_TEXT_ALIGN: c4d.PRIM_TEXT_ALIGN_MIDDLE,
                c4d.PRIM_TEXT_HEIGHT: 10,
            },
            O.splinetext: {
                # Text Spline
                c4d.PRIM_TEXT_TEXT: '1',
                c4d.PRIM_TEXT_ALIGN: c4d.PRIM_TEXT_ALIGN_MIDDLE,
                c4d.PRIM_TEXT_HEIGHT: 10,
            },
        },
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            # Modify Clone
            c4d.ID_MG_BASEEFFECTOR_CLONE: 1,
            c4d.FIELDS: {
                FL.field: {
                    c4d.ID_FIELDLAYER_BLENDINGMODE: c4d.ID_FIELDLAYER_BLENDINGMODE_ADD,
                    c4d.ID_FIELDLAYER_LINK: F.box,
                },
                FL.field: {
                    c4d.ID_FIELDLAYER_BLENDINGMODE: c4d.ID_FIELDLAYER_BLENDINGMODE_ADD,
                    c4d.ID_FIELDLAYER_LINK: F.spherical,
                },
                FL.field: {
                    c4d.ID_FIELDLAYER_BLENDINGMODE: c4d.ID_FIELDLAYER_BLENDINGMODE_ADD,
                    c4d.ID_FIELDLAYER_LINK: F.torus,
                },
            },
            F.box: {
                c4d.FIELD_BOX_SIZE: (50,),
                c4d.FIELD_COLOR: (18, 195, 62),
                T.vibrate: {
                    c4d.VIBRATEEXPRESSION_SEED: 1,
                    # Enable Position
                    c4d.VIBRATEEXPRESSION_POS_ENABLE: True,
                    # Position Amplitude.Y
                    (c4d.VIBRATEEXPRESSION_POS_AMPLITUDE, c4d.VECTOR_Y): 100,
                    # Position Frequency
                    c4d.VIBRATEEXPRESSION_POS_FREQUENCY: 1.5,
                },
            },
            F.spherical: {
                c4d.SPHERICAL_SIZE: 50,
                c4d.FIELD_COLOR: (18, 195, 62),
                T.vibrate: {
                    c4d.VIBRATEEXPRESSION_SEED: 2,
                    # Enable Position
                    c4d.VIBRATEEXPRESSION_POS_ENABLE: True,
                    # Position Amplitude.Y
                    (c4d.VIBRATEEXPRESSION_POS_AMPLITUDE, c4d.VECTOR_Y): 100,
                    # Position Frequency
                    c4d.VIBRATEEXPRESSION_POS_FREQUENCY: 1.5,
                },
            },
            F.torus: {
                c4d.FIELD_TORUS_DIRECTION: c4d.FIELD_TORUS_DIRECTION_ZP,
                c4d.FIELD_COLOR: (18, 195, 62),
                T.vibrate: {
                    c4d.VIBRATEEXPRESSION_SEED: 3,
                    # Enable Position
                    c4d.VIBRATEEXPRESSION_POS_ENABLE: True,
                    # Position Amplitude.Y
                    (c4d.VIBRATEEXPRESSION_POS_AMPLITUDE, c4d.VECTOR_Y): 100,
                    # Position Frequency
                    c4d.VIBRATEEXPRESSION_POS_FREQUENCY: 0.5,
                },
            },
        },
    })
    doc.Flush()
    tree.load()
