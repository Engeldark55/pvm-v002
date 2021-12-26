from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from view.From_Cuentas import Ui_From_Cuentas

class Cuenta(QWidget,Ui_From_Cuentas):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
