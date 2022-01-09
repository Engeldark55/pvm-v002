from PySide2.QtWidgets import QWidget,QTableWidgetItem
from db.consultas import insert_venta
from view.Main import Ui_Form_Main
from PySide2.QtCore import Qt
#db
from db.consultas import insert_cuenta
from db.consultas import select_shop
from db.consultas import select_one_account_name,update_acconut
#db busquedas
from db.consultas import busqueda_by_cliente
from db.consultas import busqueda_by_pro
from db.consultas import busqueda_by_fecha

import datetime

class Index(QWidget,Ui_Form_Main):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
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
        self.btn_Buscar_02_client.clicked.connect(self.buscar_dAnterior)
        self.btn_Buscar.clicked.connect(self.full_busqueda)
    #-----------------------------------
    #        seleccion de producto (calculo)
    #-----------------------------------
        self.comboBox_Producto.currentIndexChanged.connect(self.selecion_producto)
        
        #funcion de cliente de-uda
     
        

    
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
    #        funtionss seleccion de producto (cuent)
    #-----------------------------------
    #OPtion the PRODUCT
    def opc_busqueda(self):
        opc= (" ","Tripa","Corazon","cliente","Fecha")
        self.comboBox_filtro.addItems(opc)

    def opc_producto(self):
        opc = (" ","Tripa","Corazon")
        self.comboBox_Producto.addItems(opc)
    
    def selecion_producto(self):
       
        seleccion = self.comboBox_Producto.itemText(self.comboBox_Producto.currentIndex())

        if seleccion == "Tripa" or seleccion == "Corazon":
          
            producto_select = self.line_kg_pz.text()
            precio_product = self.line_precio.text()
            calculo = int(producto_select) * int(precio_product)
            Total_producto = calculo
            self.label_Total_producto.setText(str(Total_producto))
            ant=self.labe_text
            total_con_Anterior=ant + Total_producto
            self.label_Total_con_anterior.setText(str(total_con_Anterior))
    #-----------------------------------
    #        funtionss insert shop
    #-----------------------------------
    def buscar_dAnterior(self):
        n_cliente=self.line_nombre_cliente.text()

        try:
            d_anterior=select_one_account_name(n_cliente)
            self.labe_text=int(d_anterior[0])
            self.label_deuda_anterior.setText(str(self.labe_text))
           
        except :
            pass 
        
            
    #-----------------------------------
    #        funtionss insert shop
    #-----------------------------------
    def insert_shop(self):
        
        cliente = self.line_nombre_cliente.text()
        kg_pz = self.line_kg_pz.text()
        precio = self.line_precio.text()
        producto = self.comboBox_Producto.currentText()

   
        multi = int(kg_pz) * int(precio)
        Total  = multi
        #self.label_Total.setText(str(Total))

        pago = self.line_recivo.text()

        resta = int(Total) - int(pago) 
        acuenta = resta
        

        self.label_Acuenta.setText(str(acuenta))

        fecha =datetime.datetime.now()

        data = (cliente,kg_pz,precio,producto,Total,pago,acuenta,fecha)
        

        busca_cliente=select_one_account_name(cliente)
        if busca_cliente:
            self.label_deuda_anterior.setText(str(busca_cliente))
            suma= int(busca_cliente[0]) + acuenta 
            data_update=(suma,fecha,cliente)
            update_acconut(data_update)
            self.label_Acuenta.setText(str(suma))
            data_2=(cliente,kg_pz,precio,producto,Total,pago,suma,fecha)
            insert_venta(data_2)
            self.clear_line_shop()
        else:
            if insert_venta(data):
                self.clear_line_shop()
                print("venta Realizado en window")
                self.label_deuda_anterior.setText(str(acuenta))

                if int(resta) != 0:
                    data_client = (cliente,acuenta,fecha)
                    insert_cuenta(data_client)
            
    
    #        funtionss clear
    #-----------------------------------
    def clear_line_shop(self):
        self.line_nombre_cliente.clear()
        self.line_kg_pz.clear()
        self.line_precio.clear()
        self.line_recivo.clear()
        #label's
        self.label_deuda_anterior.setText(str("0"))

     #-----------------------------------
    
    #line_busqueda
    def buscar_by_cliente(self,filtro):
        data = busqueda_by_cliente(filtro)
        self.table(data)
    def buscar_by_pro(self,pro):
        data =busqueda_by_pro(pro)
        self.table(data)
    def buscar_by_fecha(self,fecha):
        data=busqueda_by_fecha(fecha)
        self.table(data)

    def full_busqueda(self):
        opc_s=self.comboBox_filtro.currentText()
        busqueda=self.line_buscar.text()

        if opc_s == "":
            print("seleccione opc")
        else:
            if busqueda == "":
                print("escriba su busqueda")
            else:
                if opc_s == "cliente":
                    self.buscar_by_cliente(busqueda)
                elif  opc_s == "Tripa" or opc_s == "Corazon":
                    self.buscar_by_pro(busqueda)
                
                elif  opc_s == "Fecha":
                    self.buscar_by_fecha(busqueda)

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
    
