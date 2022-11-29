"""Module for document handling."""

from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseList2D, ASSETDATA_FLAG_NONE, SELECTION_NEW
if TYPE_CHECKING:
	from c4d.modules.net import RenderJob
	from uuid import UUID
	from c4d.bitmaps import BaseBitmap
	from c4d import BaseContainer, BaseDraw, GeListHead, DescID, BaseTime, BaseObject, BaseTag, BaseMaterial, C4DAtom, CKey
	from c4d.modules.thinkingparticles import TP_MasterSystem
	from c4d.threading import BaseThread
	from c4d.modules.takesystem import TakeData
	from c4d.storage import MemoryFileStruct


class BaseDocument(BaseList2D):
	"""Represents a document."""
	def AddUndo(self, type: 'int', data: 'BaseList2D', allowFromThread: 'Optional[bool]' = False) -> 'bool':
		"""Perform a redo on this document (undo the last undo)."""
	def AnimateObject(self, op: 'BaseList2D', time: 'BaseTime', flags: 'int') -> 'None':
		"""Animate a node in this document."""
	def AutoKey(self, op: 'BaseObject', undo: 'BaseList2D', recursive: 'bool', pos: 'bool', scale: 'bool', rot: 'bool', param: 'bool', pla: 'bool') -> 'None':
		"""Automatically keys an object's parameters by comparing it to it's previous state (via the passed undo object)."""
	def DoRedo(self) -> 'bool':
		"""Perform a redo on this document (undo the last undo)."""
	def DoUndo(self, multiple: 'bool' = False) -> 'bool':
		"""Perform an undo operation."""
	def EndUndo(self) -> 'bool':
		"""End the building of multiple undo actions into a single user undo."""
	def ExecutePasses(self, bt: 'Optional[BaseThread]' = None, animation: 'Optional[bool]' = None, expressions: 'Optional[bool]' = None, caches: 'Optional[bool]' = None, flags: 'Optional[int]' = None) -> 'bool':
		"""Animate the current frame of the document."""
	def FindSceneHook(self, id: 'int') -> 'Optional[BaseList2D]':
		"""Finds a scene hook by ID."""
	def FindUndoPtr(self, bl: 'BaseList2D', type: 'int') -> 'BaseList2D':
		"""Returns the last undo state of an the Cinema 4D element"""
	def Flush(self) -> 'None':
		"""Empties the document."""
	def FlushUndoBuffer(self) -> 'None':
		"""Flushes the undo buffer."""
	def ForceCreateBaseDraw(self) -> 'None':
		"""Makes sure that GetBaseDraw(0) is accessible."""
	def GetAction(self) -> 'int':
		"""Get the current tool in the editor."""
	def GetActiveBaseDraw(self) -> 'BaseDraw':
		"""Get the activate BaseDraw in the editor."""
	def GetActiveMaterial(self) -> 'Optional[BaseMaterial]':
		"""Get the first object BaseMaterial of the document."""
	def GetActiveMaterials(self) -> 'List[BaseMaterial]':
		"""Inserts the material into the document's material list."""
	def GetActiveObject(self) -> 'Optional[BaseObject]':
		"""Get the currently active object in this document."""
	def GetActiveObjects(self, flags: 'int') -> 'List[BaseList2D]':
		"""Returns the BaseTag selection."""
	def GetActiveObjectsFilter(self, children: 'bool', type: 'int', instanceof: 'int') -> 'List[BaseList2D]':
		"""Returns the active objects filter list."""
	def GetActiveRenderData(self) -> 'RenderData':
		"""Get the active render settings for the document."""
	def GetActiveTag(self) -> 'Optional[BaseTag]':
		"""Get the currently active tag in this document.
"""
	def GetActiveTags(self) -> 'List[BaseTag]':
		"""Returns the BaseTag selection."""
	def GetActiveToolData(self) -> 'BaseContainer':
		"""Returns the current active tool."""
	def GetAllTextures(self, isNet: 'bool' = True, ar: 'Optional[List[C4DAtom]]' = None) -> 'BaseContainer':
		"""Returns all textures in the document."""
	def GetBaseDraw(self, bd: 'int') -> 'Optional[BaseDraw]':
		"""Get the BaseDraw from one of the editor views."""
	def GetBaseDrawCount(self) -> 'int':
		"""Get the BaseDraw count in the editor view."""
	def GetChanged(self) -> 'bool':
		"""Check if the document was changed since last time saved."""
	def GetData(self, type: 'int') -> 'BaseContainer':
		"""Returns the document settings."""
	def GetDefaultKey(self) -> 'Optional[Tuple[CKey, bool]]':
		"""Returns the document's default keying settings."""
	def GetDocPreviewBitmap(self) -> 'Optional[BaseBitmap]':
		"""Get the doc preview bitmap of the document."""
	def GetDocumentData(self, type: 'int') -> 'BaseContainer':
		"""Returns the document settings."""
	def GetDocumentName(self) -> 'str':
		"""Returns the document name"""
	def GetDocumentPath(self) -> 'str':
		"""Returns the document path"""
	def GetDrawTime(self) -> 'int':
		"""Get the editor redraw time."""
	def GetFirstMaterial(self) -> 'Optional[BaseMaterial]':
		"""Get the first object BaseMaterial of the document."""
	def GetFirstObject(self) -> 'Optional[BaseObject]':
		"""Get the first object BaseObject of the document"""
	def GetFirstRenderData(self) -> 'Optional[RenderData]':
		"""Get the first render settings for the document."""
	def GetFps(self) -> 'int':
		"""Get frames per second"""
	def GetHelperAxis(self) -> 'BaseObject':
		"""The helper axis for the current multi selection."""
	def GetHighest(self, type: 'int', editor: 'bool') -> 'Optional[BaseObject]':
		"""The first object in object manager hierarchy of type type."""
	def GetLOD(self) -> 'float':
		"""Returns the LOD."""
	def GetLayerObjectRoot(self) -> 'Optional[GeListHead]':
		"""Returns the list of layers of the document."""
	def GetLoopMaxTime(self) -> 'BaseTime':
		"""Returns the right boundary of the document's preview range."""
	def GetLoopMinTime(self) -> 'BaseTime':
		"""Returns the left boundary of the document's preview range."""
	def GetMaterials(self) -> 'List[BaseMaterial]':
		"""Returns a tuple of materials stored in the object manager."""
	def GetMaxTime(self) -> 'BaseTime':
		"""Returns the max time"""
	def GetMinTime(self) -> 'BaseTime':
		"""Returns the min time"""
	def GetMode(self) -> 'int':
		"""Get the main mode of the editor."""
	def GetObjects(self) -> 'List[BaseObject]':
		"""Returns a tuple of objects stored in the object manager."""
	def GetOrderedActiveObjects(self) -> 'List[BaseList2D]':
		"""Returns the active objects in an ordered list."""
	def GetParticleSystem(self) -> 'Optional[TP_MasterSystem]':
		"""Returns the particlesystem."""
	def GetPickSession(self) -> 'Optional[Tuple[List[C4DAtom], bool]]':
		"""Returns the data structure of the current pick session."""
	def GetRealActiveObject(self, help: 'Optional[Iterable[BaseObject]]' = None) -> 'Optional[Tuple[BaseObject, bool]]':
		"""Returns the active object or the dummy axis if multiple objects are selected."""
	def GetRenderBaseDraw(self) -> 'BaseDraw':
		"""This is the BaseDraw belonging to the view."""
	def GetRenderLod(self) -> 'bool':
		"""Returns the right boundary of the document's preview range."""
	def GetSelection(self) -> 'List[BaseList2D]':
		"""Returns the current selection."""
	def GetSettingsInstance(self, type: 'int') -> 'BaseContainer':
		"""Get the BaseContainer setting of the specified type."""
	def GetSplinePlane(self) -> 'int':
		"""Get the spline plane."""
	def GetTakeData(self) -> 'TakeData':
		"""Returns the take system context for this document."""
	def GetTargetObject(self) -> 'Optional[BaseObject]':
		"""Returns the target object within a multi-selection."""
	def GetTime(self) -> 'BaseTime':
		"""Returns the time"""
	def GetTrackDefaultInterpolationMode(self) -> 'int':
		"""Gets the track default interpolation mode."""
	def GetUndoPtr(self) -> 'BaseList2D':
		"""Returns the element of the last undo action."""
	def InsertMaterial(self, op: 'BaseMaterial', pred: 'Optional[BaseObject]' = None, checknames: 'Optional[bool]' = True) -> 'None':
		"""Inserts the material into the document's material list."""
	def InsertObject(self, op: 'Optional[BaseObject]' = None, parent: 'Optional[BaseObject]' = True, pred: 'Optional[BaseObject]' = True, checknames: 'Optional[bool]' = False) -> 'None':
		"""Inserts the object into the document's object hierarchy."""
	def InsertRenderData(self, rd: 'RenderData', parent: 'Optional[RenderData]' = True, pred: 'Optional[RenderData]' = True) -> 'None':
		"""Inserts a renderdata into the document's renderdata list."""
	def InsertRenderDataLast(self, rd: 'RenderData') -> 'None':
		"""Inserts the renderdata as last child into the document's render data list."""
	def IsAxisEnabled(self) -> 'bool':
		"""Returns the state of the object axis modifier."""
	def IsEditMode(self) -> 'bool':
		"""Check if the editor is in an editable mode. """
	def Polygonize(self, keepanimation: 'bool' = False) -> 'Optional[BaseDocument]':
		"""Make a clone of the document."""
	def Record(self) -> 'None':
		"""Records the state of the document."""
	def RecordKey(self, op: 'BaseList2D', id: 'DescID', time: 'BaseTime', undo: 'Optional[BaseList2D]' = None, autoKey: 'Optional[bool]' = None, eval_attribmanager: 'Optional[bool]' = None) -> 'bool':
		"""Records a key for a parameter on an object."""
	def SearchMaterial(self, name: 'str') -> 'Optional[BaseMaterial]':
		"""Search for a material with the same case sensitive name."""
	def SearchObject(self, name: 'str') -> 'Optional[BaseObject]':
		"""Search for an object with the same case sensitive name."""
	def SendInfo(self, type: 'int', format: 'int', fn: 'str', bl: 'BaseList2D', hooks_only: 'bool') -> 'None':
		"""Sends MSG_DOCUMENTINFO messages."""
	def SetAction(self, a: 'int') -> 'None':
		"""Set the current tool in the editor."""
	def SetActiveMaterial(self, mp: 'BaseMaterial', mode: 'int' = 0) -> 'None':
		"""Sets a material to active within this document."""
	def SetActiveObject(self, op: 'BaseObject', mode: 'int' = 0) -> 'None':
		"""Modifies the current multi selection with op, depending on mode."""
	def SetActiveRenderData(self, rd: 'RenderData') -> 'None':
		"""Set the active render settings for the document."""
	def SetActiveTag(self, tag: 'BaseTag', mode: 'int' = 0) -> 'None':
		"""Set the active tags for the document."""
	def SetChanged(self) -> 'None':
		"""Set the change document flag."""
	def SetDefaultKey(self, key: 'CKey', overdub: 'bool') -> 'None':
		"""Sets the document's default keying settings."""
	def SetDocumentData(self, type: 'int', bc: 'BaseContainer') -> 'None':
		"""Set the document data."""
	def SetDocumentName(self, name: 'str') -> 'None':
		"""Set the filename of the document."""
	def SetDocumentPath(self, path: 'str') -> 'None':
		"""Get previous Basedocument off list"""
	def SetFps(self, fps: 'int') -> 'None':
		"""Set frames per second."""
	def SetLOD(self, lod: 'float') -> 'None':
		"""Set the LOD."""
	def SetLoopMaxTime(self, time: 'object') -> 'None':
		"""Sets the right boundary of the document's preview range."""
	def SetLoopMinTime(self, time: 'object') -> 'None':
		"""Sets the left boundary of the document's preview range."""
	def SetMaxTime(self, time: 'object') -> 'None':
		"""Set the end time for the timeline of this document."""
	def SetMinTime(self, time: 'object') -> 'None':
		"""Set the starting time for the timeline of this document."""
	def SetMode(self, m: 'int') -> 'None':
		"""Set the main mode of the editor."""
	def SetRenderLod(self, lod: 'bool') -> 'None':
		"""Sets the right boundary of the document's preview range."""
	def SetRewind(self, flags: 'int' = 0) -> 'None':
		"""C4D rewinds the whole document."""
	def SetSelection(self, bl: 'BaseList2D', mode: 'int' = 0) -> 'None':
		"""Set the current selection."""
	def SetTargetObject(self, op: 'BaseObject') -> 'None':
		"""Sets the target object within a multi-selection."""
	def SetTime(self, time: 'object') -> 'None':
		"""Set the current time for this documents timeline."""
	def SetTrackDefaultInterpolationMode(self, mode: 'int') -> 'None':
		"""Sets the track default interpolation mode."""
	def StartPickSession(self, callback: 'Callable[..., Any]', multi: 'bool') -> 'None':
		"""Starts a new pick session."""
	def StartUndo(self) -> 'bool':
		"""Tell Cinema 4D to start building a list of undos."""
	def StopPickSession(self, cancel: 'bool') -> 'None':
		"""Ends the current pick session."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class RenderData(BaseList2D):
	"""Container for render settings."""
	def GetFirstMultipass(self) -> 'BaseList2D':
		"""Returns the first multipass object."""
	def GetFirstVideoPost(self) -> 'BaseVideoPost':
		"""Returns the first videopost."""
	def InsertMultipass(self, obj: 'BaseList2D', pred: 'Optional[BaseList2D]' = True) -> 'None':
		"""Insert a multipass object"""
	def InsertVideoPost(self, pvp: 'BaseVideoPost', pred: 'BaseVideoPost') -> 'None':
		"""Insert a videopost data."""
	def InsertVideoPostLast(self, pvp: 'BaseVideoPost') -> 'None':
		"""Insert a last videopost data."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class LayerObject(BaseList2D):
	"""Layer class."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class BatchRender(object):
	"""The batch render class."""
	def AddFile(self, file: 'str', number: 'int') -> 'bool':
		"""Add a file to the batch render."""
	def DelFile(self, file: 'str') -> 'bool':
		"""Deletes a file from the batch render."""
	def EnableElement(self, n: 'int', bSet: 'bool') -> 'None':
		"""Enable the element."""
	def GetElement(self, n: 'int') -> 'str':
		"""Set the rendering state."""
	def GetElementCount(self) -> 'int':
		"""Return the element count."""
	def GetElementStatus(self, n: 'int') -> 'int':
		"""Get the element status."""
	def GetEnableElement(self, n: 'int') -> 'bool':
		"""Enable the element."""
	def GetFrameBitmap(self, nodeUuid: 'UUID', frameUuid: 'UUID') -> 'None':
		"""Get the bitmap of a frame."""
	def GetJsonJobs(self) -> 'List[RenderJob]':
		"""Get the jobs."""
	def IsRendering(self) -> 'bool':
		"""Get the render state."""
	def Open(self) -> 'bool':
		"""Open the batch render dialog."""
	def SetRendering(self, set: 'int') -> 'None':
		"""Set the rendering state."""
	def SetUseNet(self, n: 'int', on: 'bool') -> 'None':
		"""Enable/Disable TR."""

class BaseVideoPost(BaseList2D):
	"""VideoPost base class."""
	def RenderEngineCheck(self, type: 'int') -> 'bool':
		"""Checks if a videopost is available for a certain render engine."""
	def StereoGetCameraCountEditor(self, doc: 'BaseDocument', bd: 'BaseDraw') -> 'int':
		"""Retrieves the number of stereoscopic editor cameras."""
	def StereoGetCameraCountRenderer(self, doc: 'BaseDocument', rd: 'RenderData') -> 'int':
		"""Retrieves the number of stereoscopic cameras used for rendering."""
	def StereoGetCameraInfo(self, doc: 'BaseDocument', bd: 'BaseDraw', rd: 'RenderData', index: 'int') -> 'Optional[Dict[str, object]]':
		"""Retrieves the information for a stereoscopic camera."""
	def StereoMergeImages(self, dest: 'BaseBitmap', source: 'List[BaseBitmap]', settings: 'BaseContainer', transform: 'int') -> 'bool':
		"""Merges stereoscopic images."""
	def __init__(self, type: 'int') -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def GetActiveDocument() -> BaseDocument:
	'''Get the currently active document.'''
def GetFirstDocument() -> BaseDocument:
	'''Get the first document.'''
def LoadFile(name: str) -> None:
	'''Load a file as a document.'''
def InsertBaseDocument(doc: BaseDocument) -> None:
	'''Insert a document into the list of documents.'''
def SetActiveDocument(doc: BaseDocument) -> None:
	'''Set the document in the editor.'''
def KillDocument(doc: BaseDocument) -> None:
	'''Frees all ressources of a BaseDocument.'''
def LoadDocument(name: Union[str, MemoryFileStruct], loadflags: int, thread: Optional[BaseThread]) -> Optional[BaseDocument]:
	'''Load a file and return the document.'''
def MergeDocument(doc: BaseDocument, name: Union[str, MemoryFileStruct], loadflags: int, thread: Optional[BaseThread]) -> bool:
	'''Merge two documents.'''
def SaveDocument(doc: BaseDocument, name: Union[str, MemoryFileStruct], saveflags: int, format: int) -> bool:
	'''Save a document to a file.'''
def IsolateObjects(doc: BaseDocument, t_objects: List[BaseObject]) -> BaseDocument:
	'''Isolate all objects to a new document.'''
def RenderDocument(doc: BaseDocument, rdata: BaseContainer, bmp: BaseBitmap, renderflags: int, th: Optional[BaseThread], prog: Optional[Callable[[float, int], None]], wprog: Optional[Callable[[int, Optional[BaseBitmap], str, bool, int, int, int, str], None]]) -> int:
	'''Render a document to a bitmap.'''
def InteractiveModeling_Restart(doc: BaseDocument) -> bool:
	'''Applies the last modeling undo.'''
def RunAnimation(doc: BaseDocument, stop: bool, forward: bool) -> bool:
	'''Play document.'''
def SetDocumentTime(doc: BaseDocument, time: BaseTime) -> bool:
	'''Controls the time of the active document doc.'''
def CloseAllDocuments() -> None:
	'''Close all open documents.'''
def StopExternalRenderer() -> bool:
	'''Stop the external renderer.'''
def GetBatchRender() -> BatchRender:
	'''Returns the batch render class.'''
def GetAllAssets(doc: BaseDocument, allowDialogs: bool, lastPath: str, flags: int) -> Optional[List[Dict[str, object]]]:
	'''Get all assets of the document (deprecated).'''
def SaveProject(doc: BaseDocument, flags: int, targetPath: str, assets: object, missingAssets: object) -> bool:
	'''Saves a document with all assets.'''
def Assemble(inputpath: Any):
	'''Assemble B3D files to the given output format(s).'''
def GetFirstMarker(doc: BaseDocument) -> BaseList2D:
	'''Get the the first marker.'''
def AddMarker(doc: BaseDocument, pPred: Optional[BaseList2D], time: Optional[BaseTime], name: Optional[str]) -> Optional[BaseList2D]:
	'''Adds a new marker.'''
def GetRecentDocumentsList(isBodyPaint: bool) -> None:
	'''Get the recently loaded documents list.'''
def GetAllAssetsNew(doc: BaseDocument, allowDialogs: bool, lastPath: str, flags: int, assetList: List[Dict[str, object]]) -> int:
	'''Get all assets of the document.'''

