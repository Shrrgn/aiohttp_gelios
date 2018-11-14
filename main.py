import jinja2
import aiohttp_jinja2
from aiohttp import web

try:
    from .demo.settings import config
    from .demo.routes import setup_routes
    from .demo.init_db import init_data
    from .demo.db import init_connection, close_connection
except ImportError as e:
    from demo.settings import config
    from demo.routes import setup_routes
    from demo.init_db import init_data
    from demo.db import init_connection, close_connection


async def init_app():
    app = web.Application()

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
    )

    init_data()
    app.on_startup.append(init_connection)
    #app.on_startup.append(close_connection)

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

