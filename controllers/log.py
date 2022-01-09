from PySide2.QtWidgets import QWidget
from view.From_login import Ui_Form
#db
from db.consultas import user_shop
class login(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #btn
        self.btn_entrar.clicked.connect(self.valid_user)
        
    def open_log(self):
        from controllers.Index import Index
        win_main=Index(self)
        win_main.show()
    
    def valid_user(self):
        name=self.line_name.text()
        passW= self.line_password.text()
        user_db=user_shop()
        if name == user_db[0] and passW == user_db[1]:
            self.open_log()
            self.label_ERROR.setText(" ")
            print(f"Bienbenido {name}")
            
        else:
            print("incorrecto... ") 
            self.line_name.clear()
            self.line_password.clear()
            self.label_ERROR.setText("     usuario o password incorrecto inpostor 7_7")
            
