# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'From_Cuentas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_From_Cuentas(object):
    def setupUi(self, From_Cuentas):
        if not From_Cuentas.objectName():
            From_Cuentas.setObjectName(u"From_Cuentas")
        From_Cuentas.resize(709, 318)
        From_Cuentas.setMinimumSize(QSize(709, 318))
        From_Cuentas.setMaximumSize(QSize(709, 318))
        From_Cuentas.setStyleSheet(u"background :rgb(68, 68, 68)rgb(44, 44, 44);\n"
"color:white;")
        self.frame = QFrame(From_Cuentas)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 681, 51))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 10, 181, 31))
        self.frame_2 = QFrame(From_Cuentas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 70, 251, 241))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 71, 21))
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 91, 21))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 10, 121, 21))
        self.line_nombre = QLineEdit(self.frame_2)
        self.line_nombre.setObjectName(u"line_nombre")
        self.line_nombre.setGeometry(QRect(120, 40, 113, 20))
        self.line_nombre.setMaxLength(10)
        self.line_nombre.setClearButtonEnabled(True)
        self.line_abono = QLineEdit(self.frame_2)
        self.line_abono.setObjectName(u"line_abono")
        self.line_abono.setGeometry(QRect(120, 70, 113, 20))
        self.line_abono.setMaxLength(5)
        self.line_abono.setClearButtonEnabled(True)
        self.btn_save = QPushButton(self.frame_2)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(10, 130, 111, 23))
        self.btn_save.setStyleSheet(u"background:rgb(26, 193, 23);\n"
"")
        self.btn_actualizar = QPushButton(self.frame_2)
        self.btn_actualizar.setObjectName(u"btn_actualizar")
        self.btn_actualizar.setGeometry(QRect(130, 130, 111, 23))
        self.btn_actualizar.setStyleSheet(u"background:rgb(26, 193, 23);\n"
"")
        self.frame_3 = QFrame(From_Cuentas)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(270, 70, 421, 41))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.tableWidget = QTableWidget(From_Cuentas)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(270, 120, 421, 192))
        self.tableWidget.setStyleSheet(u"background:white;\n"
"color:black;")

        self.retranslateUi(From_Cuentas)

        QMetaObject.connectSlotsByName(From_Cuentas)
    # setupUi

    def retranslateUi(self, From_Cuentas):
        From_Cuentas.setWindowTitle(QCoreApplication.translate("From_Cuentas", u"Form", None))
        self.label.setText(QCoreApplication.translate("From_Cuentas", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Accounts</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("From_Cuentas", u"<html><head/><body><p><span style=\" font-size:11pt;\">      Name </span></p><p><br/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("From_Cuentas", u"<html><head/><body><p><span style=\" font-size:12pt;\">on acconunt :</span></p><p><br/></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("From_Cuentas", u"<html><head/><body><p><span style=\" font-size:11pt;\">Abonos de cliente</span><br/></p></body></html>", None))
        self.line_nombre.setPlaceholderText(QCoreApplication.translate("From_Cuentas", u"client", None))
        self.line_abono.setPlaceholderText(QCoreApplication.translate("From_Cuentas", u"$000", None))
        self.btn_save.setText(QCoreApplication.translate("From_Cuentas", u"Save", None))
        self.btn_actualizar.setText(QCoreApplication.translate("From_Cuentas", u"update", None))
    # retranslateUi

