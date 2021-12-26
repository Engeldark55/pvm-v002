# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_Producto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_Producto(object):
    def setupUi(self, Form_Producto):
        if not Form_Producto.objectName():
            Form_Producto.setObjectName(u"Form_Producto")
        Form_Producto.resize(656, 300)
        Form_Producto.setMinimumSize(QSize(656, 300))
        Form_Producto.setMaximumSize(QSize(656, 300))
        Form_Producto.setStyleSheet(u"background:rgb(47, 47, 47);\n"
"color:white;")
        self.frame = QFrame(Form_Producto)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 10, 501, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, -10, 211, 41))
        self.frame_2 = QFrame(Form_Producto)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 80, 211, 161))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 51, 21))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 51, 21))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 51, 21))
        self.line_Numero = QLineEdit(self.frame_2)
        self.line_Numero.setObjectName(u"line_Numero")
        self.line_Numero.setGeometry(QRect(80, 20, 81, 20))
        self.line_Numero.setMaxLength(2)
        self.line_Numero.setClearButtonEnabled(True)
        self.line_Tripa = QLineEdit(self.frame_2)
        self.line_Tripa.setObjectName(u"line_Tripa")
        self.line_Tripa.setGeometry(QRect(80, 50, 81, 20))
        self.line_Tripa.setMaxLength(3)
        self.line_Tripa.setClearButtonEnabled(True)
        self.line_corazon = QLineEdit(self.frame_2)
        self.line_corazon.setObjectName(u"line_corazon")
        self.line_corazon.setGeometry(QRect(80, 80, 81, 20))
        self.line_corazon.setMaxLength(3)
        self.line_corazon.setClearButtonEnabled(True)
        self.btn_save = QPushButton(self.frame_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(20, 120, 81, 23))
        self.btn_save.setStyleSheet(u"background:rgb(28, 193, 61);")
        self.btn_actualizar = QPushButton(self.frame_2)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(120, 120, 81, 23))
        self.btn_actualizar.setStyleSheet(u"background:rgb(28, 193, 61);")
        self.tableWidget = QTableWidget(Form_Producto)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(250, 80, 381, 171))
        self.tableWidget.setStyleSheet(u"background:white;\n"
"color:black;")

        self.retranslateUi(Form_Producto)

        QMetaObject.connectSlotsByName(Form_Producto)
    # setupUi

    def retranslateUi(self, Form_Producto):
        Form_Producto.setWindowTitle(QCoreApplication.translate("Form_Producto", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_Producto", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Insert Product</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form_Producto", u"<html><head/><body><p><span style=\" font-size:10pt;\">Number :</span></p><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form_Producto", u"<html><head/><body><p><span style=\" font-size:10pt;\">Gut :</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form_Producto", u"<html><head/><body><p><span style=\" font-size:10pt;\">Heart :</span></p></body></html>", None))
        self.line_Numero.setPlaceholderText(QCoreApplication.translate("Form_Producto", u"     cantidad", None))
        self.line_Tripa.setPlaceholderText(QCoreApplication.translate("Form_Producto", u"     cantidad", None))
        self.line_corazon.setPlaceholderText(QCoreApplication.translate("Form_Producto", u"      cantidad", None))
        self.btn_save.setText(QCoreApplication.translate("Form_Producto", u"Save", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Form_Producto", u"update", None))
    # retranslateUi

