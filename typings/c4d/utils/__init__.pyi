from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import Vector, SPLINEHELPFLAGS_GLOBALSPACE, SPLINEHELPFLAGS_CONTINUECURVE, MAXLONGl, MODELINGCOMMANDMODE_ALL, MODELINGCOMMANDFLAGS_NONE, TANGENTTRANSFORMFLAG_BREAK_SCALE, ROTATIONORDER_DEFAULT
if TYPE_CHECKING:
	from . import noise
	from c4d import PolygonObject, BaseSelect, BaseObject, Matrix, LineObject, BaseList2D, SplineObject, BaseDraw, BaseContainer, PointObject, UVWTag, TextureTag, BaseView, SplineData, Quaternion, UnitScaleData
	from c4d.gui import EditorWindow
	from c4d.documents import BaseDocument
	from c4d.threading import BaseThread
	from c4d.bitmaps import BaseBitmap


class SplineHelp(object):
	"""Class for helping to deal with splines."""
	def Exists(self) -> 'bool':
		"""Check if the splinehelp was initialized."""
	def FreeSpline(self) -> 'None':
		"""Frees the spline."""
	def GetCrossNormal(self, offset: 'float', segment: 'int' = 0, smooth: 'bool' = True, realoffset: 'bool' = False) -> 'Vector':
		"""Gets a cross normal vector."""
	def GetDirty(self) -> 'int':
		"""Gets the dirty value for the splinehelp."""
	def GetLineObject(self) -> 'Optional[LineObject]':
		"""Gets a LineObject from the splinehelp."""
	def GetMatrix(self, offset: 'float', segment: 'int' = 0, smooth: 'bool' = True, realoffset: 'bool' = False) -> 'Matrix':
		"""Retrieve a full matrix for any point along the spline."""
	def GetNormal(self, offset: 'float', segment: 'int' = 0, smooth: 'bool' = True, realoffset: 'bool' = False) -> 'Vector':
		"""Gets a normal vector."""
	def GetOffsetFromReal(self, offset: 'float', segment: 'int' = 0) -> 'float':
		"""Retrieve an offset from a realworld unit"""
	def GetOffsetFromUnit(self, unitoffset: 'float', segment: 'int' = 0) -> 'float':
		"""Convert a percentage offset into a natural offset."""
	def GetPointIndex(self, offset: 'float', segment: 'int') -> 'int':
		"""Retrieves the nearest line point index to the given real offset."""
	def GetPointMatrix(self, splineVertexIndex: 'int') -> 'Matrix':
		"""Gets the matrix for a spline vertex."""
	def GetPointValue(self, offset: 'float', segment: 'int') -> 'float':
		"""Converts a natural offset value to a real percentage offset value."""
	def GetPos(self, offset: 'float', segment: 'int' = 0, smooth: 'bool' = True, realoffset: 'bool' = False) -> 'Vector':
		"""Gets a position along the spline."""
	def GetPosition(self, offset: 'float', segment: 'int' = 0, smooth: 'bool' = True, realoffset: 'bool' = False) -> 'Vector':
		"""Gets a position along the spline."""
	def GetSegmentCount(self) -> 'int':
		"""Gets the number of segments in the spline."""
	def GetSegmentLength(self, segment: 'int') -> 'float':
		"""Returns the length of a segment."""
	def GetSize(self, offset: 'float', segment: 'int' = 0, smooth: 'bool' = True, realoffset: 'bool' = False) -> 'float':
		"""Get the distance to an existing rail spline for any point along the spline."""
	def GetSplineLength(self) -> 'float':
		"""Returns the length of a spline."""
	def GetTangent(self, offset: 'float', segment: 'int' = 0, smooth: 'bool' = True, realoffset: 'bool' = False) -> 'Vector':
		"""Gets a tangent vector for any point along the spline."""
	def GetVertexCount(self, segment: 'int') -> 'int':
		"""Get the number of vertices for a spline segment."""
	def GetVertexMatrix(self, index: 'int') -> 'Matrix':
		"""Retrieves a full matrix for a specific point of the line."""
	def GetVertexSize(self, index: 'int') -> 'int':
		"""Get the distance to an existing rail spline."""
	def InitSpline(self, op: 'BaseObject', up: 'Optional[Vector]' = True, rail: 'Optional[BaseObject]' = True, target_rail: 'Optional[bool]' = True, use_deformed_points: 'Optional[bool]' = False, force_update: 'Optional[bool]' = False, use_global_space: 'Optional[bool]' = True) -> 'bool':
		"""Initializes the class."""
	def InitSplineWith(self, op: 'BaseObject', flags: 'int' = 10) -> 'bool':
		"""Initializes the class with a spline object."""
	def InitSplineWithRail(self, op: 'BaseObject', rail: 'BaseObject', flags: 'int' = 10) -> 'bool':
		"""Initializes the class with a spline object and a rail object."""
	def InitSplineWithUpVector(self, op: 'BaseObject', upvector: 'Vector', flags: 'int' = 10) -> 'bool':
		"""Initializes the class with a spline object and an up vector."""
	def SplineToLineIndex(self, index: 'int') -> 'int':
		"""Turns a percentage along the whole spline to local segment info."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class SplineLengthData(object):
	"""Class to calculate length of Splines."""
	def Free(self) -> 'None':
		"""Reset the object to initial state."""
	def GetLength(self) -> 'float':
		"""Get the length of the spline."""
	def GetSegmentLength(self, a: 'int', b: 'int') -> 'None':
		"""Get the segment length."""
	def Init(self, op: 'SplineObject', segment: 'int') -> 'None':
		"""Initialize the object."""
	def UniformToNatural(self, t: 'float') -> 'float':
		"""Get the natural position along the spline."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class Neighbor(object):
	"""Class to recieve neighbor edges and polygons."""
	def Flush(self) -> 'None':
		"""Flushes the neighbor information."""
	def GetEdgeCount(self) -> 'int':
		"""Returns the number of edges."""
	def GetEdgePolys(self, a: 'int', b: 'int') -> 'Tuple[int, int]':
		"""Retrieves the polygons that neighbor the given edge."""
	def GetNeighbor(self, a: 'int', b: 'int', poly: 'int') -> 'None':
		"""Gets the polygon opposite."""
	def GetPointOneRingPoints(self, pnt: 'int') -> 'List[int]':
		"""Gets the points that are attached through one edge to the given point."""
	def GetPointPolys(self, pnt: 'int') -> 'List[object]':
		"""Retrieves the polygons for a point."""
	def GetPolyInfo(self, poly: 'int') -> 'None':
		"""Gets the polygon information."""
	def Init(self, op: 'PolygonObject', bs: 'Optional[BaseSelect]' = None) -> 'None':
		"""Initializes the internal polygon information."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class ViewportSelect(object):
	"""Used to extract information from a viewport."""
	def ClearPixelInfo(self, x: 'int', y: 'int', mask: 'int') -> 'None':
		"""Clear the pixel info."""
	def DrawHandle(self, p: 'Vector', i: 'int', op: 'BaseObject', onlyvisible: 'int' = -1) -> 'bool':
		"""Draws a handle into the internal pixel structur"""
	def DrawPolygon(self, p: 'object', i: 'int', op: 'BaseObject', onlyvisible: 'int' = -1) -> 'bool':
		"""Draws a polygon into the internal pixel structure."""
	def GetCameraCoordinates(self, x: 'float', y: 'float', z: 'float') -> 'Vector':
		"""Convert pixel position to camera coordinates."""
	def GetNearestEdge(self, op: 'BaseObject', x: 'int', y: 'int', maxrad: 'int' = 2147483647, onlyselected: 'bool' = False, ignorelist: 'Optional[List[int]]' = None, ignorecnt: 'Optional[int]' = 0) -> 'Optional[Dict[str, object]]':
		"""Retrieves nearest edge information."""
	def GetNearestPoint(self, op: 'BaseObject', x: 'int', y: 'int', maxrad: 'int' = 2147483647, onlyselected: 'bool' = False, ignorelist: 'Optional[List[int]]' = None, ignorecnt: 'Optional[int]' = 0) -> 'Optional[Dict[str, object]]':
		"""Retrieves nearest point information."""
	def GetNearestPolygon(self, op: 'BaseObject', x: 'int', y: 'int', maxrad: 'int' = 2147483647, onlyselected: 'bool' = False, ignorelist: 'Optional[List[int]]' = None, ignorecnt: 'Optional[int]' = 0) -> 'Optional[Dict[str, object]]':
		"""Retrieves nearest polygon information."""
	def GetPixelInfoEdge(self, x: 'int', y: 'int') -> 'Optional[Dict[str, object]]':
		"""Return information about an edge at a pixel."""
	def GetPixelInfoPoint(self, x: 'int', y: 'int') -> 'Optional[Dict[str, object]]':
		"""Return information about a point at a pixel."""
	def GetPixelInfoPolygon(self, x: 'int', y: 'int') -> 'Optional[Dict[str, object]]':
		"""Return information about an polygon at a pixel."""
	def Init(self, w: 'int', h: 'int', bd: 'BaseDraw', ops: 'List[BaseObject]', mode: 'int', onlyvisible: 'bool', flags: 'int') -> 'None':
		"""Gets the polygon opposite"""
	@staticmethod
	def PickObject(bd: 'BaseDraw', doc: 'BaseDocument', x: 'int', y: 'int', rad: 'int', flags: 'int') -> 'Optional[List[BaseObject]]':
		"""Pick object from a provided list."""
	def SetBrushRadius(self, r: 'float') -> 'None':
		"""Set brush radious."""
	def ShowHotspot(self, bw: 'EditorWindow', x: 'int', y: 'int') -> 'None':
		"""Set the hotspot."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class GeRayCollider(object):
	"""Evaluate intersections of rays and objects."""
	def GetIntersection(self, number: 'int') -> 'Dict[str, object]':
		"""Return the intersections."""
	def GetIntersectionCount(self) -> 'int':
		"""Initalizes the ray collider"""
	def GetNearestIntersection(self) -> 'Optional[Dict[str, object]]':
		"""Retrieves the closest intersection."""
	def Init(self, goal: 'PolygonObject', force: 'bool' = False) -> 'bool':
		"""Initalizes the ray collider"""
	def Intersect(self, ray_p: 'Vector', ray_dir: 'Vector', length: 'object', only_test: 'bool' = False) -> 'bool':
		"""Check an intersection."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class PolygonReduction(object):
	"""Performs polygon reduction for a polygon object."""
	def GetData(self) -> 'Dict[str, object]':
		"""Retrieves the associated polygon reduction data dictionary."""
	def GetMaxReductionStrengthLevel(self) -> 'float':
		"""Queries the maximum reduction strength percentage."""
	def GetMaxRemainingEdgesLevel(self) -> 'int':
		"""Queries the total number of possible edge collapses."""
	def GetMaxTriangleLevel(self) -> 'int':
		"""Queries the triangle count when no reduction has been performed."""
	def GetMaxVertexLevel(self) -> 'int':
		"""Queries the vertex count when no reduction has been performed."""
	def GetMinTriangleLevel(self) -> 'int':
		"""Queries the triangle count when complete reduction has been performed."""
	def GetMinVertexLevel(self) -> 'int':
		"""Queries the vertex count when complete reduction has been performed."""
	def GetReductionStrengthLevel(self) -> 'int':
		"""Queries the current reduction strength level."""
	def GetRemainingEdgesLevel(self) -> 'int':
		"""Queries the current remaining number of edges available to collapse."""
	def GetTriangleLevel(self) -> 'int':
		"""Queries the current triangle count."""
	def GetVertexLevel(self) -> 'int':
		"""Queries the current vertex count."""
	def IsPreprocessing(self) -> 'bool':
		"""Checks whether the background preprocessing thread is still running."""
	def IsValid(self) -> 'bool':
		"""Checks if a valid object and a valid document are associated with the PolygonReduction instance."""
	def PreProcess(self, data: 'Dict[str, object]') -> 'bool':
		"""Starts the background or synchronous preprocessing that sets up the Polygon reduction cache."""
	def Reset(self) -> 'None':
		"""Aborts preprocessing if it is running in the background and frees all temporary data."""
	def SetReductionStrengthLevel(self, strengthLevel: 'float') -> 'bool':
		"""Sets the reduction strength level."""
	def SetRemainingEdgesLevel(self, desiredLevel: 'int') -> 'bool':
		"""Reduces or restores the mesh to the desired number of edges remaining to collapse."""
	def SetTriangleLevel(self, desiredLevel: 'int') -> 'bool':
		"""Reduces or restores the mesh to the desired number of triangles."""
	def SetVertexLevel(self, desiredLevel: 'int') -> 'bool':
		"""Reduces or restores the mesh to the desired number of vertices."""
	def StopPreprocessing(self) -> 'None':
		"""Aborts preprocessing if it is running in the background. Resets the interactive setting values."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def SendModelingCommand(command: int, list: List[BaseObject], mode: int, bc: Optional[BaseContainer], doc: Optional[BaseDocument], flags: Optional[int]) -> Union[bool, List[BaseObject]]:
	'''Sends a modeling command to Cinema 4D to change an object.'''
