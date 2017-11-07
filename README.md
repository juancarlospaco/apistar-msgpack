# apistar-msgpack

[Apistar](https://github.com/encode/apistar) [MessagePack](https://msgpack.org) Renderer pluggable component for Python 3.6+.

- Change your Apistar App from JSON to MessagePack just adding 1 line.
- Single file tiny module installs to `/usr/lib/python3.6/site-packages/apistar_msgpack.py`
- 1 Dependency, the Official Python MessagePack Lib.


### Usage:

Usage from `settings`:
```python
from apistar_msgpack import MessagePackRenderer

settings = {'RENDERERS': (MessagePackRenderer(), )}
```

Alternatively we can specify the renderers to use on a specific handler function:

```python
from apistar import annotate
from apistar_msgpack import MessagePackRenderer

@annotate(renderers=(MessagePackRenderer(), ))
def helloworld():
    return {'message': 'Hello World.'}  # Return a MessagePack.

```

[The `helloworld` from Apistar Docs with MessagePackRenderer.](https://github.com/juancarlospaco/apistar-msgpack/blob/master/app.py)


Parser usage:
```python
from apistar_msgpack import MessagePackParser

settings = {'PARSERS': (MessagePackParser(), )}
```

Alternatively we can specify the parsers to use on a specific handler function:
```python
from apistar import annotate
from apistar_msgpack import MessagePackParser

@annotate(parsers=(MessagePackParser(), ))
def helloworld():
    # Parses MessagePack, Return a Python dict, normal Python object types.
```

- See [Apistar Docs for more info.](https://github.com/encode/apistar#configuring-the-installed-renderers)


### Requisites:

- [msgpack-python](https://github.com/msgpack/msgpack-python) Official Python MessagePack Lib.

Alternatively it also works with [u-msgpack-python](https://github.com/vsergeev/u-msgpack-python) (Unofficial, Slower, Unsupported).


### Notes:

We also look for other alternatives, like [Smile](https://github.com/FasterXML/smile-format-specification) which is Faster and Smaller, but Development is dead.
Eg. its JavaScript Lib is incomplete and abandoned, No Python3 Lib, etc.
