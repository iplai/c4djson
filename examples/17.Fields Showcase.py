from c4djson import *


if __name__ == "__main__":
    tree = Tree({
        O.mgcloner: {
            c4d.MG_GRID_RESOLUTION: (20, 20, 1),
            c4d.MGCLONER_MODE: c4d.MGCLONER_MODE_BLEND,
            c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
            c4d.MG_GRID_SIZE: (30, 20, 0),
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain],
            O.splinetext: {
                c4d.PRIM_TEXT_TEXT: "0",
                c4d.PRIM_TEXT_HEIGHT: 10,
                c4d.PRIM_TEXT_ALIGN: c4d.PRIM_TEXT_ALIGN_MIDDLE,
            },
            O.splinetext: {
                c4d.PRIM_TEXT_TEXT: "1",
                c4d.PRIM_TEXT_HEIGHT: 10,
                c4d.PRIM_TEXT_ALIGN: c4d.PRIM_TEXT_ALIGN_MIDDLE,
            },
        },
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_CLONE: 1,
            c4d.FIELDS: {
                FL.field: {
                    c4d.ID_FIELDLAYER_LINK: F.box,
                    c4d.ID_FIELDLAYER_BLENDINGMODE: c4d.ID_FIELDLAYER_BLENDINGMODE_ADD,
                },
                FL.field: {
                    c4d.ID_FIELDLAYER_LINK: F.spherical,
                    c4d.ID_FIELDLAYER_BLENDINGMODE: c4d.ID_FIELDLAYER_BLENDINGMODE_ADD,
                },
                FL.field: {
                    c4d.ID_FIELDLAYER_LINK: F.torus,
                    c4d.ID_FIELDLAYER_BLENDINGMODE: c4d.ID_FIELDLAYER_BLENDINGMODE_ADD,
                },
            },
            F.box: {
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X): -50,
                c4d.FIELD_BOX_SIZE: (50,),
                T.vibrate: {
                    c4d.VIBRATEEXPRESSION_SEED: 1,
                    c4d.VIBRATEEXPRESSION_POS_ENABLE: True,
                    c4d.VIBRATEEXPRESSION_POS_AMPLITUDE: (100, 100, 0),
                    c4d.VIBRATEEXPRESSION_POS_FREQUENCY: 1.5,
                },
            },
            F.spherical: {
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X): 50,
                c4d.SPHERICAL_SIZE: 50,
                T.vibrate: {
                    c4d.VIBRATEEXPRESSION_SEED: 2,
                    c4d.VIBRATEEXPRESSION_POS_ENABLE: True,
                    c4d.VIBRATEEXPRESSION_POS_AMPLITUDE: (100, 100, 0),
                    c4d.VIBRATEEXPRESSION_POS_FREQUENCY: 1.5,
                },
            },
            F.torus: {
                # (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): 100,
                c4d.FIELD_TORUS_DIRECTION: c4d.FIELD_TORUS_DIRECTION_ZP,
                T.vibrate: {
                    c4d.VIBRATEEXPRESSION_SEED: 3,
                    c4d.VIBRATEEXPRESSION_POS_ENABLE: True,
                    c4d.VIBRATEEXPRESSION_POS_AMPLITUDE: (100, 100, 0),
                    c4d.VIBRATEEXPRESSION_POS_FREQUENCY: 0.5,
                },
            },
        },
    })
    doc.Flush()
    tree.load().print()
    Command.unfoldall()
    # Command.playforward()
