from c4djson import *

code = r"""from c4djson import *
def main():
    angle = op[c4d.ID_USERDATA, 3]
    amin, amax = map(c4d.utils.DegToRad, (5, 90))
    inner_radius = c4d.utils.RangeMap(angle, amin, amax, 15, 18, True)
    tree = Tree({
        O.null @ "Root": {
            O.loft: {
                c4d.LOFTOBJECT_SUBX: 24,
                c4d.LOFTOBJECT_SUBY: 5,
                O.mgcloner: {
                    c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_OBJECT,
                    c4d.MG_OBJECT_LINK: O.splinearc,
                    c4d.MG_SPLINE_LOOP: False,
                    c4d.MG_SPLINE_COUNT: op[c4d.ID_USERDATA, 2],
                    O.splinecircle @ "1": {c4d.PRIM_CIRCLE_RADIUS: 18},
                    O.splinecircle @ "2": {c4d.PRIM_CIRCLE_RADIUS: inner_radius},
                },
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
            O.splinearc: {
                c4d.PRIM_ARC_RADIUS: 100,
                c4d.PRIM_ARC_END: c4d.utils.RadToDeg(angle),
            },
        },
    })
    if "Bellows" not in database:
        tree.print()
        database["Bellows"] = True
    return tree[O.null @ "Root"]
"""
if __name__ == "__main__":
    database.pop("Bellows", None)
    Tree({
        O.python @ "Bellows Generator": {
            c4d.OPYTHON_CODE: code,
            c4d.ID_USERDATA: {
                "Bellows": {  # 1
                    "Segments": {  # 2
                        c4d.DTYPE_: c4d.DTYPE_LONG,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_LONGSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_LONG,
                        c4d.DESC_DEFAULT: 15,
                        c4d.DESC_STEP: 2,
                        c4d.DESC_MINSLIDER: 3,
                        c4d.DESC_MAXSLIDER: 50,
                    },
                    "End Angle": {  # 3
                        c4d.DTYPE_: c4d.DTYPE_REAL,
                        c4d.DESC_CUSTOMGUI: c4d.CUSTOMGUI_REALSLIDER,
                        c4d.DESC_UNIT: c4d.DESC_UNIT_DEGREE,
                        c4d.DESC_DEFAULT: 40,
                        c4d.DESC_MINSLIDER: 5,
                        c4d.DESC_MAXSLIDER: 90,
                        c4d.DESC_STEP: 1,
                    },
                }
            },
            (c4d.ID_USERDATA, 3): [(0, 30), (15, 90)],
            CT.base: {  # Track of the userdata animation
                c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OSCILLATE,
            },
        },
    }).load().print()
    Command.unfoldall()
    Command.playforward()
