import os, pathlib


def scrape():
    path = pathlib.Path("typings")
    for i in path.glob("**/*"):
        if i.is_dir():
            if i.name == "__pycache__":
                for j in i.iterdir():
                    j.unlink()
                pathlib.Path.rmdir(i)
                continue
            rel_path = i.relative_to(path)
            c4dpy_path = "C:\Program Files\Maxon Cinema 4D 2023.1.0\c4dpy.exe"
            mod_name = str(rel_path).replace("\\", ".")
            command = f'"{c4dpy_path}" scrape_module.py {mod_name} > {i}\__init__.pyi'
            print(command)
            os.system(command)


if __name__ == "__main__":
    scrape()
