# c4djson

Introduction
============

The `c4djson` is a useful module to load and dump objects with [CINEMA 4D](http://www.maxon.net) in python dict format which is similar to the standard python json module.

It uses json structure (dict in python) to mimic the hierarchy of object manager in cinema 4d in a brief way, both for build and for show. It can free you from a mass of parameter settings by only focusing on changed paramters.

Besides, animation key frames are parsed as python list and userdata are parsed as python dict. Thus, a simple c4d document can be saved as a python script!

A brief example:

- The dict in python script [example 01](https://github.com/iplai/c4djson/blob/master/examples/01.Deformers%20and%20Animation.py):

![](https://github.com/iplai/c4djson/raw/master/images/example01.code.png)

- Run the script then we get the objects in c4d:

![](https://github.com/iplai/c4djson/raw/master/images/example01.png)

- The print output:

```
{
  O.null @ 'Deformed Cylinder': {
    O.sds: {
      Type: OpenSubdiv Bilinear,
      Subdivision Viewport: 1,
      Subdivision Renderer: 1,
      O.cylinder: {
        Radius: 20,
        Height: 200,
        Height Segments: 20,
        Rotation Segments: 3,
        Caps: False,
        Rotation.H: [ (0, 0), (90, 360) ],
        T.phong: { Angle Limit: True },
      },
    },
    O.twist: {
      Size: (40, 200, 40),
      Angle: 360,
    },
    O.bend: {
      Size: (40, 200, 40),
      Strength: 360,
    },
  },
  O.mgcloner: {
    Mode: Object,
    Object: O.sds,
    Distribution: Edge,
    O.sphere: {
      Radius: 5,
      Segments: 24,
      T.phong: { Angle Limit: True },
    },
  },
}
```

The [dump](https://github.com/iplai/c4djson/blob/master/dump.py) function can do a reversed process of the former example:

```python
from c4djson import dump
dump(indent=2, ident=True)
```

It can print the selected objects (include materials) as dict (same as the first picture) which can be directly used in python script.

Installation
============

Take the inner `c4djson` folder (not the root `c4djson` folder) in this repository, and put it under **any** of the following paths:

```
C:\Program Files\Maxon Cinema 4D 2023\resource\modules\python\libs\python39
C:\Users\Administrator\AppData\Roaming\Maxon\Maxon Cinema 4D 2023_BCDB4759\python39
C:\Program Files\Maxon Cinema 4D 2023\resource\modules\python\libs\python39.win64.framework\lib
C:\Program Files\Maxon Cinema 4D 2023\resource\modules\python\libs\python39.win64.framework\dlls
C:\Program Files\Maxon Cinema 4D 2023
C:\Users\Administrator\AppData\Roaming\Maxon\python\python39\libs
C:\Users\Administrator\AppData\Roaming\Maxon\Maxon Cinema 4D 2023_BCDB4759\python39\libs
C:\Program Files\Maxon Cinema 4D 2023\resource\modules\python\libs\python39.win64.framework\lib\site-packages
```

The paths can be got by run this line of code in cinema 4d python console:

```python
import sys;print("\n".join(sys.path))
```

For my preference, I put it in the first one, which is the same path of `c4d` dummy package.

Usage
=====

- Load

Simply import all from c4djson you'd like to use in your scripts or plugins, like you normally would:

```python
from c4djson import *
Tree({
    # Put your objects here as the first picture above.
}).load().print()
```
Following is how the `load` and `print` defined.
```python
class Tree:
  def load(self, replace=True):
      """
      Parse and load the python dict to c4d.
      @param: replace
          If true, remove existing highest level objects in c4d object
              manager with same name and type as the correspondings in dict
              and materials with same name.
          If false, just load, don't check existing objects.
      """
  def print(self, indent=2, ident=False):
      """
      Print the parsed dict to console.
      @param: indent
          The space number of indent.
      @param: ident
          If true, print indentifier e.g."c4d.PRIM_CUBE_LEN".
          If false, print name instead of indentifier e.g."Size".
      """
```

- Dump

Put `dump.py` and `dump.tif` in your c4d scripts folder. Make it a button as the following gif do.

![](https://github.com/iplai/c4djson/raw/master/images/dump.gif)

Contributions
=============

I'd be very happy to accept code contributions. If you'd like to contribute  
please fork this repository, commit your changes to your local fork and then  
send me a pull request.

If that’s too much of a hassle, you can also go ahead and create a gist or a   
pastebin post (or whatever copypasta service you fancy) and send me the URL so   
that I can include the code manually.
