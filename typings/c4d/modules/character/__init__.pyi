from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import BaseTag, BaseObject
if TYPE_CHECKING:
	from c4d.documents import BaseDocument
	from c4d import Matrix, DescID, Vector, BaseList2D, BaseContainer

import c4d.modules.character.builder

class CAMorph(object):
	"""Morph object."""
	def Apply(self, doc: 'BaseDocument', tag: 'CAPoseMorphTag', flags: 'int') -> 'None':
		"""Apply."""
	def CopyFrom(self, src: 'CAMorph', trn: 'Optional[object]' = None, flags: 'Optional[int]' = None) -> 'bool':
		"""Copy data from a pose morph to another."""
	def FindIndex(self, tag: 'CAPoseMorphTag', bl: 'BaseList2D') -> 'int':
		"""Find the index."""
	def GetFirst(self) -> 'CAMorphNode':
		"""Returns the first morph node."""
	def GetID(self) -> 'int':
		"""Return the ID of a morph."""
	def GetName(self) -> 'str':
		"""Return the name of the morph."""
	def SetMode(self, doc: 'BaseDocument', tag: 'CAPoseMorphTag', flags: 'int', mode: 'int') -> 'int':
		"""SetMode"""
	def SetName(self, name: 'str') -> 'None':
		"""Set the name of a pose morph."""
	def Store(self, doc: 'BaseDocument', tag: 'CAPoseMorphTag', flags: 'int') -> 'None':
		"""Store."""

