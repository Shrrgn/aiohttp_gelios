import json
from urllib.request import urlopen


async def get_data(url):
    #with urlopen(url) as jdata:
    data = json.loads(urlopen(url).read().decode())

    return data