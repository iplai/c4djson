from c4djson.core import *

doc.Flush()
code = """import c4d
from math import sin, cos, pi as π
def main():
    spline: c4d.SplineObject = op.GetObject()
    samples = spline[c4d.ID_USERDATA, 2] or 2
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
        O.spline @ 'Torus Knot': {
            c4d.SPLINEOBJECT_TYPE: c4d.SPLINEOBJECT_TYPE_CUBIC,
            # Close Spline
            c4d.SPLINEOBJECT_CLOSED: True,
            c4d.ID_USERDATA: {
                (c4d.ID_USERDATA, 1): {
                    c4d.DTYPE_: c4d.DTYPE_GROUP,
                    c4d.DESC_NAME: 'Torus Knot',
                    c4d.DESC_SHORT_NAME: 'Torus Knot',
                    c4d.DESC_PARENTGROUP: (),
                    c4d.DESC_TITLEBAR: 1,
                },
                (c4d.ID_USERDATA, 2): {
                    c4d.DTYPE_: c4d.DTYPE_LONG,
                    c4d.DESC_NAME: 'Samples',
                    c4d.DESC_SHORT_NAME: 'Samples',
                    c4d.DESC_MIN: -2147483648,
                    c4d.DESC_MAX: 2147483647,
                    c4d.DESC_MINEX: 0,
                    c4d.DESC_MAXEX: 0,
                    c4d.DESC_STEP: 1,
                    c4d.DESC_UNIT: c4d.DESC_UNIT_INT,
                    c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                    c4d.DESC_PARENTGROUP: ((700, 5, 0), (1, 1, 0)),
                    c4d.DESC_DEFAULT: 80,
                    c4d.DESC_MINSLIDER: 2,
                    c4d.DESC_MAXSLIDER: 1000,
                },
                (c4d.ID_USERDATA, 3): {
                    c4d.DTYPE_: c4d.DTYPE_REAL,
                    c4d.DESC_NAME: 'Radius Outer',
                    c4d.DESC_SHORT_NAME: 'Radius Outer',
                    c4d.DESC_MIN: -1e+20,
                    c4d.DESC_MAX: 1e+20,
                    c4d.DESC_MINEX: 0,
                    c4d.DESC_MAXEX: 0,
                    c4d.DESC_STEP: 1,
                    c4d.DESC_UNIT: c4d.DESC_UNIT_REAL,
                    c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                    c4d.DESC_PARENTGROUP: ((700, 5, 0), (1, 1, 0)),
                    c4d.DESC_DEFAULT: 150,
                    c4d.DESC_MINSLIDER: -100,
                    c4d.DESC_MAXSLIDER: 1000,
                },
                (c4d.ID_USERDATA, 4): {
                    c4d.DTYPE_: c4d.DTYPE_REAL,
                    c4d.DESC_NAME: 'Radius Inner',
                    c4d.DESC_SHORT_NAME: 'Radius Inner',
                    c4d.DESC_MIN: -1e+20,
                    c4d.DESC_MAX: 1e+20,
                    c4d.DESC_MINEX: 0,
                    c4d.DESC_MAXEX: 0,
                    c4d.DESC_STEP: 1,
                    c4d.DESC_UNIT: c4d.DESC_UNIT_REAL,
                    c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                    c4d.DESC_PARENTGROUP: ((700, 5, 0), (1, 1, 0)),
                    c4d.DESC_DEFAULT: 50,
                    c4d.DESC_MINSLIDER: -100,
                    c4d.DESC_MAXSLIDER: 1000,
                },
                (c4d.ID_USERDATA, 5): {
                    c4d.DTYPE_: c4d.DTYPE_LONG,
                    c4d.DESC_NAME: 'q',
                    c4d.DESC_SHORT_NAME: 'q',
                    c4d.DESC_MIN: -2147483648,
                    c4d.DESC_MAX: 2147483647,
                    c4d.DESC_MINEX: 0,
                    c4d.DESC_MAXEX: 0,
                    c4d.DESC_STEP: 1,
                    c4d.DESC_UNIT: c4d.DESC_UNIT_INT,
                    c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                    c4d.DESC_PARENTGROUP: ((700, 5, 0), (1, 1, 0)),
                    c4d.DESC_DEFAULT: 3,
                    c4d.DESC_MINSLIDER: 1,
                    c4d.DESC_MAXSLIDER: 50,
                },
                (c4d.ID_USERDATA, 6): {
                    c4d.DTYPE_: c4d.DTYPE_LONG,
                    c4d.DESC_NAME: 'p',
                    c4d.DESC_SHORT_NAME: 'p',
                    c4d.DESC_MIN: -2147483648,
                    c4d.DESC_MAX: 2147483647,
                    c4d.DESC_MINEX: 0,
                    c4d.DESC_MAXEX: 0,
                    c4d.DESC_STEP: 1,
                    c4d.DESC_UNIT: c4d.DESC_UNIT_INT,
                    c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                    c4d.DESC_PARENTGROUP: ((700, 5, 0), (1, 1, 0)),
                    c4d.DESC_DEFAULT: 7,
                    c4d.DESC_MINSLIDER: 1,
                    c4d.DESC_MAXSLIDER: 50,
                },
                (c4d.ID_USERDATA, 7): {
                    c4d.DTYPE_: c4d.DTYPE_REAL,
                    c4d.DESC_NAME: 'Phase',
                    c4d.DESC_SHORT_NAME: 'Phase',
                    c4d.DESC_MIN: -5.7296e+21,
                    c4d.DESC_MAX: 5.7296e+21,
                    c4d.DESC_MINEX: 0,
                    c4d.DESC_MAXEX: 0,
                    c4d.DESC_STEP: 0.1,
                    c4d.DESC_UNIT: c4d.DESC_UNIT_DEGREE,
                    c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                    c4d.DESC_PARENTGROUP: ((700, 5, 0), (1, 1, 0)),
                    c4d.DESC_DEFAULT: 0,
                    c4d.DESC_MINSLIDER: 0,
                    c4d.DESC_MAXSLIDER: 360,
                },
            },
            # Samples
            (c4d.ID_USERDATA, 2): 80,
            # Animated Radius Outer
            (c4d.ID_USERDATA, 3): [
                (0, -100),
                (60, 100),
                (90, 40),
                {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OSCILLATE},
            ],
            # Animated Radius Inner
            (c4d.ID_USERDATA, 4): [
                (0, -40),
                (60, -40),
                (90, 160),
                {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OSCILLATE},
            ],
            # q
            (c4d.ID_USERDATA, 5): 3,
            # p
            (c4d.ID_USERDATA, 6): 7,
            # Animated Phase
            (c4d.ID_USERDATA, 7): [
                (0, 0, c4d.CINTER_LINEAR),
                (60, 360, c4d.CINTER_LINEAR),
                {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_CONTINUE},
            ],
            T.python: {
                c4d.TPYTHON_CODE: code,
            },
        },
    })
    tree.load()
    doc.SetMaxTime(c4d.BaseTime(179, doc.GetFps()))
    doc.SetSelection(tree[O.spline @ "Torus Knot"])
    doc.SetMode(c4d.Mpoints)
