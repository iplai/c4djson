from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
if TYPE_CHECKING:
	from c4d import Vector, Matrix


class Particle(object):
	"""Single particle information."""
	off: Vector
	v1: Vector
	v3: Vector
	t: float
	bits: int

class BaseParticle(object):
	"""Particle information."""
	v: Vector
	count: int


def CalcParticleMatrix(cp: Particle) -> Matrix:
	'''Calculate the particles matrix'''

