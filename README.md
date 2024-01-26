# python_bazel_sandbox
Playing around with different python rules for bazel

## repro

```
bazel test //... --test_output=all
```

```
=================================== FAILURES ===================================
________________________________ test_type_repr ________________________________

    def test_type_repr():
>       assert project1.foo.type_repr(Foo) == "project1.test_foo.Foo"
E       AssertionError: assert 'lib.project1....test_foo.Foo' == 'project1.test_foo.Foo'
E         - project1.test_foo.Foo
E         + lib.project1.project1.test_foo.Foo
E         ? +++++++++++++

lib/project1/project1/test_foo.py:9: AssertionError
```