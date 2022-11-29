from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseTag, BaseList2D, GV_INSERT_AFTER, GV_PORT_FLAG_IS_VISIBLE
if TYPE_CHECKING:
	from c4d import BaseContainer, DescID
	from c4d.threading import BaseThread
	from c4d.bitmaps import BaseBitmap


class GvNodeMaster(BaseList2D):
	"""Handles a collection of nodes."""
	def AddUndo(self) -> 'bool':
		"""Call this to make it undoable."""
	def AllocNode(self, id: 'int') -> 'GvNode':
		"""Allocates a node without inserting it."""
	def CreateNode(self, parent: 'GvNode', id: 'int', insert: 'Optional[GvNode]' = None, x: 'Optional[int]' = -1, y: 'Optional[int]' = -1) -> 'GvNode':
		"""Creates a node and inserts it."""
	def Execute(self, thread: 'Optional[BaseThread]' = None) -> 'int':
		"""Execute GvNodeMaster calculation"""
	def GetOwner(self) -> 'BaseList2D':
		"""Retrieves the owner of the node master."""
	def GetPrefs(self) -> 'BaseContainer':
		"""Returns settings container"""
	def GetRoot(self) -> 'Optional[GvNode]':
		"""Retrieves the root node."""
	def InsertFirst(self, parent: 'GvNode', node: 'GvNode') -> 'bool':
		"""Inserts a node first."""
	def InsertLast(self, parent: 'GvNode', node: 'GvNode') -> 'bool':
		"""Inserts a node last."""
	def IsEnabled(self) -> 'GvNodeMaster':
		"""Returns True if the node master is enabled."""
	def SetHierarchy(self, insert: 'GvNode', node: 'GvNode', mode: 'int' = 3) -> 'bool':
		"""Set the hierarchy."""
	def SetPrefs(self, bc: 'BaseContainer') -> 'None':
		"""Set settings container."""
	def __init__(self, host: 'BaseList2D') -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class GvNode(BaseList2D):
	"""Represents a node in XPresso."""
	def AddPort(self, io: 'int', id: 'Union[int, DescID]', flag: 'int' = 1, message: 'bool' = False) -> 'Optional[GvPort]':
		"""Adds a port to this node and returns the new port."""
	def AddPortIsOK(self, io: 'int', id: 'int') -> 'bool':
		"""Checks if it's OK to add a port to this node."""
	def GetInPort(self, id: 'int') -> 'Optional[GvPort]':
		"""Retrieves an in port by index."""
	def GetInPortCount(self) -> 'int':
		"""Counts the number of in ports of this node."""
	def GetInPorts(self, type: 'int' = -1) -> 'Optional[List[GvPort]]':
		"""Returns all inports."""
	def GetNodeMaster(self) -> 'Optional[GvNodeMaster]':
		"""Returns the GvNodeMaster where the node is attached to."""
	def GetOpContainerInstance(self) -> 'BaseContainer':
		"""Returns a reference to the internal operator's container"""
	def GetOperatorContainer(self) -> 'BaseContainer':
		"""Returns a copy of the internal operator's container."""
	def GetOperatorID(self) -> 'int':
		"""Returns the operator ID."""
	def GetOutPort(self, id: 'int') -> 'Optional[GvPort]':
		"""Retrieves an out port by index."""
	def GetOutPortCount(self) -> 'int':
		"""Counts the number of out ports of this node."""
	def GetOutPorts(self, type: 'int' = -1) -> 'Optional[List[GvPort]]':
		"""Returns all outports."""
	def GetOwnerID(self) -> 'int':
		"""Returns the owner ID."""
	def GetPort(self, sub_id: 'int') -> 'Optional[GvPort]':
		"""Returns a subport by sub ID."""
	def GetPortIndex(self, id: 'int') -> 'int':
		"""Gets the index of a port by sub ID."""
	def IsGroupNode(self) -> 'bool':
		"""Checks if this node is a group node."""
	def OperatorSetData(self, type: 'int', data: 'object', mode: 'int') -> 'bool':
		"""Sets data in the operator."""
	def Redraw(self) -> 'None':
		"""Redraws the node."""
	def RemoveConnections(self) -> 'None':
		"""Removes all connections from all ports of this node."""
	def RemovePort(self, port: 'GvPort', message: 'bool' = False) -> 'None':
		"""Removes a port."""
	def RemovePortIsOK(self, port: 'GvPort') -> 'bool':
		"""Check if you can delete a port."""
	def RemoveUnusedPorts(self, message: 'bool' = True) -> 'None':
		"""Removes all unused ports from this node."""
	def ResetPortType(self, id: 'int') -> 'None':
		"""Changes the type of the port. Used to manage dynamic data ports."""
	def SetOperatorContainer(self, bc: 'BaseContainer') -> 'None':
		"""Sets the operator container."""
	def SetPortType(self, port: 'GvPort', id: 'int') -> 'None':
		"""Set the port type."""

class GvPort(object):
	"""A port of a node."""
	def Connect(self, port: 'GvPort') -> 'bool':
		"""Adds a connection between two nodes"""
	def GetDestination(self) -> 'List[GvPort]':
		"""Returns all destinations"""
	def GetIO(self) -> 'int':
		"""Get the IO mode for this port."""
	def GetMainID(self) -> 'int':
		"""Get the main ID of the port."""
	def GetName(self, node: 'GvNode') -> 'str':
		"""Get the name of this port."""
	def GetNode(self) -> 'GvNode':
		"""Returns the host object where the port is attached to."""
	def GetNrOfConnections(self) -> 'int':
		"""Get the number of connections."""
	def GetSubID(self) -> 'int':
		"""Get the sub ID of the port."""
	def GetUserData(self) -> 'None':
		"""Get the user data for the port."""
	def GetUserID(self) -> 'int':
		"""Get the user ID of the port."""
	def GetValueType(self) -> 'int':
		"""Get the value type of the node."""
	def GetVisible(self) -> 'bool':
		"""Checks if this port is hidden or visible."""
	def IsIncomingConnected(self) -> 'bool':
		"""Returns if incoming port is connected"""
	def Remove(self) -> 'bool':
		"""Removes the incoming connection."""
	def SetMainID(self, id: 'int') -> 'None':
		"""Set the sub ID of the port."""
	def SetName(self, name: 'str') -> 'None':
		"""Set the name of this port."""
	def SetUserData(self) -> 'None':
		"""Set the user data for the port."""
	def SetUserID(self, id: 'int') -> 'None':
		"""Set the user ID of the port."""
	def SetVisible(self, v: 'bool') -> 'None':
		"""Set the visibility of the port."""

class XPressoTag(BaseTag):
	"""Class for XPresso tags."""
	def GetNodeMaster(self) -> 'GvNodeMaster':
		"""Retrieves the node master."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def GetMaster(id: int) -> GvNodeMaster:
	'''Get one of the current active master nodes.'''
def OpenDialog(id: int, master: GvNodeMaster) -> bool:
	'''Opens the Xpresso dialog.'''
def CloseDialog(id: int) -> None:
	'''Close the Xpresso dialog.'''
def GetPrefs() -> BaseContainer:
	'''Gets the preferences for this world.'''
def SetPrefs(bc: BaseContainer) -> None:
	'''Sets the preferences for this world.'''
def RedrawMaster(master: GvNodeMaster) -> None:
	'''Redraws a node master.'''
def GetDefaultOperatorIcon(type: int) -> BaseBitmap:
	'''Gets the default operator icon'''

