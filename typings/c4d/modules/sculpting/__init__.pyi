from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseTag, BaseObject, BaseList2D
if TYPE_CHECKING:
	from c4d import PolygonObject, Vector, BaseDraw, CPolygon, BaseContainer
	from c4d.utils import Neighbor
	from c4d.bitmaps import BaseBitmap
	from c4d.documents import BaseDocument


class SculptTag(BaseTag):
	"""Tag which represents a sculpt tag."""
	def GetSculptObject(self) -> 'SculptObject':
		"""Returns the Sculpt Object."""

class SculptObject(BaseObject):
	"""Sculpt object."""
	def AddFolder(self) -> 'SculptFolder':
		"""Add a folder."""
	def AddLayer(self) -> 'SculptLayer':
		"""Adds a layer at the current subdivision level."""
	def DecreaseSubdivisionLevel(self) -> 'bool':
		"""Decrease the subdivision level of the sculpt object."""
	def DeleteSelectedLayer(self) -> 'bool':
		"""Delete the currently selected layer."""
	def EndUndo(self) -> 'None':
		"""Called when the user has finished making changes to the layers."""
	def GetAllowDeformations(self) -> 'bool':
		"""Is the allow deformations option enabled."""
	def GetBaseLayer(self) -> 'SculptLayerBase':
		"""Get the base layer of the sculpt object."""
	def GetCurrentLayer(self) -> 'SculptLayerBase':
		"""Get the currently selected layer on the sculpt object."""
	def GetCurrentLevel(self) -> 'int':
		"""Get the current subdivision level."""
	def GetDisplayPolygonObject(self) -> 'PolygonObject':
		"""Get the PolygonObject for the currently displayed subdivision level."""
	def GetFaceNormal(self, index: 'int') -> 'Vector':
		"""Get the face normal for a given polygon."""
	def GetFirstLayer(self) -> 'SculptLayerBase':
		"""Get the first layer of the sculpt object."""
	def GetMaskCachePoint(self, id: 'int') -> 'float':
		"""Get the mask value from the mask cache."""
	def GetMemoryUsage(self) -> 'int':
		"""Get the amount of memory used by the sculpt object."""
	def GetOriginalObject(self) -> 'PolygonObject':
		"""Get the object the sculpt tag is applied to for this sculpt object."""
	def GetPoint(self, index: 'int') -> 'Vector':
		"""Get the vertex position for a given point."""
	def GetPointCount(self) -> 'int':
		"""Get the point count at the current subdivision level."""
	def GetPolygon(self, index: 'int') -> 'Optional[CPolygon]':
		"""Get the polygon on the current subdivision give the polygon index."""
	def GetPolygonCopy(self, level: 'int', includeTopLevels: 'bool') -> 'PolygonObject':
		"""Get a copy of the current subdivision level from the sculpt object."""
	def GetPolygonCount(self) -> 'int':
		"""Get the polygon count at the current subdivision level"""
	def GetSubdivisionCount(self) -> 'int':
		"""Get the number of subdivisions for this sculpt object."""
	def GetVertexNormal(self, index: 'int') -> 'Vector':
		"""Get the vertex normal for a given point."""
	def HitObject(self, rayp: 'Vector', rayv: 'Vector', backfaces: 'bool') -> 'None':
		"""Get the hit data for the sculpt object by casting a ray in object space."""
	def HitScreen(self, bd: 'BaseDraw', mx: 'float', my: 'float', backfaces: 'bool') -> 'None':
		"""Get the hit data for the sculpt object using screen coordinates."""
	def IncreaseSubdivisionLevel(self) -> 'bool':
		"""Increase the subdivision level of the sculpt object."""
	def InitOpenGL(self, bd: 'Optional[BaseDraw]' = None) -> 'None':
		"""Private! Ensure the object is initialized in OpenGL correctly for the given viewport."""
	def IsFrozen(self) -> 'bool':
		"""Is the sculpt object frozen."""
	def IsPointSelected(self, index: 'int') -> 'bool':
		"""Returns true if the object is a Polygon Object, the doc mode is Mpoints and the point is selected."""
	def IsPolygonSelected(self, index: 'int') -> 'bool':
		"""Returns true if the object is a Polygon Object, the doc mode is Mpolygons and the polygon is selected."""
	def NeedCollisionUpdate(self, fullUpdate: 'bool') -> 'None':
		"""Tell the sculpt object that it needs its collision data updated."""
	def SetAllowDeformations(self, allowDef: 'bool') -> 'None':
		"""Set the allow deformations option."""
	def SetFrozen(self, frozen: 'bool') -> 'None':
		"""Set the frozen state for the sculpt object."""
	def Smooth(self, count: 'int', respectMask: 'bool') -> 'None':
		"""Smooth the sculpt object and apply the offsets to the currently selected layer."""
	def StartUndo(self) -> 'None':
		"""Allow changes to a layer to be undo-able."""
	def Subdivide(self) -> 'bool':
		"""Subdivide the sculpt object."""
	def Update(self) -> 'None':
		"""Re-composite and update the sculpt object."""
	def UpdateCollision(self) -> 'None':
		"""Update the collision date for the sculpt object."""
	def UpdateMask(self, fullUpdate: 'bool') -> 'None':
		"""Update the Mask Cache."""

