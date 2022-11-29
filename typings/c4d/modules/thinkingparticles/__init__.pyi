from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseList2D
if TYPE_CHECKING:
	from c4d import BaseObject, BaseContainer, BaseTime, Vector, Matrix
	from c4d.modules.graphview import GvNode


class TP_PGroup(BaseList2D):
	"""Represents a particle group."""
	def Cache(self, onoff: 'bool') -> 'None':
		"""Sets this group to contain cached data only."""
	def EditSettings(self) -> 'bool':
		"""Opens the edit dialog for this group."""
	def GetColor(self) -> 'Vector':
		"""Get the color of this group."""
	def GetGroupID(self) -> 'int':
		"""Gets the ID of this group."""
	def GetLevel(self) -> 'int':
		"""Calculates the level of this group."""
	def GetParticles(self) -> 'List[int]':
		"""Return all particles of the group."""
	def GetShowObjects(self) -> 'int':
		"""Get the show-objects flag."""
	def GetTitle(self) -> 'str':
		"""Set the group title."""
	def GetUseColor(self) -> 'bool':
		"""Get the use-color flag."""
	def GetViewType(self) -> 'int':
		"""Get the view type."""
	def IsCache(self) -> 'bool':
		"""Checks if this group represents cached data."""
	def IsOpened(self) -> 'bool':
		"""Checks if this group is opened."""
	def IsSelected(self) -> 'bool':
		"""Checks if this group is selected."""
	def IsSubGroup(self, group: 'TP_PGroup') -> 'bool':
		"""Check if group is a subgroup."""
	def NumParticles(self) -> 'int':
		"""Calculates the number of particles in this group."""
	def Open(self, onoff: 'bool') -> 'None':
		"""Opens or closes this group."""
	def Select(self, mode: 'int') -> 'None':
		"""Sets the selection status."""
	def SetColor(self, col: 'Vector') -> 'None':
		"""Set the color of this group."""
	def SetShowObjects(self, bool: 'object') -> 'None':
		"""Set the show-objects flag."""
	def SetTitle(self, title: 'str') -> 'None':
		"""Get the group title."""
	def SetUseColor(self, use: 'bool') -> 'None':
		"""Set the use-color flag."""
	def SetViewType(self, type: 'object') -> 'None':
		"""Set the view type."""

