from PySide2.QtWidgets import QWidget,QTableWidgetItem
from PySide2.QtCore import Qt
from view.Form_gastos import Ui_Form_gastos
from db.consultas import insert_gasto
from db.consultas import select_gasto
import datetime

class Gastos(QWidget,Ui_Form_gastos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.table_config()
        self.table(select_gasto())
        self.btn_actualizar.clicked.connect(lambda: self.table(select_gasto()))
        self.btn_guardar.clicked.connect(self.insert_gasto)
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
                    