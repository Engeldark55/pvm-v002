from PySide2.QtWidgets import QApplication
from controllers.Index import Index as Main

if __name__ == "__main__":
    app = QApplication()
    window = Main()
    window.show()
    app.exec_()