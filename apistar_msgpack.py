#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""MessagePack Renderer/Parser for Apistar, see https://msgpack.org."""


import typing

from apistar import exceptions, http
from apistar.renderers import Renderer

try:
    from ujson import loads  # https://github.com/esnme/ultrajson#ultrajson
    JSONDecodeError = Exception
except ImportError:
    from json import loads, JSONDecodeError

try:
    import msgpack   # https://github.com/msgpack/msgpack-python  (Official)
    has_msgpack = True
except ImportError:
    import umsgpack  # https://github.com/vsergeev/u-msgpack-python
    has_msgpack = False


__version__ = "1.5.0"
__license__ = "GPLv3+ LGPLv3+"
__author__ = "Juan Carlos"
__email__ = "juancarlospaco@gmail.com"
__contact__ = "https://t.me/juancarlospaco"
__maintainer__ = "Juan Carlos"
__url__ = "https://github.com/juancarlospaco/apistar-msgpack#apistar-msgpack"
__all__ = ("MessagePackRenderer", "MessagePackParser")


class MessagePackRenderer(Renderer):
    media_type = 'application/msgpack'  # 'application/x-msgpack'
    charset = 'utf-8'                   # Its a Binary format anyways.
    precision = 'single'                # 'double' (only for u-msgpack-python)

    def render(self, data: http.ResponseData) -> bytes:
        if has_msgpack:
            return msgpack.packb(data)
        else:
            return umsgpack.packb(data, force_float_precision=self.precision)


class MessagePackParser():
    media_type = 'application/msgpack'  # 'application/x-msgpack'

    def parse(self, body: http.Body) -> typing.Any:
        if not body:
            raise exceptions.BadRequest(detail=f'Empty MessagePack: {body}.')
        try:
            if has_msgpack:
                data_from_msgpack = loads(msgpack.unpackb(body))
            else:
                data_from_msgpack = loads(umsgpack.unpackb(body))
        except UnicodeEncodeError as error:
            raise exceptions.BadRequest(
                detail=f'Invalid Unicode UTF-8 on MessagePack error: {error}.')
        except ValueError as error:
            raise exceptions.BadRequest(
                detail=f'Invalid Keys or Values on MessagePack error: {error}')
        except JSONDecodeError as error:
            raise exceptions.BadRequest(detail=f'Invalid MessagePack: {error}')
        except Exception as error:
            raise exceptions.BadRequest(
                detail=f'{self} Unknown Exception: {error}, parsing {body}.')
        else:
            return data_from_msgpack
