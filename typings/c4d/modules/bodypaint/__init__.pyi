from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseList2D, COLORMODE_ARGB
if TYPE_CHECKING:
	from c4d import Vector, CPolygon, BaseSelect, BaseContainer, BaseObject
	from c4d.bitmaps import ColorProfile, BaseBitmap
	from c4d.documents import BaseDocument


class PaintBitmap(BaseList2D):
	"""The base class of all paint classes"""
	def AddAlphaChannel(self, bitdepth: 'int', prev: 'Optional[PaintLayer]' = True, undo: 'Optional[bool]' = True, activate: 'Optional[bool]' = True) -> 'Optional[PaintLayerBmp]':
		"""Add an alpha channel to the layer."""
	def AskApplyAlphaMask(self) -> 'bool':
		"""Check if an alpha mask can be applied."""
	def GetAlphaFirst(self) -> 'Optional[PaintLayer]':
		"""Get the first alpha channel layer."""
	def GetAlphaLast(self) -> 'Optional[PaintLayer]':
		"""Get the last alpha channel layer."""
	def GetBh(self) -> 'int':
		"""Get the height of the paint bitmap."""
	def GetBw(self) -> 'int':
		"""Get the width of the paint bitmap."""
	def GetColorMode(self) -> 'int':
		"""Get the color mode of the paint bitmap."""
	def GetDirty(self, flags: 'int') -> 'int':
		"""Get dirty count."""
	def GetLayerDownFirst(self) -> 'Optional[PaintLayer]':
		"""Get the first child layer."""
	def GetLayerDownLast(self) -> 'Optional[PaintLayer]':
		"""Get the last child layer."""
	def GetPaintTexture(self) -> 'Optional[PaintTexture]':
		"""Get the paint texture if possible."""
	def GetParent(self) -> 'Optional[PaintBitmap]':
		"""Get the parent."""
	def UpdateRefresh(self, xmin: 'int', ymin: 'int', xmax: 'int', ymax: 'int', flags: 'int') -> 'None':
		"""Refresh an area of the paint bitmap."""
	def UpdateRefreshAll(self, flags: 'int', reallyall: 'bool') -> 'None':
		"""Refresh the complete paint bitmap."""

class PaintMaterial(PaintBitmap):
	"""A class for paint materials"""
	def EnableMaterial(self, doc: 'BaseDocument', on: 'bool', suppressevent: 'bool' = False, domaterialundo: 'bool' = True) -> 'None':
		"""Enable material for painting."""

class PaintTexture(PaintBitmap):
	"""A class for paint textures."""
	def AddLayerBmp(self, insertafter: 'Optional[PaintLayer]' = None, layerset: 'Optional[PaintLayer]' = None, mode: 'Optional[int]' = 5, useundo: 'Optional[bool]' = True, activate: 'Optional[bool]' = True) -> 'PaintLayerBmp':
		"""Add a bitmap layer."""
	def AddLayerFolder(self, insertafter: 'Optional[PaintLayer]' = None, insertunder: 'Optional[PaintLayer]' = None, useundo: 'Optional[bool]' = True, activate: 'Optional[bool]' = True) -> 'PaintLayerBmp':
		"""Add a layer folder."""
	@staticmethod
	def CreateNewTexture(path: 'str', settings: 'BaseContainer') -> 'Optional[PaintTexture]':
		"""Create a new paint texture."""
	def GetActive(self) -> 'Optional[PaintLayer]':
		"""Get the selected layer."""
	def GetAlphaCount(self) -> 'int':
		"""Get the number of alpha channels."""
	def GetColorProfile(self) -> 'ColorProfile':
		"""Get the color profile."""
	def GetFilename(self) -> 'str':
		"""Get the filename."""
	def GetFirstLayer(self) -> 'Optional[PaintLayer]':
		"""Get the first layer."""
	def GetLastLayer(self) -> 'Optional[PaintLayer]':
		"""Get the last layer."""
	def GetLayerCount(self) -> 'int':
		"""Get the number flayers."""
	def GetLinkLayers(self, addfolders: 'bool') -> 'List[PaintLayer]':
		"""Get linked layers."""
	@staticmethod
	def GetSelectedTexture() -> 'Optional[PaintTexture]':
		"""Get the selected paint texture."""
	@staticmethod
	def GetTextureDefaults(channel: 'object') -> 'BaseContainer':
		"""Get the default settings for textures."""
	def SetActiveLayer(self, layer: 'PaintLayer', activatetexture: 'bool', show: 'bool' = True) -> 'None':
		"""Select a layer."""
	def SetColorMode(self, newcolormode: 'int', doundo: 'bool') -> 'None':
		"""Change the color mode."""
	def SetColorProfile(self, profile: 'ColorProfile') -> 'bool':
		"""Set the color profile."""
	@staticmethod
	def SetSelected_Texture(bmp: 'PaintBitmap', preferred: 'Optional[PaintMaterial]' = None) -> 'bool':
		"""Select a paint texture."""

