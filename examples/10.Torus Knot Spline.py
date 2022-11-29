from c4djson.core import *
from math import sqrt, sin, cos, pi as π


if __name__ == "__main__":
    samples = 64
    R = 200
    r = 50
    q = 3
    p = 5
    points: list[c4d.Vector] = []
    t = -1
    while t < 1:
        a = π * t * q
        b = π * t * p
        c = R + r * cos(b)
        x = c * cos(a)
        y = c * sin(a)
        z = r * sin(b)
        points.append(c4d.Vector(x, y, z))
        t += 2 / samples

    tree = Tree({
        O.spline: {
            c4d.SPLINEOBJECT_TYPE: c4d.SPLINEOBJECT_TYPE_CUBIC,
            # Close Spline
            c4d.SPLINEOBJECT_CLOSED: True,
        },
        # The difference is Formula Spline cannot close spline unless make editable
        O.splineformula: {
            # Position.X
            (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X): 500,
            c4d.PRIM_FORMULA_X: f"({R} + {r} * cos(pi * t * {p})) * cos(pi * t * {q})",
            c4d.PRIM_FORMULA_Y: f"({R} + {r} * cos(pi * t * {p})) * sin(pi * t * {q})",
            c4d.PRIM_FORMULA_Z: f"{r} * sin(pi * t * {p})",
            c4d.PRIM_FORMULA_SAMPLES: samples,
            # Cubic Interpolation
            c4d.PRIM_FORMULA_CUBIC: True,
        },
    })

    spline: c4d.SplineObject = tree[O.spline]
    spline.ResizeObject(len(points))
    spline.SetAllPoints(points)
    spline.Message(c4d.MSG_UPDATE)
    tree.load()

    doc.SetSelection(spline)
    doc.SetMode(c4d.Mpoints)
