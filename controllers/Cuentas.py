from PySide2.QtWidgets import QWidget,QTableWidgetItem
from PySide2.QtCore import Qt
from view.From_Cuentas import Ui_From_Cuentas
#db
from db.consultas import select_cuentas, update_acconut
from db.consultas import select_one_account_name
from db.consultas import delete_account

import datetime

class Cuenta(QWidget,Ui_From_Cuentas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        #tablevalues
        self.table_configWidget()
        self.table(select_cuentas())        
        delete_account()
        #btn_save
        self.btn_save.clicked.connect(self.accont_client)    
        self.btn_actualizar.clicked.connect(lambda: self.table(select_cuentas()))

    def accont_client(self):
        client = self.line_nombre.text()
        abono = self.line_abono.text()
        fecha = datetime.datetime.now()
        
        d_actual = select_one_account_name(client)
        calculo = int(d_actual[0]) - int(abono)

    
        data = (calculo,fecha,client)
        update_acconut(data)
        self.line_nombre.clear()
        self.line_abono.clear()
        delete_account()
            
    
                          


    def table_configWidget(self):
        colum_heders=("client","Deuda" ,"fecha")
        #titulos dinamicos
        self.tableWidget.setColumnCount(len(colum_heders))
        self.tableWidget.setHorizontalHeaderLabels(colum_heders)

    def table(self,data):
        self.tableWidget.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
            for(index_cell,cell) in enumerate(row):
                self.tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))
    
