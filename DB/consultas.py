from os import extsep
import sqlite3
from sqlite3 import Error
from .conexion import create_conection

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#        INSERT'S 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def insert_venta(data):
    conn = create_conection()
    sql = """INSERT INTO Shop(Cliente,kg_pz,coste,producto,Total_venta,recibo,acuenta,fecha)VALUES(?, ?, ?, ?, ?, ?, ?, ?)"""

    try:
        conn.cursor()
        conn.execute(sql,data)
        conn.commit()
        print("[insert shop ok]")
        return True
    except Error as e:
        print(f"err.. {e}")
    finally:
        if conn:
            conn.close()
            print("conexion close")
def insert_cuenta(data):
    conn = create_conection()
    sql = """INSERT INTO Account(name_client,abono,fecha)VALUES(?, ?, ?)"""
    try:
        conn.cursor()
        conn.execute(sql, data)
        conn.commit()
        print("[+] insert cuenta ok")
        return True
    except Error as e:
        print(f"error... {e}")

    finally:
        if conn:
            conn.close()
            print("conexion close")

def insert_gasto(data):
    conn = create_conection()
    sql = """INSERT INTO Expenses(name,cost,description,fecha)VALUES(?, ?, ?, ?)"""
    try:
        conn.cursor()
        conn.execute(sql, data)
        conn.commit()
        print("[+] insert gasto ok")
        return True
    except Error as e:
        print(f"error... {e}")

    finally:
        if conn:
            conn.close()
            print("conexion close")

def insert_producto(data):
    conn = create_conection()
    sql = """INSERT INTO product(n_socio,n_tri,n_cor,fecha)VALUES(?, ?, ?, ?) """
    try:
        conn.cursor()
        conn.execute(sql,data)
        conn.commit()
        print("[+] insert procut ok")
        return True
    except Error as e:
        print(f"error ....{e}")
    finally:
        if conn:
            conn.close()
            print("conexion close")

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#        UPDATE'S 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*






# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#        consult'S all 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*






# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#        consult'S One 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*