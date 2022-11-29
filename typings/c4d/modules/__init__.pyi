from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
if TYPE_CHECKING:
	from . import bodypaint, character, colorchooser, graphview, hair, mograph, motiontracker, net, particles, render, sculpting, snap, substance, takesystem, thinkingparticles, tokensystem, volume

import uuid
import c4d.modules.onlinehelp
import c4d.modules.character
import c4d.modules.mograph
import c4d.modules.net
import c4d.modules.hair
import c4d.modules.bodypaint
import c4d.modules.particles
import c4d.modules.thinkingparticles
import c4d.modules.render
import c4d.modules.sculpting
import c4d.modules.graphview
import c4d.modules.snap
import c4d.modules.takesystem
import c4d.modules.tokensystem
import c4d.modules.colorchooser
import c4d.modules.substance
import c4d.modules.motiontracker
import c4d.modules.volume


def CheckTP() -> bool:
	'''Check if 'Thinking Particles' is installed.'''
def CheckCA() -> bool:
	'''Check if 'Character Animation' is installed.'''
def CheckMoGraph() -> bool:
	'''Check if 'MoGraph' is installed.'''
def CheckAR() -> bool:
	'''Check if 'Advanced Render' is installed.'''
def CheckHair() -> bool:
	'''Check if 'Hair' is installed.'''
def CheckSketch() -> bool:
	'''Check if 'Sketch and Toon' is installed.'''
def CheckDynamics() -> bool:
	'''Check if 'Dynamics' is installed.'''
def CheckSculpting() -> bool:
	'''Check if 'Sculpting' is installed.'''
def CheckMotionTracker() -> bool:
	'''Check if 'Motion Tracker' is installed.'''

