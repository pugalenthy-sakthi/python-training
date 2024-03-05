import pymysql
from config import Config as configuration

mysql = pymysql.connections.Connection(
    host=configuration.host,
    user=configuration.user,
    password=configuration.password,
    database=configuration.database
    )

def getCursor():
    return mysql