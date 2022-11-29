from c4djson.core import *


if __name__ == "__main__":
    # CPU killer!
    tree = Tree({
        O.connector @ "Geometry": {
            # Viewport Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
            # Renderer Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
            O.platonic: {},
        },
        O.connector @ "Source": {
            # Viewport Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
            # Renderer Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
            # X-Ray
            c4d.ID_BASEOBJECT_XRAY: True,
            O.instance: {
                # Reference Object
                c4d.INSTANCEOBJECT_LINK: O.connector @ 'Geometry',
            },
            O.mgrandom: {
                # Random Mode: Noise
                c4d.MGRANDOMEFFECTOR_MODE: c4d.MGRANDOMEFFECTOR_MODE_NOISE,
                # Deformation: Point
                c4d.ID_MG_EFFECTORDEFORMER_MODE: c4d.ID_MG_EFFECTORDEFORMER_MODE_POINT,
            },
        },
        O.mgvoronoifracture: {
            # Offset Fragments
            c4d.ID_FRACTURE_GAP: 2,
            c4d.ID_FRACTURE_GAP_INVERT: True,
            # Hull Only
            c4d.ID_FRACTURE_SHELL: True,
            c4d.ID_FRACTURE_THICKNESS: 4,
            # Sources
            c4d.ID_FRACTURE_INPUT_POINTS: [O.connector @ 'Source'],
            O.instance: {
                # Reference Object
                c4d.INSTANCEOBJECT_LINK: O.connector @ 'Geometry',
            },
        }
    } | {  # Dictionary Union
        O.mgvoronoifracture @ f"Voronoi Fracture {i}": {
            # Offset Fragments
            c4d.ID_FRACTURE_GAP: i * 4,
            # Sources
            c4d.ID_FRACTURE_INPUT_POINTS: [O.connector @ 'Source'],
            O.mgvoronoifracture @ f"Voronoi Fracture {i}.1": {
                # Offset Fragments
                c4d.ID_FRACTURE_GAP: 2.5 + i * 4,
                c4d.ID_FRACTURE_GAP_INVERT: True,
                # Hull Only
                c4d.ID_FRACTURE_SHELL: True,
                c4d.ID_FRACTURE_THICKNESS: 4,
                # Sources
                c4d.ID_FRACTURE_INPUT_POINTS: [O.connector @ 'Source'],
                O.instance: {
                    # Reference Object
                    c4d.INSTANCEOBJECT_LINK: O.connector @ 'Geometry',
                },
            }
        } for i in range(1, 3)  # Dictionary Comprehension
    }
    ).load()
