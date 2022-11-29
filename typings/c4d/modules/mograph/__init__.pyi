from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseObject, BaseList2D, MDDIRTY_NONE, NOTOK, FIELDSAMPLE_FLAG_VALUE, FIELDSAMPLE_FLAG_DIRECTION, FIELDSAMPLE_FLAG_COLOR
if TYPE_CHECKING:
	from c4d.storage import HyperFile
	from c4d import DescID, BaseContainer, Vector, GeListHead, Matrix, Description, HandleInfo, BaseDraw, BaseTime, BaseSelect
	from c4d.documents import BaseDocument
	from c4d.threading import BaseThread
	from c4d.plugins import BaseDrawHelp


class MoData(object):
	"""MoData class"""
	def AddArray(self, id: 'DescID', name: 'str' = '', default_flags: 'int' = 0) -> 'int':
		"""Add the specified array."""
	def Clear(self, reset: 'bool') -> 'None':
		"""Clear the data in the arrays."""
	def Flush(self) -> 'None':
		"""Flushes the data."""
	def GetArray(self, id: 'int') -> 'List[object]':
		"""Get a specified array list."""
	def GetArrayCount(self) -> 'int':
		"""Get the number of arrays."""
	def GetArrayDescID(self, index: 'int') -> 'DescID':
		"""Get the description ID for the specified array index."""
	def GetArrayID(self, index: 'int') -> 'int':
		"""Get the ID for the specified array index."""
	def GetArrayIndex(self, id: 'DescID') -> 'int':
		"""Get the array index for the specified ID."""
	def GetArrayIndexType(self, index: 'int') -> 'int':
		"""Get the data type of the specified array."""
	def GetArrayType(self, id: 'int') -> 'None':
		"""Get the data type of the specified array."""
	def GetBlendID(self) -> 'int':
		"""Returns the current blend ID."""
	def GetCount(self) -> 'int':
		"""Get the length of the arrays."""
	def GetCurrentIndex(self) -> 'int':
		"""Returns the current index."""
	def GetData(self, id: 'int' = -1) -> 'BaseContainer':
		"""Get a copy container for the specified array."""
	def GetDataIndexInstance(self, index: 'int') -> 'BaseContainer':
		"""Get the original container for the specified array."""
	def GetDataInstance(self, id: 'DescID') -> 'BaseContainer':
		"""Get the original container for the specified array."""
	def GetDirty(self, mask: 'int' = 0) -> 'int':
		"""Get dirty count."""
	def GetFalloffs(self) -> 'List[float]':
		"""Returns the established falloff."""
	def GetGenerator(self) -> 'BaseList2D':
		"""Returns the established generator object."""
	def GetIndexName(self, index: 'int') -> 'str':
		"""Get the name of the specified array."""
	def GetMemorySize(self) -> 'int':
		"""Get the size of the data in bytes."""
	def GetName(self, id: 'DescID') -> 'str':
		"""Get the name of the specified array."""
	def Read(self, hf: 'HyperFile') -> 'bool':
		"""Read the data from a hyper file."""
	def RemoveArray(self, id: 'DescID') -> 'bool':
		"""Remove the specified array."""
	def SetArray(self, id: 'int', arr: 'List[object]', apply_strength: 'bool') -> 'None':
		"""Set a specified array list."""
	def SetCount(self, cnt: 'int') -> 'bool':
		"""Set the length of the arrays."""
	def SetDirty(self, mask: 'int' = 0) -> 'None':
		"""Mark the data as dirty."""
	def SetIndexName(self, index: 'int', name: 'str') -> 'None':
		"""Set the name for the specified array."""
	def SetLimit(self, limit: 'int' = -1) -> 'None':
		"""Limits the array."""
	def SetName(self, id: 'DescID', name: 'str') -> 'None':
		"""Set the name for the specified array."""
	def SetOffset(self, offset: 'int' = 0) -> 'None':
		"""Set an offset from the beginning of the arrays."""
	def Write(self, hf: 'HyperFile') -> 'bool':
		"""Write the data from a hyper file."""

class FalloffDataData(object):
	"""Structure to hold falloff data."""

