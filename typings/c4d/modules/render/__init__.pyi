from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import Vector
if TYPE_CHECKING:
	from c4d import BaseList2D, BaseTime
	from c4d.documents import BaseDocument
	from c4d.threading import BaseThread


class BaseVolumeData(object):
	"""Base volume data information class."""
	version: int
	fps: int
	ambient: Vector
	time: float
	col: Vector
	trans: Vector
	refl: Vector
	alpha: float
	tray: Optional[Ray]
	rray: Ray
	p: Vector
	ray: Ray
	bumpn: Vector
	orign: Vector
	n: Vector
	dispn: Vector
	dist: Vector
	cosc: Vector
	uvw: Vector
	delta: Vector
	lhit: Any
	ddu: Vector
	ddv: Vector
	raydepth: int
	calc_trans: int
	calc_refl: int
	calc_shadow: bool
	calc_illum: int
	calc_mip: int
	pp: Tuple[Vector, Vector, Vector]
	nn: Tuple[Vector, Vector, Vector]
	raybits: int
	recursion_id: int
	back_p: Vector
	back_delta: Vector
	global_mip: float
	sid: int
	par_u: float
	par_v: float

class VolumeData(BaseVolumeData):
	"""Base volume data information class."""
	def CalcArea(self, light: 'object', nodiffuse: 'bool', nospecular: 'bool', specular_exponent: 'float', ray_vector: 'Vector', p: 'Vector', bumpn: 'Vector', orign: 'Vector', raybits: 'int', ignoreLightColor: 'bool') -> 'Tuple[Vector, Vector]':
		"""Sample area lights."""
	def CalcFgBg(self, foreground: 'bool', x: 'int', y: 'int', subx: 'int', suby: 'int') -> 'Tuple[Vector, float]':
		"""Calculates the foreground or background."""
	def CalcShadow(self, l: 'object', p: 'Vector', bumpn: 'Vector', phongn: 'Vector', orign: 'Vector', rayv: 'Vector', transparency: 'bool', hitid: 'object', raybits: 'int') -> 'Vector':
		"""Computes the shadow."""
	def CalcVisibleLight(self, ray: 'Vector', maxdist: 'float') -> 'Tuple[Vector, Vector]':
		"""Return the mixed color of all visible lights on a given ray span."""
	def CameraToScreen(self, p: 'Vector') -> 'Vector':
		"""Transform screen to camera coordinates."""
	def CopyTo(self, dst: 'VolumeData') -> 'None':
		"""Copy this to another VolumeData."""
	def FindVideoPost(self, id: 'int') -> 'Optional[BaseList2D]':
		"""Returns a video post effect for this render process by ID."""
	def GetCPUCount(self) -> 'int':
		"""The cpu count."""
	def GetCurrentCPU(self) -> 'int':
		"""The current cpu."""
	def GetLight(self, index: 'int') -> 'object':
		"""Get the light source."""
	def GetLightCount(self) -> 'int':
		"""The light count."""
	def GetLightFalloff(self) -> 'None':
		"""Calculate the light falloff function."""
	def GetObjCount(self) -> 'int':
		"""The object count."""
	def GetRS(self, hitid: 'object', p: 'Vector') -> 'Tuple[bool, float, float]':
		"""Calculate the R/S parameters for a point."""
	def GetRay(self, x: 'float', y: 'float', ray: 'Ray') -> 'None':
		"""Generate the view ray for a position."""
	def GetSkyCount(self) -> 'int':
		"""The sky count."""
	def GetSmoothedNormal(self, hitid: 'object', p: 'Vector') -> 'Vector':
		"""Returns the phong normal for a point."""
	def GetVideoPost(self, nth: 'int') -> 'Optional[BaseList2D]':
		"""Returns the n-th video post effect for this render process."""
	def GetWeights(self, hitid: 'object', p: 'Vector') -> 'Tuple[float, float, float, float]':
		"""Returns barycentric coordinates for a point on the surface of a polygon."""
	def GetXY(self) -> 'Tuple[int, int, int]':
		"""Returns the current X/Y pixel position in render resolution."""
	def IlluminanceAnyPoint(self, p: 'Vector', flags: 'int', raybits: 'int') -> 'Vector':
		"""Used for custom illumination models."""
	def IlluminateSurfacePoint(self, rl: 'object', p: 'Vector', bumpn: 'Vector', phongn: 'Vector', orign: 'Vector', ray_vector: 'Vector', flags: 'int', hitid: 'object', raybits: 'int', cosine_cutoff: 'bool') -> 'Tuple[Vector, Vector]':
		"""Calculate the intensity of incoming light for a given light and surface point."""
	def Init(self, from_: 'VolumeData') -> 'None':
		"""Initializes the values of this object with values from another object."""
	def OutOfMemory(self) -> 'None':
		"""Notify on out of memory."""
	def ScreenToCamera(self, p: 'Vector') -> 'Vector':
		"""Transform camera to screen coordinates."""
	def SetXY(self, x: 'float', y: 'float') -> 'None':
		"""Sets the current X/Y pixel position."""
	def SkipRenderProcess(self) -> 'None':
		"""Skip the render process."""
	def StatusSetBar(self) -> 'None':
		"""Set the progress bar"""
	def StatusSetSpinMode(self, on: 'bool') -> 'None':
		"""Set the render progress bar spinning."""
	def StatusSetText(self, str: 'str') -> 'None':
		"""Set the status bar text"""

class ChannelData(object):
	"""Channel information class."""
	p: Vector
	n: Vector
	d: Vector
	t: float
	texflag: int
	vd: VolumeData
	off: float
	scale: float
	def __init__(self, t_vd: 'BaseVolumeData') -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class Ray(object):
	"""Ray class."""
	p: Vector
	v: Vector
	ior: float
	pp: Tuple[Vector, Vector, Vector]
	vv: Tuple[Vector, Vector, Vector]
	transport: Vector

class InitRenderStruct(object):
	"""InitRenderStruct class"""
	version: int
	time: BaseTime
	fps: int
	docpath: str
	vd: Optional[VolumeData]
	doc: Optional[BaseDocument]
	thread: Optional[BaseThread]
	flags: int
	linear_workflow: bool
	document_colorprofile: int
	def __init__(self, doc: 'Optional[BaseDocument]' = True) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""



