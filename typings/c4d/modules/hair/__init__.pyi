from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseObject, BaseTag
if TYPE_CHECKING:
	from c4d import Vector, BaseSelect, Matrix, SplineObject
	from c4d.documents import BaseDocument
	from c4d.threading import BaseThread


class HairLibrary(object):
	"""The hair library."""
	def BlendColors(self, mode: 'int', colA: 'Vector', colB: 'Vector') -> 'Vector':
		"""Blend colors."""
	def GetHairVersion(self) -> 'int':
		"""Get the hair version."""
	def GetMode(self, doc: 'BaseDocument') -> 'int':
		"""Get hair mode."""
	def GetPolyPointST(self, p: 'Vector', pa: 'Vector', pb: 'Vector', pc: 'Vector', pd: 'Vector', bQuad: 'bool') -> 'Tuple[float, float]':
		"""Calculate the s and t coordinates of the point p in the polygon."""
	def MixST(self, s: 'float', t: 'float', pa: 'Vector', pb: 'Vector', pc: 'Vector', pd: 'Vector', bQuad: 'bool') -> 'Tuple[float, float]':
		"""Mix coordinates."""
	def SetMode(self, doc: 'BaseDocument', mode: 'int') -> 'None':
		"""Set hair mode."""

class HairObject(BaseObject):
	"""The hair object."""
	def GenerateHair(self, flags: 'int', count: 'int', segments: 'int') -> 'None':
		"""Generates hair for this hair object."""
	def GetDynamicGuides(self) -> 'HairGuides':
		"""Gets the dynamic guides of this hair object."""
	def GetGuides(self) -> 'HairGuides':
		"""Gets the guides of this hair object."""
	def GetRootObject(self) -> 'None':
		"""Gets the root object for this hair object."""
	def IsLocked(self) -> 'bool':
		"""Returns True if the hair is locked."""
	def Lock(self, pDoc: 'BaseDocument', pThread: 'BaseThread', bValidate: 'bool' = True, flags: 'int' = 0) -> 'bool':
		"""Lock the hair object."""
	def RemoveGuides(self) -> 'None':
		"""Remove the guides of the object."""
	def SetGuides(self, guides: 'HairGuides', clone: 'bool') -> 'None':
		"""Set the guides."""
	def Unlock(self) -> 'None':
		"""Unlock the hair object."""
	def Update(self) -> 'bool':
		"""Update the object."""

class HairGuides(object):
	"""The hair guides."""
	def ConvertSelection(self, from_mode: 'int', to_mode: 'int', from_select: 'BaseSelect', to_select: 'BaseSelect') -> 'None':
		"""Converts the selection state."""
	def CopyFrom(self, src: 'BaseSelect') -> 'bool':
		"""Copies the guide data."""
	def CreateSpline(self) -> 'SplineObject':
		"""Create splines from the guides."""
	def DisplaceRoots(self) -> 'None':
		"""Displaces the roots."""
	def GetCount(self) -> 'int':
		"""Gets the number of guides."""
	def GetFlags(self) -> 'int':
		"""Gets the flags."""
	def GetGuidePointCount(self) -> 'int':
		"""Gets the number of points per segment."""
	def GetMg(self) -> 'Matrix':
		"""Gets the global matrix."""
	def GetObject(self) -> 'HairObject':
		"""Returns the host object."""
	def GetPointCount(self) -> 'int':
		"""Gets the number of points per guide."""
	def GetPoints(self) -> 'List[Vector]':
		"""Get point vectors for the guides."""
	def GetRootAxis(self, index: 'int', bAlign: 'bool' = False, bLocal: 'bool' = True, bInitial: 'bool' = False, bZAxis: 'object' = False) -> 'Matrix':
		"""Gets the root axis."""
	def GetRootUV(self, index: 'int') -> 'Vector':
		"""Gets the root UV at index."""
	def GetSegmentCount(self) -> 'int':
		"""Gets the number of segments per guide."""
	def GetSelected(self, mode: 'int') -> 'Optional[BaseSelect]':
		"""Gets the selection state."""
	def GetTangent(self, guide: 'int', segment: 'int', t: 'float') -> 'None':
		"""Gets the tangent."""
	def GetTransformMatrix(self, index: 'int') -> 'List[Matrix]':
		"""Gets the transformation matrix list."""
	def SetFlags(self, flags: 'int') -> 'int':
		"""Sets the flags."""
	def SetMg(self, mg: 'Matrix') -> 'None':
		"""Sets the global matrix."""
	def SetPoint(self, id: 'int', p: 'Vector') -> 'None':
		"""Set point vector."""
	def SetSelected(self, mode: 'int', select: 'BaseSelect') -> 'bool':
		"""Sets the selection state."""
	def ToLocal(self) -> 'None':
		"""Changes points to local coordinate system."""
	def ToWorld(self) -> 'None':
		"""Changes points to world coordinate system."""
	def UndisplaceRoots(self) -> 'None':
		"""Undisplaces the roots."""

class HairSelectionTag(BaseTag):
	"""The hair object."""
	def GetCount(self) -> 'int':
		"""Gets the count."""
	def GetSegments(self) -> 'int':
		"""Gets the segment count."""
	def GetSelected(self) -> 'Optional[BaseSelect]':
		"""Gets the selection."""
	def GetSelectionType(self) -> 'int':
		"""Returns the selection type."""
	def SetSelected(self, bs: 'BaseSelect') -> 'bool':
		"""Sets the selection."""
	def SetSelectionType(self, mode: 'int') -> 'None':
		"""Set the mode."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class HairVertexMapTag(BaseTag):
	"""Hair vertex tag."""
	def GetCount(self) -> 'int':
		"""Gets the hair count."""
	def GetPointCount(self) -> 'int':
		"""Gets the point count."""
	def GetSegments(self) -> 'int':
		"""Gets the segment count."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class HairTangentTag(BaseTag):
	"""Hair tangent tag."""
	def GetCount(self) -> 'int':
		"""Gets the tangent count."""
	def GetPointCount(self) -> 'int':
		"""Gets the number of points."""
	def GetPolygonsSegments(self) -> 'int':
		"""Gets the number of polygon segments."""
	def GetSegments(self) -> 'int':
		"""Gets the segment count."""
	def GetTangents(self) -> 'List[Vector]':
		"""Get all tangents."""
	def SetTangent(self, i: 'int', p: 'Vector') -> 'None':
		"""Set a tangent."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""



