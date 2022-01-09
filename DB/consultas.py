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

def select_one_account_name(name):
    conn = create_conection()
    sql = f"""SELECT deuda_actual FROM Account WHERE name_client= '{name}' """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchone()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()

def busqueda_by_cliente(name):
    conn = create_conection()
    sql = f"""SELECT  Cliente,kg_pz,coste,producto,Total_venta,recibo,acuenta,fecha FROM Shop where Cliente = '{name}' """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()

def busqueda_by_pro(name):
    conn = create_conection()
    sql = f"""SELECT  Cliente,kg_pz,coste,producto,Total_venta,recibo,acuenta,fecha FROM Shop where producto = '{name}' """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()
def busqueda_by_fecha(fecha):
    conn = create_conection()
    sql = f"""SELECT  Cliente,kg_pz,coste,producto,Total_venta,recibo,acuenta,fecha FROM Shop where fecha like "%{fecha}%" """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()

#produtos busqueda
def busqueda_by_N_socio(s):
    conn = create_conection()
    sql = f"""SELECT n_socio,n_tri,n_cor,fecha FROM product WHERE n_socio = {s} """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()

def busqueda_by_N_tripa(t):
    conn = create_conection()
    sql = f"""SELECT n_socio,n_tri,n_cor,fecha FROM product WHERE n_tri = {t} """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()

def busqueda_by_N_cora(c):
    conn = create_conection()
    sql = f"""SELECT n_socio,n_tri,n_cor,fecha FROM product WHERE n_cor = {c} """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()

def busqueda_by_fecha_pro(f):
    conn = create_conection()
    sql = f"""SELECT n_socio,n_tri,n_cor,fecha FROM product WHERE fecha like  "%{f}%" """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()


#gas busqueda_by_fecha_pro
def busqueda_by_name_gastos(c):
    conn = create_conection()
    sql = f"""SELECT name,cost,description,fecha FROM Expenses WHERE name ="{c}" """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()
def busqueda_by_cost_gastos(c):
    conn = create_conection()
    sql = f"""SELECT name,cost,description,fecha FROM Expenses WHERE cost ="{c}" """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        client_deuda = cur.fetchall()
        return client_deuda

    except Error as e:
        print(f"error al buscar gastos... {e}")
    finally:
        if conn:
            conn.close()

def busqueda_by_fecha_gasto(f):
    conn = create_conection()
    sql = f"""SELECT  name,cost,description,fecha FROM Expenses WHERE fecha like  "%{f}%" """
    try:
        cur = conn.cursor()
        cur.execute(sql)
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

def delete_account():
    conn = create_conection()
    sql = f"""DELETE FROM Account WHERE deuda_actual <= 0"""
    try:
        conn.cursor()
        conn.execute(sql)
        conn.commit()

    except Error as e:
        print(f"error eliminar cuenta... {e}")
    finally:
        if conn:
            conn.close()




# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
#       log 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

def user_shop():
    conn = create_conection()
    data= f"""SELECT name,password FROM user_shop """
    try:
        cur = conn.cursor()
        cur.execute(data)
        user= cur.fetchone()
        return user
    except Error as e:
          print(f"error eliminar cuenta... {e}")
    finally:
        if conn:
            cur.close()
