import sqlite3 
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor

def create_conection():
    try:
        conexion = sqlite3.connect('db/db_PVM.db')
        print("conexion correctamente [+]")
        return conexion
    except Error as e:
        print(f"oh currio un problema.... {e}")


