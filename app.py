from PySide2.QtWidgets import QApplication
#from controllers.Index import Index as Main
from controllers.log import login

if __name__ == "__main__":
    app = QApplication()
    window = login()
    window.show()
    app.exec_()