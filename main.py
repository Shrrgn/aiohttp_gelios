from os import path

import jinja2
import aiohttp_jinja2
from aiohttp import web

try:
    from demo.settings import config
    from demo.routes import setup_routes
except ImportError as e:
    from .demo.settings import config
    from .demo.routes import setup_routes



def init_app():
    app = web.Application()

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )

    setup_routes(app)

    return app


def main():
    app = init_app()
    web.run_app(
        app,
        host=config['host'],
        port=config['port']
    )


if __name__ == '__main__':
    main()

