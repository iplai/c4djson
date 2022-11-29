"""Module for IO operations"""

from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import FILESELECTTYPE_ANYTHING, FILESELECT_LOAD, SAVEBIT_ALPHA
if TYPE_CHECKING:
	from c4d import Vector, Matrix, BaseTime, BaseContainer, GeListNode
	from c4d.bitmaps import BaseBitmap
	from c4d.documents import BaseDocument
	from c4d.plugins import BasePlugin


class HyperFile(object):
	"""Hyper files are used to store data."""
	def Close(self) -> 'bool':
		"""Close a hyper file."""
	def GetDocument(self) -> 'Optional[BaseDocument]':
		"""Returns the document of the HyperFile."""
	def GetError(self) -> 'int':
		"""Returns the last error."""
	def GetFileVersion(self) -> 'int':
		"""Returns the file version."""
	def GetFilterFlags(self) -> 'int':
		"""Returns the filter flags of a file, the value is valid only at load or merge time."""
	def Open(self, ident: 'int', filename: 'Union[str, MemoryFileStruct]', mode: 'int', error_dialog: 'int') -> 'bool':
		"""Open a hyper file."""
	def ReadBool(self) -> 'Optional[bool]':
		"""Read a boolean value."""
	def ReadChar(self) -> 'Optional[int]':
		"""Read a character."""
	def ReadChunkEnd(self) -> 'bool':
		"""Read chunk end."""
	def ReadChunkStart(self) -> 'None':
		"""Read chunk start."""
	def ReadContainer(self) -> 'Optional[BaseBitmap]':
		"""Read a container."""
	def ReadData(self) -> 'Optional[Any]':
		"""Read an GeData."""
	def ReadFilename(self) -> 'Optional[str]':
		"""Read a filename."""
	def ReadFloat(self) -> 'Optional[float]':
		"""Read a float."""
	def ReadFloat32(self) -> 'Optional[float]':
		"""Read a float."""
	def ReadFloat64(self) -> 'Optional[float]':
		"""Read a long real (double precision)."""
	def ReadImage(self) -> 'Optional[BaseBitmap]':
		"""Read an image."""
	def ReadInt16(self) -> 'Optional[int]':
		"""Read a word (integer)."""
	def ReadInt32(self) -> 'Optional[int]':
		"""Read an int."""
	def ReadInt64(self) -> 'Optional[int]':
		"""Read a long."""
	def ReadMatrix(self) -> 'Optional[Matrix]':
		"""Read a Matrix."""
	def ReadMatrix32(self) -> 'Optional[Matrix]':
		"""Read a Matrix."""
	def ReadMatrix64(self) -> 'Optional[Matrix]':
		"""Read a (double precision) Matrix."""
	def ReadMemory(self) -> 'Optional[bytes]':
		"""Read a block of memory from the hyper file."""
	def ReadString(self) -> 'Optional[str]':
		"""Read a string."""
	def ReadTime(self) -> 'Optional[BaseTime]':
		"""Read a BaseTime."""
	def ReadUChar(self) -> 'Optional[int]':
		"""Read an unsigned character."""
	def ReadUInt16(self) -> 'Optional[int]':
		"""Read an unsigned word."""
	def ReadUInt32(self) -> 'Optional[int]':
		"""Read an unsigned int."""
	def ReadUInt64(self) -> 'Optional[int]':
		"""Read a long."""
	def ReadValueHeader(self) -> 'Optional[int]':
		"""Reads the value header."""
	def ReadVector(self) -> 'Optional[Vector]':
		"""Read a Vector."""
	def ReadVector32(self) -> 'Optional[Vector]':
		"""Read a Vector32."""
	def ReadVector64(self) -> 'Optional[Vector]':
		"""Read a Vector64."""
	def SetError(self, err: 'int') -> 'None':
		"""Set an error."""
	def SkipToEndChunk(self) -> 'bool':
		"""Skip to end chunk."""
	def SkipValue(self, h: 'int') -> 'bool':
		"""Skip the next value."""
	def WriteBool(self, v: 'bool') -> 'bool':
		"""Write a bool."""
	def WriteChar(self, v: 'int') -> 'bool':
		"""Write a character."""
	def WriteChunkEnd(self) -> 'bool':
		"""Write chunk end."""
	def WriteChunkStart(self, id: 'int', level: 'int') -> 'bool':
		"""Write chunk start."""
	def WriteContainer(self, v: 'BaseContainer') -> 'bool':
		"""Write the settings container."""
	def WriteData(self, v: 'object') -> 'bool':
		"""Write data to the hyperfile."""
	def WriteFilename(self, v: 'str') -> 'bool':
		"""Write a filename."""
	def WriteFloat32(self, v: 'float') -> 'bool':
		"""Write a long real (double precision) value."""
	def WriteFloat64(self, v: 'float') -> 'bool':
		"""Write a long real (double precision) value."""
	def WriteImage(self, v: 'BaseBitmap', format: 'int', data: 'Optional[BaseContainer]' = None, savebits: 'Optional[int]' = 1) -> 'bool':
		"""Write a bitmap image."""
	def WriteInt16(self, v: 'int') -> 'bool':
		"""Write a word (integer)."""
	def WriteInt32(self, v: 'int') -> 'bool':
		"""Write an int32 value."""
	def WriteInt64(self, v: 'int') -> 'bool':
		"""Write an int64 value."""
	def WriteMatrix(self, v: 'Matrix') -> 'bool':
		"""Write a Matrix."""
	def WriteMatrix32(self, v: 'Matrix') -> 'bool':
		"""Write a Matrix32."""
	def WriteMatrix64(self, v: 'Matrix') -> 'bool':
		"""Write a Matrix64."""
	def WriteMemory(self, data: 'bytearray') -> 'bool':
		"""Write a block of memory to the hyperfile."""
	def WriteString(self, v: 'str') -> 'bool':
		"""Write a string."""
	def WriteTime(self, v: 'BaseTime') -> 'bool':
		"""Write a BaseTime."""
	def WriteUChar(self, v: 'int') -> 'bool':
		"""Write an unsigned character."""
	def WriteUInt16(self, v: 'int') -> 'bool':
		"""Write a word (integer)."""
	def WriteUInt32(self, v: 'int') -> 'bool':
		"""Write an unsigned int32 value."""
	def WriteUInt64(self, v: 'int') -> 'bool':
		"""Write an unsigned int64 value."""
	def WriteVector(self, v: 'Vector') -> 'bool':
		"""Write a Vector."""
	def WriteVector32(self, v: 'Vector') -> 'bool':
		"""Write a Vector."""
	def WriteVector64(self, v: 'Vector') -> 'bool':
		"""Write a double precision Vector."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class MemoryFileStruct(object):
	"""Used to open byte sequences."""
	def GetData(self) -> 'Tuple[bytearray, int]':
		"""Get the byte sequence object."""
	def SetMemoryReadMode(self, adr: 'Union[bytearray, memoryview]', size: 'int') -> 'None':
		"""Sets the filename to read from a memory block instead of from a file."""
	def SetMemoryWriteMode(self) -> 'None':
		"""Sets the filename to write to memory instead of to a file."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def ShowInFinder(path: str, open: bool) -> bool:
	'''Shows a file in the Explorer / Finder.'''
