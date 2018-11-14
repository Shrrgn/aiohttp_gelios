import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'demo.yaml'

URL_UNITS = "http://admin.geliospro.com/sdk/?login=demo&pass=demo&svc=get_units&params={}"
URL_USERS = "http://admin.geliospro.com/sdk/?login=demo&pass=demo&svc=get_users&params={}"


def get_config(path):
    with open(path) as f:
        config_data = yaml.load(f)

    return config_data


config = get_config(config_path)

DSN = "mysql://{user}:{password}@{host}:{port}/{database}"
ADMIN_DB_URL = DSN.format(
    user=config["mysql"]["user"],
    password=config["mysql"]["password"],
    host=config["mysql"]["host_mysql"],
    port=config["mysql"]["port_mysql"],
    database=config["mysql"]["database"]
)