class CAWeightTag(BaseTag):
	"""Tag which contains weight information."""
	def AddJoint(self, op: 'BaseObject') -> 'int':
		"""Add a Joint object to the Weight tag's joint list."""
	def CalculateBoneStates(self, index: 'int') -> 'None':
		"""Helper function to initialize the Joint at index."""
	def FindJoint(self, op: 'BaseObject', doc: 'Optional[BaseDocument]' = None) -> 'None':
		"""Return the index of this object or NOTOK if not found."""
	def GetGeomMg(self) -> 'Matrix':
		"""Get the global matrix for the bind geometry."""
	def GetIndexWeight(self, index: 'int', windex: 'int') -> 'Tuple[int, int]':
		"""Get the windex weight."""
	def GetJoint(self, index: 'int', doc: 'Optional[BaseDocument]' = None) -> 'Optional[CAJointObject]':
		"""Get joint object at index."""
	def GetJointCount(self) -> 'int':
		"""Get total joint count."""
	def GetJointRestState(self, index: 'int') -> 'None':
		"""Get the rest state for the joint at index."""
	def GetWeight(self, index: 'int', pntindex: 'int') -> 'float':
		"""Return the weight for the point pntindex."""
	def GetWeightCount(self, index: 'int') -> 'int':
		"""Get total stored weights"""
	def GetWeightDirty(self) -> 'int':
		"""Get the dirty state of the weights."""
	def GetWeightMap(self, index: 'int', cnt: 'int', includeEffectors: 'bool' = False) -> 'List[float]':
		"""Retrieves the weights of a given joint index."""
	def RemoveJoint(self, op: 'BaseObject') -> 'None':
		"""Remove Joint object from the Weight tag's joints list."""
	def SetGeomMg(self, mg: 'Matrix') -> 'None':
		"""Set the global matrix for the bind geometry."""
	def SetJointRestState(self, index: 'int', m_bMg: 'Matrix', m_bMi: 'Matrix', m_oMg: 'Matrix', m_oMi: 'Matrix', m_Len: 'float') -> 'None':
		"""Set the rest state for the joint at index."""
	def SetWeight(self, index: 'int', pntindex: 'int', weight: 'float') -> 'bool':
		"""Set the weight for pntindex."""
	def SetWeightMap(self, index: 'int', map: 'List[float]') -> 'bool':
		"""Sets the weights of a given joint index with map."""
	def TransferWeightMap(self, doc: 'BaseDocument', dst: 'CAWeightTag', sindex: 'int', dindex: 'int', offset: 'int', cnt: 'int') -> 'None':
		"""Transfer the weights from one Weight tag to another."""
	def WeightDirty(self) -> 'None':
		"""Marks the weights dirty."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class CAWeightMgr(object):
	"""Weight Manager"""
	def ApplyWeightFunction(self, doc: 'BaseDocument', allPoints: 'BaseDocument' = False) -> 'bool':
		"""Applies a weight function on the weights of the selected joints."""
	def AutoWeight(self, doc: 'BaseDocument') -> 'bool':
		"""Runs the autoweight algorithm on the selected joints."""
	def BakeWeights(self, doc: 'BaseDocument', normalize: 'bool') -> 'bool':
		"""Bakes the effector weights on the selected joints."""
	def ClearWeights(self, doc: 'BaseDocument') -> 'bool':
		"""Clears the weights of the selected joints."""
	def CopyWeights(self, doc: 'BaseDocument') -> 'bool':
		"""Copies the weights of the selected joints into the weight clipboard."""
	def FlipWeights(self, doc: 'BaseDocument') -> 'bool':
		"""Flip the weights of the selected joints."""
	def GetAutoWeightAlgoId(self, doc: 'BaseDocument', index: 'int') -> 'maxon.Id':
		"""Get the autoweight algo id associated with the given index."""
	def GetAutoWeightAlgoIndex(self, doc: 'BaseDocument', stringId: 'maxon.Id') -> 'int':
		"""Get the autoweight algo index associated with the given id."""
	def GetAutoWeightDictionary(self, doc: 'BaseDocument', stringId: 'maxon.Id') -> 'maxon.DataDictionary':
		"""Grab the dictionary of the autoweight parameters."""
	def GetJointCount(self, doc: 'BaseDocument', tagIdx: 'int') -> 'int':
		"""Gets the joint count for a weight tag in the joint list."""
	def GetJointId(self, doc: 'BaseDocument', tag: 'CAWeightTag', joint: 'CAJointObject') -> 'int':
		"""Gets the unique joint identifier."""
	def GetJointIndex(self, doc: 'BaseDocument', tag: 'CAWeightTag', joint: 'CAJointObject') -> 'Tuple[int, int]':
		"""Gets the joint/tag index in the joint list."""
	def GetJointObject(self, doc: 'BaseDocument', tagIdx: 'int', jointIdx: 'int') -> 'Optional[CAJointObject]':
		"""Gets the joint object."""
	def GetMeshObject(self, doc: 'BaseDocument', tagIdx: 'int') -> 'Optional[BaseObject]':
		"""Gets a BaseObject from and joint list index."""
	def GetParameter(self, doc: 'BaseDocument', id: 'int') -> 'Optional[Any]':
		"""Gets a parameter in the Weight Manager plugin."""
	def GetTagCount(self, doc: 'BaseDocument') -> 'int':
		"""Gets the weight tag count in the joint list."""
	def GetTagIndex(self, doc: 'BaseDocument', tag: 'CAWeightTag') -> 'int':
		"""Gets the weight tag index in the joint list."""
	def GetWeightTag(self, doc: 'BaseDocument', tagIdx: 'int') -> 'Optional[CAWeightTag]':
		"""Gets a CAWeightTag from and joint list index."""
	def IsJointLocked(self, doc: 'BaseDocument', tagIdx: 'int', jointIdx: 'int') -> 'bool':
		"""Checks if the specified joint is locked."""
	def IsJointSelected(self, doc: 'BaseDocument', tagIdx: 'int', jointIdx: 'int') -> 'bool':
		"""Checks if the specified joint is selected."""
	def LockAllJoints(self, doc: 'BaseDocument') -> 'bool':
		"""Locks all joints in the weight manager."""
	def LockSelectedJoints(self, doc: 'BaseDocument') -> 'bool':
		"""Locks the selected joints in the weight manager."""
	def MirrorWeights(self, doc: 'BaseDocument') -> 'bool':
		"""Mirrors the weights of the selected joints."""
	def NormalizeWeights(self, doc: 'BaseDocument') -> 'bool':
		"""Normalizes the weights of the selected joints."""
	def PasteWeights(self, doc: 'BaseDocument', merge: 'bool') -> 'bool':
		"""Pastes the weights of the clipboard on the selected joints."""
	def SelectAllJoints(self, doc: 'BaseDocument') -> 'None':
		"""Selects all joints in the weight manager."""
	def SelectJoint(self, doc: 'BaseDocument', tagIdx: 'int', jointIdx: 'int') -> 'bool':
		"""Selects the specified joint in the weight manager."""
	def SetAutoWeightDictionary(self, doc: 'BaseDocument', dataDictionary: 'object', stringId: 'maxon.Id') -> 'bool':
		"""Set the dictionary of the autoweight parameters."""
	def SetDirty(self, doc: 'BaseDocument') -> 'bool':
		"""Set the Weight Manager dirty for the next update."""
	def SetParameter(self, doc: 'BaseDocument', id: 'int', newValue: 'object') -> 'bool':
		"""Sets a parameter in the Weight Manager plugin."""
	def SmoothWeights(self, doc: 'BaseDocument') -> 'bool':
		"""Smooths the weights of the selected joints."""
	def UnlockAllJoints(self, doc: 'BaseDocument') -> 'bool':
		"""Unlocks all joints in the weight manager."""
	def UnlockSelectedJoints(self, doc: 'BaseDocument') -> 'bool':
		"""Unlocks the selected joints in the weight manager."""
	def UnselectAllJointListNodes(self, doc: 'BaseDocument') -> 'None':
		"""Unselects all nodes in the weight manager joint list."""
	def UnselectAllJoints(self, doc: 'BaseDocument') -> 'None':
		"""Unselects all joints in the weight manager."""
	def UnselectJoint(self, doc: 'BaseDocument', tagIdx: 'int', jointIdx: 'int') -> 'bool':
		"""Unselects the specified joint in the weight manager."""
	def Update(self, doc: 'BaseDocument') -> 'bool':
		"""Updates the Weight Manager."""
	def ValidateJointIndex(self, doc: 'BaseDocument', tagIdx: 'int', jointIdx: 'int') -> 'bool':
		"""Validates a joint index tuple for Weight Manager list access."""

class CAJointObject(BaseObject):
	"""Joint object."""
	def GetBone(self) -> 'List[Matrix, float]':
		"""Get the bone data for this joint."""
	def GetWeightTag(self) -> 'None':
		"""Get the weight tag corresponding to this joint."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class CAPoseMorphTag(BaseTag):
	"""Tag which represents a morph tag."""
	def AddMorph(self) -> 'CAMorph':
		"""Add a new morph."""
	def ExitEdit(self, doc: 'BaseDocument', apply: 'bool') -> 'bool':
		"""Exit edit."""
	def GetActiveMorph(self) -> 'CAMorph':
		"""Gets the active morph"""
	def GetActiveMorphIndex(self) -> 'int':
		"""Return the active morph index."""
	def GetMode(self) -> 'int':
		"""Return the mode."""
	def GetMorph(self, index: 'int') -> 'CAMorph':
		"""Returns a morph by index."""
	def GetMorphBase(self) -> 'CAMorph':
		"""Return the morph base."""
	def GetMorphCount(self) -> 'int':
		"""Returns the count of morph objects."""
	def GetMorphID(self, index: 'int') -> 'DescID':
		"""Returns the description element of the morph."""
	def GetMorphIndex(self, morph: 'CAMorph') -> 'int':
		"""Retrieves the index for the given morph."""
	def GetMorphPSDID(self, morphIndex: 'int', psdAttributeID: 'int') -> 'DescID':
		"""Returns the description element of the PSD attribute."""
	def GetPSDFeedbackColor(self) -> 'Vector':
		"""Retrieves the PSD color used for feedback."""
	def GetPSDFeedbackColorEnabled(self) -> 'bool':
		"""Checks if PSD color feedback is enabled or disabled."""
	def GetPSDOrientThreshold(self) -> 'float':
		"""Retrieves the PSD orient radian threshold used in automatic weighting."""
	def GetPSDPositionThreshold(self) -> 'float':
		"""Retrieves the PSD position distance threshold used in automatic weighting."""
	def GetPSDTwistThreshold(self) -> 'float':
		"""Retrieves the PSD twist radian threshold used in automatic weighting."""
	def InitMorphs(self) -> 'None':
		"""Initialize the morph tag."""
	def RemoveMorph(self, index: 'int') -> 'None':
		"""Remove a morph by index."""
	def SetActiveMorphIndex(self, index: 'int') -> 'None':
		"""Set the active morph index."""
	def SetPSDFeedbackColor(self, color: 'Vector') -> 'bool':
		"""Sets the PSD color used for feedback."""
	def SetPSDFeedbackColorEnabled(self, active: 'bool') -> 'bool':
		"""Sets the enable/disable state of the PSD color used for feedback."""
	def SetPSDOrientThreshold(self, radianThreshold: 'float') -> 'bool':
		"""Sets the PSD orient radian threshold used in automatic weighting."""
	def SetPSDPositionThreshold(self, distanceThreshold: 'float') -> 'bool':
		"""Sets the PSD position distance threshold used in automatic weighting."""
	def SetPSDTwistThreshold(self, radianThreshold: 'float') -> 'bool':
		"""Sets the PSD twist radian threshold used in automatic weighting."""
	def UpdateMorphs(self) -> 'None':
		"""Update the morphs."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class CAMorphNode(object):
	"""Morph object."""
	def GetDown(self) -> 'Optional[CAMorphNode]':
		"""Return the first child morph node."""
	def GetInfo(self) -> 'int':
		"""Return the info."""
	def GetLink(self, tag: 'CAPoseMorphTag', morph: 'CAMorph', doc: 'BaseDocument') -> 'Optional[BaseList2D]':
		"""Retrieves the object linked to the morph node."""
	def GetNext(self) -> 'Optional[CAMorphNode]':
		"""Return the next morph node."""
	def GetP(self) -> 'Vector':
		"""Return the position vector."""
	def GetPSDReference(self) -> 'CAReferencePSD':
		"""Get the PSD Reference object."""
	def GetParam(self, index: 'int') -> 'None':
		"""Get the param."""
	def GetParamCount(self) -> 'int':
		"""Get the param count."""
	def GetPoint(self, index: 'int') -> 'Vector':
		"""Return a point."""
	def GetPointCount(self) -> 'int':
		"""Return the point count."""
	def GetPrev(self) -> 'Optional[CAMorphNode]':
		"""Return the previous morph node."""
	def GetR(self) -> 'Vector':
		"""Return the rotation vector."""
	def GetS(self) -> 'Vector':
		"""Return the scale vector."""
	def GetTangent(self, index: 'int') -> 'Vector':
		"""Return a tangent."""
	def GetTangentCount(self) -> 'int':
		"""Return the tangent count."""
	def GetUV(self, tindex: 'int', index: 'int') -> 'Tuple[Vector, Vector, Vector, Vector]':
		"""Get the uv."""
	def GetUVCount(self, tindex: 'int') -> 'int':
		"""Get the uv count."""
	def GetUVTagCount(self) -> 'int':
		"""Get the uv tag count."""
	def GetUp(self) -> 'Optional[CAMorphNode]':
		"""Return the parent morph node."""
	def GetVertexMap(self, tindex: 'int', index: 'int') -> 'float':
		"""Get the vertex map value."""
	def GetVertexMapCount(self, tindex: 'int') -> 'int':
		"""Return the vertexmap count."""
	def GetVertexMapTagCount(self) -> 'int':
		"""Return the vertexmap tag count."""
	def GetWeightMap(self, tindex: 'int', jindex: 'int', index: 'int') -> 'float':
		"""Get the weight map."""
	def GetWeightMapCount(self, tindex: 'int', jindex: 'int') -> 'int':
		"""Get the weight map joint count."""
	def GetWeightMapJointCount(self, tindex: 'int') -> 'int':
		"""Get the weight map joint count."""
	def GetWeightMapTagCount(self) -> 'int':
		"""Get the weight map tag count."""
	def SetParam(self, index: 'int', data: 'object', id: 'DescID') -> 'None':
		"""Set the param."""
	def SetParamCount(self, cnt: 'int') -> 'None':
		"""Get the param count."""
	def SetPoint(self, index: 'int', pnt: 'Vector') -> 'None':
		"""Set a point."""
	def SetPointCount(self, cnt: 'int') -> 'bool':
		"""Set the point count."""
	def SetTangent(self, index: 'int', v: 'Vector') -> 'None':
		"""Set a tangent."""
	def SetTangentCount(self, cnt: 'int') -> 'bool':
		"""Set the tangent count."""
	def SetUV(self, tindex: 'int', index: 'int', a: 'Vector', b: 'Vector', c: 'Vector', d: 'Vector') -> 'None':
		"""Set the uv."""
	def SetUVCount(self, tindex: 'int', cnt: 'int') -> 'bool':
		"""Set the uv count."""
	def SetVertexMap(self, tindex: 'int', index: 'int', v: 'float') -> 'None':
		"""Set the vertex mal value."""
	def SetVertexMapTagCount(self, tindex: 'int', cnt: 'int') -> 'bool':
		"""Return the vertexmap count."""
	def SetWeightMap(self, tindex: 'int', jindex: 'int', index: 'int', v: 'float') -> 'None':
		"""Set the weight map."""
	def SetWeightMapCount(self, tindex: 'int', jindex: 'int', cnt: 'int') -> 'bool':
		"""Set the weight map joint count."""

class CAReferencePSD(object):
	"""PSD object"""
	def ClearAllExternalControllers(self) -> 'None':
		"""Removes all external controllers assigned to the reference pose."""
	def ClearAllForcedDrivers(self) -> 'None':
		"""Removes all user defined joint as driver and let the system manage it automatically."""
	def ForceJointAsDriver(self, jointIndex: 'int', forceDriver: 'bool') -> 'None':
		"""Forces the joint index to be a driver."""
	def GetExternalController(self, controllerIndex: 'int') -> 'Optional[BaseObject]':
		"""Returns the controller assigned to the given index."""
	def GetExternalControllerCount(self) -> 'int':
		"""Return the number of external controllers associated with the reference pose."""
	def GetExternalControllerMatrix(self, controllerIndex: 'int') -> 'Matrix':
		"""Returns the matrix stored at the given index."""
	def GetInterpolationMode(self) -> 'int':
		"""Returns the auto weighting interpolation mode."""
	def IsJointForcedAsDriver(self, jointIndex: 'int') -> 'bool':
		"""Checks if the joint index is a user forced driver"""
	def RemoveExternalController(self, controllerIndex: 'int') -> 'bool':
		"""Removes the controller at the given index."""
	def RestoreReferencePose(self) -> 'None':
		"""Displays skeleton and user defined controller at the reference pose."""
	def SetExternalControllerMatrix(self, controllerIndex: 'int', globalMatrix: 'Matrix') -> 'int':
		"""Adds or adjusts the given controller global matrix to be part of the reference pose."""
	def SetInterpolationMode(self, interpMode: 'int') -> 'None':
		"""Sets the auto weighting interpolation mode."""
	def UpdateReferencePose(self) -> 'None':
		"""Updates the current skeleton state as the PSD reference pose."""

class MTBodyPartParameters(object):
	"""Handle type."""
	_identifier: InternedId
	_name: str
	_skeletonNodes: List[BaseList2D]
	_controllerNodes: List[BaseList2D]
	_skeletonKeywords: List[str]
	_skeletonDiscardKeywords: List[str]
	_transferPosition: bool
	_transferRotation: bool
	_transferScale: bool
	_exposeInSolver: bool
	_transferUserData: bool
	_transferUserDataMode: int
	def CopyFrom(self, src: 'object') -> 'None':
		"""Copy all the data of the source MTBodyPartParameters object"""

class MTCharacterBodyPart(object):
	"""MTCharacterBodyPart type."""
	def DeleteChild(self, index: 'int') -> 'bool':
		"""Deletes the child at the given index."""
	def GetChild(self, index: 'int') -> 'None':
		"""Gets the child at the given index."""
	def GetChildCount(self) -> 'int':
		"""Gets the child at the given index."""
	def GetParameters(self) -> 'None':
		"""Gets the parameters structure."""
	def GetParent(self) -> 'None':
		"""Gets the parent if any."""
	def InsertChild(self, child: 'object') -> 'bool':
		"""Inserts the given child."""
	def SetParameters(self, param: 'object') -> 'None':
		"""Sets the parameter for the body part."""

class MTCharacterDefinitionTag(BaseTag):
	"""Represents the Character Definition tag."""
	def ApplyRestPose(self, undo: 'bool') -> 'bool':
		"""Applies the current rest pose."""
	def ClearRestPose(self, undo: 'bool') -> 'bool':
		"""Clears the current rest pose."""
	def CreateSolver(self, undo: 'bool') -> 'None':
		"""Creates a solver and assign to the object owner."""
	def ExtractRestPose(self, undo: 'bool') -> 'bool':
		"""Gets current skeleton pose and set it as rest pose."""
	def ExtractSkeleton(self, undo: 'bool') -> 'bool':
		"""Automatic body part extraction for the skeleton."""
	def GetRootBodyPart(self) -> 'None':
		"""Returns a copy of the body part hierarchy."""
	def SetRootBodyPart(self, rootBodyPart: 'object') -> 'bool':
		"""Sets the body part hierarchy."""

class MTCharacterMotionTransferTag(BaseTag):
	"""Represents the Character Definition tag."""
	def GetExposedBodyPartSettings(self, bodyPartIdentifier: 'object') -> 'BaseContainer':
		"""Returns BaseContainer containing the solver settings for the given identifier."""
	def SetExposedBodyPartSettings(self, bodyPartSettings: 'BaseContainer') -> 'None':
		"""Sets body part solver settings for an exposed body part."""



import maxon
