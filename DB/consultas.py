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

def select_producto():
    conn = create_conection()
    sql = """SELECT n_socio,n_tri,n_cor,fecha FROM product"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        product = cur.fetchall()
        return product
    except Error as e:
        print(f"error al buscar all {e}")
    
    finally:
        if conn:
            conn.close()
def select_gasto():
    conn = create_conection()
    sql= """SELECT name,cost,description,fecha FROM Expenses"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        gastos = cur.fetchall()
        return gastos
    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()




# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#        consult'S One 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*