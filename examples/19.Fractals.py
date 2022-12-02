from c4djson.core import *
from c4djson.fractals import curves
from math import sqrt

code = r"""from c4djson.core import *
mospline = op.GetObject()
def main():
    curve: dict = Tree.database["curves"][op[c4d.ID_USERDATA, 2]]
    Tree().ParseParams({k: v for k, v in curve.items() if type(k) == int}, BL.FromObj(mospline))

"""
del Tree.database["curves"]
Tree.database.setdefault("curves", curves)
data = {
    O.mospline: {
        c4d.MGMOSPLINEOBJECT_MODE: c4d.MGMOSPLINEOBJECT_MODE_TURTLE,
        c4d.MGMOSPLINEOBJECT_DISPLAYMODE: c4d.MGMOSPLINEOBJECT_DISPLAYMODE_LINE,
        # Premise
        c4d.MGMOSPLINEOBJECT_TURTLE: '',
        # Rules
        c4d.MGMOSPLINEOBJECT_TURTLE_MODIFIER: '',
        T.python: {
            c4d.TPYTHON_CODE: code,
            c4d.ID_USERDATA: {
                (c4d.ID_USERDATA, 1): {
                    c4d.DTYPE_: c4d.DTYPE_GROUP,
                    c4d.DESC_NAME: 'Fractals',
                    c4d.DESC_SHORT_NAME: 'Fractals',
                    c4d.DESC_COLUMNS: 1,
                    c4d.DESC_TITLEBAR: 1,
                    c4d.DESC_PARENTGROUP: (),
                    c4d.DESC_DEFAULT: 1,
                },
                (c4d.ID_USERDATA, 2): {
                    c4d.DTYPE_: c4d.DTYPE_LONG,
                    c4d.DESC_NAME: 'Preset',
                    c4d.DESC_SHORT_NAME: 'Preset',
                    c4d.DESC_MIN: 0,
                    c4d.DESC_MAX: 100,
                    c4d.DESC_MINEX: 0,
                    c4d.DESC_MAXEX: 0,
                    c4d.DESC_STEP: 1,
                    c4d.DESC_UNIT: c4d.DESC_UNIT_INT,
                    c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_CYCLE,
                    c4d.DESC_PARENTGROUP: ((700, 5, 0), (1, 1, 0)),
                    c4d.DESC_CYCLE: {i: item["name"] for i, item in enumerate(curves)},
                    c4d.DESC_CYCLEICONS: {},
                },
            },
            # Preset: H Tree
            (c4d.ID_USERDATA, 2): 0,
        },
    },
}
Tree(data).load()