def DisjointMesh(op: PointObject) -> bool:
	'''Seperate the mesh.'''
def FitCurve(padr: List[Vector], error: float, bt: Optional[BaseThread]) -> None:
	'''Create a spline object that has a best fit through the given points.'''
def CheckDisplayFilter(op: BaseObject, filter: int) -> bool:
	'''Checks if an object is covered by a filter.'''
def CalculateVisiblePoints(bd: BaseDraw, op: PolygonObject, visible: Optional[bool]) -> Optional[List[int]]:
	'''Checks which points are visible in the current view.'''
def GenerateUVW(op: BaseObject, opmg: Matrix, tp: TextureTag, texopmg: Matrix, view: Optional[BaseView]) -> Optional[UVWTag]:
	'''Generate a UVW tag for an object.'''
def GetBBox(pObj: BaseObject, mg: Matrix) -> Tuple[Vector, Vector]:
	'''Get the bounding box of a hierarchie.'''
def FormatNumber(val: object, format: int, fps: int, bUnit: bool) -> str:
	'''Converts val to a string.'''
def StringToNumber(text: str, format: int, fps: int, lengthunit: int) -> Any:
	'''Converts a string to a data value.'''
def MixVec(v1: Vector, v2: Vector, t: float) -> Vector:
	'''Mixes the two vectors together, such as mixing two colours.'''
