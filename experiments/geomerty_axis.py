import maxon, c4d


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
    cube = c4d.BaseObject(c4d.Ocube)
    loadGeometryAxis(y=1, parent=cube)
    doc.InsertObject(cube)
