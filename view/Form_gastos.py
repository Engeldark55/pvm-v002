# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Form_gastos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form_gastos(object):
    def setupUi(self, Form_gastos):
        if not Form_gastos.objectName():
            Form_gastos.setObjectName(u"Form_gastos")
        Form_gastos.resize(484, 500)
        Form_gastos.setMinimumSize(QSize(484, 500))
        Form_gastos.setMaximumSize(QSize(484, 500))
        Form_gastos.setStyleSheet(u"background:rgb(79, 79, 79);\n"
"color:white;")
        self.frame = QFrame(Form_gastos)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 461, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 10, 151, 31))
        self.tableWidget = QTableWidget(Form_gastos)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 280, 441, 181))
        self.tableWidget.setStyleSheet(u"background:white;\n"
"color:black;")
        self.frame_2 = QFrame(Form_gastos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 80, 431, 131))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 16))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 111, 16))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 70, 91, 16))
        self.line_nombre_gasto = QLineEdit(self.frame_2)
        self.line_nombre_gasto.setObjectName(u"line_nombre_gasto")
        self.line_nombre_gasto.setGeometry(QRect(130, 10, 113, 20))
        self.line_nombre_gasto.setStyleSheet(u"background:white;\n"
"color:black;")
        self.line_nombre_gasto.setMaxLength(15)
        self.line_nombre_gasto.setClearButtonEnabled(True)
        self.line_costo_gasto = QLineEdit(self.frame_2)
        self.line_costo_gasto.setObjectName(u"line_costo_gasto")
        self.line_costo_gasto.setGeometry(QRect(130, 40, 113, 20))
        self.line_costo_gasto.setStyleSheet(u"background:white;\n"
"color:black;")
        self.line_costo_gasto.setMaxLength(5)
        self.line_costo_gasto.setClearButtonEnabled(True)
        self.textEdit_descripcion = QTextEdit(self.frame_2)
        self.textEdit_descripcion.setObjectName(u"textEdit_descripcion")
        self.textEdit_descripcion.setGeometry(QRect(110, 70, 151, 51))
        self.textEdit_descripcion.setStyleSheet(u"background:white;\n"
"color:black;")
        self.textEdit_descripcion.setFrameShape(QFrame.Box)
        self.textEdit_descripcion.setFrameShadow(QFrame.Plain)
        self.btn_guardar = QPushButton(self.frame_2)
        self.btn_guardar.setObjectName(u"btn_guardar")
        self.btn_guardar.setGeometry(QRect(320, 70, 75, 23))
        self.btn_guardar.setStyleSheet(u"background:green;\n"
"color:white;")
        self.btn_actualizar = QPushButton(self.frame_2)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(320, 100, 75, 23))
        self.btn_actualizar.setStyleSheet(u"background:green;\n"
"color:white;")
        self.frame_3 = QFrame(Form_gastos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(30, 230, 431, 41))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 10, 41, 21))
        self.line_buscar = QLineEdit(self.frame_3)
        self.line_buscar.setObjectName(u"line_buscar")
        self.line_buscar.setGeometry(QRect(220, 10, 113, 20))
        self.line_buscar.setMaxLength(15)
        self.line_buscar.setClearButtonEnabled(True)
        self.btn_buscar = QPushButton(self.frame_3)
        self.btn_buscar.setObjectName(u"btn_buscar")
        self.btn_buscar.setGeometry(QRect(340, 10, 75, 23))
        self.btn_buscar.setStyleSheet(u"background:green;\n"
"color:white;")

        self.retranslateUi(Form_gastos)

        QMetaObject.connectSlotsByName(Form_gastos)
    # setupUi

    def retranslateUi(self, Form_gastos):
        Form_gastos.setWindowTitle(QCoreApplication.translate("Form_gastos", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form_gastos", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Expenses</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form_gastos", u"<html><head/><body><p><span style=\" font-size:10pt;\">Name-expense :</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form_gastos", u"<html><head/><body><p><span style=\" font-size:10pt;\">Cost - expense  $:</span></p><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form_gastos", u"<html><head/><body><p>Description :</p></body></html>", None))
        self.line_nombre_gasto.setPlaceholderText(QCoreApplication.translate("Form_gastos", u"gas, renta, etc", None))
        self.line_costo_gasto.setPlaceholderText(QCoreApplication.translate("Form_gastos", u"$ 0000", None))
        self.textEdit_descripcion.setPlaceholderText(QCoreApplication.translate("Form_gastos", u"ejem. algo usual", None))
        self.btn_guardar.setText(QCoreApplication.translate("Form_gastos", u"Save", None))
        self.btn_actualizar.setText(QCoreApplication.translate("Form_gastos", u"update", None))
        self.label_5.setText(QCoreApplication.translate("Form_gastos", u"<html><head/><body><p><span style=\" font-size:10pt;\">search</span></p></body></html>", None))
        self.line_buscar.setPlaceholderText(QCoreApplication.translate("Form_gastos", u"ejm. desayuno", None))
        self.btn_buscar.setText(QCoreApplication.translate("Form_gastos", u"ok", None))
    # retranslateUi

