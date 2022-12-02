from c4djson.core import *


def GetPointsByMoSpline(params: dict):
    tree = Tree({
        O.mospline: params,
    })
    mospline: c4d.BaseObject = tree[O.mospline]
    spline = mospline.GetRealSpline()
    points = spline.GetAllPoints()
    # Remove redundant points
    points = [v for i, v in enumerate(points) if v not in points[i - 1:i]]
    return points


def main(n=7):
    splines: list[list[c4d.Vector]] = []

    for i in range(1, n + 1):
        splines.append(GetPointsByMoSpline({
            c4d.MGMOSPLINEOBJECT_MODE: c4d.MGMOSPLINEOBJECT_MODE_TURTLE,
            # Premise
            c4d.MGMOSPLINEOBJECT_TURTLE: 'F',
            # Rules
            c4d.MGMOSPLINEOBJECT_TURTLE_MODIFIER: 'F=F-F+F+F-F',
            c4d.MGMOSPLINEOBJECT_TURTLE_GROWTH: i,
            # Default Angle
            c4d.MGMOSPLINEOBJECT_TURTLE_BASEANGLE: 90,
            # Default Movement
            c4d.MGMOSPLINEOBJECT_TURTLE_BASEMOVE: 200,
        }))

    splineObjects: list[c4d.SplineObject] = []
    for i in range(1, len(splines)):
        points = splines[i - 1]
        pointsBlendA = []
        pointsBlendB = splines[i]
        # Interpolate points to A, so A and B have same points count.
        for j in range(len(points) - 1):
            pointsBlendA.append(points[j])
            point_a = points[j] + (points[j + 1] - points[j]) / 3
            point_b = points[j] + (points[j + 1] - points[j]) * 2 / 3
            pointsBlendA.append(point_a)
            if i < 5:  # Save memory for higher iteration
                pointsBlendA.append(point_a)
            pointsBlendA.append(point_b)
            if i < 5:
                pointsBlendA.append(point_b)
        pointsBlendA.append(points[-1])

        for j, points in enumerate([pointsBlendA, pointsBlendB]):
            spline = c4d.SplineObject(len(points), c4d.SPLINETYPE_LINEAR)
            a = 1 / 3**(i - 1 + j)
            points = [v * a for v in points]
            spline.SetAllPoints(points)
            splineObjects.append(spline)

    Tree({
        O.mgplain: {
            c4d.ID_MG_BASEEFFECTOR_POSITION_ACTIVE: False,
            # Animated Modify Clone
            c4d.ID_MG_BASEEFFECTOR_CLONE: [(0, 0, c4d.CINTER_LINEAR), (120, 1)],
        },
        O.mgcloner: {
            c4d.ID_MG_MOTIONGENERATOR_MODE: c4d.ID_MG_MOTIONGENERATOR_MODE_LINEAR,
            # Clones: Blend
            c4d.MGCLONER_MODE: c4d.MGCLONER_MODE_BLEND,
            c4d.MG_LINEAR_COUNT: 1,
            c4d.MGCLONER_FIX_CLONES: False,
            # Effectors
            c4d.ID_MG_MOTIONGENERATOR_EFFECTORLIST: {(0, 1): O.mgplain},
        } | {
            BL.FromObj(spline): {} for spline in splineObjects
        },
    }).load(dumpWhenLoaded=False)


if __name__ == "__main__":
    main()
