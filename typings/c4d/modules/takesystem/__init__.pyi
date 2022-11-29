from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseList2D
if TYPE_CHECKING:
	from c4d import DescID, BaseObject, BaseTag
	from c4d.documents import RenderData, BaseDocument


class TakeData(object):
	"""Take Data."""
	def AddTake(self, name: 'str', parent: 'Optional[BaseTake]' = True, cloneFrom: 'Optional[BaseTake]' = True) -> 'BaseTake':
		"""Create and insert a new take and return a pointer to it."""
	def CheckOverrideEnabling(self, mask: 'int') -> 'bool':
		"""Check for a specific OVERRIDEENABLING, internally also check for OVERRIDEENABLING::ALL and if it is not set return false even if the specific mask is set."""
	def DeleteTake(self, take: 'BaseTake') -> 'None':
		"""Delete passed take and all connected overrides, if take is the current take The main Take will be set as current."""
	def FindOverrideCounterPart(self, overrideNode: 'BaseOverride', descID: 'DescID') -> 'Tuple[BaseOverride, BaseTake]':
		"""Find the backup node that fit with override (for example the backup node in the main take)."""
	def GetCurrentTake(self) -> 'BaseTake':
		"""Retrieve a pointer to the current for doc."""
	def GetDocument(self) -> 'Optional[BaseDocument]':
		"""Retrieve the BaseDocument for this TakeData."""
	def GetMainTake(self) -> 'BaseTake':
		"""Retrieve a pointer to the Main take in doc."""
	def GetOverrideEnabling(self) -> 'int':
		"""Retrieve the ability for the take system to override a specific kind of node based on global switch."""
	def GetTakeMode(self) -> 'int':
		"""Retrieve the take system global mode, can be TAKE_MODE::MANUAL or TAKE_MODE::AUTO."""
	def GetTakeSelection(self, children: 'object') -> 'List[BaseTake]':
		"""Fill selection with all selected takes in doc."""
	def GetUndoState(self) -> 'bool':
		"""Returns if the takes automatic undo system is active or not."""
	def InsertTake(self, takeToMove: 'BaseTake', destTake: 'Optional[BaseTake]' = None, insertMode: 'Optional[int]' = None) -> 'None':
		"""Function to move a take in hierarchy in a safe way."""
	def ResetSystem(self) -> 'None':
		"""Reset completely the take system for the document, usually not needed."""
	def SaveTakesWithAssets(self, selected: 'bool') -> 'bool':
		"""Execute a Save Project With Assets for takes in document, each new file represent a take."""
	def SetCurrentTake(self, take: 'BaseTake') -> 'bool':
		"""Set take as current Take in doc, if nullptr is passed as take MainTake will be used."""
	def SetUndoState(self, state: 'bool') -> 'None':
		"""Set the state of the takes automatic undo system."""
	def TakeToDocument(self, take: 'BaseTake') -> 'BaseDocument':
		"""Isolate passed take in a new document, the new document will be allocated and filled by the function."""

