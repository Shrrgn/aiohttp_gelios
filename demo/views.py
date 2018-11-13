import aiohttp_jinja2
from aiohttp import web
from demo.utils import get_data


@aiohttp_jinja2.template('wrapper.html')
async def index(request):
	return {}


@aiohttp_jinja2.template('users.html')
async def users(requset):
	url = "http://admin.geliospro.com/sdk/?login=demo&pass=demo&svc=get_users&params={}"
	users_data = await get_data(url)
	return {'users_data':users_data}

@aiohttp_jinja2.template('units.html')
async def units(request):
	url = "http://admin.geliospro.com/sdk/?login=demo&pass=demo&svc=get_units&params={}"
	units_data = await get_data(url)
	return {'units_data':units_data}
