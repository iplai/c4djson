import maxon, c4d
from c4djson import *


def loadGeometryAxis(x=0, y=0, z=0, parent: c4d.BaseObject = None):
    repository = maxon.AssetInterface.GetUserPrefsRepository()
    if not repository:
        raise RuntimeError("Could not access the user preferences repository.")
    # Geometry Axis asset id
    assetid = maxon.Id("net.maxon.neutron.asset.geo.geometryaxis")
    assetsToLoad = [(assetid, ""), ]
    maxon.AssetManagerInterface.LoadAssets(repository, assetsToLoad)
    capsule = doc.GetFirstObject()
    for i, (bc, descid, _) in enumerate(capsule.GetDescription(c4d.DESCFLAGS_DESC_0)):
        if i == 59:
            capsule[descid] = x
        if i == 60:
            capsule[descid] = y
        if i == 61:
            capsule[descid] = z
    if parent is not None:
        capsule.InsertUnderLast(parent)
    return capsule


if __name__ == "__main__":
    rps = 0.5  # The number of revolutions per second
    radius = 200
    LINEAR = c4d.CINTERPOLATION_LINEAR
    rot_keyframes = [(0, 0, LINEAR), (doc.GetFps(), 360 * rps, LINEAR)]
    spline = {
        O.splinecircle: {
            c4d.PRIM_CIRCLE_RADIUS: 400,
            c4d.PRIM_PLANE: c4d.PRIM_PLANE_XZ,
        },
    }
    spline_tree = Tree(spline)
    spline_key = list(spline.keys())[0]
    spline_help = c4d.utils.SplineHelp()
    spline_help.InitSplineWith(spline_tree[spline_key])
    # key frames definition for Align to Spline tag position percent
    pos_keyframes = [
        (0, 0, LINEAR),
        (doc.GetFps(), radius * rps * 4 / spline_help.GetSplineLength(), LINEAR)
        # (doc.GetFps(), radius * rps * pi / spline_help.GetSplineLength(), LINEAR)
    ]

    tree = Tree({
        O.null @ "Replace Your Spline": spline,
        O.sweep: {
            T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            O.splinenside: {
                c4d.PRIM_NSIDE_RADIUS: 100,
                c4d.PRIM_NSIDE_SIDES: 2,
            },
            O.instance: {c4d.INSTANCEOBJECT_LINK: spline_key},
        },
        O.connector: {
            T.aligntospline: {
                c4d.ALIGNTOSPLINETAG_LINK: spline_key,
                c4d.ALIGNTOSPLINETAG_TANGENTIAL: True,
                c4d.ALIGNTOSPLINETAG_AXIS: c4d.ALIGNTOSPLINETAG_AXIS_X,
                # Animate Position
                c4d.ALIGNTOSPLINETAG_POSITION: pos_keyframes,
                CT.base: {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_CONTINUE},
            },
            O.cube: {
                # Animate Rotation.B
                (c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Z): rot_keyframes,
                CT.base: {c4d.ID_CTRACK_AFTER: c4d.ID_CTRACK_CONTINUE},
                T.phong: {c4d.PHONGTAG_PHONG_ANGLELIMIT: True},
            },
        },
    })
    loadGeometryAxis(y=1, parent=tree[O.connector])
    tree.load().print()
