from c4djson import *


if __name__ == "__main__":
    # CPU killer!
    tree = Tree({
        O.connector @ "Geometry": {
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.MODE_OFF,
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.MODE_OFF,
            O.platonic: {},
        },
        O.connector @ "Source": {
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.MODE_OFF,
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.MODE_OFF,
            O.instance: {c4d.INSTANCEOBJECT_LINK: O.connector @ "Geometry"},
            O.mgrandom: {
                c4d.ID_MG_EFFECTORDEFORMER_MODE: c4d.ID_MG_EFFECTORDEFORMER_MODE_POINT,
                c4d.MGRANDOMEFFECTOR_MODE: c4d.MGRANDOMEFFECTOR_MODE_NOISE,
            }
        },
        O.mgvoronoifracture: {
            c4d.ID_FRACTURE_GAP: 2,
            c4d.ID_FRACTURE_GAP_INVERT: True,
            c4d.ID_FRACTURE_SHELL: True,
            c4d.ID_FRACTURE_THICKNESS: 4,
            c4d.ID_FRACTURE_INPUT_POINTS: [O.connector @ 'Source'],
            O.instance: {c4d.INSTANCEOBJECT_LINK: O.connector @ 'Geometry'},
        }
    } | {  # Dictionary Union
        O.mgvoronoifracture @ f"Voronoi Fracture {i}": {
            c4d.ID_FRACTURE_INPUT_POINTS: [O.connector @ "Source"],
            c4d.ID_FRACTURE_GAP: i * 4,
            O.mgvoronoifracture @ f"Voronoi Fracture {i}.1": {
                c4d.ID_FRACTURE_INPUT_POINTS: [O.connector @ "Source"],
                c4d.ID_FRACTURE_GAP: 2.5 + i * 4,
                c4d.ID_FRACTURE_GAP_INVERT: True,
                c4d.ID_FRACTURE_SHELL: True,
                c4d.ID_FRACTURE_THICKNESS: 4,
                O.instance: {c4d.INSTANCEOBJECT_LINK: O.connector @ "Geometry"},
            }
        } for i in range(1, 3)  # Dictionary Comprehension
    }
    ).load().print()
    Command.unfoldall()
