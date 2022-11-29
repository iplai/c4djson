from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import THREADMODE_ASYNC, THREADPRIORITYEX_NORMAL

class BaseThread(object):
	"""BaseThread class."""
	def End(self, wait: 'bool' = True) -> 'None':
		"""Ends the thread."""
	def IsRunning(self) -> 'bool':
		"""Check if the thread is running."""
	def TestBreak(self) -> 'bool':
		"""Check if the thread received a break command to stop processing."""

class C4DThread(object):
	"""User thread object"""
	def End(self, wait: 'bool' = True) -> 'None':
		"""End the thread."""
	def Get(self) -> 'BaseThread':
		"""Check if thread is running."""
	def IsRunning(self) -> 'bool':
		"""Check if thread is running."""
	def Main(self) -> 'None':
		"""Start the thread running."""
	def Start(self, mode: 'int' = 1, priority: 'int' = 0) -> 'bool':
		"""Start the thread running."""
	def TestBreak(self) -> 'bool':
		"""Checks if the thread recieved a break command."""
	def TestDBreak(self) -> 'bool':
		"""Check if thread is running."""
	def Wait(self, checkevents: 'bool') -> 'None':
		"""Wait until thread has finished."""


def GeThreadLock() -> None:
	'''Lock global semaphore.'''
def GeThreadUnlock() -> None:
	'''Unlock global semaphore.'''
def GeIsMainThread() -> bool:
	'''Checks if you are in the main thread.'''
def GeIsMainThreadAndNoDrawThread() -> bool:
	'''Checks if you are in the main thread and the main thread is not executing any drawing code.'''
def GeGetCPUCount() -> int:
	'''Get the number of threads for the current render context.'''
def GeGetCurrentThreadCount() -> int:
	'''Get the number of threads for the current render context.'''
def GeGetCurrentThreadId() -> int:
	'''Returns a unique ID for the current thread.'''
def IdentifyThread(bt: BaseThread) -> int:
	'''Identifies a thread's type.'''
def GeGetCurrentThread() -> None:
	'''Returns the current thread.'''
def GeGetDummyThread() -> None:
	'''Returns a dummy thread.'''
def GeGetEscTestThread() -> None:
	'''Returns a dummy thread for escape key testing.'''
def GeCheckBackgroundThreadsRunning(typeclass: int, all: bool) -> bool:
	'''Stops all running background threads of the give typeclass.'''
def GeStopBackgroundThreads(typeclass: int, flags: int) -> None:
	'''Allows you to see if any of the threads matching typeclass is running.'''

