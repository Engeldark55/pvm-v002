from PySide2.QtWidgets import QWidget,QTableWidgetItem
from db.consultas import insert_venta
from view.Main import Ui_Form_Main
from db.consultas import insert_cuenta
from db.consultas import select_shop

import datetime

class Index(QWidget,Ui_Form_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #-----------------------------------
    #   funciones ejecutadas por defecto 
    #-----------------------------------
        self.opc_busqueda()
        self.opc_producto()
        self.table_configWidget()
        self.table(select_shop())
    #-----------------------------------
    #         Bottons windows
    #-----------------------------------
        self.btn_add_product.clicked.connect(self.Form_Productos)
        self.btn_Express.clicked.connect(self.From_Gastos)
        self.btn_Accounts.clicked.connect(self.Form_Cuenta)

    #-----------------------------------
    #        Botones de ventana
    #-----------------------------------

        self.btn_save.clicked.connect(self.insert_shop)
        self.btn_actualizar.clicked.connect(lambda: self.table(select_shop()))
    #-----------------------------------
    #        funtionss open windows
    #-----------------------------------

    def Form_Productos(self):
        from controllers.Producto import Productos
        windo_producto=Productos(self)
        windo_producto.show()

    def From_Gastos(self):
        from controllers.Gastos import Gastos
        windo_gasto=Gastos(self)
        windo_gasto.show()
    
    def Form_Cuenta(self):
        from controllers.Cuentas import Cuenta
        windo_cuenta = Cuenta(self)
        windo_cuenta.show()

    #-----------------------------------
    #        funtionss insert shop
    #-----------------------------------
    #OPtion the PRODUCT
    def opc_busqueda(self):
        opc= (" ","Tripa","Corazon","cliente","Fecha")
        self.comboBox_filtro.addItems(opc)

    def opc_producto(self):
        opc = (" ","Tripa","Corazon")
        self.comboBox_Producto.addItems(opc)
    
    def insert_shop(self):
        
        cliente = self.line_nombre_cliente.text()
        kg_pz = self.line_kg_pz.text()
        precio = self.line_precio.text()
        producto = self.comboBox_Producto.currentText()

        multi = int(kg_pz) * int(precio)
        Total  = multi

        pago = self.line_recivo.text()

        resta = int(Total) - int(pago) 
        acuenta = resta
        fecha =datetime.datetime.now()

        data = (cliente,kg_pz,precio,producto,Total,pago,acuenta,fecha)
        if insert_venta(data):
            self.clear_line_shop()
            print("venta Realizado en window")
    #-----------------------------------
    #        funtionss clear
    #-----------------------------------
    def clear_line_shop(self):
        self.line_nombre_cliente.clear()
        self.line_kg_pz.clear()
        self.line_precio.clear()
        self.line_recivo.clear()
     #-----------------------------------
    #        funtionss table
    #-----------------------------------  
    
    def table_configWidget(self):
        colum_heders=("client","KG-PZ" ,"cost","Product","Total","R","Acuenta","fecha")
        #titulos dinamicos
        self.tableWidget.setColumnCount(len(colum_heders))
        self.tableWidget.setHorizontalHeaderLabels(colum_heders)

    def table(self,data):
        self.tableWidget.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
            for(index_cell,cell) in enumerate(row):
                self.tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))

