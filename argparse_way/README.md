Usage:
```
% python run_cli.py list_python_files 
run_cli.py
executor.py
test/unit/test.py
package/__init__.py
```
This method relies on calling functions using
```
sub_parser.set_defaults(func=funcname_to_call)
```