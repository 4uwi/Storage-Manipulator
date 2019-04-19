# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'history.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_history(object):
    def setupUi(self, history):
        history.setObjectName("history")
        history.resize(432, 413)
        self.incomeList_table = QtWidgets.QTableWidget(history)
        self.incomeList_table.setGeometry(QtCore.QRect(250, 100, 171, 301))
        self.incomeList_table.setColumnCount(3)
        self.incomeList_table.setObjectName("incomeList_table")
        self.incomeList_table.setRowCount(0)
        self.incomeList_table.horizontalHeader().setDefaultSectionSize(56)
        self.incomeList_table.horizontalHeader().setStretchLastSection(False)
        self.incomeHead_table = QtWidgets.QTableWidget(history)
        self.incomeHead_table.setGeometry(QtCore.QRect(10, 10, 231, 391))
        self.incomeHead_table.setColumnCount(4)
        self.incomeHead_table.setObjectName("incomeHead_table")
        self.incomeHead_table.setRowCount(0)
        self.incomeHead_table.horizontalHeader().setDefaultSectionSize(57)
        self.incomeHead_table.horizontalHeader().setStretchLastSection(False)
        self.label = QtWidgets.QLabel(history)
        self.label.setGeometry(QtCore.QRect(260, 10, 131, 16))
        self.label.setObjectName("label")
        self.nameProduct_label = QtWidgets.QLabel(history)
        self.nameProduct_label.setGeometry(QtCore.QRect(260, 30, 151, 31))
        self.nameProduct_label.setText("")
        self.nameProduct_label.setObjectName("nameProduct_label")

        self.retranslateUi(history)
        QtCore.QMetaObject.connectSlotsByName(history)

    def retranslateUi(self, history):
        _translate = QtCore.QCoreApplication.translate
        history.setWindowTitle(_translate("history", "Журнал"))
        self.label.setText(_translate("history", "Назва продукту:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    history = QtWidgets.QWidget()
    ui = Ui_history()
    ui.setupUi(history)
    history.show()
    sys.exit(app.exec_())

