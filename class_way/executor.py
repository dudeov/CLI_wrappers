"""This module just lists all the .py files in the given dir"""

from pathlib import Path
from typing import Callable

class ListFiles:
    def __init__(self, args: "argparse.Namespace"):
        self._args = args
        self._path_str = self._args.path_str
        self._path = Path(self._path_str)
        self._func_map = {
            "list_python_files": self.list_python_files,
            "list_abs_python_files": self.list_abs_python_files 
        }

    def list_python_files(self):
        l = list(self._path.glob('**/*.py'))
        for file in l:
            print(file)

    def list_abs_python_files(self):
        l = [f.absolute() for f in self._path.glob('**/*.py')]
        for file in l:
            print(file)

    def run(self):
        try:
            handler: Callable = self._func_map[self._args.function_name]
        except KeyError as ex:
            raise SystemExit("Wrong fuction name!")

        handler()
