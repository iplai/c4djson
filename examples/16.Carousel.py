from c4djson import *


if __name__ == "__main__":
    size = 50
    count = 7
    radius = size * 3
    tree = Tree({
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_RADIAL,
            c4d.MG_RADIAL_RADIUS: radius,
            c4d.MG_RADIAL_COUNT: count,
            c4d.MG_RADIAL_OFFSET: [(0, 0), (20, 360 / count), (30, 360 / count)],
            CT.base: {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_OFFSETREPEAT},
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: [O.mgplain, O.mgdelay],
            O.cube: {
                c4d.PRIM_CUBE_LEN: (size,),
                c4d.PRIM_CUBE_DOFILLET: True,
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
        },
        O.mgdelay: {
            c4d.MGDELAYEFFECTOR_MODE: c4d.MGDELAYEFFECTOR_MODE_SPRING,
        },
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            c4d.ID_MG_BASEEFFECTOR_SCALE_ACTIVE: True,
            c4d.ID_MG_BASEEFFECTOR_UNIFORMSCALE: True,
            c4d.ID_MG_BASEEFFECTOR_USCALE: 1,
            c4d.FIELDS: {
                FL.field: {c4d.ID_FIELDLAYER_LINK: F.box},
            },
            F.box: {
                (c4d.ID_BASEOBJECT_REL_POSITION, c4d.VECTOR_Z): radius,
            },
        },
    })
    doc.Flush()
    tree.load().print()
    Command.unfoldall()
    Command.playforward()
