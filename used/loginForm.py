# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import datetime , time

class Ui_LogonWindow(object):
    def setupUi(self, LogonWindow):
        LogonWindow.setObjectName("LogonWindow")
        LogonWindow.setEnabled(True)
        LogonWindow.setFixedSize(200, 184)
        self.centralwidget = QtWidgets.QWidget(LogonWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameLine = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLine.setGeometry(QtCore.QRect(10, 50, 180, 20))
        self.nameLine.setObjectName("nameLine")
        self.nameLine.setText('Artem')
        self.passLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passLine.setGeometry(QtCore.QRect(10, 80, 180, 20))
        self.passLine.setObjectName("passLine")
        self.passLine.setText('12345')
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(10, 110, 180, 41))
        self.loginButton.setObjectName("loginButton")
        LogonWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LogonWindow)
        self.statusbar.setObjectName("statusbar")
        LogonWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LogonWindow)
        QtCore.QMetaObject.connectSlotsByName(LogonWindow)
        self.loginButton.clicked.connect(self.login)

    def loginlabel_errLogin(self):
        self.label.setText('Wrong login or password')

    def retranslateUi(self, LogonWindow):
        _translate = QtCore.QCoreApplication.translate
        LogonWindow.setWindowTitle(_translate("LogonWindow", "Login"))
        self.label.setText(_translate("LogonWindow", "Input login and password"))
        self.loginButton.setText(_translate("LogonWindow", "Login"))

    def login(self):
        login = self.nameLine.text()
        pas = self.passLine.text()
        cursor.execute('SELECT id_employee FROM employee WHERE name=? AND password=?', [(login), (pas)])
        a = cursor.fetchone()
        if (a == None):
            self.loginlabel_errLogin()
        else:
            self.closing()