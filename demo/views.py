import aiohttp_jinja2

try:
    from demo.db import get_users, get_units
except ImportError as e:
    from .db import get_users, get_units


@aiohttp_jinja2.template('wrapper.html')
async def index(request):
    return {}


@aiohttp_jinja2.template('users.html')
async def users(request):
    async with request.app['db'].acquire() as conn:
        users_data = await get_users(conn)
    return {'users_data': users_data}


@aiohttp_jinja2.template('units.html')
async def units(request):
    async with request.app['db'].acquire() as conn:
        units_data = await get_units(conn)
    return {'units_data': units_data}
