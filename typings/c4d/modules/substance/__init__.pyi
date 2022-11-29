from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
if TYPE_CHECKING:
	from c4d import BaseList2D, Material, C4DAtom, BaseMaterial
	from c4d.documents import BaseDocument
	from c4d.bitmaps import BaseBitmap



def ImportSubstance(doc: BaseDocument, fn: str, copyFile: int, errPopup: bool, addUndo: bool, createMaterial: bool) -> Tuple[int, BaseList2D, int]:
	'''Import a Substance Asset file (.sbsar) into a document.'''
def CreateMaterial(asset: BaseList2D, graphIndex: int, mode: int) -> None:
	'''Create a Cinema 4D standard material from a Substance asset.'''
def CreateSubstanceShader(asset: Optional[BaseList2D]) -> None:
	'''Create a Substance shader linked to Substance asset.'''
def AssignChannelToMaterial(asset: BaseList2D, mat: Material, channelId: int, outputUid: int, addUndo: bool) -> bool:
	'''Creates a Substance shader, links it to a Substance asset, sets the Substance output to outputUid and assigns the shader to channelId of c4dMaterial.'''
def GetFirstSubstance(doc: BaseDocument) -> Optional[BaseList2D]:
	'''Get a pointer to the first Substance asset in a document (if any).'''
def GetSubstances(doc: BaseDocument, onlySelected: bool) -> List[C4DAtom]:
	'''Have an @formatParam{arr} filled with pointers to all (or only selected) Substance assets in a document.'''
def InsertLastSubstance(doc: BaseDocument, asset: BaseList2D) -> bool:
	'''Insert aSubstance asset into in the document (as last element).'''
def GetSubstanceGraph(asset: BaseList2D, prevGraph: Optional[object]) -> Tuple[object, str]:
	'''This function may be used to iterate over the graphs of a Substance asset.'''
def GetSubstanceInput(asset: BaseList2D, graph: object, prevInput: Optional[object]) -> Tuple[Optional[object], int, int, int, int, str]:
	'''This function may be used to iterate over the inputs of a graph of a Substance asset.'''
def GetSubstanceOutput(asset: BaseList2D, graph: object, getBitmap: bool, prevOutput: Optional[object]) -> Tuple[Optional[object], int, int, str, BaseBitmap]:
	'''This function may be used to iterate over the outputs of a graph of a Substance asset.'''
def PrefsGetMaterialModeSetting() -> int:
	'''Convenience function to get the material creation mode set in Substance preferences.'''
def PrefsGetPreviewSetting() -> int:
	'''Convenience function to get the preview mode for Content Browser set in Substance preferences.'''
def MaterialUsesSubstance(mat: BaseMaterial) -> bool:
	'''Check if a BaseMaterial contains any Substance shaders.'''
def GetSubstanceMosaicPreview(asset: BaseList2D, w: int, h: int) -> None:
	'''Returns an image with previews of the output channels of a Substance asset.'''

