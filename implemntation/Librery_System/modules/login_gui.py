# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import ctypes,subprocess,platform
import subprocess

from modules.Message import myMessage

class Ui_form(object):
    def setupUi(self, form : QMainWindow) -> None:
        if not form.objectName():
            form.setObjectName(u"form")
            
        if platform.system() == "Windows":
            user32 = ctypes.windll.user32   
            resolution = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        else:
            output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
            resolution = [int(x.decode('UTF-8')) for x in output.split()[0].split(b'x')]
            
        form.setWindowModality(Qt.NonModal)
        form.resize(400, 300)
        form.move(resolution[0]/2 - form.width()/2,resolution[1]/2 - form.height()/2)
        form.setMouseTracking(True)
        form.setContextMenuPolicy(Qt.NoContextMenu)
        form.setStyleSheet(u"QWidget{\n""	\n""	background-color: rgba(26, 20, 20, 204);\n""}")
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.offset = None
        
        self.exit = QPushButton(form)
        self.exit.clicked.connect(lambda: exit(0))
        self.exit.setStyleSheet(u"QPushButton{\n""}\n""\n""QPushButton:hover{\n""	background-color: rgb(255, 0, 0);\n""}")
        self.exit.setGeometry(form.width()-22,6,15,15)
        
        self.pushButton = QPushButton(form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 190, 200, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n""	color: rgb(255, 255, 255);\n""	background-color: rgb(0, 93, 243);\n""	border: none;\n""}\n""\n""QPushButton:hover{\n""	color: rgb(255, 255, 255);\n""	background-color: rgb(0, 64, 168);\n""	border: none;\n""}")
        
        self.username = QLineEdit(form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(100, 100, 200, 30))
        
        font = QFont()
        font.setPointSize(11)
        
        self.username.setFont(font)
        self.username.setStyleSheet(u"QLineEdit { \n""	color: white;\n""}")
        
        self.password = QLineEdit(form)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(100, 140, 200, 30))
        self.password.setFont(font)
        self.password.setStyleSheet(u"QLineEdit { \n""	color: white;\n""}")
        self.password.setEchoMode(QLineEdit.Password)
        
        self.label = QLabel(form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 131, 31))
        
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)
        
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n""	color: rgb(255, 255, 255);\n""}")
        
        self.label_2 = QLabel(form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 291, 21))
        
        font2 = QFont()
        font2.setFamily(u"DejaVu Sans")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50)
        
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n""	color: rgb(238, 238, 236);\n""}")
        
        self.message = myMessage(form,self)
        #self.message.setHeigth(50)
        
        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"Login", None))
        self.pushButton.setText(QCoreApplication.translate("form", u"Login", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("form", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("form", u"Password", None))
        self.label.setText(QCoreApplication.translate("form", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("form", u"Welcome back, please login in to your account", None))

    # retranslateUi                              
