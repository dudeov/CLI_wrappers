Similar to loose functions approach but now all functions are class-methods.

We pass a function name to a sub-parser called `subparsers = parser.add_subparsers(dest="function_name")`:
```
args = Namespace(path_str='/Users/aleksei.chuvakov/workplace/CLI_wrappers', function_name='list_python_files')
```
Then we can fetch the function name as `args.function_name`

And then run the function from pre-created mapping:
```
...
self._func_map = {
    "list_python_files": self.list_python_files,
    "list_abs_python_files": self.list_abs_python_files 
}
...
handler: Callable = self._func_map[self._args.function_name]
handler()
...
```

Usage:
```
% python run_cli.py list_python_files
/Users/aleksei.chuvakov/workplace/CLI_wrappers/argparse_way/run_cli.py
/Users/aleksei.chuvakov/workplace/CLI_wrappers/argparse_way/executor.py
/Users/aleksei.chuvakov/workplace/CLI_wrappers/loose_functions_way/run_cli.py
/Users/aleksei.chuvakov/workplace/CLI_wrappers/loose_functions_way/executor.py
/Users/aleksei.chuvakov/workplace/CLI_wrappers/class_way/run_cli.py
/Users/aleksei.chuvakov/workplace/CLI_wrappers/class_way/executor.py
```