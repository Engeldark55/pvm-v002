from PySide2.QtWidgets import QWidget, QTableWidgetItem
from PySide2.QtCore import Qt
from view.Form_Producto import Ui_Form_Producto
from db.consultas import insert_producto
from db.consultas import select_producto

#busquedas
from db.consultas import busqueda_by_N_socio
from db.consultas import busqueda_by_N_tripa
from db.consultas import busqueda_by_N_cora
from db.consultas import busqueda_by_fecha_pro


import datetime

class Productos(QWidget,Ui_Form_Producto):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #funtions
        self.table_configWidget()
        self.table(select_producto())
        self.opc_busqueda()
        #btn
        self.btn_save.clicked.connect(self.insert_db)
        self.btn_actualizar.clicked.connect(lambda:self.table(select_producto()))
        self.btn_buscar.clicked.connect(self.full_busqueda)
        
    def insert_db(self):
        socio = self.line_Numero.text()
        tripa = self.line_Tripa.text()
        corazon = self.line_corazon.text()
        fecha = datetime.datetime.now()
        data = (socio,tripa,corazon,fecha)
        if insert_producto(data):
            self.clear_line()
            #self.close()

    def clear_line(self):
        self.line_Numero.clear()
        self.line_corazon.clear()
        self.line_Tripa.clear()

    def table_configWidget(self):
        colum_heders=("N_Socio","N_Tripa" ,"N_corazon","Fecha")
        #titulos dinamicos
        self.tableWidget.setColumnCount(len(colum_heders))
        self.tableWidget.setHorizontalHeaderLabels(colum_heders)

    def table(self,data):
        self.tableWidget.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
            for(index_cell,cell) in enumerate(row):
                self.tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))
    #busquedas
    def opc_busqueda(self):
        opc= (" ","Numero_S","Tripaje","Asadura","Fecha")
        self.comboBox_filtro.addItems(opc)
    def buscar_by_Nsocio(self,s):
        data = busqueda_by_N_socio(s)
        self.table(data)
    def buscar_by_Triaje(self,pro):
        data =busqueda_by_N_tripa(pro)
        self.table(data)
    def buscar_by_asadura(self,pro):
        data =busqueda_by_N_cora(pro)
        self.table(data)
    def buscar_by_fecha(self,fecha):
        data=busqueda_by_fecha_pro(fecha)
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
                if opc_s == "Numero_S":
                    self.buscar_by_Nsocio(busqueda)
                elif  opc_s == "Tripaje":
                    self.buscar_by_Triaje(busqueda)
                elif  opc_s == "Asadura":
                    self.buscar_by_asadura(busqueda)
                
                elif  opc_s == "Fecha":
                    self.buscar_by_fecha(busqueda)
                elif  opc_s == " ":
                     self.table(select_producto())
                
