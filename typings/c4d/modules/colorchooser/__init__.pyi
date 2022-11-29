from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import SWATCH_CATEGORY_DOCUMENT
if TYPE_CHECKING:
	from c4d.documents import BaseDocument
	from c4d import Vector


class ColorSwatchGroup(object):
	"""Color Swatch Group class."""
	def AddColor(self, color: 'maxon.ColorA', selected: 'bool' = False, insertAt: 'int' = -1) -> 'int':
		"""Adds a color to this group."""
	def AddColors(self, colors: 'object', selected: 'bool' = False, merge: 'bool' = True, insertAt: 'int' = -1) -> 'int':
		"""Adds colors to this group."""
	def CopyFrom(self, group: 'ColorSwatchGroup') -> 'bool':
		"""Copies group."""
	def GetColor(self, index: 'int') -> 'None':
		"""Returns the color at the given index."""
	def GetColorCount(self) -> 'int':
		"""Returns the number of colors stored in this group."""
	def GetColors(self, selectedOnly: 'bool' = False) -> 'None':
		"""Gets the colors stored in this group."""
	def GetName(self) -> 'str':
		"""Returns the group name."""
	def HasDuplicatedColors(self) -> 'bool':
		"""Checks if the group has duplicated colors."""
	def InvertSelection(self) -> 'None':
		"""Inverts the selected colors, so the currently selected colors will be uselected and vice-versa."""
	def IsColorSelected(self, index: 'int') -> 'bool':
		"""Checks if the color at the given index is selected."""
	def IsGroupSelected(self) -> 'bool':
		"""Checks if the group is selected."""
	def Merge(self, group: 'ColorSwatchGroup') -> 'bool':
		"""Merges groups."""
	def RemoveColor(self, index: 'int', removeCount: 'int' = 1) -> 'bool':
		"""Removes the color at the given index."""
	def RemoveDuplicatedColors(self) -> 'None':
		"""Removes duplicated colors in this group."""
	def RemoveSelectedColors(self) -> 'None':
		"""Removes all selected colors in this group."""
	def Reset(self) -> 'None':
		"""Removes all colors in this group."""
	def SelectColor(self, index: 'int', selected: 'bool') -> 'bool':
		"""Selects/unselects the color at the given index."""
	def SelectGroup(self, select: 'bool') -> 'None':
		"""Selects the group. This will select/unselect the group icon and all colors in the group."""
	def SetColor(self, index: 'int', color: 'maxon.ColorA', selected: 'int') -> 'bool':
		"""Edits the color at the given index."""
	def SetName(self, name: 'str') -> 'None':
		"""Sets the group name."""
	def SortColors(self) -> 'None':
		"""Sorts colors in this group based in its HSV values."""
	def __init__(self, name: 'str' = '', selected: 'bool' = False, colors: 'object' = None) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class ColorSwatchData(object):
	"""Color Swatch Data class."""
	def AddGroup(self, category: 'Optional[int]' = 1, name: 'Optional[str]' = '', selected: 'Optional[bool]' = False, insertAt: 'Optional[int]' = -1, colors: 'Optional[object]' = None) -> 'Optional[ColorSwatchGroup]':
		"""Adds a new document-based group."""
	def CopyFrom(self, data: 'ColorSwatchData') -> 'bool':
		"""Copies color swatch data."""
	def GetGroupAtIndex(self, index: 'int', category: 'Optional[int]' = 1) -> 'Optional[ColorSwatchGroup]':
		"""Gets the group at given index."""
	def GetGroupCount(self, category: 'Optional[int]' = 1) -> 'int':
		"""Returns the number of document-based groups stored. Global group is ignored."""
	def InsertGroup(self, group: 'ColorSwatchGroup', insertAt: 'Optional[int]' = -1, category: 'Optional[int]' = 1) -> 'bool':
		"""Adds a new document-based group."""
	def Load(self, doc: 'BaseDocument', merge: 'Optional[bool]' = False, globalColors: 'Optional[bool]' = False) -> 'bool':
		"""Loads the document-based groups from the given BaseDocument."""
	def Merge(self, data: 'ColorSwatchData') -> 'bool':
		"""Merges swatch data."""
	def RemoveGroup(self, index: 'int', category: 'Optional[int]' = 1) -> 'bool':
		"""Removes the document-based group at the given index."""
	def RemoveSelectedItems(self) -> 'None':
		"""Removes selected groups and colors, including selected global colors."""
	def Reset(self) -> 'None':
		"""Removes all groups and colors, including globals."""
	def Save(self, doc: 'BaseDocument', globalColors: 'Optional[bool]' = False) -> 'bool':
		"""Saves the document-based color groups to the given BaseDocument."""
	def SetGroupAtIndex(self, index: 'int', group: 'ColorSwatchGroup', category: 'Optional[int]' = 1) -> 'bool':
		"""Sets the group at given index."""
	def __init__(self, doc: 'Optional[BaseDocument]' = True, global_: 'Optional[bool]' = False) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def ColorRGBToString(color: Vector) -> str:
	'''Converts a RGB color to string.'''
