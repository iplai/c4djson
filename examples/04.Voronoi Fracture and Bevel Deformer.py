from c4djson import *

if __name__ == "__main__":
    tree = Tree({
        O.connector: {
            c4d.ID_BASEOBJECT_GENERATOR_FLAG: False,
            c4d.CONNECTOBJECT_WELD: False,
            O.null @ 'Geo': {
                O.mgvoronoifracture: {
                    c4d.ID_FRACTURE_INPUT_POINTS: [O.cube @ 'Points Source'],
                    c4d.ID_FRACTURE_GLUE_ACTIVATE: True,
                    c4d.ID_FRACTURE_GLUE_TYPE: c4d.ID_FRACTURE_GLUE_TYPE_CLUSTER,
                    c4d.ID_FRACTURE_GLUE_CLUSTERSIZE: 100,
                    c4d.ID_MG_VF_MOTIONGENERATOR_EFFECTORLIST: [O.mgpushapart],
                    O.cube: {},
                },
                O.bevel: {c4d.O_BEVEL_SUB: 4},
                O.mgpushapart: {
                    c4d.MGPUSHAPARTEFFECTOR_RADIUS: [(10, 0), (20, 30)],
                    CT.base @ 'Radius': {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OSCILLATE},
                },
            },
        },
        O.cube @ 'Points Source': {
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
            c4d.ID_BASEOBJECT_XRAY: True,
            c4d.PRIM_CUBE_LEN: (200 * 6 / 7,),
            c4d.PRIM_CUBE_SUBX: 6,
            c4d.PRIM_CUBE_SUBY: 6,
            c4d.PRIM_CUBE_SUBZ: 6,
        },
    })
    tree.load().print()
    Command.unfoldall()
    Command.playforward()