def MixNum(v1: float, v2: float, t: float) -> float:
	'''Returns a mixed value of v1 and v2 using the parameter t.'''
def Step(a: float, b: float) -> float:
	'''Returns 1.0 if x is greater than or equal to a, else 0.0.'''
def ClampValue(x: float, a: float, b: float) -> float:
	'''Returns a if x is less than a and b if x is greater than b, else returns x.'''
def Clamp(a: float, b: float, x: float) -> float:
	'''Returns a if x is less than a and b if x is greater than b, else returns x.'''
def Boxstep(a: float, b: float, x: float) -> float:
	'''Returns 0.0 if x is less than a and 1.0 if x is greater than b.'''
def Smoothstep(a: float, b: float, x: float) -> float:
	'''Returns 0.0 if x is less than a and 1.0 if x is greater than b.'''
def Bias(b: float, x: float) -> float:
	'''Returns the bias.'''
def CutColor(vec: Vector) -> Vector:
	'''Limit a color vector between 0.0 and 1.0.'''
def Truncate(x: float) -> float:
	'''Return the next int value towards zero.'''
def VectorSum(vec: object) -> float:
	'''Sum the vector components.'''
def VectorGray(vec: Vector) -> float:
	'''Sum the vector components and multiply by 1/3.'''
def VectorAngle(vec1: Vector, vec2: Vector) -> float:
	'''Calculates the angle between two vectors in radians.'''