class SculptLayerBase(BaseObject):
	"""Sculpt Layer Base."""
	def GetStrength(self) -> 'float':
		"""Gets the strength of the sculpt layer."""
	def IsLocked(self) -> 'bool':
		"""Returns true if the sculpt layer is locked."""
	def IsVisible(self) -> 'bool':
		"""Returns true if the sculpt layer is visible."""
	def Select(self) -> 'bool':
		"""Set this layer as the currently selected one."""
	def SetLocked(self, state: 'bool') -> 'None':
		"""Sets the locked state of the sculpt layer."""
	def SetStrength(self, strength: 'float') -> 'None':
		"""Sets the strength of the sculpt layer."""
	def SetVisible(self, state: 'bool') -> 'None':
		"""Sets the visibility of the sculpt layer."""

class SculptLayer(SculptLayerBase):
	"""Sculpt Layer."""
	def AddOffset(self, index: 'int', offset: 'Vector') -> 'None':
		"""Add an offset to the point on the sculpt layer."""
	def AddToMask(self, index: 'int', mask: 'float') -> 'None':
		"""Add to the mask value for the point on the sculpt layer."""
	def ClearLayer(self) -> 'None':
		"""Removes the sculpting data from the sculpt layer."""
	def ClearMask(self) -> 'None':
		"""Removes the mask data from the sculpt layer."""
	def GetCurrentSculptLayer(self) -> 'SculptLayerData':
		"""Get the currently used layer data. In the case of the BaseLayer it will get the data for the current subdivision level. For all other layers it will return the same as GetFirstSculptLayerData()."""
	def GetFirstSculptLayer(self) -> 'SculptLayerData':
		"""Get the first layer data for this layer, the BaseLayer will have more than one, other layers only have 1."""
	def GetMask(self, index: 'int') -> 'float':
		"""Get the mask value for a point on the sculpt layer."""
	def GetOffset(self, index: 'int') -> 'Vector':
		"""Get the offset for a point on the sculpt layer."""
	def GetPointCount(self) -> 'int':
		"""Get point count for the sculpt layer."""
	def HasMask(self) -> 'bool':
		"""Does this sculpt layer have a mask."""
	def InitializeAllMaskData(self) -> 'None':
		"""Ensures all the data is allocated for the layers mask data"""
	def InitializeAllPointData(self) -> 'None':
		"""Ensures all the data is allocated for the layers point data"""
	def IsBaseLayer(self) -> 'bool':
		"""Is this sculpt layer the base layer."""
	def IsMaskEnabled(self) -> 'bool':
		"""Is the mask enabled fro the sculpt layer."""
	def SetMask(self, index: 'int', mask: 'float') -> 'None':
		"""Set the mask value for a point on the sculpt layer."""
	def SetMaskEnabled(self, state: 'bool') -> 'None':
		"""Enable or Disable the mask for the sculpt layer."""
	def SetOffset(self, index: 'int', offset: 'Vector') -> 'None':
		"""Set the offset for a point on the sculpt layer."""
	def TouchMaskForUndo(self, index: 'int') -> 'None':
		"""Marks a mask so that any changes to it can be undone. Must be called after SculptObject.StartUndo()"""
	def TouchPointForUndo(self, index: 'int') -> 'None':
		"""Marks a point so that any changes to it can be undone. Must be called after SculptObject.StartUndo()"""

