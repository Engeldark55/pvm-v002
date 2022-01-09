from PySide2.QtWidgets import QWidget
from view.From_login import Ui_Form

class login(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #btn
        self.btn_entrar.clicked.connect(self.open_log)
        
    def open_log(self):
        from controllers.Index import Index
        win_main=Index(self)
        win_main.show()