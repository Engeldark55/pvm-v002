from PySide2.QtWidgets import QWidget,QTableWidgetItem
from PySide2.QtCore import Qt
from view.From_Cuentas import Ui_From_Cuentas
from db.consultas import select_cuentas


class Cuenta(QWidget,Ui_From_Cuentas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        #tablevalues
        self.table_configWidget()
        self.table(select_cuentas())        
        
    def table_configWidget(self):
        colum_heders=("client","Deuda" ,"Abonos","fecha")
        #titulos dinamicos
        self.tableWidget.setColumnCount(len(colum_heders))
        self.tableWidget.setHorizontalHeaderLabels(colum_heders)

    def table(self,data):
        self.tableWidget.setRowCount(len(data))
        for(index_row,row) in enumerate(data):
            for(index_cell,cell) in enumerate(row):
                self.tableWidget.setItem(index_row,index_cell,QTableWidgetItem(str(cell)))
    
