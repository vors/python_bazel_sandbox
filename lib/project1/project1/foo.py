import types
import typing

def type_repr(typ) -> str:
    # Similar to typing._type_repr
    if isinstance(typ, (types.GenericAlias, typing._GenericAlias)):
        return repr(typ)

    module = getattr(typ, "__module__", None)
    name = getattr(typ, "__qualname__", None)
    if name is None:
        name = getattr(typ, "__name__", None)
    if name is not None:
        if module is not None and module != "builtins":
            return f"{module}.{name}"
        return name

    if typ is ...:
        return "..."
    return repr(typ)

def foo():
    return 42
