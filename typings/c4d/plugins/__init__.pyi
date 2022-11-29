from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseList2D
if TYPE_CHECKING:
	from c4d import GeListNode, BaseDraw, BaseTag, Matrix, BaseContainer, Vector, DescID, HandleInfo, Description, C4DAtom, BaseObject, AliasTrans, SplineObject, BaseShader
	from c4d.documents import BaseDocument
	from c4d.bitmaps import BaseBitmap
	from c4d.modules.mograph import FalloffDataData
	from c4d.threading import BaseThread
	from c4d.gui import EditorWindow, SubDialog
	from c4d.modules.sculpting import BrushDabData, SculptBrushParams
	from c4d.modules.particles import Particle, BaseParticle
	from c4d.modules.render import InitRenderStruct, ChannelData


class BasePlugin(BaseList2D):
	"""Base class for registered plugins."""
	def GetFilename(self) -> 'str':
		"""Gets the filename for the plugin file."""
	def GetID(self) -> 'int':
		"""Returns the ID."""
	def GetInfo(self) -> 'int':
		"""Flags for the plugin."""

class GeResource(object):
	"""Load strings from res files."""
	def Init(self, path: 'str') -> 'bool':
		"""Initialise the resources."""
	def InitAsGlobal(self) -> 'bool':
		"""Initialise the C4D main application string resource."""
	def LoadString(self, id: 'int') -> 'str':
		"""Load a string."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class PriorityList(object):
	"""Useful helper for drawing objects."""
	def Add(self, node: 'GeListNode', priority: 'int', flags: 'int') -> 'None':
		"""Adds an execution point."""

class BaseDrawHelp(object):
	"""Useful helper for drawing objects."""
	def GetActiveTag(self) -> 'Optional[BaseTag]':
		"""Returns the currently active tag."""
	def GetDisplay(self) -> 'BaseContainer':
		"""Returns a container with the display mode."""
	def GetDocument(self) -> 'BaseDocument':
		"""Returns the relevant document for the current draw operation."""
	def GetMg(self) -> 'Matrix':
		"""Returns the global matrix."""
	def GetViewSchedulerFlags(self) -> 'int':
		"""Returns flags which were passed to DrawViews()."""
	def IsActive(self) -> 'bool':
		"""Checks if the related BaseDraw is active."""
	def IsHighlight(self) -> 'bool':
		"""Checks if the current object is highlighted."""
	def SetDisplay(self, bc: 'BaseContainer') -> 'None':
		"""Sets the display mode container."""
	def SetMg(self, mg: 'Matrix') -> 'None':
		"""Sets the matrix returned by GetMg()."""
	def __init__(self, bd: 'BaseDraw', doc: 'BaseDocument') -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class BaseData(object):
	"""Base class for all plugin classes."""

class FalloffData(BaseData):
	"""A class for tag plugins."""

class CommandData(BaseData):
	"""A class for creating new commands."""
	def Execute(self, doc: 'BaseDocument') -> 'bool':
		"""Override this method."""
	def ExecuteOptionID(self, doc: 'BaseDocument', plugid: 'int', subid: 'int') -> 'bool':
		"""Override this method."""
	def ExecuteSubID(self, doc: 'BaseDocument', subid: 'int') -> 'bool':
		"""Override this method."""
	def GetScriptName(self) -> 'str':
		"""Override this method."""
	def GetSubContainer(self, doc: 'BaseDocument', submenu: 'BaseContainer') -> 'bool':
		"""Override this method."""
	def Message(self, type: 'int', data: 'object') -> 'bool':
		"""Override this method."""
	def RestoreLayout(self, secret: 'object') -> 'bool':
		"""Override this method."""

class BitmapLoaderData(BaseData):
	"""A class for creating bitmap loaders."""

class BitmapSaverData(BaseData):
	"""A class for creating bitmap savers."""

class ToolData(BaseData):
	"""A data class for creating tool plugins."""

class SculptBrushToolData(BaseData):
	"""A data class for creating sculpt brushes."""

class MessageData(BaseData):
	"""A data class for creating message plugins."""

class NodeData(BaseData):
	"""A class for creating node plugins."""
	def InitAttr(self, host: 'BaseObject', type: 'object', id: 'DescID') -> 'bool':
		"""Initialize a value of an object."""

class ObjectData(NodeData):
	"""A class for object plugins."""
	def Draw(self, op: 'BaseObject', drawpass: 'int', bd: 'BaseDraw', bh: 'BaseDrawHelp') -> 'int':
		"""Draw additional information for your object in the editor."""
	def DrawShadow(self, op: 'BaseObject', bd: 'BaseDraw', bh: 'BaseDrawHelp') -> 'int':
		"""Draw the shadow for your object in the editor."""
	def SetOptimizeCache(self, cache: 'bool') -> 'None':
		"""Set optimize cache."""

class TagData(NodeData):
	"""A class for tag plugins."""

class ShaderData(NodeData):
	"""A class for shader plugins."""
	def SetExceptionColor(self, col: 'Vector') -> 'None':
		"""Set exception color."""

class SceneSaverData(NodeData):
	"""A class for creating scene savers."""

class SceneLoaderData(NodeData):
	"""A class for creating scene loaders."""

class PreferenceData(NodeData):
	"""A class for preferences plugins."""
	def InitPreferenceValue(self, id: 'int', data: 'object', desc: 'Optional[Description]' = None, descid: 'Optional[DescID]' = None, bc: 'Optional[BaseContainer]' = None) -> 'None':
		"""Initializes preference values."""


def GetFirstPlugin() -> BasePlugin:
	'''Gets the first registered plugin in the plugin list.'''
def FindPlugin(id: int, type: Optional[int]) -> BasePlugin:
	'''Finds a plugin from ID and type.'''
def FilterPluginList(type: int, sortbyname: bool) -> List[BasePlugin]:
	'''Get a list of all plugins.'''
def RemovePlugin(plug: Any):
	'''Removes a plugin - private.'''
def GeLoadString(id: int, p1: Optional[str], p2: Optional[str], p3: Optional[str], p4: Optional[str]) -> str:
	'''Load a string from a res instance.'''
def ReloadPythonPlugin(path: Any):
	'''Reload a Python plugin.'''
def ReloadAllPythonPlugins():
	'''Reload all Python plugins.'''
def UpdateAfterReload() -> None:
	'''Update the document.'''
def ReloadDocumentAfterReload() -> None:
	'''Update the document.'''
def RegisterToolPlugin(id: int, str: str, info: int, icon: Optional[BaseBitmap], help: Optional[str], dat: Optional[ToolData]) -> bool:
	'''Registers a tool plugin.'''
def RegisterSculptBrushPlugin(id: int, str: str, info: int, icon: Optional[BaseBitmap], help: Optional[str], sculptparams: Optional[SculptBrushParams], dat: Optional[SculptBrushToolData], res: Optional[GeResource]) -> bool:
	'''Registers a sculpt brush.'''
def RegisterCommandPlugin(id: int, str: str, info: int, icon: Optional[BaseBitmap], help: Optional[str], dat: Optional[CommandData]) -> bool:
	'''Registers a command plugin.'''
def RegisterFalloffPlugin(id: int, str: str, info: int, g: FalloffData, description: str, res: Optional[GeResource]) -> bool:
	'''Registers a falloff plugin.'''
def RegisterMessagePlugin(id: int, str: str, info: int, dat: MessageData) -> bool:
	'''Registers a message plugin.'''
def RegisterBitmapSaverPlugin(id: int, str: str, info: int, dat: BitmapSaverData, suffix: str) -> bool:
	'''Registers a bitmap saver plugin.'''
def RegisterBitmapLoaderPlugin(id: int, str: str, info: int, dat: BitmapLoaderData) -> bool:
	'''Registers a bitmap loader plugin.'''
def RegisterSceneSaverPlugin(id: int, str: str, g: object, info: int, description: str, suffix: str, res: Optional[GeResource]) -> bool:
	'''Registers a scene saver plugin'''
def RegisterSceneLoaderPlugin(id: int, str: str, g: object, info: int, description: str, res: Optional[GeResource]) -> bool:
	'''Registers a scene loader plugin'''
def RegisterTagPlugin(id: int, str: str, info: int, g: object, description: str, icon: Optional[BaseBitmap], disklevel: Optional[int], res: Optional[GeResource]) -> bool:
	'''Registers a tag plugin.'''
def RegisterShaderPlugin(id: int, str: str, info: int, g: object, description: str, disklevel: int, res: Optional[GeResource]) -> bool:
	'''Registers a shader plugin.'''
def RegisterObjectPlugin(id: int, str: str, g: object, description: str, info: int, icon: Optional[BaseBitmap], disklevel: Optional[int], res: Optional[GeResource]) -> bool:
	'''Registers an object plugin.'''
def RegisterManagerInformation(id: int, str: str, info: int) -> bool:
	'''Registers manager information.'''
def RegisterPreferencePlugin(id: int, g: object, name: str, description: str, parentid: int, sortid: int) -> None:
	'''Registers a preference plugin.'''
def RegisterNodePlugin(id: int, str: str, info: int, g: object, icon: Optional[BaseBitmap], disklevel: Optional[int]) -> bool:
	'''Register node plugin.'''
def RegisterDescription(id: int, str: str, res: Optional[GeResource]) -> bool:
	'''Register description.'''
def RegisterToken(key: str, help: str, example: str, hook: Callable[..., Any]) -> str:
	'''Registers a new Token that can be used in a render filename.'''
def RegisterHiddenToken(key: str, help: str, example: str, hook: Callable[..., Any]) -> str:
	'''Registers a new Token that can be used in a render filename but hides it from the render filename menu.'''
def ReadRegInfo(pluginid: int, size: int) -> bytes:
	'''Read private serial information for a plugin.'''
def WriteRegInfo(pluginid: int, buffer: bytes) -> None:
	'''Write private serial information for a plugin.'''
def ReadPluginInfo(pluginid: int, size: int) -> bytes:
	'''Read private serial information for a plugin.'''
def WritePluginInfo(pluginid: int, buffer: bytes) -> None:
	'''Write private serial information for a plugin.'''
def SetWorldPluginData(id: int, bc: BaseContainer, add: bool) -> bool:
	'''Retrieves a plugin container.'''
def GetWorldPluginData(id: int) -> BaseContainer:
	'''Add a plugin container.'''
def GetToolData(doc: BaseDocument, pluginid: int) -> BaseContainer:
	'''Returns the container of a tool.'''
def Update():
	'''Subscribes the current plugin to be updated for the c4d module.'''
def RegisterPluginHelpCallback(pluginid: int, callback: Callable[..., Any]) -> bool:
	'''Registers a callback for plugin help.'''

