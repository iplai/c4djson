import importlib, sys
module = "c4d"
module = sys.argv[1]
module_dummy = module.replace("c4d", "c4d_dummy")
if module == "c4d.utils.noise":
    import c4d.utils
    from c4d.utils import noise as module
else:
    module = importlib.import_module(module)
module_dummy = importlib.import_module(module_dummy)
import inspect, re

should_import_maxon = False

dummy_dict = module_dummy.__dict__

arg_type_mappings = {
    "str": "str",
}
ret_type_mappings = {
    "stdin_read": "str",
}


def dump_function(val):
    global should_import_maxon
    name = val.__name__
    raw = dummy_dict.get(name)
    annotations = raw.__annotations__ if raw else {}
    if raw is None:
        ret = ret_type_mappings.get(name)
        if ret:
            annotations["return"] = ret
        else:
            try:
                annotations["return"] = type(val()).__name__.replace("NoneType", "None")
            except BaseException as e:
                e = str(e)
                find = re.findall(r"'(.*)'", e)
                for arg in find:
                    annotations[arg] = arg_type_mappings.get(arg, "Any")
    args = ", ".join(f"{n}: {t}" for n, t in annotations.items() if n != "return")
    ret = annotations.get("return")
    if ret:
        result = f"def {name}({args}) -> {ret}:\n\t'''{val.__doc__}'''"
    else:
        result = f"def {name}({args}):\n\t'''{val.__doc__}'''"
    if "maxon" in result:
        should_import_maxon = True
    return result


def dump_class(val):
    global should_import_maxon
    name = val.__name__
    raw: type = dummy_dict.get(name)
    d = {"name": name, "doc": val.__doc__, "bases": ", ".join(base.__name__ for base in val.__bases__)}
    print(f"class {name}({d['bases']}):")
    print(f'\t"""{d["doc"]}"""')
    if raw:
        annotations = raw.__dict__.get("__annotations__", {})
        if annotations:
            for k, v in annotations.items():
                if "maxon" in v:
                    should_import_maxon = True
                print(f"\t{k}: {v}")
        members = inspect.getmembers(raw)
        for k, v in members:
            if callable(v):
                if k not in raw.__dict__:
                    continue
                attr = getattr(val, k, None)
                if attr is None:
                    continue
                sig = inspect.signature(v)
                if "self" not in sig.parameters:
                    print(f"\t@staticmethod")
                sig = re.sub(r"(<[^>]*>)", "None", str(sig))
                sig = sig.replace("c4d_dummy", "c4d")
                sig = sig.replace("NoneType", "None")
                if "maxon" in sig:
                    should_import_maxon = True
                print(f"\tdef {k}{sig}:")
                print(f'\t\t"""{attr.__doc__.strip()}"""')
    print()


if module.__doc__:
    print(f'"""{module.__doc__}"""', end="\n\n")

# TYPE_CHECKING
source = inspect.getsource(module_dummy)
flag = False
for line in source.splitlines():
    if line.startswith("from"):
        print(line.replace("c4d_dummy", "c4d"))
        continue
    if line == "if TYPE_CHECKING:":
        flag = True
        print(line)
        continue
    if flag and line == "":
        print()
        break
    if flag:
        print("\t" + line.replace("c4d_dummy", "c4d").strip())

# module
for key, val in module.__dict__.items():
    if key.startswith("__"):
        continue
    if inspect.ismodule(val):
        if val.__name__ in ["c4d.internals", "c4d.modules.noise"]:
            continue
        print(f"import {val.__name__}")

print()

# class
for key, val in module.__dict__.items():
    if key.startswith("__"):
        continue
    if callable(val) and inspect.isclass(val):
        dump_class(val)

print()

# function
for key, val in module.__dict__.items():
    if key.startswith("__"):
        continue
    if callable(val) and not inspect.isclass(val):
        print(dump_function(val))
print()

# const
for key, val in module.__dict__.items():
    if key.startswith("__"):
        continue
    if not callable(val) and not inspect.ismodule(val):
        print(f"{key}: {type(val).__name__} = {val}")

# print("NoneType = type(None)")
if should_import_maxon:
    print("import maxon")
if module.__name__ == "c4d":
    print("""
from c4d.documents import BaseDocument, LayerObject, RenderData
from c4d.storage import HyperFile
from c4d.bitmaps import BaseBitmap, GeClipMap
from c4d.utils import Neighbor
from c4d.modules.render import ChannelData, InitRenderStruct
from c4d.plugins import BaseDrawHelp
from c4d.gui import EditorWindow
from c4d.modules.mograph import FieldInfo, FieldInput, FieldOutput, FieldLayer
from c4d.modules.net import NetRenderService
from c4d.threading import BaseThread""")