class SculptLayerData(BaseList2D):
	"""Sculpt Layer."""
	def AddOffset(self, index: 'int', offset: 'Vector') -> 'None':
		"""Add an offset to the point on the sculpt layer."""
	def AddToMask(self, index: 'int', mask: 'float') -> 'None':
		"""Add to the mask value for the point on the sculpt layer."""
	def ClearLayer(self) -> 'None':
		"""Removes the sculpting data from the sculpt layer."""
	def ClearMask(self) -> 'None':
		"""Removes the mask data from the sculpt layer."""
	def GetMask(self, index: 'int') -> 'Optional[float]':
		"""Get the mask value for a point on the sculpt layer."""
	def GetOffset(self, index: 'int') -> 'Vector':
		"""Get the offset for a point on the sculpt layer."""
	def GetPointCount(self) -> 'int':
		"""Get point count for the sculpt layer."""
	def GetSubdivisionLevel(self) -> 'int':
		"""Get point count for the sculpt layer."""
	def HasMask(self) -> 'bool':
		"""Does this sculpt layer have a mask."""
	def InitializeAllMaskData(self) -> 'None':
		"""Ensures all the data is allocated for the layers mask data"""
	def InitializeAllPointData(self) -> 'None':
		"""Ensures all the data is allocated for the layers point data"""
	def SetMask(self, index: 'int', mask: 'float') -> 'None':
		"""Set the mask value for a point on the sculpt layer."""
	def SetOffset(self, index: 'int', offset: 'Vector') -> 'None':
		"""Set the offset for a point on the sculpt layer."""
	def TouchMaskForUndo(self, index: 'int') -> 'None':
		"""Marks a mask so that any changes to it can be undone. Must be called after SculptObject.StartUndo()"""
	def TouchPointForUndo(self, index: 'int') -> 'None':
		"""Marks a point so that any changes to it can be undone. Must be called after SculptObject.StartUndo()"""

class SculptFolder(SculptLayerBase):
	"""Sculpt Folder."""

