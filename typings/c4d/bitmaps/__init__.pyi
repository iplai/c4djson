"""Module for color chooser"""

from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import INITBITMAPFLAGS_NONE, SAVEBIT_NONE, MPB_GETLAYERS_IMAGE, MPB_GETLAYERS_ALPHA
if TYPE_CHECKING:
	from c4d.storage import MemoryFileStruct
	from c4d import BaseContainer, Vector
	from c4d.modules.bodypaint import PaintBitmap


class BaseBitmap(object):
	"""Class to handle bitmaps."""
	def AddChannel(self, internal: 'bool', straight: 'bool') -> 'int':
		"""Add an layer."""
	def CopyPartTo(self, dst: 'BaseBitmap', x: 'int', y: 'int', w: 'int', h: 'int') -> 'bool':
		"""Copy part to."""
	def CopyTo(self, dst: 'BaseBitmap') -> 'bool':
		"""Copies the image."""
	def FlushAll(self) -> 'None':
		"""Resets the bitmap to its initial state."""
	def GetAlphaPixel(self, channel: 'object', x: 'int', y: 'int') -> 'int':
		"""Get an alpha pixel"""
	def GetBh(self) -> 'int':
		"""Returns the pixel width of the bitmap."""
	def GetBpz(self) -> 'int':
		"""Returns the count of bits per line."""
	def GetBt(self) -> 'int':
		"""Returns the number of bits per pixel."""
	def GetBw(self) -> 'int':
		"""Returns the width of the bitmap in pixels."""
	def GetChannelCount(self) -> 'int':
		"""Returns the number of alpha channels."""
	def GetChannelNum(self, num: 'int') -> 'BaseBitmap':
		"""Returns an alpha layer."""
	def GetClone(self) -> 'BaseBitmap':
		"""Returns a clone part of this image."""
	def GetClonePart(self, x: 'int', y: 'int', w: 'int', h: 'int') -> 'Optional[BaseBitmap]':
		"""Returns a clone of this image."""
	def GetColorMode(self) -> 'int':
		"""Returns the color mode of the bitmap."""
	def GetColorProfile(self) -> 'ColorProfile':
		"""Get the color profile."""
	def GetData(self, id: 'int', default: 'object') -> 'Any':
		"""Gets bitmap data."""
	def GetDirty(self) -> 'int':
		"""Get the dirty flag."""
	def GetInternalChannel(self) -> 'Optional[BaseBitmap]':
		"""Get the internal read-only alpha channel."""
	def GetMemoryInfo(self) -> 'int':
		"""Get the size of the memory used by the bitmap."""
	def GetPixel(self, x: 'int', y: 'int') -> 'List[int]':
		"""Get the pixel."""
	def GetPixelCnt(self, x: 'int', y: 'int', cnt: 'int', buffer: 'Union[bytearray, memoryview]', inc: 'int', dstmode: 'int', flags: 'int', conversion: 'Optional[ColorProfileConvert]' = None) -> 'bool':
		"""Read a pixel buffer object from the image."""
	def GetPixelDirect(self, x: 'int', y: 'int') -> 'Vector':
		"""Get the pixel without loose of precision."""
	def GetSize(self) -> 'List[int]':
		"""Returns the size of the bitmap."""
	def GetUpdateRegionBitmap(self) -> 'BaseBitmap':
		"""Get the updated region of a bitmap."""
	def Init(self, x: 'int', y: 'int', depth: 'int' = 24, flags: 'int' = 0) -> 'int':
		"""Inits a BaseBitmap."""
	def InitWith(self, name: 'Union[str, MemoryFileStruct]', frame: 'Optional[int]' = -1) -> 'Tuple[int, bool]':
		"""Inits a BaseBitmap by Filename."""
	def IsMultipassBitmap(self) -> 'bool':
		"""Checks if bitmap is MultipassBitmap."""
	def RemoveChannel(self, channel: 'BaseBitmap') -> 'None':
		"""Remove an alpha layer."""
	def Save(self, name: 'Union[str, MemoryFileStruct]', format: 'int', data: 'Optional[BaseContainer]' = None, savebits: 'Optional[int]' = 0) -> 'int':
		"""Saves the bitmap to a file."""
	def Scale(self, dst: 'BaseBitmap', intens: 'int', sample: 'bool', nprop: 'bool') -> 'None':
		"""Scales the bitmap."""
	def ScaleBicubic(self, dst: 'BaseBitmap', src_xmin: 'int', src_ymin: 'int', src_xmax: 'int', src_ymax: 'int', dst_xmin: 'int', dst_ymin: 'int', dst_xmax: 'int', dst_ymax: 'int') -> 'None':
		"""Scales the bitmap."""
	def ScaleIt(self, dst: 'BaseBitmap', intens: 'int', sample: 'bool', nprop: 'bool') -> 'None':
		"""Scales the bitmap."""
	def SetAlphaPixel(self, channel: 'object', x: 'int', y: 'int', val: 'int') -> 'None':
		"""Sets an alpha pixel"""
	def SetCMAP(self, i: 'int', r: 'int', g: 'int', b: 'int') -> 'None':
		"""Set the palette entries.."""
	def SetColorProfile(self, profile: 'ColorProfile') -> 'bool':
		"""Set the color profile."""
	def SetData(self, id: 'int', data: 'object') -> 'bool':
		"""Sets bitmap data."""
	def SetDirty(self) -> 'None':
		"""Set the dirty flag."""
	def SetPixel(self, x: 'int', y: 'int', r: 'int', g: 'int', b: 'int') -> 'bool':
		"""Set the pixel."""
	def SetPixelCnt(self, x: 'int', y: 'int', cnt: 'int', buffer: 'Union[bytearray, memoryview]', inc: 'int', srcmode: 'int', flags: 'int') -> 'bool':
		"""Write a pixel buffer object to the image."""
	def Within(self, x: 'int', y: 'int') -> 'bool':
		"""Checks if x and or y is in the range of the bitmap."""
	def __eq__(self, other: 'object') -> 'None':
		"""Return self==value."""
	def __getitem__(self, key: 'int') -> 'Tuple[int, int, int]':
		"""Return self[key]."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""
	def __ne__(self, other: 'object') -> 'None':
		"""Return self!=value."""
	def __setitem__(self, key: 'int', value: 'Tuple[int, int, int]') -> 'None':
		"""Set self[key] to value."""

class MultipassBitmap(BaseBitmap):
	"""Extension class for BaseBitmap."""
	def AddAlpha(self, insertafter: 'MultipassBitmap', colormode: 'int') -> 'Optional[MultipassBitmap]':
		"""Adds a alpha."""
	def AddFolder(self, insertafter: 'MultipassBitmap', hidden: 'bool' = False) -> 'Optional[MultipassBitmap]':
		"""Adds a folder."""
	def AddLayer(self, insertafter: 'MultipassBitmap', colormode: 'int', hidden: 'bool' = False) -> 'None':
		"""Adds a layer."""
	@staticmethod
	def AllocWrapper(bmp: 'BaseBitmap') -> 'Optional[MultipassBitmap]':
		"""Initialize the MultipassBitmap with a BaseBitmap"""
	def ClearImageData(self) -> 'None':
		"""Clears the image data for all layers."""
	def DeleteLayer(self, layer: 'MultipassBitmap') -> 'bool':
		"""Delete a layer."""
	def FindUserID(self, id: 'int', subid: 'int' = 0) -> 'Optional[MultipassBitmap]':
		"""Finds a layer."""
	def FreeHiddenLayers(self) -> 'None':
		"""Free hidden layers."""
	def GetAlphaLayerCount(self) -> 'int':
		"""Retrieves the number of alpha layers in the bitmap. """
	def GetAlphaLayerNum(self, num: 'int') -> 'Optional[MultipassBitmap]':
		"""Gets the alpha layer with number num."""
	def GetHiddenLayerCount(self) -> 'int':
		"""Retrieves the number of hidden layers in the bitmap. """
	def GetHiddenLayerNum(self, num: 'int') -> 'Optional[MultipassBitmap]':
		"""Gets the hidden layer with number num."""
	def GetHiddneLayerNum(self, num: 'int') -> 'Optional[MultipassBitmap]':
		"""Gets the hidden layer with number num."""
	def GetLayerCount(self, num: 'int') -> 'int':
		"""Retrieves the number of layers in the bitmap. """
	def GetLayerNum(self, num: 'int') -> 'Optional[MultipassBitmap]':
		"""Gets the layer with number num."""
	def GetLayers(self, flags: 'int' = 6) -> 'List[BaseBitmap]':
		"""Gets the layers."""
	def GetPaintBitmap(self) -> 'PaintBitmap':
		"""Gets a paint bitmap."""
	def GetParameter(self, id: 'int') -> 'Optional[Any]':
		"""Returns parameter"""
	def SetParameter(self, id: 'int', t_data: 'object') -> 'Any':
		"""Set parameter"""
	def __init__(self, bx: 'int', by: 'int', mode: 'int') -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class GeClipMap(object):
	"""Used to manipulate bitmaps."""
	def Arc(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int', seg: 'object') -> 'None':
		"""Draw an arc."""
	def BeginDraw(self) -> 'None':
		"""Begin to draw."""
	def Blit(self, dx: 'int', dy: 'int', s_dp: 'GeClipMap', sx1: 'int', sy1: 'int', sx2: 'int', sy2: 'int', rop: 'int') -> 'None':
		"""Blits from s_dp to this clip map."""
	def ClipArea(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'int':
		"""Checks if a rectangle is inside the clip region."""
	def ClipPoint(self, x: 'int', y: 'int') -> 'bool':
		"""Checks if a point is inside the clip region."""
	def Destroy(self) -> 'None':
		"""Resets the clip map to its initial state."""
	def Ellipse(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draw an ellipse."""
	def EndDraw(self) -> 'None':
		"""End draw."""
	@staticmethod
	def EnumerateFonts(sort_mode: 'str') -> 'BaseContainer':
		"""Enumerates all fonts."""
	def FillArc(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int', seg: 'object') -> 'None':
		"""Draw an filled arc."""
	def FillEllipse(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draw an filled ellipse."""
	def FillPolygon(self, p: 'Tuple[int, int]') -> 'None':
		"""Draw an filled polygon."""
	def FillRect(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draw a filled rect."""
	def GetBh(self) -> 'int':
		"""Retrieves the pixel height."""
	def GetBitmap(self) -> 'BaseBitmap':
		"""Returns the bitmap."""
	def GetBw(self) -> 'int':
		"""Retrieves the pixel width."""
	@staticmethod
	def GetDefaultFont(type: 'int') -> 'BaseContainer':
		"""Gets the default font."""
	def GetDim(self) -> 'Tuple[int, int]':
		"""Retrieves the pixel dimensions."""
	def GetFont(self, font_description: 'BaseContainer') -> 'float':
		"""Gets the font."""
	@staticmethod
	def GetFontDescription(name: 'str', type: 'int') -> 'BaseContainer':
		"""Gets a font description."""
	@staticmethod
	def GetFontName(font_description: 'BaseContainer', type: 'int') -> 'str':
		"""Gets a font name."""
	@staticmethod
	def GetFontSize(font_description: 'BaseContainer', type: 'int') -> 'float':
		"""Gets a font size."""
	def GetPixelRGBA(self, x: 'int', y: 'int') -> 'List[int]':
		"""Return pixel at a given position."""
	def Init(self, w: 'int', h: 'int', bits: 'int' = 32) -> 'bool':
		"""Init with the given dimensions."""
	def InitWith(self, name: 'Union[str, MemoryFileStruct]', frame: 'int') -> 'Tuple[int, bool]':
		"""Init with a filename."""
	def InitWithBitmap(self, bm: 'BaseBitmap', alpha_channel: 'Optional[BaseBitmap]' = None) -> 'bool':
		"""Init with a bitmap and alpha."""
	def Line(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draws a line."""
	def PolyLine(self, p: 'Tuple[int, int]') -> 'None':
		"""Draws the polygon line."""
	def Rect(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draw a rect."""
	def SetColor(self, r: 'int', g: 'int', b: 'int', alpha: 'int' = 255) -> 'None':
		"""Sets the draw color."""
	def SetDrawMode(self, mode: 'int', par: 'int') -> 'None':
		"""Sets the draw mode."""
	def SetFont(self, font_description: 'Optional[BaseContainer]' = None, font_size: 'Optional[float]' = None) -> 'bool':
		"""Sets the font."""
	@staticmethod
	def SetFontSize(font_description: 'BaseContainer', type: 'int', size: 'float') -> 'bool':
		"""Sets a font size."""
	def SetOffset(self, off_x: 'int', off_y: 'int') -> 'None':
		"""Offsets all the following draw command."""
	def SetPixel(self, x: 'int', y: 'int') -> 'None':
		"""Sets the pixel."""
	def SetPixelRGBA(self, x: 'int', y: 'int', r: 'int', g: 'int', b: 'int', a: 'int' = 255) -> 'None':
		"""Set Pixel RGBA."""
	def TextAscent(self) -> 'None':
		"""Calculates the ascent in the current font."""
	def TextAt(self, x: 'int', y: 'int', txt: 'str') -> 'None':
		"""Prints the string."""
	def TextHeight(self) -> 'None':
		"""Return the height of the current font."""
	def TextWidth(self, txt: 'str') -> 'int':
		"""Returns the width of a passed text."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class MovieSaver(object):
	"""The movie saver class."""
	def Choose(self, format: 'int', bc: 'BaseContainer') -> 'None':
		"""Opens the standard compression chooser for movie formats."""
	def Close(self) -> 'None':
		"""Closes the movie stream."""
	def Open(self, name: 'Union[str, MemoryFileStruct]', bm: 'BaseBitmap', fps: 'int', format: 'int', data: 'BaseContainer', savebits: 'int') -> 'None':
		"""Opens a movie stream."""
	def Write(self, bm: 'BaseBitmap') -> 'int':
		"""Adds another frame to the end of the movie stream."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class MovieLoader(object):
	"""The movie saver class."""
	def Close(self) -> 'None':
		"""Closes the movie stream."""
	def GetInfo(self) -> 'Tuple[int, float]':
		"""Open a movie file."""
	def Open(self, fn: 'Union[str, MemoryFileStruct]') -> 'None':
		"""Adds another frame to the end of the movie stream."""
	def Read(self, new_frame_idx: 'int') -> 'Optional[Tuple[int, BaseBitmap]]':
		"""Opens the standard compression chooser for movie formats."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class ColorProfile(object):
	"""The color profile class"""
	def CheckColorMode(self, colormode: 'int') -> 'bool':
		"""Check the color mode."""
	@staticmethod
	def GetDefaultLinearGray() -> 'ColorProfile':
		"""Return the default linear gray profile."""
	@staticmethod
	def GetDefaultLinearRGB() -> 'ColorProfile':
		"""Return the default linear color profile."""
	@staticmethod
	def GetDefaultSGray() -> 'ColorProfile':
		"""Return the default linear standard gray profile."""
	@staticmethod
	def GetDefaultSRGB() -> 'ColorProfile':
		"""Return the default SRGB color profile."""
	def GetInfo(self) -> 'str':
		"""Returns the info."""
	def HasProfile(self) -> 'bool':
		"""Check if the instance has a profile."""
	def IsMonitorProfileMode(self) -> 'bool':
		"""Check if the color profile is in profile mode."""
	def OpenProfileFromFile(self, fn: 'Union[str, MemoryFileStruct]') -> 'None':
		"""Open a color profile file."""
	def SetMonitorProfileMode(self, on: 'bool') -> 'bool':
		"""Set the monitor profile mode."""
	def WriteProfileToFile(self, fn: 'Union[str, MemoryFileStruct]') -> 'bool':
		"""Write the profile to file."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class ColorProfileConvert(object):
	"""ColorProfileConvert class"""
	def Convert(self, src: 'bytes', dst: 'bytes', cnt: 'int', skipInputComponents: 'bool', skipOutputComponents: 'bool') -> 'None':
		"""Convert the color profiles."""
	def PrepareTransform(self, srccolormode: 'int', srcprofile: 'ColorProfile', dstcolormode: 'ColorProfile', dstprofile: 'ColorProfile', bgr: 'bool') -> 'bool':
		"""Prepare the color conversion."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def ShowBitmap(bmp: BaseBitmap) -> None:
	'''Display a bitmap image.'''
def InitResourceBitmap(resource_id: int) -> Optional[BaseBitmap]:
	'''Loads the global icon.'''
def GetImageSettingsDictionary(data: BaseContainer, filterId: int) -> maxon.DataDictionary:
	'''Returns the DataDictionary stored in the BaseContainer for the given image format.'''
def SetImageSettingsDictionary(settings: maxon.DataDictionary, data: BaseContainer, filterId: int) -> None:
	'''Stores a DataDictionary in the BaseContainer for the given image format.'''

import maxon
