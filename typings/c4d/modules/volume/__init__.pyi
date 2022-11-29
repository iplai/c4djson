from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseObject
if TYPE_CHECKING:
	from c4d import BaseContainer
	from c4d.documents import BaseDocument


class VolumeObject(BaseObject):
	"""Volume Object class."""
	def GetGridClass(self) -> 'int':
		"""Retrieves the volumes grid class."""
	def GetGridType(self) -> 'int':
		"""Retrieves the volumes grid type."""
	def GetVolume(self) -> 'None':
		"""Retrieves the volume interface."""
	def SetVolume(self, volume: 'object') -> 'None':
		"""Set the volume interface."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class VolumeBuilder(BaseObject):
	"""Volume Builder object class."""
	def AddSceneObject(self, object: 'BaseObject', index: 'int' = 0) -> 'bool':
		"""Adds a valid object from the scene to the Objects list."""
	def ClearInputObjects(self) -> 'None':
		"""Clears the Objects list."""
	def GetBoolMode(self, index: 'int') -> 'int':
		"""Gets the bool mode for the index."""
	def GetEnable(self, index: 'int') -> 'bool':
		"""Gets the enabled state for the index."""
	def GetInputObject(self, index: 'int') -> 'Optional[BaseObject]':
		"""Retrieves the object referenced at the given index."""
	def GetInputObjectByType(self, type: 'int', startIndex: 'int') -> 'Optional[Tuple[BaseObject, int]]':
		"""Retrieves the object referenced in the Sources list with the given type."""
	def GetInputObjectCount(self, countDouble: 'bool' = True) -> 'int':
		"""Retrieves the number of elements in the Objects list."""
	def GetListEntryCount(self) -> 'int':
		"""Returns the number of elements in the "Objects" list containing folders."""
	def GetMixMode(self, index: 'int') -> 'int':
		"""Gets the mix mode for the index."""
	def GetMixVectorMode(self, index: 'int') -> 'int':
		"""Gets the mix vector mode for the index."""
	def GetSelected(self, index: 'int') -> 'bool':
		"""Gets the selection state for the index."""
	def GetSettingsContainerForIndex(self, index: 'int') -> 'Optional[BaseContainer]':
		"""Returns the internal container for the settings of an object input."""
	def GetSettingsContainerForObject(self, object: 'BaseObject') -> 'Optional[BaseContainer]':
		"""Returns the internal container for the settings of an object input."""
	def InputObjectIsChild(self, index: 'int') -> 'bool':
		"""Returns if an object index in the Object list is a child of the generator."""
	def RemoveObject(self, index: 'int') -> 'bool':
		"""Removes the object in the list at the given index."""
	def SetBoolMode(self, index: 'int', boolmode: 'int') -> 'None':
		"""Sets the bool mode for the index."""
	def SetEnable(self, index: 'int', enable: 'bool') -> 'None':
		"""Sets the enabled state for the index."""
	def SetMixMode(self, index: 'int', mixmode: 'int') -> 'None':
		"""Sets the mix mode for the index."""
	def SetMixVectorMode(self, index: 'int', mixmode: 'int') -> 'None':
		"""Sets the mix vector mode for the index."""
	def SetSelected(self, index: 'int', select: 'bool') -> 'None':
		"""Sets the selection state for the index."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def SendVolumeCommand(command: int, list: List[BaseObject], bc: BaseContainer, doc: BaseDocument) -> Union[bool, List[BaseObject]]:
	'''Sends a volume command to Cinema 4D to change an volume object.'''