def VectorMin(vec: Vector) -> float:
	'''Find the minimum component of the vector.'''
def VectorMax(vec: Vector) -> float:
	'''Find the maximum component of the vector.'''
def VectorEqual(v1: Vector, v2: Vector, epsilon: float) -> bool:
	'''Check if two vectors are equal.'''
def MatrixMove(vec: Vector) -> Matrix:
	'''Create a translation matrix.'''
def MatrixScale(s: Vector) -> Matrix:
	'''Create a scaling matrix.'''
def MatrixRotX(w: float) -> Matrix:
	'''Create a rotation matrix about the X axis.'''
def MatrixRotY(w: float) -> Matrix:
	'''Create a rotation matrix about the Y axis.'''
def MatrixRotZ(w: float) -> Matrix:
	'''Create a rotation matrix about the Z axis.'''
def QSlerp(q1: Quaternion, q2: Quaternion, alfa: float) -> Quaternion:
	'''Linear interpolates quaternions.'''
def QSquad(q0: Quaternion, q1: Quaternion, q2: Quaternion, q3: Quaternion, alfa: float) -> Quaternion:
	'''Cubic interpolates quaternions.'''
def QBlend(q1: Quaternion, q2: Quaternion, r: object) -> Quaternion:
	'''Smooth interpolates quaternions.'''
