# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addproduct.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addProduct(object):
    def setupUi(self, addProduct):
        addProduct.setObjectName("addProduct")
        addProduct.resize(565, 464)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addProduct.sizePolicy().hasHeightForWidth())
        addProduct.setSizePolicy(sizePolicy)
        addProduct.setFixedSize(565, 464)
        self.nameProduct_label = QtWidgets.QLabel(addProduct)
        self.nameProduct_label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.nameProduct_label.setObjectName("nameProduct_label")
        self.barcodeProduct_label = QtWidgets.QLabel(addProduct)
        self.barcodeProduct_label.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.barcodeProduct_label.setObjectName("barcodeProduct_label")
        self.serteficateProduct_label = QtWidgets.QLabel(addProduct)
        self.serteficateProduct_label.setGeometry(QtCore.QRect(20, 80, 71, 21))
        self.serteficateProduct_label.setObjectName("serteficateProduct_label")
        self.countProduct_label = QtWidgets.QLabel(addProduct)
        self.countProduct_label.setGeometry(QtCore.QRect(20, 110, 51, 21))
        self.countProduct_label.setObjectName("countProduct_label")
        self.countProduct_label_2 = QtWidgets.QLabel(addProduct)
        self.countProduct_label_2.setGeometry(QtCore.QRect(20, 140, 51, 21))
        self.countProduct_label_2.setObjectName("countProduct_label_2")
        self.expirDataProduct_label = QtWidgets.QLabel(addProduct)
        self.expirDataProduct_label.setGeometry(QtCore.QRect(280, 20, 71, 16))
        self.expirDataProduct_label.setObjectName("expirDataProduct_label")
        self.expirDataProduct_datedit = QtWidgets.QDateEdit(addProduct)
        self.expirDataProduct_datedit.setGeometry(QtCore.QRect(280, 40, 131, 21))
        self.expirDataProduct_datedit.setCalendarPopup(True)
        self.expirDataProduct_datedit.setDate(QtCore.QDate(2019, 1, 1))
        self.expirDataProduct_datedit.setObjectName("expirDataProduct_datedit")
        self.serteficateProduct_lineEdit = QtWidgets.QLineEdit(addProduct)
        self.serteficateProduct_lineEdit.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.serteficateProduct_lineEdit.setObjectName("serteficateProduct_lineEdit")
        self.countProduct_lineEdit = QtWidgets.QLineEdit(addProduct)
        self.countProduct_lineEdit.setGeometry(QtCore.QRect(130, 110, 113, 20))
        self.countProduct_lineEdit.setObjectName("countProduct_lineEdit")
        self.unitProduct_lineEdit = QtWidgets.QLineEdit(addProduct)
        self.unitProduct_lineEdit.setGeometry(QtCore.QRect(130, 140, 113, 20))
        self.unitProduct_lineEdit.setObjectName("unitProduct_lineEdit")
        self.shipperProduct_label = QtWidgets.QLabel(addProduct)
        self.shipperProduct_label.setGeometry(QtCore.QRect(20, 170, 61, 21))
        self.shipperProduct_label.setObjectName("shipperProduct_label")
        self.shipperProduct_combobox = QtWidgets.QComboBox(addProduct)
        self.shipperProduct_combobox.setGeometry(QtCore.QRect(130, 170, 113, 20))
        self.shipperProduct_combobox.setEditable(True)
        self.shipperProduct_combobox.setObjectName("shipperProduct_combobox")
        self.addShipper_pushbutton = QtWidgets.QPushButton(addProduct)
        self.addShipper_pushbutton.setGeometry(QtCore.QRect(130, 200, 111, 31))
        self.addShipper_pushbutton.setObjectName("addShipper_pushbutton")
        self.nameProduct_combobox = QtWidgets.QComboBox(addProduct)
        self.nameProduct_combobox.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.nameProduct_combobox.setEditable(True)
        self.nameProduct_combobox.setObjectName("nameProduct_combobox")
        self.barcodeProduct_combox = QtWidgets.QComboBox(addProduct)
        self.barcodeProduct_combox.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.barcodeProduct_combox.setEditable(True)
        self.barcodeProduct_combox.setObjectName("barcodeProduct_combox")
        self.saveProduct_pushbutton = QtWidgets.QPushButton(addProduct)
        self.saveProduct_pushbutton.setGeometry(QtCore.QRect(20, 270, 101, 31))
        self.saveProduct_pushbutton.setObjectName("saveProduct_pushbutton")
        self.cancel_pushbutton = QtWidgets.QPushButton(addProduct)
        self.cancel_pushbutton.setGeometry(QtCore.QRect(130, 270, 101, 31))
        self.cancel_pushbutton.setObjectName("cancel_pushbutton")
        self.listView = QtWidgets.QListView(addProduct)
        self.listView.setGeometry(QtCore.QRect(6, 310, 553, 151))
        self.listView.setObjectName("listView")

        self.retranslateUi(addProduct)
        QtCore.QMetaObject.connectSlotsByName(addProduct)

    def retranslateUi(self, addProduct):
        _translate = QtCore.QCoreApplication.translate
        addProduct.setWindowTitle(_translate("addProduct", "Add Product"))
        self.nameProduct_label.setText(_translate("addProduct", "Product name"))
        self.barcodeProduct_label.setText(_translate("addProduct", "Product Barcode"))
        self.serteficateProduct_label.setText(_translate("addProduct", "Serteficate"))
        self.countProduct_label.setText(_translate("addProduct", "Count"))
        self.countProduct_label_2.setText(_translate("addProduct", "Unit"))
        self.expirDataProduct_label.setText(_translate("addProduct", "Expir Data"))
        self.shipperProduct_label.setText(_translate("addProduct", "Shipper"))
        self.addShipper_pushbutton.setText(_translate("addProduct", "Add Shipper"))
        self.saveProduct_pushbutton.setText(_translate("addProduct", "Save"))
        self.cancel_pushbutton.setText(_translate("addProduct", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addProduct = QtWidgets.QWidget()
    ui = Ui_addProduct()
    ui.setupUi(addProduct)
    addProduct.show()
    sys.exit(app.exec_())

