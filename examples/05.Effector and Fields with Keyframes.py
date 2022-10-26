from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.mgvoronoifracture: {
            c4d.ID_FRACTURE_INPUT_POINTS: [O.mospline],
            c4d.ID_MG_VF_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain],
            O.platonic: {
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): 100,
            },
        },
        O.mospline: {
            (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X): 200,
            (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Y): 90,
        },
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_ROTATE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_ROTATION: (360, 0, 0),
            c4d.FIELDS: {
                FL.delay: {c4d.FIELDLAYER_DELAY_MODE: c4d.FIELDLAYER_DELAY_MODE_SPRING},
                FL.field: {c4d.ID_FIELDLAYER_LINK: F.linear},
            },
            F.linear: {
                c4d.LINEAR_DIRECTION: c4d.LINEAR_DIRECTION_YP,
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Y): [(0, -100), (60, 300)],
            },
        },
    })
    doc.Flush()
    tree.load().print()
    Command.unfoldall()
    # Command.playforward()
