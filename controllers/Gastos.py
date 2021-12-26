from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from view.Form_gastos import Ui_Form_gastos

class Gastos(QWidget,Ui_Form_gastos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
