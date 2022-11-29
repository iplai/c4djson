from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import MACHINELIST_ALL, VERIFICATIONBIT_NONE
if TYPE_CHECKING:
	from c4d import BaseContainer
	from uuid import UUID
	from c4d.threading import BaseThread
	from c4d.documents import BaseDocument


class RenderJob(BaseList2D):
	"""The base class of all paint classes"""
	def GetDefaultScene(self) -> 'None':
		"""Get the default scene"""
	def GetUuid(self) -> 'str':
		"""Get the uuid"""

class NetRenderService(object):
	"""Service class for net"""
	def AddLogToJob(self, jobUuid: 'object', log: 'str', doLock: 'bool', append: 'bool' = True) -> 'bool':
		"""Add a string to the job log."""
	def AddLogToMachine(self, jobUuid: 'object', log: 'str', doLock: 'bool') -> 'bool':
		"""Add a string to the machine log."""
	def AddMachine(self, address: 'str', securityToken: 'str', allowGui: 'bool', uuidOfMachineToOverwrite: 'object') -> 'bool':
		"""Add a new machine."""
	def ClearResults(self, jobUuid: 'object') -> 'bool':
		"""Clear Results."""
	def CopyRenderTaskFrom(self, jobUuid: 'object', resolveMachineUuids: 'bool' = False) -> 'None':
		"""Get the render task."""
	def CreateRenderJob(self, docName: 'str', jobUuid: 'object', creator: 'int', username: 'str', bt: 'Optional[BaseThread]' = None, watchFolderName: 'Optional[str]' = '') -> 'int':
		"""Create a job."""
	def DeleteRenderJob(self, jobUuid: 'object', informClients: 'bool') -> 'bool':
		"""Delete a job."""
	def GetAllMachineUuids(self, list: 'int' = 7, bits: 'int' = 0, includeLocalMachine: 'bool' = True, includeBonjourMachines: 'bool' = True) -> 'List[UUID]':
		"""Get the UUIDs of all machines."""
	def GetJobsList(self, triggerWatchDog: 'bool', rdata: 'int', assets: 'int', results: 'int', log: 'int', selectedJob: 'object' = None, selectedJobOnly: 'bool' = False, user: 'object' = None, settings: 'Optional[BaseContainer]' = None) -> 'List[BaseContainer]':
		"""Get jobs list."""
	def GetMachinesList(self, logCount: 'int' = -1, getOnlyThisMachine: 'object' = None) -> 'List[BaseContainer]':
		"""Get machines list."""
	def GetName(self) -> 'str':
		"""Get the name of the service."""
	def GetNetPreferences(self) -> 'BaseContainer':
		"""Get the net preferences."""
	def GetRepository(self) -> 'Repository':
		"""Get the repository."""
	def GetUserPool(self) -> 'UserPool':
		"""Get user pool."""
	def GetUuid(self) -> 'None':
		"""Get the uuid of the service."""
	def InitAndStartRenderingFullAsync(self, jobUuid: 'UUID') -> 'bool':
		"""Start a job fully asynchronous."""
	def InitRendering(self, doc: 'BaseDocument', rdata: 'BaseContainer', jobUuid: 'UUID', flags: 'int', machines: 'BaseContainer') -> 'int':
		"""Init a job."""
	def InsertJobAfter(self, jobUuid1: 'object', jobUuid2: 'object') -> 'bool':
		"""Insert a job after another."""
	def InsertJobBefore(self, jobUuid1: 'object', jobUuid2: 'object') -> 'bool':
		"""Insert a job before another."""
	def Message(self, userUuid: 'object', op: 'object', isPrivate: 'bool', msg: 'BaseContainer', result: 'Optional[BaseContainer]' = True) -> 'bool':
		"""Send a message."""
	def NetConsoleOutput(self, flags: 'int', value: 'str') -> 'None':
		"""Print a string to the service."""
	def RemoveResult(self, jobUuid: 'object', relResultPath: 'str') -> 'bool':
		"""Remove a result."""
	def SetDefaultSceneName(self, jobUuid: 'object', defaultSceneName: 'str') -> 'bool':
		"""Set the Default Scene Name."""
	def StartRendering(self, mode: 'int', doc: 'BaseDocument', jobUuid: 'object', bt: 'BaseThread') -> 'int':
		"""Start a job."""
	def StopRendering(self, mode: 'int', jobUuid: 'object', result: 'int') -> 'None':
		"""Stop a job."""

class UserPool(object):
	"""User Pool for net service"""
	def AddUser(self, username: 'str', password: 'str', description: 'str', isAdmin: 'bool') -> 'bool':
		"""Adds a user to the user pool."""
	def ChangeLanguage(self, userUuid: 'object', language: 'str') -> 'bool':
		"""Changes the default language for a user."""
	def ChangePassword(self, userUuid: 'object', oldPassword: 'str', newPassword: 'str') -> 'bool':
		"""Change the password for a user."""
	def ChangeUserAccountType(self, userUuid: 'object', isAdmin: 'bool') -> 'bool':
		"""Edit user account type."""
	def CheckUserCredentials(self, username: 'str', password: 'str') -> 'bool':
		"""Check the verification for a user."""
	def DeleteUser(self, userUuid: 'object') -> 'bool':
		"""Delete a user from the user pool."""
	def EditUserInfo(self, userUuid: 'object', description: 'str') -> 'bool':
		"""Edit user description."""
	def EditUserPassword(self, userUuid: 'object', password: 'str') -> 'bool':
		"""Edit user password."""
	def GetUsers(self) -> 'None':
		"""Returns all users."""

class Repository(object):
	"""Repository class for net"""
	def ConvertAbsolute2RelativePath(self) -> 'None':
		"""Get the uuid of the service."""
	def ConvertRelative2Absolute(self) -> 'None':
		"""Get the uuid of the service."""
	def GetJobsPath(self, server: 'bool') -> 'str':
		"""Get the uuid of the service."""
	def GetRepositoryPath(self) -> 'str':
		"""Get the default repository path."""
	def SetRepositoryPath(self, repositoryPath: 'str') -> 'None':
		"""Get the uuid of the service."""


def SetErrorLevel(printDebugErrors: bool, stackInErrors: bool, locationInErrors: bool) -> None:
	'''Returns the global netrender service'''
def GetGlobalNetRenderService() -> NetRenderService:
	'''Returns the global netrender service'''
def VerificationStateToString(state: int) -> str:
	'''Converts the verification state into a string'''
def JobCommandToString(command: int) -> str:
	'''Converts the job command state into a string'''
def JobStateToString(state: object) -> str:
	'''Converts the job command state into a string'''
def NetSpecialEventAdd(service: NetRenderService, remoteUuid: object, msg: BaseContainer, forceConnect: bool) -> bool:
	'''Sends a message to the machine with the given UUID.'''
def NetGeSyncMessage(service: NetRenderService, remoteUuid: object, msg: BaseContainer, forceConnect: bool) -> Tuple[bool, BaseContainer]:
	'''Sends a message to the machine with the given UUID.'''