def QSpline(qn_m1: Quaternion, qn: Quaternion, qn_p1: Quaternion, qn_p2: Quaternion, t: float) -> Quaternion:
	'''Smooth blends quaternions.'''
def QSmoothCubic(qn_m1: Quaternion, qn: Quaternion, qn_p1: Quaternion, t: float) -> Quaternion:
	'''Smooth blends quaternions using Cubic interpolation.'''
def QNorm(q: Quaternion) -> Quaternion:
	'''Gets a normalized copy of a quaternion.'''
def QMul(q1: Quaternion, q2: Quaternion) -> Quaternion:
	'''Calculates the quaternion product of quaternions.'''
def QMulS(q: Quaternion, s: float) -> Quaternion:
	'''Calculates the quaternion product with a scalar.'''
def QAdd(q1: Quaternion, q2: Quaternion) -> Quaternion:
	'''Calculates the addition of quaternions.'''
def QSub(q1: Quaternion, q2: Quaternion) -> Quaternion:
	'''Calculates the subtraction of quaternions.'''
def QInvert(q: Quaternion) -> Quaternion:
	'''Calculates the inverse of a quaternion.'''
def QDot(q1: Quaternion, q2: Quaternion) -> float:
	'''Calculates the dot product between 2 quaternions.'''
def QDeriv(q: Quaternion, w: Vector) -> Quaternion:
	'''Calculates the derivative of a quaternion.'''
def QLogN(q: Quaternion) -> Quaternion:
	'''Calculates the natural logarithm of a quaternion.'''
def QExpQ(q: Quaternion) -> Quaternion:
	'''Calculates the exponential of a quaternion.'''
def MatrixToHPB(m: Matrix, order: int) -> Vector:
	'''Calculate euler angles from the matrix m.'''
def VectorToHPB(p: Vector) -> Vector:
	'''Calculate euler angles from the vector p.'''
def HPBToMatrix(hpb: Vector, order: int) -> Matrix:
	'''Construct matrix from the euler angles hpb.'''
def MatrixToRotAxis(m: Matrix) -> List[object]:
	'''Calculate matrix from rotation axis and an angle.'''
def RotAxisToMatrix(v: Vector, w: float) -> Matrix:
	'''Calculate matrix from rotation axis.'''
def GetOptimalAngle(hpb_old: Vector, hpb_new: Vector, rotation_order: int) -> Vector:
	'''Helps to avoid HPB singularity effects.'''
def PointLineDistance(p0: Vector, v: Vector, p: Vector) -> Vector:
	'''Calculate the distance from a point to a line.'''
def ReflectRay(v: Vector, n: Vector) -> Vector:
	'''Find the ray vector after a reflection about a surface normal.'''
def CalcSpline(x: float, knots: List[float]) -> float:
	'''Calculate the value of a spline at a point.'''
def CalcSplineV(x: float, knots: List[Vector]) -> Vector:
	'''Calculate the value of a spline at a point.'''
def RGBToHSV(col: Vector) -> Vector:
	'''Converts RGB into HSV.'''
def HSVToRGB(col: Vector) -> Vector:
	'''Converts HSV into RGB.'''
def RGBToHSL(col: Vector) -> Vector:
	'''Converts RGB into HSL.'''
def HSLtoRGB(col: Vector) -> Vector:
	'''Converts HSL into RGB.'''
def Deg(r: float) -> float:
	'''Converts float value from radians to degrees.'''
def Rad(d: object) -> float:
	'''Converts float value from degrees to radians.'''
def RadToDeg(r: float) -> float:
	'''Converts float value from radians to degrees.'''
def DegToRad(d: object) -> float:
	'''Converts float value from degrees to radians.'''
def FCut(a: float, b: float, c: float) -> None:
	'''Limit the value of a to between b and c.'''
def CalcLOD(val: int, lod: float, min: int, max: int) -> None:
	'''This is a helper function to modify a user chosen subdivision value.'''
