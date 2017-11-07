#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""MessagePack Renderer for Apistar, see https://msgpack.org."""
# Smile is Faster and Smaller but Development is dead.
# https://github.com/FasterXML/smile-format-specification


from apistar.renderers import Renderer
from apistar import http

try:
    import msgpack   # https://github.com/msgpack/msgpack-python  (Official)
    has_msgpack = True
except ImportError:
    import umsgpack  # https://github.com/vsergeev/u-msgpack-python
    has_msgpack = False


class MessagePackRenderer(Renderer):
    media_type = 'application/msgpack'  # 'application/x-msgpack'
    charset = 'utf-8'                   # Its a Binary format anyways.
    precision = 'single'                # 'double'
    use_list = False                    # Tuple if False.

    def render(self, data: http.ResponseData) -> bytes:
        if has_msgpack:
            return msgpack.packb(data, use_list=self.use_list)
        else:
            return umsgpack.packb(data, force_float_precision=self.precision)
