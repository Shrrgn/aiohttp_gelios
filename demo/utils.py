import json
from urllib.request import urlopen


async def get_data(url):
    return json.loads(urlopen(url).read().decode())