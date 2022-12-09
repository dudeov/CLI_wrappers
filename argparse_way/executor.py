"""This module just lists all the .py files in the given dir"""

from pathlib import Path

def list_python_files(path_str: str = "."):
    p = Path(path_str)
    l = list(p.glob('**/*.py'))
    for file in l:
        print(file)

def list_abs_python_files(path_str: str = "."):
    p = Path(path_str)
    p = Path(".")
    l = [f.absolute() for f in p.glob('**/*.py')]
    for file in l:
        print(file)