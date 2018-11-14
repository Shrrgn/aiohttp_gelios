import sqlalchemy as sa
from sqlalchemy.orm import mapper, sessionmaker
#from aiomysql.sa import create_engine

try:
    from demo.settings import config, ADMIN_DB_URL, URL_USERS, URL_UNITS
    from demo.utils import get_data
except ImportError as e:
    from settings import config, ADMIN_DB_URL, URL_USERS, URL_UNITS
    from utils import get_data

metadata = sa.MetaData()

#objects for tables

users_table = sa.Table(
    'users',
    metadata,
    sa.Column('id', sa.Integer),
    sa.Column('login', sa.VARCHAR(30))
)

units_table = sa.Table(
    'units',
    metadata,
    sa.Column('id', sa.Integer),
    sa.Column('name', sa.String(30, convert_unicode=True)),
    sa.Column('creator', sa.Integer)
)


def create_tables(engine):
    tables = [users_table, units_table]
    for i in tables:
        if table_exists(engine, i.name):
            i.drop(engine)
        i.create(engine)


def table_exists(engine, name):
    return engine.dialect.has_table(engine, name)

def insert_users(engine):
    conn = engine.connect()
    data = get_data(URL_USERS)

    for i in data:
        conn.execute(users_table.insert().values(id=i["id"], login=i["login"]))
    conn.close()

def insert_units(engine):
    conn = engine.connect()
    data = get_data(URL_UNITS)

    for i in data:
        conn.execute(units_table.insert().values(id=i["id"], name=i["name"].encode('utf-8'), creator=i["creator"]))
    conn.close()

def init_data():
    engine = sa.create_engine(ADMIN_DB_URL)
    create_tables(engine)
    insert_users(engine)
    insert_units(engine)
