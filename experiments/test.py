from c4djson import *

Tree({
    O.connector: {
        (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_X): [(0, 0), (30, 400 * 3.14)],
        O.cube: {
            (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Z): [(0, 0), (30, 360)],
        }
    }
}).load().print()
