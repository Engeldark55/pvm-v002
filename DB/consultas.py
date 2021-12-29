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

def insert_cuenta(data):
    conn = create_conection()
    sql = """INSERT INTO Account(name_client,deuda_actual,fecha)VALUES(?, ?, ?)"""
    try:
        conn.execute(sql,data)
        conn.commit()
        print("[+] insert cuenta ok")
    except Error as e:
        print(f"error al insert cuenta {e}")
    finally:
        if conn:
            conn.close()

# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#        UPDATE'S 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def update_acconut(data):
    conn = create_conection()
    sql  = """UPDATE Account set deuda_actual= ?, fecha = ? WHERE name_client = ?"""
    
    try:
        conn.cursor()
        conn.execute(sql,data)
        conn.commit()
        print("[+]update db - ok")
    except Error as e:
        print(f"the update is error is .....{e}")
    finally:
        if conn:
            conn.close()




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
def select_shop():
    conn = create_conection()
    sql= """SELECT Cliente,kg_pz,coste,producto,Total_venta,recibo,acuenta,fecha FROM Shop"""
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

def select_cuentas():
    conn = create_conection()
    sql= """SELECT name_client,deuda_actual,fecha FROM Account"""
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

def select_one_cuentao_for_name(data):
    conn = create_conection()
    sql = """SELECT deuda_actual FROM Account WHERE name_client= ? """
    try:
        cur = conn.cursor()
        cur.execute(sql,data)
        client_deuda = cur.fetchall()
        return client_deuda
    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()



# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#       delete 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def delete_cuenta_cuenta():
    conn = create_conection()
    sql = """DELETE FROM Account WHERE deuda_actual = 0"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        gastos = cur.fetchall()
        return gastos
    except Error as e:
        print(f"error eliminar cuenta... {e}")
    finally:
        if conn:
            conn.close()