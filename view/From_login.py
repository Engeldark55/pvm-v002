# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'From_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(370, 469)
        Form.setMinimumSize(QSize(370, 469))
        Form.setMaximumSize(QSize(370, 469))
        Form.setStyleSheet(u"background:rgb(0, 0, 0);\n"
"color:white;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 40, 185, 191))
        self.pushButton.setMinimumSize(QSize(185, 191))
        self.pushButton.setMaximumSize(QSize(185, 191))
        icon = QIcon()
        icon.addFile(u"../assets/pvm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(187, 500))
        self.line_name = QLineEdit(Form)
        self.line_name.setObjectName(u"line_name")
        self.line_name.setGeometry(QRect(90, 280, 191, 31))
        self.line_password = QLineEdit(Form)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(90, 350, 191, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 240, 171, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 320, 171, 21))
        self.btn_entrar = QPushButton(Form)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(140, 400, 111, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"background:rgb(138, 10, 1);\n"
"color:white")
        self.label_ERROR = QLabel(Form)
        self.label_ERROR.setObjectName(u"label_ERROR")
        self.label_ERROR.setGeometry(QRect(80, 10, 47, 13))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">User Name :</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Password :</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_entrar.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic;\">Entrar!</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_entrar.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-style:italic;\">Entrar!</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_entrar.setText(QCoreApplication.translate("Form", u"Entrar", None))
        self.label_ERROR.setText("")
    # retranslateUi

