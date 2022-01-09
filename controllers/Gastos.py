from PySide2.QtWidgets import QWidget,QTableWidgetItem
from PySide2.QtCore import Qt
from view.Form_gastos import Ui_Form_gastos
from db.consultas import insert_gasto
from db.consultas import select_gasto

from db.consultas import busqueda_by_name_gastos
from db.consultas import busqueda_by_fecha_gasto
from db.consultas import busqueda_by_cost_gastos

import datetime

class Gastos(QWidget,Ui_Form_gastos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        #tabla
        self.table_config()
        self.table(select_gasto())
        #btn
        self.btn_actualizar.clicked.connect(lambda: self.table(select_gasto()))
        self.btn_guardar.clicked.connect(self.insert_gasto)
        self.btn_buscar.clicked.connect(self.full_busqueda)
        #funtion
        self.opc_busqueda()


    def table_config(self):
        colum_heders=("Name","Cost" ,"Description","Fecha")
        #titulos dinamicos
        self.tableWidget.setColumnCount(len(colum_heders))
        self.tableWidget.setHorizontalHeaderLabels(colum_heders)



    def table(self,data):
        self.tableWidget.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
            for(index_cell,cell) in enumerate(row):
                self.tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))

    def insert_gasto(self):
        nombre = self.line_nombre_gasto.text()
        costo = self.line_costo_gasto.text()
        description = self.textEdit_descripcion.toPlainText()
        fecha = datetime.datetime.now()
        
        data = (nombre,costo,description,fecha)
        
        if insert_gasto(data):
            self.clear_gasto()
    def clear_gasto(self):
        self.line_nombre_gasto.clear()
        self.line_costo_gasto.clear()
        self.textEdit_descripcion.clear()
    
     #line_busqueda

    def opc_busqueda(self):
        opc= (" ","Nombre","costo","Fecha")
        self.comboBox_filtro_2.addItems(opc)
    def buscar_by_name(self,filtro):
        data = busqueda_by_name_gastos(filtro)
        self.table(data)
    def buscar_by_cost(self,pro):
        data =busqueda_by_cost_gastos(pro)
        self.table(data)
    def buscar_by_fecha(self,fecha):
        data=busqueda_by_fecha_gasto(fecha)
        self.table(data)

    def full_busqueda(self):
        opc_s=self.comboBox_filtro_2.currentText()
        busqueda=self.line_buscar.text()

        if opc_s == "":
            print("seleccione opc")
        else:
            if busqueda == "":
                print("escriba su busqueda")
            else:
                if opc_s == "Nombre":
                    self.buscar_by_name(busqueda)
                elif  opc_s == "costo" :
                    self.buscar_by_cost(busqueda)
                
                elif  opc_s == "Fecha":
                    self.buscar_by_fecha(busqueda)