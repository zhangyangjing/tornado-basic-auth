# -*- coding: utf-8 -*-

import base64
import inspect
from functools import wraps


def basic_auth(auth_func=lambda *args, **kwargs: True):
    def auth(handler, kwargs):
        def create_auth_header(handler):
            handler.set_status(401)
            handler.set_header('WWW-Authenticate', 'Basic realm=Restricted')
            handler._transforms = []
            handler.finish()

        auth_header = handler.request.headers.get('Authorization')
        if auth_header is None or not auth_header.startswith('Basic '):
            create_auth_header(handler)
            return False
        else:
            auth_decoded = base64.b64decode(auth_header[6:]).decode()
            user, pwd = auth_decoded.split(':', 2)

            if auth_func(user, pwd):
                return True
            else:
                create_auth_header(handler)
                return False

    def basic_auth_decorator(handler_obj):
        if inspect.isfunction(handler_obj):
            @wraps(handler_obj)
            def wrap_func(self, *xargs, **kwargs):
                if auth(self, kwargs):
                    handler_obj(self, *xargs, **kwargs)
            return wrap_func
        else:
            @wraps(handler_obj)
            def wrap_execute(handler_execute):
                async def _execute(self, *args, **kwargs):
                    if auth(self, kwargs):
                        await handler_execute(self, *args, **kwargs)
                return _execute
            handler_obj._execute = wrap_execute(handler_obj._execute)
            return handler_obj

    return basic_auth_decorator