class C4D_Falloff(object):
	"""Allows to sample falloffs."""
	def AddFalloffToDescription(self, description: 'Description', bc: 'Optional[BaseContainer]' = True) -> 'bool':
		"""Adds the falloff to a description."""
	def CopyTo(self, dest: 'C4D_Falloff') -> 'bool':
		"""Copies the falloff to another."""
	def Draw(self, bd: 'BaseDraw', bh: 'BaseDrawHelp', drawpass: 'int', bc: 'Optional[BaseContainer]' = True) -> 'bool':
		"""Draws the falloff into a view."""
	def GetContainerInstance(self) -> 'BaseContainer':
		"""Returns the last container the falloff should try to use."""
	def GetData(self) -> 'FalloffDataData':
		"""Returns the falloff's data."""
	def GetDirty(self, bc: 'Optional[BaseContainer]' = True, doc: 'Optional[BaseDocument]' = None) -> 'int':
		"""Returns the falloff dirty value."""
	def GetHandle(self, index: 'int', bc: 'BaseContainer', info: 'HandleInfo') -> 'None':
		"""Returns a handle for the falloff."""
	def GetHandleCount(self, bc: 'Optional[BaseContainer]' = True) -> 'int':
		"""Returns the number of handles for the falloff."""
	def GetMg(self) -> 'Matrix':
		"""Returns the falloff's matrix."""
	def GetMode(self) -> 'int':
		"""Returns the falloff mode."""
	def InitFalloff(self, bc: 'Optional[BaseContainer]' = None, doc: 'Optional[BaseDocument]' = True, op: 'Optional[BaseObject]' = True) -> 'bool':
		"""Initializes the falloff."""
	def Message(self, id: 'int', bc: 'Optional[BaseContainer]' = True, data: 'Optional[object]' = None) -> 'bool':
		"""Sends messages to the falloff."""
	def MultiSample(self, points: 'List[Vector]', usespline: 'bool' = True, weight: 'Optional[float]' = True) -> 'List[float]':
		"""Samples the falloff for an array of points in space."""
	def Sample(self, point: 'Vector', usespline: 'bool' = True, weight: 'Optional[float]' = True) -> 'float':
		"""Samples the falloff for any point in space."""
	def SetData(self, data: 'FalloffDataData') -> 'None':
		"""Sets the falloff's data directly."""
	def SetDirty(self) -> 'None':
		"""Sets the falloff dirty."""
	def SetHandle(self, index: 'int', point: 'Vector', bc: 'BaseContainer', info: 'HandleInfo') -> 'None':
		"""Sets a handle for the falloff."""
	def SetMg(self, mg: 'Matrix') -> 'None':
		"""Sets the falloff's matrix."""
	def SetMode(self, type: 'int', bc: 'Optional[BaseContainer]' = True) -> 'bool':
		"""Sets the falloff mode."""
	def SetTime(self, time: 'BaseTime', bc: 'Optional[BaseContainer]' = True) -> 'None':
		"""Sets the current falloff time."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class FieldInput(object):
	"""FieldInput Class"""
	_blockCount: int
	_blockOffset: int
	_fullArraySize: int
	_transform: Matrix
	_position: List[Vector]
	_direction: List[Vector]
	_uvw: List[Vector]
	def GetCount(self) -> 'int':
		"""Read the FieldInput's item count."""
	def GetOffset(self) -> 'int':
		"""Read the FieldInput's first element offset in the full array."""
	def GetSubBlock(self, offset: 'int', blockSize: 'int') -> 'FieldInput':
		"""Return a subset of the FieldInput."""
	def IsPopulated(self) -> 'bool':
		"""Validate the FieldInput's content (empty not accepted)."""
	def IsValid(self) -> 'bool':
		"""Validate the FieldInput's content (empty accepted)."""
	def __init__(self, position: 'List[Vector]', allocatedCount: 'int', transform: 'Optional[Matrix]' = None, fullCount: 'Optional[int]' = -1, direction: 'Optional[List[Vector]]' = None, uvw: 'Optional[List[Vector]]' = None) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class FieldCallerStack(object):
	"""FieldCallerStack Class"""
	def Add(self, caller: 'BaseList2D') -> 'bool':
		"""Adds a new caller on top of the stack."""
	def CopyFrom(self, src: 'FieldCallerStack') -> 'bool':
		"""Copies the FieldCallerStack content from supplied source."""
	def GetCount(self) -> 'int':
		"""Reads the caller count."""
	def GetValue(self) -> 'int':
		"""Reads the caller ID."""
	def IsValid(self) -> 'bool':
		"""Validates the content of FieldCallerStack (empty accepted)."""
	def RecalcValue(self) -> 'int':
		"""Calculate the caller ID from scratch (no internal ID update)."""
	def UpdateValue(self) -> 'None':
		"""Calculate the caller new ID."""
	def __getitem__(self, key: 'int') -> 'BaseList2D':
		"""Return self[key]."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class FieldInfo(object):
	"""FieldInfo Class"""
	_flags: int
	_threadIndex: int
	_totalThreadCount: int
	_callerThread: BaseThread
	_doc: BaseDocument
	_callerStack: FieldCallerStack
	_inputData: FieldInput
	@staticmethod
	def Create(flags: 'int', thread: 'BaseThread', doc: 'BaseDocument', currentThreadIndex: 'int', threadCount: 'int', inputs: 'Optional[FieldInput]' = None, callers: 'Optional[List[BaseList2D]]' = None) -> 'FieldInfo':
		"""Create a new FieldInfo."""
	def IsPopulated(self) -> 'bool':
		"""Validate the FieldInfo's content (empty not accepted)"""
	def IsValid(self) -> 'bool':
		"""Validate the FieldInfo's content (empty accepted)"""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class FieldOutput(object):
	"""FieldOutput Class"""
	_value: List[float]
	_alpha: List[float]
	_color: List[Vector]
	_direction: List[Vector]
	_rotation: List[Vector]
	_pivot: List[Vector]
	_deactivated: List[bool]
	def CalculateCrc(self) -> 'int':
		"""Calculate crc and return the value."""
	def ClearDeactivated(self, state: 'bool' = False) -> 'None':
		"""Reset the sample's deactivated array to default values."""
	def ClearMemory(self, startIdx: 'int' = 0, count: 'int' = None, deactivatedOnly: 'bool' = False, deactivatedState: 'bool' = False) -> 'None':
		"""Reset the sample's arrays to default values."""
	def CopyArrayContentFrom(self, src: 'Union[FieldOutput, FieldOutputBlock]') -> 'bool':
		"""Copy all sample data from source block limited current allocated size."""
	def CopyFrom(self, src: 'FieldOutput') -> 'bool':
		"""Copy all sample data from source block."""
	@staticmethod
	def Create(size: 'int', flags: 'int' = 3, src: 'Optional[FieldOutputBlock]' = None) -> 'FieldOutput':
		"""Create a FieldOutput with requested arrays."""
	def Flush(self) -> 'None':
		"""Reset the sample's content (maintain array allocations)."""
	def GetAlpha(self, index: 'int') -> 'float':
		"""Read alpha float at specified index."""
	def GetBlock(self) -> 'FieldOutputBlock':
		"""Fetch a FieldOutput block."""
	def GetColor(self, index: 'int') -> 'Vector':
		"""Read color vector at specified index."""
	def GetCount(self) -> 'int':
		"""Read the sample's length."""
	def GetDeactivated(self, index: 'int') -> 'bool':
		"""Read deactivated bool at specified index."""
	def GetDirection(self, index: 'int') -> 'Vector':
		"""Read direction vector at specified index."""
	def GetPivot(self, index: 'int') -> 'Vector':
		"""Read direction pivot vector at specific index."""
	def GetRotation(self, index: 'int') -> 'Vector':
		"""Read rotation vector at specified index."""
	def GetSubBlock(self, offset: 'int', size: 'int') -> 'FieldOutputBlock':
		"""Fetch a FieldOutput subblock."""
	def GetValue(self, index: 'int') -> 'float':
		"""Read value float at specified index."""
	def IsPopulated(self) -> 'bool':
		"""Validate the FieldOutput's content (empty not accepted)"""
	def IsValid(self) -> 'bool':
		"""Validate the FieldOutput's content (empty accepted)"""
	def Reset(self) -> 'None':
		"""Reset and deallocate the sample's content."""
	def Resize(self, newSize: 'int', sampleFlags: 'int' = 0, resizeFlags: 'int' = 2) -> 'bool':
		"""Resize the sample's data arrays."""
	def SetAlpha(self, index: 'int', alpha: 'float') -> 'None':
		"""Write alpha float at specified index."""
	def SetColor(self, index: 'int', color: 'Vector') -> 'None':
		"""Write color vector at specified index."""
	def SetDeactivated(self, index: 'int', deact: 'bool') -> 'None':
		"""Write deactivated bool at specified index."""
	def SetDirection(self, index: 'int', direction: 'Vector') -> 'None':
		"""Write direction vector at specified index."""
	def SetRotation(self, index: 'int', rotation: 'Vector', pivot: 'Vector') -> 'None':
		"""Write rotation vector at specified index."""
	def SetValue(self, index: 'int', value: 'float') -> 'None':
		"""Write value float at specified index."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class FieldOutputBlock(object):
	"""FieldOutputBlock Class"""
	_value: List[float]
	_alpha: List[float]
	_color: List[Vector]
	_direction: List[Vector]
	_rotation: List[Vector]
	_pivot: List[Vector]
	_deactivated: List[bool]
	def CalculateCrc(self) -> 'int':
		"""Calculate the FieldOutputBlock CRC."""
	def ClearDeactivated(self, state: 'bool' = False) -> 'None':
		"""Reset the sample's deactivated array to default values."""
	def ClearMemory(self, startIdx: 'int' = 0, count: 'int' = None, deactivatedOnly: 'bool' = False, deactivatedState: 'bool' = False) -> 'None':
		"""Reset the sample's arrays to default values."""
	def CopyArrayContentFrom(self, src: 'FieldOutputBlock') -> 'bool':
		"""Copy all sample data from source block without changing offset or size."""
	def CopyFrom(self, src: 'FieldOutputBlock') -> 'bool':
		"""Copy all sample data from source block."""
	def GetAlpha(self, index: 'int') -> 'float':
		"""Read alpha float at specified index."""
	def GetColor(self, index: 'int') -> 'Vector':
		"""Read color vector at specified index."""
	def GetCount(self) -> 'int':
		"""Read the sample's length."""
	def GetDeactivated(self, index: 'int') -> 'bool':
		"""Read deactivated bool at specified index."""
	def GetDirection(self, index: 'int') -> 'Vector':
		"""Read direction vector at specified index."""
	def GetFullCount(self) -> 'int':
		"""Read the sample owner's length."""
	def GetOffset(self) -> 'int':
		"""Get the offset on the sample owner's allocated memory."""
	def GetOwner(self) -> 'FieldOutput':
		"""Get the owner of the sample allocated memory."""
	def GetPivot(self, index: 'int') -> 'Vector':
		"""Read rotation pivot axis at specified index."""
	def GetRotation(self, index: 'int') -> 'Vector':
		"""Read rotation vector at specified index."""
	def GetSubBlock(self) -> 'FieldOutputBlock':
		"""Fetch a FieldOutputBlock subblock."""
	def GetValue(self, index: 'int') -> 'float':
		"""Read value float at specified index."""
	def IsPopulated(self) -> 'bool':
		"""Validate the FieldOutputBlock's content (empty not accepted)"""
	def IsValid(self) -> 'bool':
		"""Validate the FieldOutputBlock's content (empty accepted)"""
	def Reset(self) -> 'None':
		"""Reset and deallocate the sample's content."""
	def SetAlpha(self, index: 'int', alpha: 'float') -> 'None':
		"""Write alpha float at specified index."""
	def SetColor(self, index: 'int', color: 'Vector') -> 'None':
		"""Write color vector at specified index."""
	def SetDeactivated(self, index: 'int', deact: 'bool') -> 'None':
		"""Write deactivated bool at specified index."""
	def SetDirection(self, index: 'int', direction: 'Vector') -> 'None':
		"""Write direction vector at specified index."""
	def SetRotation(self, index: 'int', rotation: 'Vector', pivot: 'Vector') -> 'None':
		"""Write rotation vector at specified index."""
	def SetValue(self, index: 'int', value: 'float') -> 'None':
		"""Write value float at specified index."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class FieldObject(BaseObject):
	"""FieldObject Class"""
	def FreeSampling(self, info: 'FieldInfo') -> 'None':
		"""Cleanup a sample pass."""
	def GetFieldFlags(self, doc: 'BaseDocument') -> 'int':
		"""Read the field calculation flags."""
	def InitSampling(self, info: 'FieldInfo') -> 'None':
		"""Initialize a sample pass."""
	def Sample(self, input: 'FieldInput', output: 'FieldOutputBlock', info: 'FieldInfo', flags: 'int') -> 'None':
		"""Perform field sampling."""
	def __init__(self, type: 'int') -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class FieldLayer(BaseList2D):
	"""FieldLayer Class"""
	def AddMask(self) -> 'bool':
		"""Enable the mask on the FieldLayer."""
	def Aggregate(self, input: 'object', output: 'object', info: 'object') -> 'None':
		"""Aggregate the outputs of sampled blocks."""
	def FreeSampling(self, info: 'FieldInfo') -> 'None':
		"""Cleanup a sample pass."""
	def GetBlendingMode(self) -> 'int':
		"""Read the layer's blending mode."""
	def GetChannelFlag(self, flag: 'int') -> 'bool':
		"""Read a single channel flag."""
	def GetChannelFlags(self) -> 'int':
		"""Read the layer's channel flags."""
	def GetLayerFlags(self) -> 'int':
		"""Read the layer sampling and display flags."""
	def GetLinkedObject(self, doc: 'BaseDocument') -> 'BaseList2D':
		"""Get the layer's FieldObject."""
	def GetMaskHead(self) -> 'Optional[GeListHead]':
		"""Get the FieldLayer's Mask listhead."""
	def GetStrength(self) -> 'float':
		"""Read the layer's strength."""
	def GetUniqueID(self) -> 'None':
		"""Read the layer's unique ID."""
	def InitSampling(self, info: 'FieldInfo') -> 'None':
		"""Initialize a sample pass."""
	def RemoveMask(self, link: 'bool') -> 'None':
		"""Disable the FieldLayer's Mask."""
	def Sample(self, input: 'FieldInput', output: 'FieldOutputBlock', info: 'FieldInfo') -> 'None':
		"""Perform layer sampling."""
	def SetBlendingMode(self, blendingMode: 'int') -> 'None':
		"""Set the layer's blending mode."""
	def SetChannelFlag(self, flag: 'object', state: 'bool' = True) -> 'None':
		"""Set a single channel flag."""
	def SetChannelFlags(self, flags: 'int') -> 'None':
		"""Set the layer's channel flags."""
	def SetLayerFlags(self, flags: 'int', state: 'bool' = True) -> 'None':
		"""Set the layer sampling and display flags."""
	def SetLinkedObject(self, link: 'BaseList2D') -> 'None':
		"""Set the layer's FieldObject."""
	def SetStrength(self, strength: 'float') -> 'None':
		"""Set the layer's strength."""
	def SetUniqueID(self, id: 'object') -> 'None':
		"""Set the layer's unique ID."""
	def __init__(self, type: 'int') -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def GeGetMoData(op: BaseObject) -> None:
	'''Returns the MoGraph data of an object.'''
def GeGetMoDataSelection(op: BaseList2D) -> None:
	'''Returns the MoGraph selection of an object.'''
def GeSetMoDataSelection(op: BaseList2D, selection: BaseSelect) -> bool:
	'''Sets the MoGraph selection of an object.'''
def GeGetMoDataWeights(op: BaseList2D) -> List[float]:
	'''Returns the MoGraph weights of an object.'''
def GeSetMoDataWeights(op: BaseList2D, weights: List[float]) -> bool:
	'''Sets the MoGraph weights of an object.'''
def GetMoDataDefault(id: int) -> Any:
	'''Get the default value for the specified MoData ID.'''
def GetMoDataDefaultType(id: int) -> int:
	'''Get the default type for the specified MoData ID.'''

FIELD_EXECUTION_BLOCK_SIZE: int = 400
FIELD_EXECUTION_BLOCK_SIZEf: float = 400.0