class BaseTake(BaseList2D):
	"""Take Node."""
	def AddOverrideGroup(self) -> 'BaseOverrideGroup':
		"""Add a new override group to this take."""
	def AutoTake(self, takeData: 'TakeData', node: 'BaseList2D', undo: 'BaseList2D') -> 'None':
		"""Automatically override the node by comparing it with passed undo node."""
	def DeleteOverride(self, takeData: 'TakeData', node: 'BaseList2D', descID: 'DescID') -> 'None':
		"""Delete a single parameter override for node at descID, if the override result empty (no more overridden parameters in it) will be deleted too."""
	def DeleteOverrideGroup(self, takeData: 'TakeData', og: 'BaseOverrideGroup') -> 'None':
		"""Delete the override group og from this take."""
	def FindOrAddOverrideParam(self, takeData: 'TakeData', node: 'BaseList2D', descID: 'DescID', overrideValue: 'object', backupValue: 'Optional[object]' = True, deleteAnim: 'Optional[bool]' = False) -> 'BaseOverride':
		"""Search if parameter at descID is Overridden, if not add a new override with passed value for this take."""
	def FindOverride(self, takeData: 'TakeData', node: 'BaseList2D') -> 'Optional[BaseOverride]':
		"""Search if node is overridden in this take and return a pointer if exist."""
	def FindOverrideInHierarchy(self, takeData: 'TakeData', node: 'BaseList2D', descID: 'DescID') -> 'Tuple[BaseOverride, BaseTake]':
		"""Search if node parameter at descId is overridden in this or in a parent take return a pointer if exist, also fill a real take that own the override."""
	def GetCamera(self, takeData: 'TakeData') -> 'Optional[BaseObject]':
		"""Get the camera for this take."""
	def GetEffectiveCamera(self, takeData: 'TakeData') -> 'Tuple[BaseObject, BaseTake]':
		"""Get the camera used by this take even if it come from one of the parents take."""
	def GetEffectiveRenderData(self, takeData: 'TakeData') -> 'Tuple[RenderData, BaseTake]':
		"""Get the RenderData used by this take even if it come from one of the parents take."""
	def GetFirstOverrideGroup(self) -> 'Optional[BaseOverrideGroup]':
		"""Get the first override group in this take."""
	def GetOverrideGroups(self) -> 'List[BaseOverrideGroup]':
		"""Fill selection array with all override groups nodes owned by this take."""
	def GetOverrides(self) -> 'List[BaseOverride]':
		"""Fill selection array with all override nodes owned by this take."""
	def GetRenderData(self, takeData: 'TakeData') -> 'Optional[RenderData]':
		"""Get the RenderData for this take."""
	def IsChecked(self) -> 'Tuple[RenderData, BaseTake]':
		"""Get if the take is marked."""
	def IsMain(self) -> 'bool':
		"""Check if this take is the main take."""
	def OverrideNode(self, takeData: 'TakeData', node: 'BaseList2D', deleteAnim: 'bool') -> 'BaseOverride':
		"""Override all parameters of passed node in this take."""
	def Reset(self) -> 'None':
		"""Reset all sub structures an overrides for this take."""
	def SearchHierarchy(self, op: 'BaseTake') -> 'bool':
		"""Checks if the this take is a child of op."""
	def SetCamera(self, takeData: 'TakeData', camera: 'Optional[BaseObject]' = None) -> 'None':
		"""Set the camera for this take."""
	def SetChecked(self, status: 'bool') -> 'None':
		"""Set the take mark."""
	def SetRenderData(self, takeData: 'TakeData', rData: 'Optional[RenderData]' = None) -> 'None':
		"""Set the RenderData for this take."""

class BaseOverride(BaseList2D):
	"""Override Node."""
	def GetAllOverrideDescID(self) -> 'List[DescID]':
		"""Fill a list with all DescID overridden in this BaseOverride."""
	def GetOwnerTake(self, takeData: 'TakeData') -> 'BaseTake':
		"""Get a pointer to a the take that own this override."""
	def GetSceneNode(self) -> 'BaseList2D':
		"""Returns a pointer to the original scene node connected to this override node."""
	def IsInGroup(self, takeData: 'TakeData') -> 'Tuple[bool, BaseOverrideGroup]':
		"""Check if this override is also part of a override group, and if yes returns also the restult group."""
	def IsOverriddenParam(self, descID: 'DescID') -> 'bool':
		"""Returns if the parameter at descID is overridden."""
	def UpdateSceneNode(self, takeData: 'TakeData', descID: 'DescID') -> 'None':
		"""Call this function whenever you change data directly on the base override (for example with SetParameter), this ensure the scene node is properly updated if the override affect the current document state."""

class BaseOverrideGroup(BaseList2D):
	"""Override Group Node."""
	def AddTag(self, takeData: 'TakeData', type: 'int', mat: 'Optional[TakeData]' = True) -> 'BaseTag':
		"""Add a new tag of type to this Override Group if it is not already there."""
	def AddToGroup(self, takeData: 'TakeData', node: 'BaseList2D') -> 'None':
		"""Add node to this Override Group, if node is already part of another group it will be automatically removed first."""
	def Find(self, takeData: 'TakeData', op: 'BaseObject') -> 'bool':
		"""Check if op is included in this group."""
	def GetEditorMode(self) -> 'int':
		"""Returns the editor visibility mode for this group."""
	def GetObjectsInGroup(self) -> 'List[BaseList2D]':
		"""Fill selection array with all objects in the group."""
	def GetRenderMode(self) -> 'int':
		"""Returns the render visibility mode for this group."""
	def GetTag(self, type: 'int') -> 'Optional[BaseTag]':
		"""Search for a tag of a type attached to this group."""
	def GetTake(self) -> 'BaseTake':
		"""Returns the Take that own this group."""
	def RemoveFromGroup(self, takeData: 'TakeData', node: 'BaseList2D') -> 'None':
		"""Remove node to this Override Group."""
	def RemoveTag(self, takeData: 'TakeData', type: 'int') -> 'None':
		"""Remove the tag of type from this Override Group."""
	def SetEditorMode(self, mode: 'object') -> 'None':
		"""Set the editor visibility mode for this group."""
	def SetRenderMode(self, mode: 'object') -> 'None':
		"""Set the render visibility mode for this group."""


def IsTakeRenderRunning() -> bool:
	'''Checks if a Take render is running.'''
def StopTakeRender() -> None:
	'''Stops the Take render if it is running.'''