class PaintLayer(PaintBitmap):
	"""A paint layer class."""
	def GetShowBit(self, hierarchy: 'bool', bit: 'int') -> 'bool':
		"""Get the visibilty of the layer."""
	def SetShowBit(self, onoff: 'bool', bit: 'int') -> 'bool':
		"""Set the visibility of the layer."""
	def ToPaintLayerBmp(self) -> 'PaintLayerBmp':
		"""Cast to a PaintLayerBmp."""

class PaintLayerBmp(PaintLayer):
	"""A class for layers with pixels."""
	def GetBoundingBox(self) -> 'Dict[str, object]':
		"""Get the bounding box."""
	def GetPixelCnt(self, x: 'int', y: 'int', cnt: 'int', buffer: 'Union[bytearray, memoryview]', dstmode: 'int', flags: 'int') -> 'bool':
		"""Read a pixel buffer object from the image."""
	def ImportFromBaseBitmap(self, bmp: 'object', usealpha: 'bool') -> 'bool':
		"""Import a bitmap."""
	def ImportFromBaseBitmapAlpha(self, bmp: 'object', channel: 'BaseBitmap') -> 'bool':
		"""Import a bitmap with an alpha channel."""
	def SetPixelCnt(self, x: 'int', y: 'int', cnt: 'int', buffer: 'Union[bytearray, memoryview]', inc: 'int', srcmode: 'int', flags: 'int') -> 'bool':
		"""Write a pixel buffer object to the image."""

class PaintLayerFolder(PaintLayer):
	"""A class for paint layer folders."""

class PaintLayerMask(PaintLayer):
	"""A class for paint layer masks."""

class TempUVHandle(object):
	"""Temp UV handle for BodyPaint"""
	def GetBaseObject(self) -> 'None':
		"""Retrieves the object of the UV set."""
	def GetMode(self) -> 'int':
		"""Retrieves the current UV editor mode."""
	def GetPointCount(self) -> 'int':
		"""Retrieves the point count."""
	def GetPoints(self) -> 'List[Vector]':
		"""Retrieves the read-only points array."""
	def GetPolyCount(self) -> 'int':
		"""Retrieves the polygon count."""
	def GetPolyHid(self) -> 'None':
		"""Retrieves the hidden polygons."""
	def GetPolySel(self) -> 'None':
		"""Retrieves the selected polygons."""
	def GetPolys(self) -> 'List[CPolygon]':
		"""Retrieves the read-only polygons array."""
	def GetUVEdgeSel(self) -> 'None':
		"""Retrieves the selected UV edges."""
	def GetUVPointSel(self) -> 'None':
		"""Retrieves the selected UV points."""
	def GetUVW(self) -> 'List[Dict[str, object]]':
		"""Retrieves the UV list."""
	def IsEditable(self) -> 'None':
		"""Checks if UVs are editable."""
	def SetUVEdgeSelection(self, uvEdgeSelection: 'BaseSelect') -> 'bool':
		"""Sets the UV Edge selection."""
	def SetUVPointSelectionFromTextureView(self, uvPointSelection: 'BaseSelect', bleedSelection: 'bool') -> 'bool':
		"""Selects the UV points of the object."""
	def SetUVW(self, uvw: 'List[Dict[str, object]]') -> 'bool':
		"""Applies changes of the UV set to the object."""
	def SetUVWFromTextureView(self, uvw: 'List[Dict[str, object]]', ignoreHidden: 'bool', ignoreUnselected: 'bool', autoSelectAll: 'bool', registerUndo: 'Optional[bool]' = True) -> 'bool':
		"""Applies changes of the UV set to the object."""


def IdentifyImage(texpath: str) -> int:
	'''Identifies the image's file format.'''
def PainterActivateChannel(channel: int, multi: bool, enable: bool) -> None:
	'''Activation/deactivation of paint channels.'''
def BPSetupWizardWithParameters(doc: BaseDocument, settings: object, objects: object, material: object) -> bool:
	'''Run the BodyPaint 3D paint wizard.'''
def SendPainterCommand(command: int, doc: Optional[BaseDocument], tex: Optional[PaintTexture], bc: Optional[BaseContainer]) -> bool:
	'''Sends commands to BodyPaint 3D.'''
def GetActiveUVSet(doc: BaseDocument, flags: int) -> Optional[TempUVHandle]:
	'''Retrieves the active UV set.'''
def FreeActiveUVSet(handle: TempUVHandle) -> None:
	'''Frees the active UV set.'''
def CallUVCommand(points: List[Vector], pointCount: int, polys: List[CPolygon], polyCount: int, uvw: Dict[str, object], polySelection: BaseSelect, pointSelection: BaseSelect, op: BaseObject, mode: int, cmdid: int, settings: Optional[BaseContainer]) -> bool:
	'''Calls UV commands.'''
def UpdateMeshUV(fullUpdate: bool) -> None:
	'''Updates the UV mesh from the UV tag data.'''
def GetUVSeams(object: BaseObject) -> None:
	'''Gets the UV seams for the specified object, when UV Seams are enabled in the UV viewport.'''
def GetUVSeams2(object: BaseObject, checkUVSettings: bool) -> None:
	'''Gets the UV seams for the specified object.'''

