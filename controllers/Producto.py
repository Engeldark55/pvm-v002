from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from view.Form_Producto import Ui_Form_Producto

class Productos(QWidget,Ui_Form_Producto):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