def LoadDialog(type: int, title: str, flags: int, force_suffix: str, def_path: str, def_file: str) -> str:
	'''Shows a load dialog.'''
def SaveDialog(type: int, title: str, force_suffix: str, def_path: str, def_file: str) -> str:
	'''Shows a save dialog.'''
def GeExecuteFile(path: str) -> bool:
	'''Execute a file.'''
def GeExecuteProgram(app: str, path: str) -> bool:
	'''Execute an application.'''
def GeGetMemoryStat() -> Optional[BaseContainer]:
	'''Gets Cinema 4D memory statistics.'''
def GeMemGetFreePhysicalMemoryEstimate() -> int:
	'''Get the estimated free physical memory.'''
def GeGetMovieInfo(path: Union[str, MemoryFileStruct]) -> None:
	'''Get information from a movie file.'''
def GeIdentifyFile(name: Union[str, MemoryFileStruct], probe: object, recognition: int) -> Tuple[int, BasePlugin]:
	'''Identify a file.'''
def WriteHyperFile(doc: BaseDocument, node: GeListNode, filename: Union[str, MemoryFileStruct], ident: int) -> int:
	'''Writes a single list node to disk as a hyper file.'''
def ReadHyperFile(doc: BaseDocument, node: GeListNode, filename: Union[str, MemoryFileStruct], ident: int) -> int:
	'''Read a single list node to disk as a hyper file.'''
def GeGetC4DPath(whichpath: int) -> str:
	'''Gets one of the Cinema 4D paths.'''
def GeGetPluginPath() -> str:
	'''Returns the path of plugin folder.'''
def GeGetStartupPath() -> str:
	'''Get the path for the main folder Cinema 4D.'''
def GeGetStartupWritePath() -> str:
	'''Returns the writeable startup directory.'''
def GeGetStartupApplication() -> str:
	'''Returns the complete path of the host application.'''
def GetUserSiteSpecificPath() -> str:
	'''Returns the path to the site folder in the user folder.'''
def GetFreeVolumeSpace(drive: str) -> Tuple[int, int]:
	'''Returns drive information from given drive.'''

