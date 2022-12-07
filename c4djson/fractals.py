import c4d
from math import sqrt

curves = [
    {
        "name": "H Tree",
        "params": {
            c4d.MGMOSPLINEOBJECT_MODE: c4d.MGMOSPLINEOBJECT_MODE_TURTLE,
            c4d.MGMOSPLINEOBJECT_DISPLAYMODE: c4d.MGMOSPLINEOBJECT_DISPLAYMODE_LINE,
            # Premise
            c4d.MGMOSPLINEOBJECT_TURTLE: '[FX]|[FX]',
            # Rules
            c4d.MGMOSPLINEOBJECT_TURTLE_MODIFIER: 'X="+[FX]|[FX]',
            c4d.MGMOSPLINEOBJECT_TURTLE_GROWTH: [(0, 0, c4d.CINTER_LINEAR), (300, 14)],
            # Default Angle
            c4d.MGMOSPLINEOBJECT_TURTLE_BASEANGLE: 90,
            # Move Multiplier
            c4d.MGMOSPLINEOBJECT_TURTLE_ADDMOVE: 1 / sqrt(2),
            c4d.MGMOSPLINEOBJECT_TURTLE_GROWANGLE: False,
        },
    },
    {
        "name": "Koch Flower",
        "params": {
            c4d.MGMOSPLINEOBJECT_MODE: c4d.MGMOSPLINEOBJECT_MODE_TURTLE,
            c4d.MGMOSPLINEOBJECT_DISPLAYMODE: c4d.MGMOSPLINEOBJECT_DISPLAYMODE_LINE,
            # Premise
            c4d.MGMOSPLINEOBJECT_TURTLE: 'F-F-F-F',
            # Rules
            c4d.MGMOSPLINEOBJECT_TURTLE_MODIFIER: 'F="(pow(1/3;_growth-1))FF-F-F-F-F-F+F',
            c4d.MGMOSPLINEOBJECT_TURTLE_GROWTH: [(0, 0, c4d.CINTER_LINEAR), (90, 5)],
            # Default Angle
            c4d.MGMOSPLINEOBJECT_TURTLE_BASEANGLE: 90,
            c4d.MGMOSPLINEOBJECT_TURTLE_GROWANGLE: False,
        },
    },
]

if __name__ == "__main__":
    import importlib, c4djson.fractals
    importlib.reload(c4djson.fractals)
