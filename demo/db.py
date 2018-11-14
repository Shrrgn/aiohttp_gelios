import aiomysql.sa

try:
    from demo.settings import config
    from demo.utils import get_data
    from demo.init_db import users_table, units_table
except ImportError as e:
    from settings import config
    from utils import get_data
    from init_db import users_table, units_table

# install mysqlclient


async def init_connection(app):
    engine = await aiomysql.sa.create_engine(
        db=config["mysql"]["database"],
        user=config["mysql"]["user"],
        password="123456",
        host=config["mysql"]["host_mysql"],
        port=config["mysql"]["port_mysql"],
    )
    app['db'] = engine


async def close_connection(app):
    app['db'].close()
    await app['db'].wait_closed()


async def get_users(conn):
    res = await conn.execute(users_table.select())
    users = await res.fetchall()
    return users


async def get_units(conn):
    res = await conn.execute(units_table.select())
    units = await res.fetchall()
    return units

