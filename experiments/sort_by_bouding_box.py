import c4d, sys


class BoundingBox:
    FLOATMIN = sys.float_info.min - 1000  # workaround for underflow error
    FLOATMAX = sys.float_info.max

    def __init__(self):
        self.min = c4d.Vector(self.FLOATMAX)
        self.max = c4d.Vector(self.FLOATMIN)
        self.np = 0

    def AddPoint(self, p: c4d.Vector):
        """Add metrics from point p."""
        if p.x < self.min.x:
            self.min.x = p.x
        if p.x > self.max.x:
            self.max.x = p.x
        if p.y < self.min.y:
            self.min.y = p.y
        if p.y > self.max.y:
            self.max.y = p.y
        if p.z < self.min.z:
            self.min.z = p.z
        if p.z > self.max.z:
            self.max.z = p.z

    @classmethod
    def fromObject(cls, obj: c4d.PointObject):
        allPoints = obj.GetAllPoints()
        if len(allPoints) == 0:
            raise ValueError("E: object has no points")
        bb = BoundingBox()
        for _, p in enumerate(allPoints):
            bb.AddPoint(p)
            bb.np += 1
        return bb


if __name__ == "__main__":
    root = doc.SearchObject("Root")
    # Sort polygon objects under root by it's height
    buildings: list[tuple[c4d.BaseObject, BoundingBox]] = []
    for obj in root.GetChildren():
        buildings.append((obj, BoundingBox.fromObject(obj)))
    for obj, bb in sorted(buildings, key=lambda x: (x[1].max - x[1].min).y, reverse=True):
        obj.InsertUnder(root)
