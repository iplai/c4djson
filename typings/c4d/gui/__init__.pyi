"""A module to create custom dialogs."""

from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING
from c4d import Vector, DescID, GEMB_OK, POPUP_RIGHT, POPUP_EXECUTECOMMANDS, USERAREAFLAGS_COREMESSAGE, BFH_FIT, TAB_TABS, MINLONGl, MAXLONGl, FORMAT_FLOAT, MAXTIME, DRAWTEXT_STD_ALIGN, NOTOK, LINESTYLE_NORMAL, FONT_STANDARD
if TYPE_CHECKING:
	from c4d import BaseContainer, BaseTime, BaseList2D, C4DAtom, SplineData, Gradient, BaseObject, DateTimeData, IconData
	from c4d.plugins import GeResource
	from c4d.documents import BaseDocument
	from c4d.bitmaps import BaseBitmap
	from c4d.storage import MemoryFileStruct


class GeDialog(object):
	"""Used to display GUI dialogs."""
	def Activate(self, id: 'int') -> 'bool':
		"""Enables a gadget."""
	def AddButton(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0, name: 'str' = '') -> 'C4DGadget':
		"""Creates a button."""
	def AddCheckbox(self, id: 'int', flags: 'int', initw: 'int', inith: 'int', name: 'str') -> 'C4DGadget':
		"""Creates a checkbox."""
	def AddChild(self, id: 'Union[C4DGadget, int]', subid: 'int', child: 'str') -> 'bool':
		"""Creates a child to a parent gadget."""
	def AddChildren(self, id: 'int', bc: 'BaseContainer') -> 'bool':
		"""Adds children to a dialog element using a container."""
	def AddColorChooser(self, id: 'int', flags: 'int', initw: 'int' = 80, inith: 'int' = 0, layoutflags: 'int' = False, settings: 'Optional[BaseContainer]' = None) -> 'C4DGadget':
		"""Creates a simple color chooser."""
	def AddColorField(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0, colorflags: 'int' = 0) -> 'C4DGadget':
		"""CAdds a simple color field."""
	def AddComboBox(self, id: 'int', flags: 'int', initw: 'int' = 80, inith: 'int' = 0, specialalign: 'bool' = False, allowfiltering: 'bool' = False) -> 'C4DGadget':
		"""Creates a combobox."""
	def AddCustomGui(self, id: 'int', pluginid: 'int', name: 'str', flags: 'int', minw: 'int', minh: 'int', customdata: 'BaseContainer') -> 'Optional[BaseCustomGui]':
		"""Add a custom gui gadget."""
	def AddDlgGroup(self, type: 'int') -> 'bool':
		"""Adds a dialog group with standard buttons to the layout."""
	def AddEditNumber(self, id: 'int', flags: 'int', initw: 'int' = 80, inith: 'int' = 0) -> 'C4DGadget':
		"""Creates a numberfield."""
	def AddEditNumberArrows(self, id: 'int', flags: 'int', initw: 'int' = 70, inith: 'int' = 0) -> 'C4DGadget':
		"""Creates a numberfield with arrows."""
	def AddEditSlider(self, id: 'int', flags: 'int', initw: 'int' = 80, inith: 'int' = 0) -> 'C4DGadget':
		"""Creates a slider to the layout."""
	def AddEditText(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0, editflags: 'int' = 0) -> 'C4DGadget':
		"""Creates a textbox."""
	def AddGadget(self, type: 'int', gadget: 'int') -> 'bool':
		"""Add a gadget."""
	def AddMultiLineEditText(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0, style: 'int' = 0) -> 'C4DGadget':
		"""Creates a multiline textarea."""
	def AddPopupButton(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0) -> 'C4DGadget':
		"""Creates a popup button."""
	def AddRadioButton(self, id: 'int', flags: 'int', initw: 'int' = 80, inith: 'int' = 0, name: 'str' = '') -> 'C4DGadget':
		"""Creates a radio button."""
	def AddRadioGroup(self, id: 'int', flags: 'int' = 0, columns: 'int' = 0, rows: 'int' = 0) -> 'bool':
		"""Creates a radio group."""
	def AddRadioText(self, id: 'int', flags: 'int', initw: 'int' = 80, inith: 'int' = 0, name: 'str' = '') -> 'C4DGadget':
		"""Creates a radio text."""
	def AddSeparatorH(self, initw: 'int', flags: 'int' = 24) -> 'C4DGadget':
		"""Creates a separator."""
	def AddSeparatorV(self, inith: 'int', flags: 'int' = 24) -> 'C4DGadget':
		"""Creates a separator."""
	def AddSlider(self, id: 'int', flags: 'int', initw: 'int' = 90, inith: 'int' = 0) -> 'C4DGadget':
		"""Creates a slider with an number field."""
	def AddStaticText(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0, name: 'str' = '', borderstyle: 'int' = 0) -> 'C4DGadget':
		"""Creates a static text."""
	def AddSubDialog(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0) -> 'bool':
		"""Adds a sub-dialog to the layout."""
	def AddUserArea(self, id: 'int', flags: 'int', initw: 'int' = 0, inith: 'int' = 0) -> 'C4DGadget':
		"""Adds a sub dialog to the layout."""
	def AskClose(self) -> 'bool':
		"""Called when dialog is about to close."""
	def AttachSubDialog(self, userdlg: 'SubDialog', id: 'int') -> 'bool':
		"""Attaches a sub-dialog."""
	def AttachUserArea(self, ua: 'GeUserArea', id: 'Union[C4DGadget, int]', userareaflags: 'int' = 4) -> 'bool':
		"""Assigns a GeUserArea object to a user area."""
	def CheckDropArea(self, id: 'int', msg: 'BaseContainer', horiz: 'bool', vert: 'bool') -> 'bool':
		"""Checks the drag position in a drag event message."""
	def CheckTristateChange(self, id: 'Union[C4DGadget, int]') -> 'bool':
		"""Check if a value has been changed since it was set manually."""
	def CheckValueRanges(self) -> 'bool':
		"""Checks whether all input fields."""
	def Close(self) -> 'bool':
		"""Close the Dialog."""
	def Command(self, id: 'int', msg: 'BaseContainer') -> 'bool':
		"""Called on each command."""
	def CoreMessage(self, id: 'int', msg: 'BaseContainer') -> 'bool':
		"""Called on core messages."""
	def CreateLayout(self) -> 'bool':
		"""Called to create a dialog."""
	def DestroyWindow(self) -> 'None':
		"""Called when the dialog closes."""
	def Enable(self, gadget: 'object', enable: 'bool') -> 'None':
		"""Enables a gadget."""
	def FindCustomGui(self, id: 'int', pluginid: 'int') -> 'Optional[BaseCustomGui]':
		"""Find a custom gui gadget."""
	def FreeChildren(self, id: 'Union[C4DGadget, int]') -> 'bool':
		"""Clears the item list of combo boxes and popup buttons."""
	def GetBool(self, id: 'Union[C4DGadget, int]') -> 'Optional[bool]':
		"""Retrieves the value of bool fields."""
	def GetColorField(self, id: 'Union[C4DGadget, int]') -> 'None':
		"""Retrieves the value of color fields."""
	def GetColorRGB(self, colorid: 'int') -> 'None':
		"""Gets the RGB values."""
	def GetDragObject(self, msg: 'BaseContainer') -> 'None':
		"""A convenience function to extract the data from a drag and drop message."""
	def GetDragPosition(self, msg: 'BaseContainer') -> 'None':
		"""A convenience function to extract local drag coordinates from a drag and drop event."""
	def GetFilename(self, id: 'Union[C4DGadget, int]') -> 'Optional[str]':
		"""Retrieves the value of filename fields."""
	def GetFloat(self, id: 'Union[C4DGadget, int]') -> 'Optional[float]':
		"""Retrieves the value of float fields."""
	def GetFolding(self) -> 'bool':
		"""Retrieve if the dialog is open but currently folded away in the layout."""
	def GetId(self) -> 'int':
		"""Gets the dialog ID."""
	def GetInputEvent(self, askdevice: 'int', res: 'BaseContainer') -> 'bool':
		"""Gets the next input event."""
	def GetInputState(self, askdevice: 'int', askchannel: 'int', res: 'BaseContainer') -> 'bool':
		"""Polls a certain channel of a device."""
	def GetInt32(self, id: 'Union[C4DGadget, int]') -> 'Optional[int]':
		"""Retrieves the value of integer fields."""
	def GetItemDim(self, id: 'Union[C4DGadget, int]') -> 'None':
		"""Queries a dialog control for its current size and position in pixels."""
	def GetLong(self, id: 'Union[C4DGadget, int]') -> 'Optional[int]':
		"""Retrieves the value of integer fields."""
	def GetReal(self, id: 'Union[C4DGadget, int]') -> 'Optional[float]':
		"""Retrieves the value of float fields."""
	def GetString(self, id: 'Union[C4DGadget, int]') -> 'Optional[str]':
		"""Retrieves the value of string fields."""
	def GetTime(self, id: 'Union[C4DGadget, int]', doc: 'BaseDocument') -> 'Optional[BaseTime]':
		"""Retrieves the value of time fields."""
	def GetType(self, id: 'int') -> 'int':
		"""Returns the type of the element."""
	def GetVector(self, id_x: 'Union[C4DGadget, int]', id_y: 'Union[C4DGadget, int]', id_z: 'Union[C4DGadget, int]') -> 'Optional[Vector]':
		"""Retrieves the value of Vector fields."""
	def GetVisibleArea(self, scrollgroup: 'int') -> 'None':
		"""Queries a scroll group."""
	def Global2Local(self) -> 'None':
		"""Transforms global coordinates."""
	def GroupBegin(self, id: 'int', flags: 'int', cols: 'int' = 0, rows: 'int' = 0, title: 'str' = '', groupflags: 'int' = 0, initw: 'int' = 0, inith: 'int' = 0) -> 'bool':
		"""Begins a group."""
	def GroupBeginInMenuLine(self) -> 'None':
		"""Begins a group in the menu bar."""
	def GroupBorder(self, borderstyle: 'int') -> 'None':
		"""Sets the border type with title."""
	def GroupBorderNoTitle(self, borderstyle: 'int') -> 'None':
		"""Sets the border type without title."""
	def GroupBorderSpace(self, left: 'int', top: 'int', right: 'int', bottom: 'int') -> 'bool':
		"""Sets the border size around the current group."""
	def GroupEnd(self) -> 'bool':
		"""Close a group."""
	def GroupSpace(self, spacex: 'int', spacey: 'int') -> 'bool':
		"""Sets the space in pixels."""
	def GroupWeightsLoad(self, id: 'Union[C4DGadget, int]', weights: 'BaseContainer') -> 'bool':
		"""Load the weight of a group."""
	def GroupWeightsSave(self, id: 'Union[C4DGadget, int]') -> 'Optional[BaseContainer]':
		"""Set the weight of a group."""
	def HideElement(self, id: 'int', hide: 'bool') -> 'bool':
		"""Hides a gadget."""
	def InitValues(self) -> 'bool':
		"""Called to init values."""
	def IsActive(self, id: 'int') -> 'bool':
		"""Checks if a gadget has the focus."""
	def IsOpen(self) -> 'bool':
		"""Checks if the dialog is open."""
	def IsVisible(self) -> 'bool':
		"""Checks if the dialog is visible."""
	def KillEvents(self) -> 'None':
		"""Flushes all events."""
	def LayoutChanged(self, id: 'int') -> 'bool':
		"""Tell C4D the group content has changed."""
	def LayoutChangedNoRedraw(self, id: 'Union[C4DGadget, int]') -> 'bool':
		"""Tell C4D the group content has changed."""
	def LayoutFlushGroup(self, id: 'int') -> 'bool':
		"""Flush all elements in a group."""
	def LoadDialogResource(self, id: 'int', lr: 'Optional[GeResource]' = None, flags: 'Optional[int]' = 0) -> 'bool':
		"""Loads a dialog."""
	def Local2Global(self) -> 'None':
		"""Transforms local coordinates."""
	def Local2Screen(self) -> 'None':
		"""Transforms local coordinates."""
	def MenuAddCommand(self, cmdid: 'int') -> 'bool':
		"""Adds a command item."""
	def MenuAddSeparator(self) -> 'bool':
		"""Adds a separator to the menu."""
	def MenuAddString(self, id: 'int', string: 'str') -> 'bool':
		"""Set a menu item."""
	def MenuFinished(self) -> 'bool':
		"""Call when menu has been added."""
	def MenuFlushAll(self) -> 'bool':
		"""Flushes the menu bar of."""
	def MenuInitString(self, id: 'int', enabled: 'bool', value: 'bool') -> 'bool':
		"""Change menu item state."""
	def MenuSubBegin(self, string: 'str') -> 'bool':
		"""Begin a menu."""
	def MenuSubEnd(self) -> 'bool':
		"""Closes the current menu group."""
	def Message(self, msg: 'BaseContainer', result: 'BaseContainer') -> 'int':
		"""Called on each message."""
	def Open(self, dlgtype: 'int', pluginid: 'int' = 0, xpos: 'int' = -1, ypos: 'int' = -1, defaultw: 'int' = 0, defaulth: 'int' = 0, subid: 'int' = 0) -> 'bool':
		"""Opens the dialog."""
	def RemoveElement(self, id: 'int') -> 'bool':
		"""Removes a gadget."""
	def Restore(self, pluginid: 'int', secret: 'object') -> 'bool':
		"""Used to restore an asynchronous dialog."""
	def Screen2Local(self) -> 'None':
		"""Transforms screen coordinates."""
	def ScrollGroupBegin(self, id: 'int', flags: 'int', scrollflags: 'int', initw: 'int' = 0, inith: 'int' = 0) -> 'bool':
		"""Begins a scrollable group."""
	def SendMessage(self, id: 'Union[C4DGadget, int]', value: 'BaseContainer') -> 'object':
		"""Send a message to the dialog."""
	def SendParentMessage(self, msg: 'BaseContainer') -> 'bool':
		"""Sends a message to the parent dialog."""
	def SetBool(self, id: 'Union[C4DGadget, int]', value: 'bool') -> 'bool':
		"""Set the value of checkboxes."""
	def SetColorField(self, id: 'Union[C4DGadget, int]', color: 'Vector', brightness: 'float', maxbrightness: 'float', flags: 'int') -> 'bool':
		"""Set for color fields."""
	def SetDefaultColor(self, id: 'Union[C4DGadget, int]', colorid: 'int', color: 'Vector') -> 'None':
		"""Set the default color for GUI elements."""
	def SetDegree(self, id: 'Union[C4DGadget, int]', value: 'float', min: 'int' = 2.2250738585072014e-308, max: 'int' = 1.7976931348623157e+308, step: 'float' = 1.0, tristate: 'bool' = False) -> 'bool':
		"""Set for float fields."""
	def SetDragDestination(self, cursor: 'int', gadgetid: 'int' = 0) -> 'bool':
		"""Sets the correct cursor during drag and drop handling."""
	def SetFilename(self, id: 'Union[C4DGadget, int]', fn: 'str', tristate: 'bool' = False) -> 'bool':
		"""Set for fielanem fields."""
	def SetFloat(self, id: 'Union[C4DGadget, int]', value: 'float', min: 'int' = 2.2250738585072014e-308, max: 'int' = 1.7976931348623157e+308, step: 'float' = 1.0, format: 'int' = 1718773089, min2: 'int' = 0.0, max2: 'int' = 0.0, quadscale: 'bool' = False, tristate: 'bool' = False) -> 'bool':
		"""Set for float fields."""
	def SetFolding(self, allowClose: 'bool') -> 'None':
		"""Fold the dialog away in the layout."""
	def SetInt32(self, id: 'Union[C4DGadget, int]', value: 'int', min: 'int' = -2147483647, max: 'int' = 2147483647, step: 'bool' = 1, tristate: 'object' = False, min2: 'int' = -2147483647, max2: 'int' = 2147483647) -> 'bool':
		"""Set for integer fields."""
	def SetLong(self, id: 'Union[C4DGadget, int]', value: 'int', min: 'int' = -2147483647, max: 'int' = 2147483647, step: 'bool' = 1, tristate: 'object' = False, min2: 'int' = -2147483647, max2: 'int' = 2147483647) -> 'bool':
		"""Set for integer fields."""
	def SetMeter(self, id: 'Union[C4DGadget, int]', value: 'float', min: 'int' = 2.2250738585072014e-308, max: 'int' = 1.7976931348623157e+308, step: 'float' = 1.0, tristate: 'bool' = False) -> 'bool':
		"""Set for float fields."""
	def SetMultiLineMode(self, id: 'Union[C4DGadget, int]', mode: 'int') -> 'bool':
		"""Set the multiline mode for a gadget."""
	def SetMultiLinePos(self, id: 'Union[C4DGadget, int]', line: 'int', pos: 'int') -> 'bool':
		"""Set the cursor position of the text field."""
	def SetPercent(self, id: 'Union[C4DGadget, int]', value: 'float', min: 'int' = 0.0, max: 'int' = 100.0, step: 'float' = 1.0, tristate: 'bool' = False) -> 'bool':
		"""Set for float fields."""
	def SetPopup(self, id: 'Union[C4DGadget, int]', bc: 'BaseContainer') -> 'bool':
		"""Sets the item list of a popup button using a container."""
	def SetReal(self, id: 'Union[C4DGadget, int]', value: 'float', min: 'int' = 2.2250738585072014e-308, max: 'int' = 1.7976931348623157e+308, step: 'float' = 1.0, format: 'int' = 1718773089, min2: 'int' = 0.0, max2: 'int' = 0.0, quadscale: 'bool' = False, tristate: 'bool' = False) -> 'bool':
		"""Set for float fields."""
	def SetString(self, id: 'Union[C4DGadget, int]', value: 'str', tristate: 'bool' = False, flags: 'int' = 0) -> 'bool':
		"""Set for string fields."""
	def SetTime(self, id: 'Union[C4DGadget, int]', doc: 'object', value: 'BaseTime', min: 'BaseTime' = -108000, max: 'BaseTime' = 108000, stepframes: 'int' = 1, tristate: 'bool' = False) -> 'bool':
		"""Set for time fields."""
	def SetTimer(self, value: 'int') -> 'None':
		"""Initializes the timer clock."""
	def SetTitle(self, title: 'str') -> 'None':
		"""Sets the title of the dialog window."""
	def SetVisibleArea(self, scrollgroupid: 'int', x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'bool':
		"""Scrolls a scroll group."""
	def TabGroupBegin(self, id: 'int', flags: 'int', tabtype: 'int' = 0) -> 'bool':
		"""Begins a tabbed group."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class SubDialog(GeDialog):
	"""Used to display GUI dialogs."""
	def Open(self, dlgtype: 'int', pluginid: 'int' = 0, xpos: 'int' = -1, ypos: 'int' = -1, defaultw: 'int' = 0, defaulth: 'int' = 0, subid: 'int' = 0, flags: 'int' = 0) -> 'bool':
		"""Opens the dialog."""

class LinkBoxGui(BaseCustomGui):
	"""LinkBoxGui - Dialog element."""
	def GetLink(self, doc: 'BaseDocument', instance: 'int') -> 'Optional[BaseList2D]':
		"""Get a link."""
	def SetLink(self, obj: 'BaseList2D') -> 'bool':
		"""Set a link."""

class C4DGadget(object):
	"""C4DGadget - Dialog element."""

class BaseCustomGui(object):
	"""BaseCustomGui - Base class for custom GUIs."""
	def Activate(self) -> 'bool':
		"""Activates the custom GUI."""
	def GetData(self) -> 'Any':
		"""Retrieves the custom GUI data to tristate."""
	def GetHeight(self) -> 'int':
		"""Retrieves the height of the custom GUI in pixels."""
	def GetLayoutMode(self) -> 'int':
		"""Retrieves the layout mode."""
	def GetWidth(self) -> 'int':
		"""Retrieves the width of the custom GUI in pixels."""
	def LayoutChanged(self) -> 'bool':
		"""Tells the custom GUI that the layout has changed."""
	def Redraw(self) -> 'None':
		"""Redraws the custom GUI."""
	def SetData(self, data: 'object') -> 'bool':
		"""Sets the custom GUI data."""
	def SetDefaultForResEdit(self) -> 'bool':
		"""Sets the custom GUI to the resource editor defaults."""
	def SetLayoutMode(self, mode: 'int') -> 'None':
		"""Sets the layout mode."""
	def SupportLayoutSwitch(self) -> 'bool':
		"""Checks if the custom GUI supports layout switching."""

class InExcludeCustomGui(BaseCustomGui):
	"""InExcludeCustomGui - InExclude custom GUI."""

class HtmlViewerCustomGui(BaseCustomGui):
	"""TreeView gadget - Dialog element."""
	def DoAction(self, action: 'int') -> 'None':
		"""Do an action in the HTML viewer."""
	def SetText(self, url: 'str') -> 'None':
		"""Set the HTML viewer text."""
	def SetURLCallback(self, callback: 'object', user_data: 'Optional[object]' = None) -> 'None':
		"""Set the URL callback."""
	def SetUrl(self, url: 'str', encoding: 'int') -> 'None':
		"""Set the HTML viewer URL."""

class SplineCustomGui(BaseCustomGui):
	"""SplineDialogGadget - Dialog element."""
	def GetGridLineCountH(self) -> 'int':
		"""Get the horizontal grid line count."""
	def GetGridLineCountV(self) -> 'int':
		"""Set the vertical grid line count."""
	def GetScreenPosition(self, v: 'Vector') -> 'Tuple[float, float]':
		"""Get the screen coordinates."""
	def GetSplineData(self) -> 'SplineData':
		"""Returns the SplineData."""
	def GetValue(self, x: 'int', y: 'int') -> 'Vector':
		"""Get the value."""
	def SetCustomColor(self, bSet: 'bool' = False, col: 'Vector' = None) -> 'None':
		"""Set custom color for the spline gui."""
	def SetGridLineCountH(self, l: 'int') -> 'None':
		"""Set the horizontal grid line count."""
	def SetGridLineCountV(self, l: 'int') -> 'None':
		"""Set the vertical grid line count."""
	def SetSpline(self, data: 'SplineData') -> 'bool':
		"""Set SplineData."""

class SoundEffectorCustomGui(BaseCustomGui):
	"""SoundEffectorDialogGadget - Dialog element."""
	def GetGUIOwnerOverride(self, doc: 'BaseDocument') -> 'Optional[BaseList2D]':
		"""Get GUI Owner Override."""
	def SetGUIOwnerOverride(self, bl: 'BaseList2D') -> 'bool':
		"""Set GUI Owner Override."""

class TreeViewCustomGui(BaseCustomGui):
	"""TreeView gadget - Dialog element."""
	def GetVisibleLineCount(self) -> 'int':
		"""Gets the number of currently visible lines related to folded and unfolded items of the tree."""
	def GetVisibleScrollArea(self) -> 'Tuple[int, int, int, int]':
		"""Queries the internal scroll group for its currently visible region."""
	def IsFocusItem(self, pItem: 'object') -> 'bool':
		"""Checks if object is the focus item."""
	def MakeVisible(self, pObj: 'object') -> 'bool':
		"""Scrolls to object and expands the tree if necessary."""
	def Refresh(self) -> 'None':
		"""Refresh the treeview."""
	def SetFocusItem(self, pItem: 'object') -> 'None':
		"""Sets the focus item."""
	def SetHeaderText(self, lColumnID: 'int', str: 'str') -> 'bool':
		"""Set the header text for a column."""
	def SetLayout(self, columns: 'int', data: 'BaseContainer') -> 'bool':
		"""Set the layout."""
	def SetRoot(self, root: 'object', functions: 'TreeViewFunctions', userdata: 'object') -> 'bool':
		"""Set the root."""
	def SetVisibleScrollArea(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'bool':
		"""Sets the internal scroll group currently visible region."""
	def ShowObject(self, pObj: 'object') -> 'bool':
		"""Expands the tree."""

class GradientCustomGui(BaseCustomGui):
	"""Gradient gadget - Dialog element."""
	def GetGradient(self) -> 'Gradient':
		"""Returns the Gradient"""
	def SetGradient(self, data: 'Gradient') -> 'bool':
		"""Set Gradient"""

class DescriptionCustomGui(BaseCustomGui):
	"""DescriptionCustomGui - Dialog element."""
	def SetObject(self, op: 'BaseObject') -> 'None':
		"""Sets a single objects to show."""

class BitmapButtonCustomGui(BaseCustomGui):
	"""BitmapButtonCustomGui - Dialog element."""
	def SetCommandDragId(self, cmdid: 'int') -> 'None':
		"""Sets a command ID for the bitmap button."""
	def SetImage(self, obj: 'Union[str, BaseBitmap, Dict[str, object], IconData]', copybmp: 'bool' = True, secondstate: 'bool' = False) -> 'bool':
		"""Sets the image."""
	def SetToggleState(self, set: 'bool') -> 'None':
		"""Sets the toggle state of the button."""
	def SetTooltip(self, tooltip: 'str') -> 'None':
		"""Sets the tooltip string of the button."""

class QuickTabCustomGui(BaseCustomGui):
	"""QuickTabCustomGui - Dialog element."""
	def AppendString(self, id: 'int', str: 'str', checked: 'bool') -> 'None':
		"""Appends a string."""
	def ClearStrings(self) -> 'None':
		"""Removes all strings."""
	def DoLayoutChange(self) -> 'None':
		"""Removes all strings."""
	def IsSelected(self, id: 'int') -> 'bool':
		"""Checks if a string is selected."""
	def Select(self, id: 'int', b: 'bool') -> 'bool':
		"""Change the selection state."""
	def SetLayerColor(self, id: 'int', show: 'bool', col: 'Vector') -> 'None':
		"""Set the layer color."""
	def SetTextColor(self, id: 'int', col: 'int') -> 'None':
		"""Set the text color."""

class DateTimeControl(BaseCustomGui):
	"""DateTimeControl gadget - Dialog element."""
	def GetDateTime(self) -> 'DateTimeData':
		"""Returns the datetime."""
	def SetDateTime(self, d: 'DateTimeData', bSetData: 'bool' = True, bSetTime: 'bool' = True) -> 'None':
		"""Set the datetime."""

class TreeViewFunctions(object):
	"""TreeViewFunctions Class"""

class GeUserArea(object):
	"""Used to create custom GUI components."""
	def ActivateFading(self, milliseconds: 'int') -> 'None':
		"""Activates fading for the user area."""
	def AdjustColor(self, colorid: 'int', highlightid: 'int', percent: 'float') -> 'None':
		"""Adjusts the fading color."""
	def CheckDropArea(self, msg: 'BaseContainer', horiz: 'bool', vert: 'bool') -> 'bool':
		"""Checks the drag position in a drag event message."""
	def ClearClippingRegion(self) -> 'None':
		"""Clears any clipping region."""
	def CoreMessage(self, id: 'int', msg: 'BaseContainer') -> 'bool':
		"""Called when a C4D core messages is received."""
	def DrawBezier(self, sx: 'float', sy: 'float', p: 'List[float]', closed: 'bool', filled: 'bool') -> 'None':
		"""Draws a bezier curve."""
	def DrawBezierFill(self, startPoint: 'List[float]', bezierPoints: 'List[float]', closed: 'bool') -> 'None':
		"""Draws a bezier curve filled."""
	def DrawBezierLine(self, startPoint: 'List[float]', bezierPoints: 'List[float]', closed: 'bool', lineWidth: 'float' = 1.0, lineStyle: 'int' = 0) -> 'None':
		"""Draws a bezier curve contour."""
	def DrawBitmap(self, bmp: 'BaseBitmap', wx: 'int', wy: 'int', ww: 'int', wh: 'int', x: 'int', y: 'int', w: 'int', h: 'int', mode: 'int') -> 'None':
		"""Draws a bitmap in the area."""
	def DrawBorder(self, type: 'int', x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draws a border."""
	def DrawCustomButton(self, x: 'int', y: 'int', w: 'int', h: 'int', ids: 'List[int]', nofill: 'bool', focus: 'object') -> 'None':
		"""Draws a button."""
	def DrawEllipseFill(self, centerPoint: 'List[float]', radius: 'float') -> 'None':
		"""Draws a ellipse filled."""
	def DrawEllipseLine(self, centerPoint: 'List[float]', radius: 'float', lineWidth: 'float' = 1.0, lineStyle: 'int' = 0) -> 'None':
		"""Draws a ellipse line."""
	def DrawFrame(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int', lineWidth: 'float' = 1.0, lineStyle: 'int' = 0) -> 'None':
		"""Draws a rectangular shape."""
	def DrawGetFontBaseLine(self) -> 'int':
		"""Returns the font base line."""
	def DrawGetFontHeight(self) -> 'int':
		"""Returns the height of the current font."""
	def DrawGetTextWidth(self, text: 'str') -> 'int':
		"""Returns the width in pixels of the string text."""
	def DrawGetTextWidth_ListNodeName(self, node: 'BaseList2D', fontid: 'int' = 1) -> 'int':
		"""Retrieves the width in pixels of the name of node."""
	def DrawImageRef(self, imageRef: 'object', wx: 'int', wy: 'int', ww: 'int', wh: 'int', opacity: 'float', mode: 'int') -> 'None':
		"""Draws a image into the user area."""
	def DrawLine(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draws a line with the current pen color."""
	def DrawMsg(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int', msg: 'BaseContainer') -> 'None':
		"""Draw the userarea."""
	def DrawPolyFill(self, p: 'List[float]', closed: 'bool') -> 'None':
		"""Draws a polygon filled."""
	def DrawPolyLine(self, p: 'List[float]', closed: 'bool', lineWidth: 'float' = 1.0, lineStyle: 'int' = 0) -> 'None':
		"""Draws a polygon contour."""
	def DrawRectangle(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Fills a rectangular area."""
	def DrawSetFont(self, fontid: 'int') -> 'None':
		"""Sets the text font."""
	def DrawSetOpacity(self, opacity: 'float') -> 'None':
		"""Sets the draw opacity."""
	def DrawSetPen(self, color: 'Vector') -> 'None':
		"""Sets the draw color."""
	def DrawSetTextCol(self, fg: 'Vector', bg: 'Vector') -> 'None':
		"""Sets the text foreground and background color."""
	def DrawSetTextRotation(self, textrotation: 'float') -> 'None':
		"""Set the text rotation."""
	def DrawText(self, text: 'str', x: 'int', y: 'int', flags: 'int' = 0) -> 'None':
		"""Draws a rectangle in the area."""
	def FillBitmapBackground(self, bmp: 'BaseBitmap', offsetx: 'int', offsety: 'int') -> 'None':
		"""Draws a bitmap in the area."""
	def GetBorderSize(self, type: 'int') -> 'None':
		"""Retrieves the space required to draw a border."""
	def GetColorRGB(self, colorid: 'int') -> 'None':
		"""Gets the RGB values associated with a color code."""
	def GetDialog(self) -> 'GeDialog':
		"""Gets the user area's parent dialog."""
	def GetDragObject(self, msg: 'BaseContainer') -> 'None':
		"""A convenience function to extract the data from a drag and drop message."""
	def GetDragPosition(self, msg: 'BaseContainer') -> 'None':
		"""A convenience function to extract local drag coordinates from a drag and drop event."""
	def GetHeight(self) -> 'int':
		"""Return the height."""
	def GetId(self) -> 'int':
		"""Return the ID."""
	def GetInputEvent(self, askdevice: 'int', res: 'BaseContainer') -> 'bool':
		"""Gets the next input event for a certain device."""
	def GetInputState(self, askdevice: 'int', askchannel: 'int', res: 'BaseContainer') -> 'bool':
		"""Polls a certain channel of a device."""
	def GetMinSize(self) -> 'Tuple[int, int]':
		"""Specify a minimum size for the user area."""
	def GetPixelRatio(self) -> 'float':
		"""Retrieve the Pixel Ratio."""
	def GetWidth(self) -> 'int':
		"""Return the width."""
	def Global2Local(self) -> 'None':
		"""Transforms global coordinates."""
	def HandleMouseDrag(self, msg: 'BaseContainer', type: 'int', data: 'object', dragflags: 'int') -> 'bool':
		"""Starts a drag and drop operation."""
	def HasFocus(self) -> 'bool':
		"""Indicates the focus state."""
	def Init(self) -> 'bool':
		"""Called once when the user area is initialized."""
	def InitValues(self) -> 'bool':
		"""Called after the layout is calculated."""
	def InputEvent(self, msg: 'BaseContainer') -> 'bool':
		"""Called when an input event is received."""
	def IsEnabled(self) -> 'bool':
		"""Indicates the enabled state."""
	def IsHotkeyDown(self, id: 'int') -> 'int':
		"""Checks the standard navigation hotkeys."""
	def IsR2L(self) -> 'bool':
		"""Checks if the user area has to be drawn in right-to-left layout mode."""
	def KillEvents(self) -> 'None':
		"""Flushes all events from the window message queue."""
	def LayoutChanged(self) -> 'None':
		"""Tells the GUI element that the layout has changed."""
	def Local2Global(self) -> 'None':
		"""Transforms local coordinates."""
	def Local2Screen(self) -> 'None':
		"""Transforms local coordinates."""
	def Message(self, msg: 'BaseContainer', result: 'BaseContainer') -> 'int':
		"""Override this function if you want to react to more messages."""
	def MouseDrag(self) -> 'Tuple[int, float, float, BaseContainer]':
		"""Polls the mouse during a drag started MouseDragStart."""
	def MouseDragEnd(self) -> 'int':
		"""Ends a mouse drag."""
	def MouseDragStart(self, button: 'int', mx: 'float', my: 'float', flag: 'int') -> 'None':
		"""Starts a mouse drag."""
	def OffScreenOn(self, x: 'int' = -1, y: 'int' = 0, w: 'int' = 0, h: 'int' = 0) -> 'bool':
		"""Enables double buffering to avoid blinking and flickering effects."""
	def Redraw(self, thread: 'bool' = False) -> 'None':
		"""Forces the user area to redraw itself."""
	def Screen2Local(self) -> 'None':
		"""Transforms screen coordinates."""
	def ScrollArea(self, xdiff: 'int', ydiff: 'int', x: 'int', y: 'int', w: 'int', h: 'int') -> 'None':
		"""Scrolls the area."""
	def SendParentMessage(self, msg: 'BaseContainer') -> 'None':
		"""Send a custom message."""
	def SendParentMessageResult(self, msg: 'BaseContainer') -> 'Any':
		"""Sends a custom message to the parent dialog."""
	def SetClippingRegion(self, x: 'int', y: 'int', w: 'int', h: 'int') -> 'None':
		"""Set a clipping region."""
	def SetDragDestination(self, cursor: 'int') -> 'bool':
		"""Sets the correct cursor during drag and drop handling."""
	def SetTimer(self, x: 'int') -> 'None':
		"""Initializes the timer clock."""
	def Sized(self, w: 'int', h: 'int') -> 'None':
		"""Called when the user area is resized."""
	def Timer(self, msg: 'BaseContainer') -> 'None':
		"""Called on timer subscription."""
	def __init__(self) -> 'None':
		"""Initialize self.  See help(type(self)) for accurate signature."""

class EditorWindow(object):
	"""Represents an editor window."""
	def BfGetInputEvent(self, askdevice: 'int', res: 'BaseContainer') -> 'bool':
		"""Get the state of an input device."""
	def BfGetInputState(self, askdevice: 'int', askchannel: 'int', res: 'BaseContainer') -> 'bool':
		"""Get the status of an input device."""
	def DrawXORLine(self, x1: 'int', y1: 'int', x2: 'int', y2: 'int') -> 'None':
		"""Draw an XOR line in the editor view."""
	def Global2Local(self) -> 'Tuple[int, int]':
		"""Transforms global window coordinates."""
	def IsHotkeyDown(self, id: 'int') -> 'int':
		"""Checks the standard navigation hotkeys."""
	def Local2Global(self) -> 'Tuple[int, int]':
		"""Transforms local coordinates."""
	def Local2Screen(self) -> 'Tuple[int, int]':
		"""Transforms local coordinates."""
	def MouseDrag(self) -> 'Tuple[int, float, float, BaseContainer]':
		"""Check for the mouse drag status."""
	def MouseDragEnd(self) -> 'int':
		"""Check why the mouse drag ended."""
	def MouseDragStart(self, button: 'int', mx: 'float', my: 'float', flags: 'int') -> 'None':
		"""Initialise a mouse dragging loop."""
	def Screen2Local(self) -> 'Tuple[int, int]':
		"""Transforms screen coordinates."""
	def StatusSetText(self, str: 'str') -> 'None':
		"""Sets the text in the status bar."""

class HyperLinkCustomGui(BaseCustomGui):
	"""HyperLinkCustomGui - Dialog element."""
	def GetLinkString(self) -> 'Tuple[str, str]':
		"""Get the strings."""
	def SetLinkString(self, strLink: 'str' = '', strText: 'str' = '') -> 'None':
		"""Set the strings."""

class FontChooserCustomGui(BaseCustomGui):
	"""FontChooser - Dialog element."""
	def GetFont(self) -> 'BaseContainer':
		"""Get the font."""
	def SetFont(self, bc: 'BaseContainer') -> 'None':
		"""Set the font."""

class RangeCustomGui(BaseCustomGui):
	"""RangeCustomGui - Range custom GUI."""


def GetInputState(askdevice: int, askchannel: int, res: BaseContainer) -> bool:
	'''Polls a certain channel of a device for the current input state.'''
def GetInputEvent(askdevice: int, res: BaseContainer) -> bool:
	'''Gets the next input event for a certain device from the event queue.'''
def SizePixChr(pixels: int, chars: int) -> int:
	'''Specify dialog control dimension.'''
def SizePix(pixels: int) -> int:
	'''Specify dialog control dimension.'''
def SizeChr(chars: int) -> int:
	'''Specify dialog control dimension.'''
def MessageDialog(text: str, type: int) -> int:
	'''Prints out a text to a message-box.'''
def QuestionDialog(text: str) -> bool:
	'''Opens a standard question dialog.'''
def RenameDialog(text: str) -> Optional[str]:
	'''Opens a standard rename dialog.'''
def InputDialog(title: str, preset: str) -> str:
	'''Open an input dialog.'''
def ColorDialog(flags: int, col: Vector) -> Optional[Vector]:
	'''Open a color chooser dialog.'''
def FontDialog() -> Optional[BaseContainer]:
	'''Open a font chooser dialog.'''
def SelectionListDialog(arr: List[BaseObject], doc: BaseDocument, x: int, y: int) -> int:
	'''Private.'''
def ShowPopupDialog(cd: Optional[GeDialog], bc: Optional[BaseContainer], x: Optional[int], y: Optional[int], flags: Optional[int]) -> int:
	'''Private.'''
def GeUpdateUI() -> None:
	'''Redraw the GUI.'''
def GeGetScreenDimensions(x: int, y: int, whole_screen: bool) -> None:
	'''Get the screen dimensions.'''
def ActiveObjectManager_SetObject(id: int, op: C4DAtom, flags: int, activepage: DescID) -> None:
	'''Sets the currently shown object.'''
def ActiveObjectManager_SetObjects(id: int, objects: List[C4DAtom], flags: int, activepage: DescID) -> None:
	'''Sets the currently shown objects.'''
def SetMousePointer(l: int) -> None:
	'''Set the type of mouse pointer.'''
def GetCursorBitmap(type: object, hotspotx: object, hotspoty: object) -> None:
	'''Returns the cursor bitmap.'''
def GetShortcutCount() -> int:
	'''Get the global shortcut count.'''
def Shortcut2String(shortqual: int, shortkey: int) -> str:
	'''Converts a shortcut to a readable string.'''
def AddShortcut(bc: BaseContainer) -> bool:
	'''Add a shortcut.'''
def GetShortcut(index: int) -> BaseContainer:
	'''Get a shortcut.'''
def RemoveShortcut(index: int) -> bool:
	'''Remove Shortcut.'''
def LoadShortcutSet(fn: Union[str, MemoryFileStruct], add: bool) -> bool:
	'''Load Shortcut Set.'''
def SaveShortcutSet(fn: Union[str, MemoryFileStruct]) -> bool:
	'''Save Shortcut Set.'''
def GetGuiWorldColor(cid: int) -> Vector:
	'''Private.'''
def GetMenuResource(menuname: str) -> BaseContainer:
	'''Gets the menu container of a main menu.'''
def SearchMenuResource(bc: BaseContainer, searchstr: str) -> bool:
	'''Searches a menu container.'''
def SearchPluginMenuResource(identifier: str) -> Optional[object]:
	'''Searches for the 'Plugins' main category in 'M_EDITOR'.'''
def SearchPluginSubMenuResource(identifier: str, bc: Optional[BaseContainer]) -> Optional[object]:
	'''Searches for the 'Plugins' main category in 'M_EDITOR'.'''
def UpdateMenus() -> None:
	'''Forces a menu update.'''
def GetInterfaceIcon(type: int, id_x: int, id_y: int, id_w: int, id_h: int) -> None:
	'''Returns the icon for an interface element.'''
def GetInterfaceIconEx(type: int, id_x: int, id_y: int, id_w: int, id_h: int) -> Optional[IconData]:
	'''Returns the icon for an interface element.'''
def RegisterIcon(lIconID: int, pBmp: BaseBitmap, x: Optional[int], y: Optional[int], w: Optional[int], h: Optional[int]) -> bool:
	'''Register an icon.'''
def GetIcon(lIconID: int) -> None:
	'''Returns a registered icon.'''
def UnregisterIcon(lIconID: int) -> bool:
	'''Unregister an icon.'''
def GeIsTabletMode() -> bool:
	'''Returns true when the current/preferred input device is a graphic tablet.'''
def GetMouseMoveDelta() -> float:
	'''Retrieves the mouse move delta (threshold) depending on the input device.'''
def GetDnDFilename(msg: BaseContainer, dragType: int, dragObj: object, texturesOnly: bool, updateUsage: bool, loadUrl: bool) -> str:
	'''GetDnDFilename extracts the Filename from the given drag and drop data returned by GetDragObject().'''

