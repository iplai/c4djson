from __future__ import annotations
from typing import List, Dict, Tuple, Union, Optional, Callable, Any, Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from c4d import BaseObject, BaseContainer, BaseTag, BaseList2D
    from c4d.documents import BaseDocument


class Template:
    """
    .. seealso:: :ref:`manual-python-character-tag`
    """

    def FindComponent(self, name: str, ident: bool) -> Optional[Component]:
        """
        Find component within template.
    
        :type name: str
        :param name: The component name to search for.
        :type ident: bool
        :param ident: If **true**, matches name and unique id string.
        :rtype: Optional[c4d.modules.character.builder.Component]
        :return: The found component or **None**.
        """
        pass
    
    def FindObject(self, name: str) -> Optional[BaseObject]:
        """
        Find object within template.
    
        :type name: str
        :param name: The component name to search for.
        :rtype: Optional[c4d.BaseObject]
        :return: The found object or **None**.
        """
        pass
    
    def GetDocument(self) -> BaseDocument:
        """
        Get the template BaseDocument.
    
        :rtype: c4d.documents.BaseDocument
        :return: The document.
        """
        pass
    

class ComponentObject:
    """
    .. seealso:: :ref:`manual-python-character-tag`
    """

    def GetName(self, ident: bool) -> str:
        """
        Get the component's name.
    
        :type ident: bool
        :param ident: If **true**, displays name and unique identifier.
        :rtype: str
        :return: The name.
        """
        pass
    
    def GetUp(self) -> Optional[BaseObject]:
        """
        Get the main object of the parent component.
    
        :rtype: Optional[c4d.BaseObject]
        :return: The main object of the parent component.
        """
        pass
    
    def GetDown(self) -> Optional[BaseObject]:
        """
        Get the main object of the first child component.
    
        :rtype: Optional[c4d.BaseObject]
        :return: The main object of the first child component.
        """
        pass
    
    def GetNext(self) -> Optional[BaseObject]:
        """
        Get the main object of the next component.
    
        :rtype: Optional[c4d.BaseObject]
        :return: The main object of the next component.
        """
        pass
    
    def GetPrev(self) -> Optional[BaseObject]:
        """
        Get the main object of the previous component.
    
        :rtype: Optional[c4d.BaseObject]
        :return: The main object of the previous component.
        """
        pass
    
    def CountComponent(self, name: str, ident: bool, mirrored: bool, down: bool) -> int:
        """
        Count child components.
    
        :type name: str
        :param name: String to match.
        :type ident: bool
        :param ident: If **true**, displays name and unique identifier.
        :type mirrored: bool
        :param mirrored: If **true**, matches only mirrored components.
        :type down: bool
        :param down: If **true**, matches recursively (includes children).
        :rtype: int
        :return: Number of matches.
        """
        pass
    
    def FindComponent(self, name: str, ident: bool, mirrored: bool, down: bool) -> ComponentObject:
        """
        Find a specific child component by name.
    
        :type name: str
        :param name: String to match.
        :type ident: bool
        :param ident: If **true**, displays name and unique identifier.
        :type mirrored: bool
        :param mirrored: If **true**, matches only mirrored components.
        :type down: bool
        :param down: If **true**, matches recursively (includes children).
        :rtype: c4d.modules.character.builder.ComponentObject
        :return: The first matched object.
        """
        pass
    
    def FindObject(self, name: str) -> BaseObject:
        """
        Find an object within the component by name.
    
        :type name: str
        :param name: String to match.
        :rtype: c4d.BaseObject
        :return: The first matched object.
        """
        pass
    
    def GetComponent(self) -> Component:
        """
        Get the component.
    
        :rtype: c4d.modules.character.builder.Component
        :return: The related component.
        """
        pass
    
    def GetObject(self) -> BaseObject:
        """
        Get the main object of the component.
    
        :rtype: c4d.BaseObject
        :return: The related object.
        """
        pass
    
    def GetObjects(self, type: int) -> BaseContainer:
        """
        Get a container with all the objects for this component.
    
        :type type: int
        :param type: Indicates which objects to get:
    
            .. include:: /consts/COMPONENT_OBJECT_GETOBJECTS_TYPE.rst
                :start-line: 3
    
        :rtype: c4d.BaseContainer
        :return: The BaseContainer filled with object links.
        """
        pass
    
    def GetTag(self) -> BaseTag:
        """
        Get the component tag for this component.
    
        :rtype: c4d.BaseTag
        :return: The component tag.
        """
        pass
    

