from c4djson.core import *

doc.Flush()


def reverse_formula(formula: list[str]):
    result = []
    for i in reversed(formula):
        if "'" in i:
            result.append(i.replace("'", ""))
        elif "2" in i:
            result.append(i)
        elif "'" not in i:
            result.append(i + "'")
    return result


if __name__ == "__main__":
    unit = 100  # length of cubie
    thickness = 10  # extruded length of colored cubie
    fields = {}
    effectors = {}
    currframe = 0
    duration = 10  # frames to animate one step
    # https://ruwix.com/the-rubiks-cube/rubiks-cube-patterns-algorithms/
    formula = "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2".split()
    formula += reverse_formula(formula)
    configs = {
        "F": {
            "pos": (0, 0, -1),
            "axis": c4d.VECTOR_Z,
            "size": (3, 3, 1),
            "sign": 1,
        },
        "B": {
            "pos": (0, 0, 1),
            "axis": c4d.VECTOR_Z,
            "size": (3, 3, 1),
            "sign": -1,
        },
        "R": {
            "pos": (1, 0, 0),
            "axis": c4d.VECTOR_Y,
            "size": (1, 3, 3),
            "sign": -1,
        },
        "L": {
            "pos": (-1, 0, 0),
            "axis": c4d.VECTOR_Y,
            "size": (1, 3, 3),
            "sign": 1,
        },
        "U": {
            "pos": (0, 1, 0),
            "axis": c4d.VECTOR_X,
            "size": (3, 1, 3),
            "sign": -1,
        },
        "D": {
            "pos": (0, -1, 0),
            "axis": c4d.VECTOR_X,
            "size": (3, 1, 3),
            "sign": 1,
        },
    }
    for i, code in enumerate(formula):
        config = configs[code[0]].copy()
        if code.endswith("'"):
            config['sign'] = -config["sign"]
        degree = 180 if code.endswith("2") else 90
        frames = duration * 1.8 if code.endswith("2") else duration
        fields[F.box @ f"{code}.{i}"] = {
            c4d.ID_BASEOBJECT_REL_POSITION: tuple(x * unit for x in config["pos"]),
            c4d.FIELD_BOX_SIZE: tuple(x * unit / 2 + thickness / 2 for x in config["size"]),
            c4d.FIELD_INNER_OFFSET: 1,
        }
        effectors[O.mginheritance @ f"{code}.{i}"] = {
            (c4d.ID_BASEOBJECT_REL_ROTATION, config["axis"]): [
                (currframe, 0),
                (currframe + frames, degree * config["sign"]),
            ],
            c4d.MGINHERITANCEEFFECTOR_OBJECT: O.mginheritance @ f"{code}.{i}",
            c4d.FIELDS: {
                FL.field: {c4d.ID_FIELDLAYER_LINK: F.box @ f"{code}.{i}"},
            },
        }
        currframe += frames
    tree = Tree({
        O.mgcloner @ 'Grid Cube Cloner': {
            # Count.Y
            (c4d.MG_GRID_RESOLUTION, c4d.VECTOR_Y): 3,
            c4d.MG_GRID_MODE: c4d.MG_GRID_MODE_PERSTEP,
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: list(effectors.keys()),
            O.cube @ 'Grid Cube': {
                c4d.PRIM_CUBE_LEN: (unit, unit, unit),
                c4d.PRIM_CUBE_DOFILLET: True,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
        },
        O.mgcloner @ 'Colored Cube Cloner': {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
            c4d.MG_OBJECT_LINK: O.cube @ 'Cube to clone colored cube on',
            # Distribution: Polygon Center
            c4d.MG_POLY_MODE_: c4d.MG_POLY_MODE_POLY,
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain @ "Colors"] + list(effectors.keys()),
            O.cube @ 'Colored Cube': {
                # Size
                c4d.PRIM_CUBE_LEN: (unit * 0.9, unit * 0.9, thickness),
                c4d.PRIM_CUBE_DOFILLET: True,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True}, },
        },
        O.mgplain @ "Colors": {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.FIELDS: {
                # Color Scheme for Rubik's cube
                FL.formula @ "front": {
                    c4d.FORMULAFIELD_STRING: "id < 9",
                    c4d.FIELD_COLOR: (255, 0, 0),
                },
                FL.formula @ "right": {
                    c4d.FORMULAFIELD_STRING: "(9 <= id) and (id < 18)",
                    c4d.FIELD_COLOR: (0, 128, 0),
                },
                FL.formula @ "back": {
                    c4d.FORMULAFIELD_STRING: "(18 <= id) and (id < 27)",
                    c4d.FIELD_COLOR: (255, 102, 0),
                },
                FL.formula @ "left": {
                    c4d.FORMULAFIELD_STRING: "(27 <= id) and (id < 36)",
                    c4d.FIELD_COLOR: (0, 0, 255),
                },
                FL.formula @ "top": {
                    c4d.FORMULAFIELD_STRING: "(36 <= id) and (id < 45)",
                    c4d.FIELD_COLOR: (255, 255, 0),
                },
                FL.formula @ "bottom": {
                    c4d.FORMULAFIELD_STRING: "45 <= id",
                    c4d.FIELD_COLOR: (8, 8, 8),
                },
            }
        },
        O.cube @ 'Cube to clone colored cube on': {
            # Viewport Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_EDITOR: c4d.OBJECT_OFF,
            # Renderer Visibility: Off
            c4d.ID_BASEOBJECT_VISIBILITY_RENDER: c4d.OBJECT_OFF,
            # Size
            c4d.PRIM_CUBE_LEN: (300,),
            # Segments X
            c4d.PRIM_CUBE_SUBX: 3,
            # Segments Y
            c4d.PRIM_CUBE_SUBY: 3,
            # Segments Z
            c4d.PRIM_CUBE_SUBZ: 3,
        },
        O.null @ "Effectors": effectors,
        O.null @ "Fields": fields,
    })
    tree.load(dumpWhenLoaded=False)
    doc.SetMaxTime(c4d.BaseTime(currframe / doc.GetFps()))