class SculptBrushParams(object):
	"""The sculpt brush params class."""
	def EnableBackfaceSculpting(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableBuildup(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableDrawDirection(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableFillToolIsolatedPointRemover(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableFlood(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableInvertCheckbox(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableModifier(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableMouseData(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableNonModelPickMode(self, enable: 'bool') -> 'None':
		"""None"""
	def EnablePressureHUD(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableRespectSelections(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableStamp(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableStencil(self, enable: 'bool') -> 'None':
		"""None"""
	def EnableToolSpecificSmooth(self, enable: 'bool') -> 'None':
		"""None"""
	def SetBrushMode(self, mode: 'int') -> 'None':
		"""None"""
	def SetFirstHitPointType(self, type: 'int') -> 'None':
		"""None"""
	def SetFloodType(self, type: 'int') -> 'None':
		"""None"""
	def SetPolygonObjectDirtyFlags(self, type: 'int') -> 'None':
		"""None"""
	def SetUndoType(self, type: 'int') -> 'None':
		"""None"""

class BrushDabData(object):
	"""The brush dab data class."""
	def ApplySmooth(self) -> 'None':
		"""None"""
	def DirtyAllPoints(self, flags: 'int') -> 'None':
		"""None"""
	def GetAutoScaleValue(self, noRadius: 'bool') -> 'float':
		"""None"""
	def GetAveragePointAndNormal(self) -> 'None':
		"""None"""
	def GetBaseDraw(self) -> 'int':
		"""None"""
	def GetBaseObject(self) -> 'PolygonObject':
		"""None"""
	def GetBrushFalloff(self, index: 'int', customDistance: 'float' = -1.0) -> 'float':
		"""None"""
	def GetBrushFalloffFromPos(self, pos: 'Vector') -> 'float':
		"""None"""
	def GetBrushOverride(self) -> 'int':
		"""None"""
	def GetBrushRadius(self) -> 'float':
		"""None"""
	def GetBrushStrength(self) -> 'float':
		"""None"""
	def GetData(self) -> 'BaseContainer':
		"""None"""
	def GetDrawDirectionNormal(self) -> 'Vector':
		"""None"""
	def GetEyePoint(self) -> 'Vector':
		"""None"""
	def GetFaceNormal(self, index: 'int') -> 'Vector':
		"""None"""
	def GetHitPoint(self) -> 'Vector':
		"""None"""
	def GetHitPolygon(self) -> 'int':
		"""None"""
	def GetLastHitPoint(self) -> 'Vector':
		"""None"""
	def GetLayer(self) -> 'Optional[SculptLayer]':
		"""None"""
	def GetMirrorPoint(self, point: 'Vector', isNormal: 'bool') -> 'Vector':
		"""None"""
	def GetMousePos3D(self) -> 'Vector':
		"""None"""
	def GetNeighbor(self) -> 'Optional[Neighbor]':
		"""None"""
	def GetNormal(self) -> 'Vector':
		"""None"""
	def GetObject(self) -> 'SculptObject':
		"""None"""
	def GetOriginalPoint(self, index: 'int') -> 'Vector':
		"""None"""
	def GetOriginalVertexNormal(self, index: 'int') -> 'Vector':
		"""None"""
	def GetPoint(self, index: 'int') -> 'Vector':
		"""None"""
	def GetPointCount(self) -> 'int':
		"""None"""
	def GetPointData(self, index: 'int') -> 'None':
		"""None"""
	def GetPolyCount(self) -> 'int':
		"""None"""
	def GetPolyData(self, index: 'int') -> 'None':
		"""None"""
	def GetPolygonObject(self) -> 'PolygonObject':
		"""None"""
	def GetStamp(self) -> 'BaseBitmap':
		"""None"""
	def GetStampColor(self, point: 'int', distance: 'float', mode: 'int') -> 'None':
		"""None"""
	def GetStencil(self) -> 'BaseBitmap':
		"""None"""
	def GetStencilColor(self, point: 'int', mode: 'Optional[int]' = 0) -> 'None':
		"""None"""
	def GetStrokeInstanceID(self) -> 'int':
		"""None"""
	def GetVertexNormal(self, index: 'int') -> 'Vector':
		"""None"""
	def IsBackface(self) -> 'bool':
		"""None"""
	def IsFillTool(self) -> 'bool':
		"""None"""
	def IsMirroredDab(self) -> 'bool':
		"""None"""
	def IsPointModified(self, index: 'int') -> 'bool':
		"""None"""
	def IsPreviewDab(self) -> 'bool':
		"""None"""
	def IsSculptObject(self) -> 'bool':
		"""None"""
	def OffsetPoint(self, index: 'int', offset: 'Vector', respectStrength: 'int' = 0) -> 'None':
		"""None"""
	def OffsetPreviewPoint(self, index: 'int', offset: 'Vector') -> 'None':
		"""None"""

class SculptModifierInterface(object):
	"""The Sculpt Modifier Interface."""
	def ApplyModifier(self, modifierId: 'int', vertex: 'int', brushData: 'BaseContainer', modifierData: 'BaseContainer', respectselections: 'bool' = False) -> 'bool':
		"""None"""
	def ApplyModifierExact(self, modifierId: 'int', vertex: 'int', brushData: 'BaseContainer', modifierData: 'BaseContainer', hitpoint: 'Vector', lasthitpoint: 'Vector', respectselections: 'bool' = False) -> 'bool':
		"""None"""
	def Clear(self) -> 'None':
		"""None"""
	def GetDefaultData(self) -> 'BaseContainer':
		"""None"""
	def GetModifierCount(self) -> 'int':
		"""None"""
	def GetModifierInfo(self, index: 'int') -> 'None':
		"""None"""
	def Init(self, poly: 'PolygonObject') -> 'bool':
		"""None"""
	def SetData(self, brushData: 'BaseContainer', modifierData: 'BaseContainer') -> 'bool':
		"""None"""


def MakeSculptObject(obj: PolygonObject, doc: BaseDocument) -> None:
	'''Adds a sculpt tag to a Polygon Object.'''
def GetSelectedSculptObject(doc: BaseDocument) -> None:
	'''Get the currently selected sculpt object if there is one.'''