class Component:
    """
    .. seealso:: :ref:`manual-python-character-tag`
    """

    def GetObject(self) -> BaseObject:
        """
        Get the component's object.
    
        :rtype: c4d.BaseObject
        :return: The component's BaseObject.
        """
        pass
    
    def GetTemplate(self) -> Template:
        """
        Get the component's Template.
    
        :rtype: c4d.modules.character.builder.Template
        :return: The template.
        """
        pass
    

class CharacterObject:
    """
    .. seealso:: :ref:`manual-python-character-tag`
    """

    def FindObject(self, name: str) -> Optional[BaseObject]:
        """
        Find an object by template name.
    
        :type name: str
        :param name: The object name to search for.
        :rtype: Optional[c4d.BaseObject]
        :return: The found object or **None**.
        """
        pass
    
    def GetFirst(self) -> Optional[ComponentObject]:
        """
        Returns the first character component.
    
        :rtype: Optional[c4d.modules.character.builder.ComponentObject]
        :return: The first component or **None**.
        """
        pass
    
    def GetObject(self) -> BaseObject:
        """
        Get the character object.
    
        :rtype: c4d.BaseObject
        :return: The character BaseObject.
        """
        pass
    


def AddIncludeObject(iincdata: BaseContainer, op: BaseObject, flags: int) -> int:
    """
    Add object to include container.

    :type iincdata: c4d.BaseContainer
    :param iincdata:

        All objects that will be included where each entry is a BaseLink to the object and the index is an integer corresponding to the InExcludeData flags:

        .. list-table::
            :widths: auto
            :align: left
            :header-rows: 1

            * - Value
              - Description

            * - 1
              - Hierarchy.

            * - 2
              - Sharing.

            * - 4
              - Self-Sharing.

    :type op: c4d.BaseObject
    :param op: The object where need to be inserted.
    :type flags: int
    :param flags: The bitmap. Will be copied.
    :rtype: int
    :return: **1** if success, otherwise **0**.
    """
    pass

def FindIncludeObject(incdata: object, name: str) -> int:
    """
    Find object in include container.

    :type iincdata: c4d.BaseContainer
    :param iincdata:

        All objects that will be included where each entry is a BaseLink to the object and the index is an integer corresponding to the InExcludeData flags:

        .. list-table::
            :widths: auto
            :align: left
            :header-rows: 1

            * - Value
              - Description

            * - 1
              - Hierarchy.

            * - 2
              - Sharing.

            * - 4
              - Self-Sharing.

    :type name: string
    :param name: The name to match .
    :rtype: int
    :return: **1** if a match is found, otherwise **0**.
    """
    pass

def GetComponentFlags(bl: BaseList2D) -> int:
    """
    Get component flags from an object/tag.

    :type bl: c4d.BaseList2D
    :param bl: The Component.
    :rtype: int
    :return: Type of object:

        .. include:: /consts/RIGPART_OBJECT_FLAG.rst
            :start-line: 3
    """
    pass

def RemoveIncludeObject(incdata: object, name: str) -> int:
    """
    Remove object from include container

    :type iincdata: c4d.BaseContainer
    :param iincdata: All objects that are included.
    :type name: string
    :param name: The object name to remove.
    :rtype: int
    :return: **1** if the matching object found is deleted, otherwise **0**.
    """
    pass

