import sqlite3 
from sqlite3 import Error
from sqlite3.dbapi2 import Cursor
from pathlib import Path

def create_Data_Base():
    conn = sqlite3.connect("db/db_PVM2.db")
    conn.commit()
    conn.close()
    return conn

def create_table_user():
    conn=sqlite3.connect("db/db_PVM2.db")
    data="""
        CREATE TABLE user_shop (
        ID	INTEGER NOT NULL UNIQUE,
        Name	TEXT NOT NULL,
        password	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
        )
        """
    cur=conn.cursor()
    cur.execute(data)
    conn.commit()
    conn.close()

def create_table_shop():
    conn=sqlite3.connect("db/db_PVM2.db")
    data="""
        CREATE TABLE Shop(
        ID	INTEGER NOT NULL UNIQUE,
        Cliente	TEXT NOT NULL,
        kg_pz	INTEGER NOT NULL,
        coste	INTEGER NOT NULL,
        producto	TEXT NOT NULL,
        Total_venta	INTEGER NOT NULL,
        recibo	INTEGER NOT NULL,
        acuenta	INTEGER NOT NULL,
        fecha	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
    );
    """
    cur=conn.cursor()
    cur.execute(data)
    conn.commit()
    conn.close()

def create_table_product():
    conn=sqlite3.connect("db/db_PVM2.db")
    data="""
       CREATE TABLE product (
        ID	INTEGER NOT NULL UNIQUE,
        n_socio	INTEGER NOT NULL,
        n_tri	INTEGER NOT NULL,
        n_cor	INTEGER NOT NULL,
        fecha	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
    );
   
    """
    cur=conn.cursor()
    cur.execute(data)
    conn.commit()
    conn.close()

def create_table_Expenses():
    
    conn=sqlite3.connect("db/db_PVM2.db")
    data="""
       CREATE TABLE Expenses (
        ID	INTEGER NOT NULL UNIQUE,
        name	TEXT NOT NULL,
        cost	INTEGER NOT NULL,
        description	TEXT DEFAULT 'sin observacion',
        fecha	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
    );

    """
    cur=conn.cursor()
    cur.execute(data)
    conn.commit()
    conn.close()

def create_table_Account():

    
    conn=sqlite3.connect("db/db_PVM2.db")
    data="""
       CREATE TABLE Account (
        ID	INTEGER NOT NULL UNIQUE,
        name_client	TEXT NOT NULL,
        deuda_actual	INTEGER NOT NULL,
        fecha	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)

        );

    """
    cur=conn.cursor()
    cur.execute(data)
    conn.commit()
    conn.close()

def create_use():
    con=sqlite3.connect("db/db_PVM2.db")
    sql="""INSERT INTO user_shop(Name,password)VALUES("Admin","Admin2022")"""
    con.cursor()
    con.execute(sql)
    con.commit()
    con.close()
def create_conection():
    try:
        conexion = sqlite3.connect("db/db_PVM2.db")
        print("se a creado una conexion correctamente [+]")
        
        try:
            create_table_user()
            create_table_shop()
            create_table_product()
            create_table_Expenses()
            create_table_Account()
            create_use()
        except Error as e:
            pass
            #print(f"{e} no se crearon las tables")
       
        return conexion 
        
    except Error as e:
        print(f"oh currio un problema.... {e}")
