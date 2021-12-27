from PySide2.QtWidgets import QWidget, QTableWidgetItem
from PySide2.QtCore import Qt
from view.Form_Producto import Ui_Form_Producto
from db.consultas import insert_producto
from db.consultas import select_producto
import datetime

class Productos(QWidget,Ui_Form_Producto):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        #funtions
        self.table_configWidget()
        self.table(select_producto())
        #btn
        self.btn_save.clicked.connect(self.insert_db)
        self.btn_actualizar.clicked.connect(lambda:self.table(select_producto()))
        
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
