from c4djson import *

code = """from c4djson import *

def init():
    curve = database["curves"][op[c4d.ID_USERDATA, 2]]
    op[c4d.ID_USERDATA, 3] = curve["range"][2]
    op[c4d.ID_USERDATA, 4] = curve["premise"]
    op[c4d.ID_USERDATA, 5] = curve["rules"]
    # Change the range of n for different curves.
    for cid, bc in op.GetUserDataContainer():
        if cid == c4d.DescID(*[c4d.DescLevel(i) for i in (c4d.ID_USERDATA, 3)]):
            bc[c4d.DESC_MINSLIDER] = curve["range"][0]
            bc[c4d.DESC_MAXSLIDER] = curve["range"][1]
            op.SetUserDataContainer(cid, bc)

init()

def main():
    curve = database["curves"][op[c4d.ID_USERDATA, 2]]
    tree = Tree({
        O.mospline: {
            c4d.MGMOSPLINEOBJECT_MODE: c4d.MGMOSPLINEOBJECT_MODE_TURTLE,
            c4d.MGMOSPLINEOBJECT_DISPLAYMODE: c4d.MGMOSPLINEOBJECT_DISPLAYMODE_LINE,
            c4d.MGMOSPLINEOBJECT_TURTLE: op[c4d.ID_USERDATA, 4],
            c4d.MGMOSPLINEOBJECT_TURTLE_MODIFIER: op[c4d.ID_USERDATA, 5],
            c4d.MGMOSPLINEOBJECT_TURTLE_GROWTH: op[c4d.ID_USERDATA, 3],
            c4d.MGMOSPLINEOBJECT_TURTLE_BASEANGLE: curve["baseangle"],
        },
    })
    return tree[O.mospline]

def message(id, data):
    if id == c4d.MSG_DESCRIPTION_CHECKUPDATE:
        if data["descid"] == c4d.DescID(*[c4d.DescLevel(i) for i in (c4d.ID_USERDATA, 2)]):
            init()
"""
if __name__ == "__main__":
    database["curves"] = curves = [
        {
            "name": "Default Tree",
            "premise": "^(90)FFFA",
            "rules": "\n".join(
                [
                    'A=!"[B]/(90)[B]/(90)[B]/(90)B',
                    "B=&FTFTFTA",
                ]
            ),
            "baseangle": 28,
            "range": (0, 15, 5),
        },
        {
            "name": "Example Plant",
            "premise": "^(90)A",
            "rules": "\n".join(
                [
                    "A=B+[A+X]--//[--D]B[++D]-[AX]++AX",
                    "B=FC[//&&D][//^^D]FC",
                    "C=CFC",
                    "D=[{.+f.-ff.-f.+|+f.-ff.-f.}]",
                    "X=[&&&FF/Y/(72)Y/(72)Y/(72)Y/(72)Y]",
                    "Y=[^F][{.&(72)-f.+f.|-f.+f.}]",
                ]
            ),
            "baseangle": 18,
            "range": (0, 6, 4),
        },
        {
            "name": "Stairs",
            "premise": "F",
            "rules": "F=F-F+F+F-F",
            "baseangle": 90,
            "range": (0, 7, 3),
        },
        {
            "name": "Koch Curve 1",
            "premise": "F-F-F-F",
            "rules": "F=FF-F-F-F-F-F+F",
            "baseangle": 90,
            "range": (0, 5, 3),
        },
        {
            "name": "Koch Curve 2",
            "premise": "F-F-F-F",
            "rules": "F=FF-F-F-F-FF",
            "baseangle": 90,
            "range": (0, 5, 3),
            "divide": 3,
        },
        {
            "name": "Koch Curve 3",
            "premise": "F-F-F-F",
            "rules": "F=FF-F+F-F-FF",
            "baseangle": 90,
            "range": (0, 5, 3),
        },
        {
            "name": "Koch Curve 4",
            "premise": "F-F-F-F",
            "rules": "F=FF-F--F-F",
            "baseangle": 90,
            "range": (0, 5, 3),
            "divide": 3,
        },
        {
            "name": "Koch Curve 5",
            "premise": "F-F-F-F",
            "rules": "F=F-FF--F-F",
            "baseangle": 90,
            "range": (0, 5, 3),
        },
        {
            "name": "Koch Curve 6",
            "premise": "F-F-F-F",
            "rules": "F=F-F+F-F-F",
            "baseangle": 90,
            "range": (0, 5, 3),
        },
        {
            "name": "Quadratic Koch Island",
            "premise": "F-F-F-F",
            "rules": "F=F-F+F+FF-F-F+F",
            "baseangle": 90,
            "range": (0, 5, 2),
        },
        {
            "name": "Dragon Curve",
            "premise": "FA",
            "rules": "\n".join(
                [
                    "A=A+BF+",
                    "B=-FA-B",
                ]
            ),
            "baseangle": 90,
            "range": (0, 16, 8),
        },
        {
            "name": "Islands and Lakes",
            "premise": "F+F+F+F",
            "rules": "\n".join(
                [
                    "F=F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF",
                    "f=ffffff",
                ]
            ),
            "baseangle": 90,
            "range": (0, 4, 2),
        },
        {
            "name": "Snowflake",
            "premise": "F--F--F",
            "rules": """F="(pow(1/3;(_growth-1))))F+F--F+F""",
            "baseangle": 60,
            "range": (0, 8, 3),
        },
        {
            "name": "Hilbert Curve",
            "premise": "A",
            "rules": "\n".join(
                [
                    "A=+BF-AFA-FB+",
                    "B=-AF+BFB+FA-",
                ]
            ),
            "baseangle": 90,
            "range": (0, 8, 5),
        },
        {
            "name": "Hilbert Curve 3D",
            "premise": "X",
            "rules": "X=^\XF^\XFX-F^//XFX&F+//XFX-F/X-/",
            "baseangle": 90,
            "range": (0, 5, 2),
        },
        {
            "name": "Sierpinski Triangle",
            "premise": "A",
            "rules": "A=BF-AF-B\nB=AF+BF+A",
            "baseangle": 60,
            "range": (0, 12, 5),
        },
        {
            "name": "FASS 1",
            "premise": "A",
            "rules": "\n".join(
                [
                    "A=AF+BFB+FA-F-AFAFA-FBFB+",
                    "B=-AFAF+BFBFB+F+BF-AFA-FB",
                ]
            ),
            "baseangle": 90,
            "range": (0, 6, 3),
        },
        {
            "name": "FASS 2",
            "premise": "-A",
            "rules": "\n".join(
                [
                    "A=AFAF+BFB+FAFA-FBF-AFA-FB+F+BF-AFA-FBFBFB+",
                    "B=-AFAFAF+BFB+FA-F-AF+BFB+FAF+BFBF-AFA-FBFB",
                ]
            ),
            "baseangle": 90,
            "range": (0, 6, 3),
        },
        {
            "name": "FASS 3",
            "premise": "A",
            "rules": "\n".join(
                [
                    "A=AFBFA-F-BFAFB+F+AFBFA",
                    "B=BFAFB+F+AFBFA-F-BFAFB",
                ]
            ),
            "baseangle": 90,
            "range": (0, 6, 3),
        },
        {
            "name": "FASS 4",
            "premise": "A",
            "rules": "\n".join(
                [
                    "A=A+BF++BF-FA--FAFA-BF+",
                    "B=-FA+BFBF++BF+FA--FA-B",
                ]
            ),
            "baseangle": 60,
            "range": (0, 6, 3),
        },
        {
            "name": "FASS 5",
            "premise": "A",
            "rules": "\n".join(
                [
                    "A=AFA+BF+BF-FA-FA+BF+BFFA-BF-FAFABF+FA-BF-FAFA-BF+FABF+BF+FA-FA-BFBF+",
                    "B=-FAFA+BF+BF-FA-FABF-FA+BFBF+FA+BF-FABFBF+FA+BFFA-FA-BF+BF+FA-FA-BFB",
                ]
            ),
            "baseangle": 90,
            "range": (0, 3, 2),
        },
    ]
    tree = Tree({
        O.python @ "Fractal Generator": {
            c4d.OPYTHON_CODE: code,
            c4d.ID_USERDATA: {
                "Fractals": {
                    "Curve": {
                        c4d.DTYPE_: c4d.DTYPE_LONG,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_CYCLE,
                        c4d.DESC_CYCLE: {i: v["name"] for i, v in enumerate(curves)},
                    },
                    "n": {
                        c4d.DTYPE_: c4d.DTYPE_LONG,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_LONG,
                        c4d.DESC_DEFAULT: 2,
                        c4d.DESC_MINSLIDER: 0,
                        c4d.DESC_MAXSLIDER: 15,
                    },
                    "Premise": {
                        c4d.DTYPE_: c4d.DTYPE_STRING,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_STRING,
                    },
                    "Rules": {
                        c4d.DTYPE_: c4d.DTYPE_STRING,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_STRINGMULTI,
                    },
                }
            },
        },
    })
    doc.Flush()
    tree.load().print()
