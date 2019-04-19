# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addshipper.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addShipper(object):
    def setupUi(self, addShipper):
        addShipper.setObjectName("addShipper")
        addShipper.resize(215, 180)
        addShipper.setFixedSize(215, 180)
        self.nameSipper_label = QtWidgets.QLabel(addShipper)
        self.nameSipper_label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.nameSipper_label.setObjectName("nameSipper_label")
        self.phoneNumberShipper_label = QtWidgets.QLabel(addShipper)
        self.phoneNumberShipper_label.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.phoneNumberShipper_label.setObjectName("phoneNumberShipper_label")
        self.countryShipper_label = QtWidgets.QLabel(addShipper)
        self.countryShipper_label.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.countryShipper_label.setObjectName("countryShipper_label")
        self.addressShipper_label = QtWidgets.QLabel(addShipper)
        self.addressShipper_label.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.addressShipper_label.setObjectName("addressShipper_label")
        self.nameShipper_lineEdit = QtWidgets.QLineEdit(addShipper)
        self.nameShipper_lineEdit.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.nameShipper_lineEdit.setObjectName("nameShipper_lineEdit")
        self.phoneNumberShipper_lineEdit = QtWidgets.QLineEdit(addShipper)
        self.phoneNumberShipper_lineEdit.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.phoneNumberShipper_lineEdit.setObjectName("phoneNumberShipper_lineEdit")
        self.addresShipper_lineEdit = QtWidgets.QLineEdit(addShipper)
        self.addresShipper_lineEdit.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.addresShipper_lineEdit.setObjectName("addresShipper_lineEdit")
        self.countryShipper_comboBox = QtWidgets.QComboBox(addShipper)
        self.countryShipper_comboBox.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.countryShipper_comboBox.setObjectName("countryShipper_comboBox")
        self.saveShipper_pushButton = QtWidgets.QPushButton(addShipper)
        self.saveShipper_pushButton.setGeometry(QtCore.QRect(10, 130, 191, 41))
        self.saveShipper_pushButton.setObjectName("saveShipper_pushButton")

        self.retranslateUi(addShipper)
        QtCore.QMetaObject.connectSlotsByName(addShipper)

    def retranslateUi(self, addShipper):
        _translate = QtCore.QCoreApplication.translate
        addShipper.setWindowTitle(_translate("addShipper", "Add Shipper"))
        self.nameSipper_label.setText(_translate("addShipper", "Name shipper"))
        self.phoneNumberShipper_label.setText(_translate("addShipper", "Phone number"))
        self.countryShipper_label.setText(_translate("addShipper", "Country"))
        self.addressShipper_label.setText(_translate("addShipper", "Address"))
        self.saveShipper_pushButton.setText(_translate("addShipper", "Save"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addShipper = QtWidgets.QWidget()
    ui = Ui_addShipper()
    ui.setupUi(addShipper)
    addShipper.show()
    sys.exit(app.exec_())

