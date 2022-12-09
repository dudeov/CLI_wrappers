The `globals()` method returns a dictionary with all the global variables and symbols for the current program.
```
% print(globals())
{'In': ['', 'globals()'],
 'Out': {},
 '_': '',
 '__': '',
 '___': '',
 '__builtin__': <module 'builtins' (built-in)>,
 '__builtins__': <module 'builtins' (built-in)>,
 '__name__': '__main__',
 ...}
```

```
age = 23
globals()['age'] = 25
print('The age is:', age) ## The age is: 25
```

We pass a function name to a sub-parser called `subparsers = parser.add_subparsers(dest="function_name")`

Then we fetch the function name in the `executor` as `args.function_name`

And then run the function from the global scope with the same name:
```
handler: Callable = globals()[args.function_name]
handler()
```