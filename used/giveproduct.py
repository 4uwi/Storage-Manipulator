# -*- coding: utf-8 -*-

# GiveProduct implementation generated from reading ui file 'giveproduct.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GiveProduct(object):
    def setupUi(self, GiveProduct):
        GiveProduct.setObjectName("GiveProduct")
        GiveProduct.resize(331, 300)
        self.lineEdit = QtWidgets.QLineEdit(GiveProduct)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.PrductName_label = QtWidgets.QLabel(GiveProduct)
        self.PrductName_label.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.PrductName_label.setObjectName("PrductName_label")
        self.nameProduct_label = QtWidgets.QLabel(GiveProduct)
        self.nameProduct_label.setGeometry(QtCore.QRect(130, 60, 47, 13))
        self.nameProduct_label.setText("")
        self.nameProduct_label.setObjectName("nameProduct_label")
        self.ProductCount_label = QtWidgets.QLabel(GiveProduct)
        self.ProductCount_label.setGeometry(QtCore.QRect(200, 60, 47, 13))
        self.ProductCount_label.setObjectName("ProductCount_label")
        self.countProduct_label = QtWidgets.QLabel(GiveProduct)
        self.countProduct_label.setGeometry(QtCore.QRect(260, 60, 47, 13))
        self.countProduct_label.setText("")
        self.countProduct_label.setObjectName("countProduct_label")
        self.howMany_label = QtWidgets.QLabel(GiveProduct)
        self.howMany_label.setGeometry(QtCore.QRect(10, 110, 141, 16))
        self.howMany_label.setObjectName("howMany_label")
        self.countProuct_linedit = QtWidgets.QLineEdit(GiveProduct)
        self.countProuct_linedit.setGeometry(QtCore.QRect(170, 110, 71, 20))
        self.countProuct_linedit.setObjectName("countProuct_linedit")
        self.given_listview = QtWidgets.QListView(GiveProduct)
        self.given_listview.setGeometry(QtCore.QRect(10, 140, 311, 151))
        self.given_listview.setObjectName("given_listview")
        self.giveProduct_pushButton = QtWidgets.QPushButton(GiveProduct)
        self.giveProduct_pushButton.setGeometry(QtCore.QRect(254, 110, 61, 23))
        self.giveProduct_pushButton.setObjectName("giveProduct_pushButton")

        self.retranslateUi(GiveProduct)
        QtCore.QMetaObject.connectSlotsByName(GiveProduct)

    def retranslateUi(self, GiveProduct):
        _translate = QtCore.QCoreApplication.translate
        GiveProduct.setWindowTitle(_translate("GiveProduct", "Give product"))
        self.PrductName_label.setText(_translate("GiveProduct", "Product name:"))
        self.ProductCount_label.setText(_translate("GiveProduct", "Count"))
        self.howMany_label.setText(_translate("GiveProduct", "How many you want to give"))
        self.giveProduct_pushButton.setText(_translate("GiveProduct", "Give"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GiveProduct = QtWidgets.QWidget()
    ui = Ui_GiveProduct()
    ui.setupUi(GiveProduct)
    GiveProduct.show()
    sys.exit(app.exec_())

