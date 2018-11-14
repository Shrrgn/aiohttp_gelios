import json
from urllib.request import urlopen


def get_data(url):
    return json.loads(urlopen(url).read().decode())