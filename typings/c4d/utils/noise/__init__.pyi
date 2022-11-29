from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
if TYPE_CHECKING:
	from c4d import BaseContainer, Vector


class C4DNoise(object):
	"""Class to create noise."""
	@staticmethod
	def CreateMenuContainer(bIncludeNone: 'bool' = False) -> 'BaseContainer':
		"""Creates a menu container."""
	@staticmethod
	def EvaluateSampleOffset(type: 'int', rOctaves: 'float', rDelta: 'float') -> 'float':
		"""Evaluates the sample offset."""
	def Fbm(self, p: 'Vector', rOctaves: 'float', lRepeat: 'int', t: 'float' = 0.0) -> 'float':
		"""Generate a periodic Fractional Brownian Motion value."""
	@staticmethod
	def HasAbsolute(t: 'int') -> 'bool':
		"""Checks if a certain noise type supports the absolute parameter."""
	@staticmethod
	def HasCycles(t: 'int') -> 'bool':
		"""Checks if a certain noise type supports the octaves parameter."""
	@staticmethod
	def HasOctaves(t: 'int') -> 'bool':
		"""Checks if a certain noise type supports the cycles parameter."""
	def InitFbm(self, lMaxOctaves: 'int', rLacunarity: 'float', h: 'float') -> 'bool':
		"""Initializes fractal brownian motion."""
	def Noise(self, t: 'int', two_d: 'bool', p: 'Vector', time: 'float' = 0.0, octaves: 'float' = 4.0, absolute: 'bool' = False, sampleRad: 'float' = 0.25, detailAtt: 'float' = 0.25, t_repeat: 'int' = 0) -> 'float':
		"""Samples a 2D or 3D noise."""
	def RidgedMultifractal(self, p: 'Vector', rOctaves: 'float', rOffset: 'float', rGain: 'float', lRepeat: 'float', t: 'float' = 0) -> 'float':
		"""Generate a periodic fractal function."""
	def SNoise(self, p: 'Vector', lRepeat: 'int', t: 'float' = 0.0) -> 'float':
		"""Generate a signed noise value."""
	def Turbulence(self, p: 'Vector', rOctaves: 'float', bAsolute: 'object', lRepeat: 'int', t: 'float' = 0.0) -> 'float':
		"""Generate a periodic turbulence value."""
	def __init__(self, seed: 'int' = 665) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""


def Noise(p: Vector, t: float) -> float:
	'''Generate a noise value.'''
def SNoise(p: Vector, t: float) -> float:
	'''Generate a signed noise value.'''
def PNoise(p: Vector, d: Vector, dt: float, t: float) -> float:
	'''Generate a periodical noise value.'''
def Turbulence(p: Vector, oct: int, abs: bool, t: int) -> float:
	'''Generate a turbulence value.'''
def WavyTurbulence(p: Vector, t: float, oct: int, start: int) -> float:
	'''Generate a wavy turbulence value.'''

