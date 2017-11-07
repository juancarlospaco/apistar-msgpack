#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""MessagePack Renderer for Apistar, see https://msgpack.org."""


from apistar import http
from apistar.renderers import Renderer

try:
    import msgpack   # https://github.com/msgpack/msgpack-python  (Official)
    has_msgpack = True
except ImportError:
    import umsgpack  # https://github.com/vsergeev/u-msgpack-python
    has_msgpack = False


__version__ = "1.0.0"
__license__ = "GPLv3+ LGPLv3+"
__author__ = "Juan Carlos"
__email__ = "juancarlospaco@gmail.com"
__contact__ = "https://t.me/juancarlospaco"
__maintainer__ = "Juan Carlos"
__url__ = "https://github.com/juancarlospaco/apistar-msgpack#apistar-msgpack"


class MessagePackRenderer(Renderer):
    media_type = 'application/msgpack'  # 'application/x-msgpack'
    charset = 'utf-8'                   # Its a Binary format anyways.
    precision = 'single'                # 'double' (only for u-msgpack-python)

    def render(self, data: http.ResponseData) -> bytes:
        if has_msgpack:
            return msgpack.packb(data)
        else:
            return umsgpack.packb(data, force_float_precision=self.precision)
