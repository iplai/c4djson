from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import NOTOK
if TYPE_CHECKING:
	from c4d.documents import BaseDocument
	from c4d import BaseContainer, BaseDraw, BaseObject, Matrix



def IsSnapEnabled(doc: BaseDocument, snapmode: Optional[int]) -> bool:
	'''Test if a snap mode is enabled or not.'''
def EnableSnap(state: bool, doc: BaseDocument, snapmode: Optional[int]) -> None:
	'''Set the snap enabled status for a particular mode.'''
def GetSnapSettings(doc: BaseDocument, snapmode: Optional[int]) -> BaseContainer:
	'''Routine to get the snap settings for the current document.'''
def SetSnapSettings(doc: BaseDocument, bc: BaseContainer, snapmode: Optional[int]) -> None:
	'''Routine to set the snap settings for the current mode/document.'''
def IsQuantizeEnabled(doc: BaseDocument) -> bool:
	'''Test if quantizing is enabled or not.'''
def GetQuantizeStep(doc: BaseDocument, bd: Optional[BaseDraw], quantize_mode: Optional[int]) -> None:
	'''Retrieve the quantize step values from QUANTIZE_MOVE, QUANTIZE_SCALE, etc.'''
def SetQuantizeStep(doc: BaseDocument, bd: Optional[BaseDraw], quantize_mode: Optional[int], val: Optional[float]) -> None:
	'''Sets the quantize step values for QUANTIZE_MOVE, QUANTIZE_SCALE etc.'''
def GetWorkplaneObject(doc: BaseDocument) -> BaseObject:
	'''Retrieve the workplane object for the document.'''
def IsWorkplaneLock(doc: BaseDocument) -> bool:
	'''Get the current workplane locked status.'''
def SetWorkplaneLock(bd: BaseDraw, locked: bool) -> None:
	'''Set the current workplane locked status.'''
def GetWorkplaneMatrix(doc: BaseDocument, bd: Optional[BaseDraw]) -> Matrix:
	'''Get the current workplane Matrix.'''

