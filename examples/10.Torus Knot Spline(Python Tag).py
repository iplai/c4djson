from c4djson import *

code = """import c4d
from math import sin, cos, pi as π
def main():
    spline: c4d.SplineObject = op.GetObject()
    samples = spline[c4d.ID_USERDATA, 2]
    R = spline[c4d.ID_USERDATA, 3]
    r = spline[c4d.ID_USERDATA, 4]
    q = spline[c4d.ID_USERDATA, 5]
    p = spline[c4d.ID_USERDATA, 6]
    phase = spline[c4d.ID_USERDATA, 7]
    points: list[c4d.Vector] = []
    t = -1
    while t < 1:
        a = π * t * q
        b = π * t * p + phase
        c = R + r * cos(b)
        x = c * cos(a)
        y = c * sin(a)
        z = r * sin(b)
        points.append(c4d.Vector(x, y, z))
        t += 2 / samples
    spline.ResizeObject(len(points))
    spline.SetAllPoints(points)
    spline.Message(c4d.MSG_UPDATE)
"""

if __name__ == "__main__":
    tree = Tree({
        O.spline @ "Torus Knot": {
            c4d.SPLINEOBJECT_TYPE: c4d.SPLINEOBJECT_TYPE_CUBIC,
            c4d.SPLINEOBJECT_CLOSED: True,
            c4d.ID_USERDATA: {
                "Torus Knot": {  # 1
                    "Samples": {  # 2
                        c4d.DTYPE_: c4d.DTYPE_LONG,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_LONG,
                        c4d.DESC_DEFAULT: 80,
                        c4d.DESC_MINSLIDER: 2,
                        c4d.DESC_MAXSLIDER: 1000,
                    },
                    "Radius Outer": {  # 3
                        c4d.DTYPE_: c4d.DTYPE_REAL,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_REAL,
                        c4d.DESC_DEFAULT: 150,
                        c4d.DESC_STEP: 1,
                        c4d.DESC_MINSLIDER: -100,
                        c4d.DESC_MAXSLIDER: 1000,
                    },
                    "Radius Inner": {  # 4
                        c4d.DTYPE_: c4d.DTYPE_REAL,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_REAL,
                        c4d.DESC_DEFAULT: 50,
                        c4d.DESC_STEP: 1,
                        c4d.DESC_MINSLIDER: -100,
                        c4d.DESC_MAXSLIDER: 1000,
                    },
                    "q": {  # 5
                        c4d.DTYPE_: c4d.DTYPE_LONG,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_LONG,
                        c4d.DESC_DEFAULT: 3,
                        c4d.DESC_MINSLIDER: 1,
                        c4d.DESC_MAXSLIDER: 50,
                    },
                    "p": {  # 6
                        c4d.DTYPE_: c4d.DTYPE_LONG,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_LONG,
                        c4d.DESC_DEFAULT: 7,
                        c4d.DESC_MINSLIDER: 1,
                        c4d.DESC_MAXSLIDER: 50,
                    },
                    "Phase": {  # 7
                        c4d.DTYPE_: c4d.DTYPE_REAL,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_DEGREE,
                        c4d.DESC_DEFAULT: 0,
                        c4d.DESC_MINSLIDER: 0,
                        c4d.DESC_MAXSLIDER: 360,
                        c4d.DESC_STEP: 0.1,
                    },
                }
            },
            (c4d.ID_USERDATA, 3): [(0, -100), (60, 100), (90, 40)],
            CT.base: {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OSCILLATE},
            (c4d.ID_USERDATA, 4): [(0, -40), (60, -40), (90, 160)],
            CT.base: {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OSCILLATE},
            (c4d.ID_USERDATA, 7): [
                (0, 0, c4d.CINTERPOLATION_LINEAR),
                (60, 360, c4d.CINTERPOLATION_LINEAR)
            ],
            CT.base: {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_CONTINUE},
            T.python: {
                c4d.TPYTHON_CODE: code
            },
        }
    })
    doc.Flush()
    tree.load().print()
    doc.SetMaxTime(c4d.BaseTime(179, doc.GetFps()))
    doc.SetSelection(tree[O.spline @ "Torus Knot"])
    doc.SetMode(c4d.Mpoints)
    Command.playforward()
