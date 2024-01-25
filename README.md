# python_bazel_sandbox
Playing around with different python rules for bazel

## repro

```
bazel test //... --test_output=all
```

```
    self.loader.exec_module(module)
lib/project1/project1/test_foo.py:1: in <module>
    import project1.foo
E   ModuleNotFoundError: No module named 'project1'
```