class TP_MasterSystem(BaseList2D):
	"""Represents the engine for TP."""
	def AddDataChannel(self, type: 'int', str: 'str') -> 'bool':
		"""Adds a new data channel."""
	def Age(self, pid: 'int') -> 'BaseTime':
		"""Retrieves the age of a particle."""
	def Alignment(self, pid: 'int') -> 'Matrix':
		"""Retrieves the alignment matrix of a particle."""
	def Alive(self, pid: 'int') -> 'bool':
		"""Retrieves the alive bit of a particle."""
	def AllocParticle(self) -> 'int':
		"""Allocates a particle."""
	def AllocParticleGroup(self) -> 'TP_PGroup':
		"""Allocates a new particle group."""
	def AllocParticles(self, num: 'int') -> 'List[int]':
		"""Allocates a particle."""
	def CheckCollision(self, collision: 'int', pid: 'int', t: 'float', pos: 'Vector', vel: 'Vector', dt: 'float') -> 'None':
		"""Increments the dirty counter."""
	def Color(self, pid: 'int') -> 'Vector':
		"""Retrieves the color of a particle."""
	def DTFactor(self, pid: 'int') -> 'float':
		"""Retrieves the delta time factor."""
	def DataChannelID(self, unique_id: 'int') -> 'int':
		"""Retrieves the index of a data channel."""
	def DataChannelName(self, chan: 'int') -> 'str':
		"""Retrieves the name of a data channel."""
	def DataChannelType(self, chan: 'int') -> 'int':
		"""Retrieves the data type of a data channel."""
	def DataChannelUniqueID(self, chan: 'int') -> 'int':
		"""Retrieves a unique ID."""
	def EntersGroup(self, pid: 'int') -> 'bool':
		"""Retrieves the enters-group bit """
	def Flags(self, pid: 'int') -> 'Matrix':
		"""Retrieves the flags of a particle."""
	def FreeAllParticles(self) -> 'None':
		"""Frees all particles."""
	def FreeParticle(self, pid: 'int') -> 'None':
		"""Free a particle."""
	def FreeParticleGroup(self, group: 'TP_PGroup') -> 'None':
		"""Frees a particle group."""
	def GetDirty(self) -> 'int':
		"""A dirty counter for the master system."""
	def GetGroupFromInfo(self, info: 'BaseContainer') -> 'Optional[TP_PGroup]':
		"""Retrieves a group from the information."""
	def GetGroupInfo(self, group: 'TP_PGroup') -> 'BaseContainer':
		"""Retrieves the group information."""
	def GetGroupParticleCount(self, ingroup: 'TP_PGroup', subgroups: 'bool' = True) -> 'int':
		"""Calculates the number of particles."""
	def GetOperatorID(self, op: 'GvNode') -> 'int':
		"""Retrieves the operator for an ID."""
	def GetPData(self, pid: 'int', chan: 'int') -> 'Any':
		"""Retrieves the data channel value for a particle."""
	def GetParticleGroups(self, ingroup: 'TP_PGroup', mode: 'int', subgroups: 'bool' = True) -> 'List[TP_PGroup]':
		"""Returns the particle groups."""
	def GetParticles(self, all: 'bool' = False) -> 'None':
		"""Retrieves particles in a list."""
	def GetRootGroup(self) -> 'TP_PGroup':
		"""Return the main group."""
	def GetVirtualObjects(self, ingroup: 'TP_PGroup', inRender: 'bool' = True, subgroups: 'bool' = True, hh: 'Optional[object]' = None) -> 'Optional[BaseObject]':
		"""Creates the virtual object hierarchy."""
	def Group(self, pid: 'int') -> 'Optional[bool]':
		"""Retrieves the group of a particle."""
	def IsBorn(self, pid: 'int') -> 'bool':
		"""Retrieves the is-born bit of a particle."""
	def IsDie(self, pid: 'int') -> 'bool':
		"""Retrieves the is-die bit of a particle."""
	def Life(self, pid: 'int') -> 'BaseTime':
		"""Retrieves the lifetime of a particle."""
	def Mass(self, pid: 'int') -> 'float':
		"""Retrieves the mass of a particle."""
	def NumDataChannels(self) -> 'int':
		"""Retrieves the data channel count."""
	def NumParticles(self) -> 'int':
		"""Retrieves the number of allocated particles."""
	def Position(self, pid: 'int') -> 'Vector':
		"""Retrieves the position of a particle."""
	def Randomseed(self, pid: 'int') -> 'Matrix':
		"""Retrieves the random seed of a particle."""
	def RemoveDataChannel(self, chan: 'int') -> 'bool':
		"""Removes a data channel."""
	def Scale(self, pid: 'int') -> 'Vector':
		"""Retrieves the scale of a particle."""
	def SetAge(self, pid: 'int', age: 'BaseTime') -> 'None':
		"""Sets the age for a particle."""
	def SetAlignment(self, pid: 'int', align: 'Matrix') -> 'None':
		"""Sets the alignment matrix for a particle."""
	def SetCollision(self, pid: 'int', collision: 'int') -> 'None':
		"""Sets the collision handling information for a particle."""
	def SetColor(self, pid: 'int', color: 'Vector') -> 'None':
		"""Sets the color for a particle."""
	def SetDTFactor(self, pid: 'int', dt: 'float') -> 'None':
		"""Sets the delta time factor for a particle."""
	def SetDirty(self) -> 'None':
		"""Increments the dirty counter."""
	def SetGroup(self, pid: 'int', group: 'TP_PGroup') -> 'None':
		"""Inserts a particle into another group."""
	def SetLife(self, pid: 'int', life: 'BaseTime') -> 'None':
		"""Sets the lifetime for a particle."""
	def SetMass(self, pid: 'int', mass: 'float') -> 'None':
		"""Sets the mass for a particle."""
	def SetPData(self, pid: 'int', chan: 'int', value: 'Union[int, float, str, Vector, BaseTime, Matrix, BaseList2D]') -> 'bool':
		"""Sets the data channel value for a particle."""
	def SetPGroupHierarchy(self, parent: 'TP_PGroup', group: 'TP_PGroup', mode: 'int') -> 'None':
		"""Performs a hierarchy action on"""
	def SetPosition(self, pid: 'int', p: 'Vector') -> 'None':
		"""Sets the position for a particle."""
	def SetRandomseed(self, pid: 'int', seed: 'int') -> 'None':
		"""Sets the random seed for a particle."""
	def SetScale(self, pid: 'int', scale: 'Vector') -> 'None':
		"""Sets the scale for a particle."""
	def SetSize(self, pid: 'int', size: 'float') -> 'None':
		"""Sets the size for a particle."""
	def SetSpin(self, pid: 'int', axis: 'Vector', speed: 'float') -> 'None':
		"""Sets the spin for a particle."""
	def SetVelocity(self, pid: 'int', p: 'Vector') -> 'None':
		"""Sets the velocity for a particle."""
	def Size(self, pid: 'int') -> 'float':
		"""Retrieves the size of a particle."""
	def Spin(self, pid: 'int') -> 'float':
		"""Retrieves the spin of a particle."""
	def Transform(self, pid: 'int') -> 'Matrix':
		"""Retrieves the transformation matrix."""
	def UpdateGroup(self, group: 'TP_PGroup', timeDelta: 'BaseTime') -> 'bool':
		"""Updates a group with a time delta from the last update."""
	def Velocity(self, pid: 'int') -> 'Vector':
		"""Retrieves the velocity of a particle."""



