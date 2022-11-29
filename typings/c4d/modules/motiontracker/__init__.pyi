from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseObject

class MotionTrackerObject(BaseObject):
	"""Motion Tracker object class."""
	def Get2dTrackData(self) -> 'Mt2dTrackData':
		"""Return 2d Tracking data."""
	def GetFootageData(self) -> 'MtFootageData':
		"""Return data about the footage."""

class MtFootageData(object):
	"""Motion Tracker Footage data."""
	def GetDownsamplingFactor(self) -> 'float':
		"""Return the footage downsampling ratio used for tracking."""
	def GetFirstFrameNumber(self) -> 'int':
		"""Return the first frame of the footage."""
	def GetFootageName(self) -> 'str':
		"""Return the footage filename."""
	def GetImageAspectRatio(self) -> 'float':
		"""Return the footage aspect ratio."""
	def GetLastFrameNumber(self) -> 'int':
		"""Return the last frame of the footage."""
	def GetPixelAspectRatio(self) -> 'float':
		"""Return the footage pixel aspect ratio."""
	def GetResolutionAspectRatio(self) -> 'float':
		"""Return the footage aspect ratio from the resolution."""
	def GetResolutionHeightPix(self, originalRes: 'int') -> 'int':
		"""Return the height in pixels of the footage."""
	def GetResolutionWidthPix(self, originalRes: 'int') -> 'int':
		"""Return the width in pixels of the footage."""

class Mt2dTrackData(object):
	"""Motion Tracker collection of 2d Tracks."""
	def GetTrackByGid(self, trkGid: 'MtTrkGid') -> 'Mt2dTrack':
		"""Return the track with the given global ID."""
	def GetTrackByIndex(self, index: 'int') -> 'Mt2dTrack':
		"""Return the track with the given index."""
	def GetTrackByName(self, name: 'str') -> 'Mt2dTrack':
		"""Return the track with the given name."""
	def GetTrackCount(self) -> 'int':
		"""Return the number of tracks."""
	def GetTrackIndices(self, userTracks: 'bool', autoTracks: 'bool') -> 'None':
		"""Return the indices of all tracks."""

class Mt2dTrack(object):
	"""Motion Tracker single 2d Track."""
	def GetDataForCurrentFrame(self) -> 'Optional[MtData]':
		"""Return the track data for the current frame."""
	def GetDataForFrame(self, frameNum: 'int') -> 'Optional[MtData]':
		"""Return the track data for given frame."""
	def GetFramesWithTrackData(self) -> 'None':
		"""Return the frames on which the track has data."""
	def GetId(self) -> 'MtTrkGid':
		"""Return the global ID of the track."""
	def GetName(self) -> 'str':
		"""Return the name of the track."""
	def GetStatus(self) -> 'int':
		"""Return the track status."""

class MtData(object):
	"""Motion Tracker 2d Track data for a single frame."""
	def GetCameraSpaceDirection(self, focalLength: 'float', sensorWidth: 'float') -> 'None':
		"""Return camera space ray corresponding to track position."""
	def GetNormalisedPosition(self) -> 'None':
		"""Return the track position in normalised coordinates"""
	def GetPixelPosition(self, footageData: 'MtFootageData', originalRes: 'int') -> 'None':
		"""Return the track position in pixel coordinates."""

class MtTrkGid(object):
	"""Motion Tracker global ID for a 2d Track."""
	def ToInt(self) -> 'int':
		"""Return the global ID value as an integer."""