def SinCos(w: float) -> List[object]:
	'''Get sine and cosine of the argument.'''
def RangeMap(value: float, mininput: float, maxinput: float, minoutput: float, maxoutput: float, clampval: bool, curve: Optional[SplineData]) -> float:
	'''Converts ranges.'''
def GetAngle(v1: Vector, v2: Vector) -> float:
	'''Returns the angel between two vectors.'''
def CompareFloatTolerant(a: float, b: float) -> bool:
	'''Compares if two floats are close to each other.'''
def TransformColor(input: Vector, colortransformation: int) -> Vector:
	'''Converts HSV into the RGB.'''
def CalculateTranslationScale(src: Union[BaseDocument, UnitScaleData], dst: Union[BaseDocument, UnitScaleData]) -> float:
	'''Transforms a color from one color profile to another.'''
def SphereLineIntersection(linePoint1: Vector, linePoint2: Vector, sphereCenter: Vector, sphereRadius: float) -> Tuple[bool, float, float, Vector, Vector]:
	'''Calculate the intersection points of a line through a sphere.'''
def CircleLineIntersection(linePoint1: Vector, linePoint2: Vector, circleCenter: Vector, circleRadius: float) -> Tuple[bool, float, float, Vector, Vector]:
	'''Calculate the intersection points of a line through a circle.'''
def PointLineSegmentDistance(segmentPoint1: Vector, segmentPoint2: Vector, pos: Vector) -> Tuple[float, Vector, float]:
	'''Calculate the distance from a point to a line segment between two points.'''
def PointLineSegmentDistance2D(segmentPoint1: Vector, segmentPoint2: Vector, pos: Vector) -> Tuple[float, Vector, float]:
	'''Calculate the distance from a point to a line segment between two points in 2D ignoring the Z value.'''
def CalcSplinePoint(offset: float, type: int, closed: bool, pcnt: int, padr: List[Vector], tadr: object) -> Vector:
	'''Calculate a point along a spline curve from a set of points in 3D space.'''
def CalcSplineTangent(offset: float, type: int, closed: bool, pcnt: int, padr: List[Vector], tadr: object) -> Vector:
	'''Calculate the tangent of a point along a spline curve from a given set of points and optional tangents.'''
def CalcSplineInsert(offset: float, type: int, closed: bool, pcnt: int, padr: List[Vector], tadr: object) -> None:
	'''Calculate data about a point would if it were inserted into the spline at the passed offset.'''
def TransformTangent(newPos: Vector, planeNormal: Vector, position: Vector, tangent: Dict[str, object], tangentSide: int, flags: int) -> None:
	'''Create a transformed tangent around a point and plane.'''
def CalcSplineMovement(newPos: Vector, offset: float, type: int, splineMg: Matrix, bd: Optional[BaseDraw], planeNormal: Optional[Vector], closed: Optional[bool], lockTangentAngle: Optional[bool], lockTangentLength: Optional[bool], breakTangents: Optional[int], pcnt: Optional[int], padr: Optional[List[Vector]], tadr: Optional[object]) -> None:
	'''Move a point on a spline curve to a user specified new position.'''
def CalcSplineDefaultTangents(type: int, closed: bool, pcnt: int, padr: List[Vector]) -> None:
	'''Calculate the default tangents for the passed points (spline segment) based on the spline type.'''
def BooleanSplines(initialSpline: BaseObject, booleanObjects: List[SplineObject], doc: BaseDocument, bd: BaseDraw, projectionAxis: int, booleanMode: int) -> Optional[BaseList2D]:
	'''Boolean an initial SplineObject with an array of other SplineObjects along a passed projection axis (in 2D).'''
def InitBakeTexture(doc: BaseDocument, textags: TextureTag, texuvws: UVWTag, destuvws: Optional[UVWTag], bc: Optional[BaseContainer], th: Optional[BaseThread]) -> Tuple[BaseDocument, int]:
	'''Initialize a bake operation.'''
def BakeTexture(doc: BaseDocument, data: BaseContainer, bmp: BaseBitmap, th: Optional[BaseThread], hook: Optional[Callable[[Dict[str, object]], Optional[bool]]]) -> int:
	'''Bake texture.'''
def IsUVToolMode(document: Any):
	'''Check if the current context is UV, if UV mode is selected or the UV Texture Editor is the last one used.'''

