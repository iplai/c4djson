"""
Some Python environments are customized to include additional builtins symbols.
If you are using such an environment, you may want to tell Pyright about these 
additional symbols that are available at runtime.
To do so, you can add a local type stub file called __builtins__.pyi.
This file can be placed at the root of your project directory or at the root of 
the subdirectory specified in the stubPath setting (which is named typings by default).
"""
import c4d
from typing import Union

# Before execution, the following module attributes will be injected into each module.
# This means these symbols can be used in code although they are not defined in the module.
doc: c4d.documents.BaseDocument  # The active document.
op: Union[c4d.BaseObject, c4d.BaseTag]  # The selected object. Can be None.
tp: c4d.modules.thinkingparticles.TP_MasterSystem  # The Thinking Particles Master system of the document. Can be None.
