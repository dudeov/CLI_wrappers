"""This module just lists all the .py files in the given dir"""

from pathlib import Path
from typing import Callable

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

def main(args: "argparse.Namespace"):
    print(globals())
    try:
        handler: Callable = globals()[args.function_name]
    except KeyError as ex:
        raise SystemExit("Wrong fuction name!")

    handler()
