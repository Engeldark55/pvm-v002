from PySide2.QtWidgets import QWidget,QTableWidgetItem
from view.Main import Ui_Form_Main

class Index(QWidget,Ui_Form_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #-----------------------------------
    #         Bottons windows
    #-----------------------------------
        self.btn_add_product.clicked.connect(self.Form_Productos)
        self.btn_Express.clicked.connect(self.From_Gastos)
        self.btn_Accounts.clicked.connect(self.Form_Cuenta)


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