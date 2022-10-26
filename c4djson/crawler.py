"""
Get IDs from official Python SDK document.
"""
import re, c4d, urllib.request

prefix = "https://developers.maxon.net/docs/Cinema4DPythonSDK"
# prefix = "http://127.0.0.1:8090/docs/Cinema4DPythonSDK"

cates = [
    {
        "path": "objects",
        "code": "O",
        "items": {
            "mospline": 440000054,
            "python": "c4d.Opython",
            "layer": "c4d.Olayer",
        },
    },
    {
        "path": "tags",
        "code": "T",
        "items": {},
    },
    {
        "path": "shaders",
        "code": "X",
        "items": {},
    },
    {
        "path": "fields_object",
        "code": "F",
        "items": {},
    },
    {
        "path": "fields_layer",
        "code": "FL",
        "items": {},
    },
    {
        "path": "tracks",
        "code": "CT",
        "items": {
            "base": "c4d.CTbase"
        },
    },
    {
        "path": "videoposts",
        "code": "VP",
        "items": {},
    },
    {
        "path": "materials",
        "code": "M",
        "items": {},
    },
]


def crawl():
    for cate in cates:
        path, code, items = cate.values()
        url = f"{prefix}/html/types/{path}.html"
        html = urllib.request.urlopen(url)
        pattern = r'<tr class="row-(?:odd|even)"><td><p><em>(\w+)</em></p></td>'
        for line in html.readlines():
            result = re.search(pattern, line.decode())
            if result:
                ident = result.group(1)
                name = ident.lstrip(code).lower()
                if not name.isidentifier():
                    name = f"{code.lower()}{name}"
                try:
                    c4d.__dict__[ident]
                    items[name] = f"c4d.{ident}"
                except KeyError:
                    ident_new = code + name.title()
                    c4d.__dict__[ident_new]
                    print(f"'{ident}' not in c4d, try '{ident_new}'", end="\n\n")
                    items[name] = f"c4d.{ident_new}"
    for cate in cates:
        items: dict[str, int]
        path, code, items = cate.values()
        print(f"class {code}(Type):")
        for key, val in sorted(items.items()):
            print(f"    {key} = {val}")
        print()


if __name__ == "__main__":
    crawl()
