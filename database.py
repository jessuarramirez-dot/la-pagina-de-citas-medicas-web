import mysql.connector
from confi import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def conectar():
    conexion = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conexion