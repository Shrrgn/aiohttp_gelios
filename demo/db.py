from sqlalchemy import create_engine

try:
    from demo.settings import config
    from demo.utils import get_data
except ImportError as e:
    from .demo.settings import config
    from .demo.utils import get_data

# install mysqlclient

DSN = "mysql://{user}:{password}@{host}:{port}/{database}"
ADMIN_DB_URL = DSN.format(
    user=config["mysql"]["user"],
    password=config["mysql"]["password"],
    host=config["mysql"]["host"],
    port=config["mysql"]["port"],
    database=config["mysql"]["database"]
)


class DataInDB:

    def __int__(self):
        engine = create_engine(ADMIN_DB_URL)
        self.conn = engine.connect()

    async def insert_users(self, url):
        data = await get_data(url)

        for i in data:
            conn.execute("INSERT INTO users (id,login) VALUES ({0},{1});".format(i["id"], i["login"]))

    async def insert_units(self, url):
        data = await get_data(url)

        for i in data:
            conn.execute(
                "INSERT INTO users (id,name,creator) VALUES ({0},{1},{2});".format(
                                                                               i["id"],
                                                                               i["name"],
                                                                               i["creator"]
                                                                               )
            )

    def tear_down(self):
        self.conn.close()


'''
import json
from urllib.request import urlopen

url = "http://admin.geliospro.com/sdk/?login=demo&pass=demo&svc=get_users&params={}"

data = json.loads(urlopen(url).read().decode())

conn

create table users(
    id INT,
    login VARCHAR(20)
) ENGINE=INNODB;

create table units(
    id INT,
    name VARCHAR(20),
    creator INT
) ENGINE=INNODB;

'''