def ColorHSVToString(color: Vector) -> str:
	'''Converts a HSV color to string.'''
def ColorComponentFloatTo8Bit(colorComponentInput: float) -> int:
	'''Converts a RGB float color component in range [0.0, 1.0] to 8-bit (range [0, 255]).'''
def ColorComponent8BitToFloat(colorComponentInput: int) -> float:
	'''Converts a RGB 8-bit color component (range [0, 255]) to float in range [0.0, 1.0].'''
def ColorFloatTo8Bit(floatColor: Vector) -> List[int, int, int]:
	'''Converts a RGB float color in range [0.0, 1.0] to 8bit color (range [0, 255]).'''
def Color8BitToFloat(red: int, green: int, blue: int) -> None:
	'''Converts a RGB 8-bit color (range [0, 255]) to float color in range [0.0, 1.0].'''
def ColorComponentFloatTo16Bit(colorComponentInput: float) -> int:
	'''Converts a RGB float color component in range [0.0, 1.0] to 16bit (range [0, 65535]).'''
def ColorComponent16BitToFloat(colorComponentInput: int) -> float:
	'''Converts a RGB 16bit color component (range [0, 65535]) to float in range [0.0, 1.0].'''
def ColorFloatTo16Bit(floatColor: Vector) -> List[int, int, int]:
	'''Converts a RGB float color in range [0.0, 1.0] to 16bit color (range [0, 65535]).'''
def Color16BitToFloat(red: int, green: int, blue: int) -> None:
	'''Converts a RGB 16bit color (range [0, 65535]) to float color in range [0.0, 1.0].'''
def ColorKelvinTemperatureToRGB(kelvinDegree: float, tint: float) -> None:
	'''Converts color Kelvin temperature to RGB value.'''
def ColorHarmonyGetComplementary(color: Vector, ryb: bool) -> List[Vector]:
	'''Generates a Complementary Color Harmony palette.'''
def ColorHarmonyGetSplitComplementary(color: Vector, ryb: bool) -> List[Vector]:
	'''Generates a Split Complementary Color Harmony palette.'''
def ColorHarmonyGetTetradic(color: Vector, ryb: bool) -> List[Vector]:
	'''Generates a Tetradric Color Harmony palette.'''
def ColorHarmonyGetAnalogous(color: Vector, colorCount: int, ryb: bool) -> List[Vector]:
	'''Generates an Analogous Color Harmony palette.'''
def ColorHarmonyGetEquiangular(color: Vector, colorCount: int, ryb: bool) -> List[Vector]:
	'''Generates an Equiangular Color Harmony palette.'''
def ColorHarmonyRotateColor(color: Vector, colorCount: int, angle: int, ryb: bool) -> List[Vector]:
	'''Generates an Equiangular Color Harmony palette.'''
def ColorHarmonyInterpolateColors(color1: Vector, color2: Vector, colorCount: int, ryb: bool) -> List[Vector]:
	'''Generates an interpolated palette between 2 colors.'''

import maxon
