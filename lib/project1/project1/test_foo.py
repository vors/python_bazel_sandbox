import project1.foo
def test_foo():
    assert project1.foo.foo() == 42

class Foo:
    pass

def test_type_repr():
    # assert project1.foo.type_repr(Foo) == "project1.test_foo.Foo"
    assert Foo.__module__ == "project1.test_foo"

