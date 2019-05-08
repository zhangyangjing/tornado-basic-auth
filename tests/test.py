#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from tornado_basic_auth import basic_auth
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler


def test(user, pswd):
    return 'zyj' == user and '123' == pswd


@basic_auth(test)
class TestHandler(RequestHandler):
    # @basic_auth(test)
    def get(self):
        self.finish('ok')


def main():
    handlers = [('/test', TestHandler)]
    application = tornado.web.Application(handlers)
    application.listen(8081, xheaders=True)
    IOLoop.current().start()


if __name__ == "__main__":
    exit(main())
