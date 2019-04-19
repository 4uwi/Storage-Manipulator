import sys
import datetime
import sqlite3
import re
from PyQt5 import QtCore, QtGui, QtWidgets

conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()

password_for_operation = "admin"

class sql():
    res = []

class employee():
    login: str = ""
    pas: str = ""

class Ui_StorageMap(object):
    def setupUi(self, StorageMap):
        StorageMap.setWindowIcon(ico)
        StorageMap.setObjectName("Storage Map")
        StorageMap.resize(651, 451)
        StorageMap.setStyleSheet("image: url(./map.png)\n"
"")
        self.pushButton_1 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_1.setGeometry(QtCore.QRect(12, 13, 252, 38))
        self.pushButton_1.setStyleSheet("")
        self.pushButton_1.setFlat(True)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_2.setGeometry(QtCore.QRect(13, 62, 251, 42))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_3.setGeometry(QtCore.QRect(13, 116, 251, 38))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_4.setGeometry(QtCore.QRect(14, 166, 251, 41))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_5.setGeometry(QtCore.QRect(15, 222, 251, 37))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_6.setGeometry(QtCore.QRect(15, 270, 252, 42))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_7.setGeometry(QtCore.QRect(14, 331, 252, 37))
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_8.setGeometry(QtCore.QRect(14, 380, 253, 41))
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_9.setGeometry(QtCore.QRect(374, 9, 252, 39))
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_10.setGeometry(QtCore.QRect(373, 59, 254, 42))
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_11.setGeometry(QtCore.QRect(376, 114, 252, 38))
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_12.setGeometry(QtCore.QRect(377, 163, 252, 42))
        self.pushButton_12.setFlat(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_13.setGeometry(QtCore.QRect(377, 220, 252, 38))
        self.pushButton_13.setFlat(True)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_14.setGeometry(QtCore.QRect(378, 269, 252, 41))
        self.pushButton_14.setFlat(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_15.setGeometry(QtCore.QRect(378, 328, 252, 37))
        self.pushButton_15.setFlat(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(StorageMap)
        self.pushButton_16.setGeometry(QtCore.QRect(379, 377, 251, 41))
        self.pushButton_16.setAutoFillBackground(False)
        self.pushButton_16.setFlat(True)
        self.pushButton_16.setObjectName("pushButton_16")

        self.retranslateUi(StorageMap)
        QtCore.QMetaObject.connectSlotsByName(StorageMap)

    def retranslateUi(self, StorageMap):
        _translate = QtCore.QCoreApplication.translate
        StorageMap.setWindowTitle(_translate("StorageMap", "Мапа складу"))
        self.pushButton_1.setText(_translate("StorageMap", "C1S[1-10]F[1-5]"))
        self.pushButton_2.setText(_translate("StorageMap", "C2S[1-10]F[1-5]"))
        self.pushButton_3.setText(_translate("StorageMap", "C3S[1-10]F[1-5]"))
        self.pushButton_4.setText(_translate("StorageMap", "C4S[1-10]F[1-5]"))
        self.pushButton_5.setText(_translate("StorageMap", "C5S[1-10]F[1-5]"))
        self.pushButton_6.setText(_translate("StorageMap", "C6S[1-10]F[1-5]"))
        self.pushButton_7.setText(_translate("StorageMap", "C7S[1-10]F[1-5]"))
        self.pushButton_8.setText(_translate("StorageMap", "C8S[1-10]F[1-5]"))
        self.pushButton_9.setText(_translate("StorageMap", "C9S[1-10]F[1-5]"))
        self.pushButton_10.setText(_translate("StorageMap", "C10S[1-10]F[1-5]"))
        self.pushButton_11.setText(_translate("StorageMap", "C11S[1-10]F[1-5]"))
        self.pushButton_12.setText(_translate("StorageMap", "C12S[1-10]F[1-5]"))
        self.pushButton_13.setText(_translate("StorageMap", "C13S[1-10]F[1-5]"))
        self.pushButton_14.setText(_translate("StorageMap", "C14S[1-10]F[1-5]"))
        self.pushButton_15.setText(_translate("StorageMap", "C15S[1-10]F[1-5]"))
        self.pushButton_16.setText(_translate("StorageMap", "C16S[1-10]F[1-5]"))
        self.pushButton_1.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_1.objectName()))
        self.pushButton_2.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_2.objectName()))
        self.pushButton_3.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_3.objectName()))
        self.pushButton_4.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_4.objectName()))
        self.pushButton_5.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_5.objectName()))
        self.pushButton_6.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_6.objectName()))
        self.pushButton_7.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_7.objectName()))
        self.pushButton_8.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_8.objectName()))
        self.pushButton_9.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_9.objectName()))
        self.pushButton_10.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_10.objectName()))
        self.pushButton_11.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_11.objectName()))
        self.pushButton_12.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_12.objectName()))
        self.pushButton_13.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_13.objectName()))
        self.pushButton_14.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_14.objectName()))
        self.pushButton_15.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_15.objectName()))
        self.pushButton_16.clicked.connect(lambda: self.viewProductFromMap(self.pushButton_16.objectName()))

    def viewProductFromMap(self, map_button_index_str):
        MainWindowUi.productListWidget.clear()
        but_num = map_button_index_str[11:]
        que = "SELECT name_product, sertificate, count, unit, place FROM product WHERE place LIKE '%c" + but_num + "%' "
        sql.res = cursor.execute(que).fetchall()
        MainWindowUi.productListUpdate()
        StorageMap.hide()

class Ui_GiveProduct(object):
    def setupUi(self, GiveProduct):
        GiveProduct.setObjectName("GiveProduct")
        GiveProduct.resize(331, 300)
        GiveProduct.setWindowIcon(ico)
        self.lineEdit = QtWidgets.QLineEdit(GiveProduct)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 311, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.ProductName_label = QtWidgets.QLabel(GiveProduct)
        self.ProductName_label.setGeometry(QtCore.QRect(10, 60, 90, 16))
        self.ProductName_label.setObjectName("ProductName_label")
        self.nameProduct_label = QtWidgets.QLabel(GiveProduct)
        self.nameProduct_label.setGeometry(QtCore.QRect(100,60, 150, 16))
        self.nameProduct_label.setText("")
        self.nameProduct_label.setObjectName("nameProduct_label")
        self.ProductCount_label = QtWidgets.QLabel(GiveProduct)
        self.ProductCount_label.setGeometry(QtCore.QRect(240, 60, 49, 13))
        self.ProductCount_label.setObjectName("ProductCount_label")
        self.countProduct_label = QtWidgets.QLabel(GiveProduct)
        self.countProduct_label.setGeometry(QtCore.QRect(290, 60, 49, 13))
        self.countProduct_label.setText("")
        self.areDelete_pushbutton = QtWidgets.QPushButton(GiveProduct)
        self.areDelete_pushbutton.setGeometry(QtCore.QRect(240,78, 60, 19))
        self.areDelete_pushbutton.setObjectName("areDelete_pushbutton")
        self.areDelete_pushbutton.setDisabled(True)
        self.countProduct_label.setObjectName("countProduct_label")
        self.howMany_label = QtWidgets.QLabel(GiveProduct)
        self.howMany_label.setGeometry(QtCore.QRect(10, 110, 141, 16))
        self.howMany_label.setObjectName("howMany_label")
        self.countProuct_linedit = QtWidgets.QLineEdit(GiveProduct)
        self.countProuct_linedit.setGeometry(QtCore.QRect(170, 110, 71, 20))
        self.countProuct_linedit.setObjectName("countProuct_linedit")
        self.given_listview = QtWidgets.QListWidget(GiveProduct)
        self.given_listview.setGeometry(QtCore.QRect(10, 140, 311, 151))
        self.given_listview.setObjectName("given_listview")
        self.giveProduct_pushButton = QtWidgets.QPushButton(GiveProduct)
        self.giveProduct_pushButton.setGeometry(QtCore.QRect(254, 109, 68, 23))
        self.giveProduct_pushButton.setObjectName("giveProduct_pushButton")
        self.lineEdit.textChanged.connect(self.searchTextEdited)
        self.given_listview.clicked.connect(self.listItemSelected)
        self.giveProduct_pushButton.clicked.connect(self.giveProduct)
        self.areDelete_pushbutton.clicked.connect(self.delete0item)
        self.retranslateUi(GiveProduct)
        QtCore.QMetaObject.connectSlotsByName(GiveProduct)

    def delete0item(self):
        que = "DELETE FROM product WHERE name_product = '"+self.nameProduct_label.text()+"' AND count = '0'"
        cursor.execute(que)
        conn.commit()
        self.searchTextEdited()

    def searchTextEdited(self):
        if(self.lineEdit.text() == ""):
            self.given_listview.clear()
        else:
            self.given_listview.clear()
            que = "SELECT name_product, count FROM product WHERE name_product LIKE '%" + self.lineEdit.text() +"%'"
            names = cursor.execute(que).fetchall()
            for row_number, item in enumerate(names):
                self.given_listview.insertItem(row_number, str(item).strip("()"))

    def listItemSelected(self, index):
        self.areDelete_pushbutton.setDisabled(True)
        text = self.given_listview.itemFromIndex(index).text()
        count = re.findall('\d+', text)
        i = 0
        name = ""
        while text[i] !=',':
            name += text[i]
            i += 1
        if(count[0] == "0"):
            self.areDelete_pushbutton.setEnabled(True)
        self.countProduct_label.setText(count[0])
        self.nameProduct_label.setText(name.strip("'"))

    def giveProduct(self):
        if ( re.match('^\D+$', self.countProuct_linedit.text()) or self.countProuct_linedit.text() == '' or int(self.countProuct_linedit.text()) <= 0 or self.countProduct_label.text() == '' or int(self.countProduct_label.text()) <= 0 or self.countProuct_linedit.text() == "Помилка!"):
            self.countProuct_linedit.setText("Помилка!")
        else:
            have = int(self.countProduct_label.text())
            want = int(self.countProuct_linedit.text())
            if (have >= want):
                count = int(self.countProduct_label.text()) - int(self.countProuct_linedit.text())
                que = "UPDATE product SET count = '" + str(count) + "'WHERE name_product ='" + self.nameProduct_label.text() + "'"
                cursor.execute(que)
                conn.commit()
                que = "SELECT id_employee FROM employee WHERE name = '" + employee.login + "'"
                id_employee = str(cursor.execute(que).fetchone()).strip("(,')")
                que = "SELECT MAX(id_income) FROM income_head"
                id_income = str(cursor.execute(que).fetchone()).strip("(,')")
                if(id_income != None):
                    id_income = int(id_income) + 1
                else:
                    id_income = 1
                que = "INSERT INTO income_head VALUES ('" + str(
                    datetime.datetime.today().replace(microsecond=0)) + "','" + str(id_employee) + "','" + str(
                    id_income) + "','outcome')"
                cursor.execute(que)
                conn.commit()
                que = "SELECT id_product FROM product WHERE name_product='" + self.nameProduct_label.text() + "'"
                id_product = str(cursor.execute(que).fetchone()).strip("(,')")
                que = "INSERT INTO income_list VALUES ('" + str(id_product) + "','" + str(id_income) + "', '"+ str(self.countProuct_linedit.text())+"')"
                cursor.execute(que)
                conn.commit()
                self.countProuct_linedit.clear()
                self.searchTextEdited()
            else:
                self.countProuct_linedit.setText("Помилка!")


    def retranslateUi(self, GiveProduct):
        _translate = QtCore.QCoreApplication.translate
        GiveProduct.setWindowTitle(_translate("GiveProduct", "Видати продукт"))
        self.ProductName_label.setText(_translate("GiveProduct", "Назва продукту:"))
        self.ProductCount_label.setText(_translate("GiveProduct", "Кількість:"))
        self.howMany_label.setText(_translate("GiveProduct", "Кількість видачі:"))
        self.giveProduct_pushButton.setText(_translate("GiveProduct", "Видати"))
        self.areDelete_pushbutton.setText(_translate("GiveProduct", "Видалити?"))

class Ui_addShipper(object):
    def setupUi(self, addShipper):
        AddShipper.setWindowIcon(ico)
        addShipper.setObjectName("addShipper")
        addShipper.resize(265, 180)
        addShipper.setFixedSize(265, 180)
        self.nameSipper_label = QtWidgets.QLabel(addShipper)
        self.nameSipper_label.setGeometry(QtCore.QRect(10, 10, 113, 16))
        self.nameSipper_label.setObjectName("nameSipper_label")
        self.phoneNumberShipper_label = QtWidgets.QLabel(addShipper)
        self.phoneNumberShipper_label.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.phoneNumberShipper_label.setObjectName("phoneNumberShipper_label")
        self.countryShipper_label = QtWidgets.QLabel(addShipper)
        self.countryShipper_label.setGeometry(QtCore.QRect(10, 70, 97, 13))
        self.countryShipper_label.setObjectName("countryShipper_label")
        self.addressShipper_label = QtWidgets.QLabel(addShipper)
        self.addressShipper_label.setGeometry(QtCore.QRect(10, 100, 97, 13))
        self.addressShipper_label.setObjectName("addressShipper_label")
        self.nameShipper_lineEdit = QtWidgets.QLineEdit(addShipper)
        self.nameShipper_lineEdit.setGeometry(QtCore.QRect(140, 10, 113, 20))
        self.nameShipper_lineEdit.setObjectName("nameShipper_lineEdit")
        self.phoneNumberShipper_lineEdit = QtWidgets.QLineEdit(addShipper)
        self.phoneNumberShipper_lineEdit.setGeometry(QtCore.QRect(140, 40, 113, 20))
        self.phoneNumberShipper_lineEdit.setObjectName("phoneNumberShipper_lineEdit")
        self.addresShipper_lineEdit = QtWidgets.QLineEdit(addShipper)
        self.addresShipper_lineEdit.setGeometry(QtCore.QRect(140, 100, 113, 20))
        self.addresShipper_lineEdit.setObjectName("addresShipper_lineEdit")
        self.countryShipper_comboBox = QtWidgets.QComboBox(addShipper)
        self.countryShipper_comboBox.setGeometry(QtCore.QRect(140, 70, 113, 20))
        self.countryShipper_comboBox.setObjectName("countryShipper_comboBox")
        self.saveShipper_pushButton = QtWidgets.QPushButton(addShipper)
        self.saveShipper_pushButton.setGeometry(QtCore.QRect(10, 130, 241, 41))
        self.saveShipper_pushButton.setObjectName("saveShipper_pushButton")
        self.load_countries()
        self.nameShipper_lineEdit.textChanged.connect(lambda : self.nameSipper_label.setText("Назва постачальника"))
        self.saveShipper_pushButton.clicked.connect(self.addShipper)
        self.retranslateUi(addShipper)
        QtCore.QMetaObject.connectSlotsByName(addShipper)

    def load_countries(self):
        f = open("countries.txt", "r")
        i = 0
        while i < 241:
            item = f.readline().strip()
            self.countryShipper_comboBox.addItem(item, str)
            i += 1

    def addShipper(self):
        ch = True

        if(self.nameShipper_lineEdit.text() == "" or self.nameShipper_lineEdit.text() == "Помилка!" or self.nameShipper_lineEdit.text() == " "):
            self.nameShipper_lineEdit.setText("Помилка!")
            ch = False

        if(self.addresShipper_lineEdit.text() == "" or self.addresShipper_lineEdit.text() == "Помилка!" or self.addresShipper_lineEdit.text() == " "):
            self.addresShipper_lineEdit.setText("Помилка!")
            ch = False

        if(self.phoneNumberShipper_lineEdit.text() == "" or self.phoneNumberShipper_lineEdit.text() == "Помилка!" or re.match('^\D+={,10}$',self.phoneNumberShipper_lineEdit.text())):
            self.phoneNumberShipper_lineEdit.setText("Помилка!")
            ch = False

        if ch != False:
            que = "SELECT id_shipper FROM shipper WHERE name_shipper ='" + str(self.nameShipper_lineEdit.text()) + "'"
            id_shipper_check = cursor.execute(que).fetchone()
            if(id_shipper_check == None):
                que = "SELECT Max(id_shipper) FROM shipper"
                id_shipper = int(str(cursor.execute(que).fetchone()).strip("(,)"))
                id_shipper += 1
                que = "INSERT INTO shipper VALUES('"+self.nameShipper_lineEdit.text()+"','"+str(id_shipper)+"','"+str(self.phoneNumberShipper_lineEdit.text())+"','"+str(self.addresShipper_lineEdit.text())+"','"+str(self.countryShipper_comboBox.currentText())+"')"
                cursor.execute(que)
                conn.commit()
                self.phoneNumberShipper_lineEdit.clear()
                self.addresShipper_lineEdit.clear()
                self.nameShipper_lineEdit.clear()
                AddShipper.hide()
                AddProductUi.load_shippers()
            else:
                self.nameSipper_label.setText("Уже існує")

    def retranslateUi(self, addShipper):
        _translate = QtCore.QCoreApplication.translate
        addShipper.setWindowTitle(_translate("addShipper", "Додати постачальника"))
        self.nameSipper_label.setText(_translate("addShipper", "Назва постачальника"))
        self.phoneNumberShipper_label.setText(_translate("addShipper", "Телефонний номер"))
        self.countryShipper_label.setText(_translate("addShipper", "Країна"))
        self.addressShipper_label.setText(_translate("addShipper", "Адресс"))
        self.saveShipper_pushButton.setText(_translate("addShipper", "Зберегти"))

class Ui_addProduct(object):
    def setupUi(self, addProduct):
        addProduct.setWindowIcon(ico)
        addProduct.setObjectName("addProduct")
        addProduct.resize(565, 514)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addProduct.sizePolicy().hasHeightForWidth())
        addProduct.setSizePolicy(sizePolicy)
        addProduct.setFixedSize(565, 514)
        self.nameProduct_label = QtWidgets.QLabel(addProduct)
        self.nameProduct_label.setGeometry(QtCore.QRect(20, 20, 90, 21))
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
        self.expirDataProduct_label.setGeometry(QtCore.QRect(280, 20, 90, 16))
        self.expirDataProduct_label.setObjectName("expirDataProduct_label")
        self.expirDataProduct_datedit = QtWidgets.QDateEdit(addProduct)
        self.expirDataProduct_datedit.setGeometry(QtCore.QRect(280, 40, 131, 21))
        self.expirDataProduct_datedit.setCalendarPopup(True)
        self.expirDataProduct_datedit.setDate(datetime.datetime.today())
        self.expirDataProduct_datedit.setDisplayFormat("yyyy-MM-dd")
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
        self.shipperProduct_label.setGeometry(QtCore.QRect(20, 170, 90, 21))
        self.shipperProduct_label.setObjectName("shipperProduct_label")
        self.shipperProduct_combobox = QtWidgets.QComboBox(addProduct)
        self.shipperProduct_combobox.setGeometry(QtCore.QRect(130, 170, 113, 20))
        self.shipperProduct_combobox.setEditable(False)
        self.shipperProduct_combobox.setObjectName("shipperProduct_combobox")
        self.addShipper_pushbutton = QtWidgets.QPushButton(addProduct)
        self.addShipper_pushbutton.setGeometry(QtCore.QRect(111, 250, 130, 31))
        self.addShipper_pushbutton.setObjectName("addShipper_pushbutton")
        self.nameProduct_linedit = QtWidgets.QLineEdit(addProduct)
        self.nameProduct_linedit.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.nameProduct_linedit.setObjectName("nameProduct_linedit")
        self.barcodeProduct_linedit = QtWidgets.QLineEdit(addProduct)
        self.barcodeProduct_linedit.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.placeProduct_linedit = QtWidgets.QLineEdit(addProduct)
        self.placeProduct_linedit.setGeometry(QtCore.QRect(130, 200 , 113, 20))
        self.placeProduct_label = QtWidgets.QLabel(addProduct)
        self.placeProduct_label.setGeometry(QtCore.QRect(20, 200, 130, 21))
        self.dateTimeErro_label = QtWidgets.QLabel(addProduct)
        self.dateTimeErro_label.setGeometry(QtCore.QRect(430,40, 131, 21))#280, 40, 131, 21
        self.dateTimeErro_label.setText("")

        self.barcodeProduct_linedit.setObjectName("barcodeProduct_linedit")
        self.saveProduct_pushbutton = QtWidgets.QPushButton(addProduct)
        self.saveProduct_pushbutton.setGeometry(QtCore.QRect(20, 320, 101, 31))
        self.saveProduct_pushbutton.setObjectName("saveProduct_pushbutton")
        self.cancel_pushbutton = QtWidgets.QPushButton(addProduct)
        self.cancel_pushbutton.setGeometry(QtCore.QRect(130, 320, 101, 31))
        self.cancel_pushbutton.setObjectName("cancel_pushbutton")
        self.listWidget = QtWidgets.QListWidget(addProduct)
        self.listWidget.setGeometry(QtCore.QRect(6, 360, 553, 151))
        self.listWidget.setObjectName("listWidget")
        self.delShippers()
        self.load_shippers()
        self.saveProduct_pushbutton.clicked.connect(self.addProduct)
        self.cancel_pushbutton.clicked.connect(self.cancel)

        self.retranslateUi(addProduct)
        QtCore.QMetaObject.connectSlotsByName(addProduct)
        self.addShipper_pushbutton.clicked.connect(self.addshipper)

    def delShippers(self):
        que = "DELETE FROM shipper WHERE id_shipper NOT IN(SELECT id_shipper FROM product)"
        cursor.execute(que)
        conn.commit()

    def cancel(self):
        AddProduct.hide()
        MainWindow.show()

    def load_shippers(self):
        self.shipperProduct_combobox.clear()
        que = "SELECT name_shipper FROM shipper"
        shippers = cursor.execute(que).fetchall()
        for item in shippers:
            self.shipperProduct_combobox.addItem(str(item).strip("(',')"),userData=str)

    def addProduct(self):
        ch = True

        if(self.nameProduct_linedit.text() == " " or  not(re.match('\w+', self.nameProduct_linedit.text())) or self.nameProduct_linedit.text() == "Помилка!"):
            self.nameProduct_linedit.setText("Помилка!")
            ch = False

        if(self.barcodeProduct_linedit.text() == " " or not(re.match('\d={,14}', self.barcodeProduct_linedit.text())) or self.barcodeProduct_linedit.text() == "Помилка!"):
            self.barcodeProduct_linedit.setText("Помилка!")
            ch = False

        if(self.serteficateProduct_lineEdit.text() == " " or not(re.match('^.+={,25}$', self.serteficateProduct_lineEdit.text())) or self.serteficateProduct_lineEdit.text() == "Помилка!"):
            self.serteficateProduct_lineEdit.setText("Помилка!")
            ch = False

        if(self.countProduct_lineEdit.text() == " " or not(re.match('^\d+={,10}$', self.countProduct_lineEdit.text())) or self.countProduct_lineEdit.text() == "Помилка!"):
            self.countProduct_lineEdit.setText("Помилка!")
            ch = False

        if(self.unitProduct_lineEdit.text() == " " or not(re.match('^.+={,5}$', self.unitProduct_lineEdit.text())) or self.unitProduct_lineEdit.text() == "Помилка!"):
            self.unitProduct_lineEdit.setText("Помилка!")
            ch = False

        if(self.placeProduct_linedit.text() == " " or not(re.match(r'c[\d+]s[\d+]f[\d+]', self.placeProduct_linedit.text())) or self.placeProduct_linedit.text() == "Помилка!"):
            self.placeProduct_linedit.setText("Помилка!")
            ch = False

        if(self.expirDataProduct_datedit.date() <= datetime.date.today() or self.expirDataProduct_datedit.date() == "Помилка!"):
            self.dateTimeErro_label.setText("Помылка!")
            ch = False

        if ch == True:
            que = "SELECT id_shipper FROM shipper WHERE name_shipper='" + self.shipperProduct_combobox.currentText()+ "'"
            cursor.execute(que)
            shipper_id = str(cursor.fetchone()).strip("(,)")

            que = "SELECT MAX(id_product) FROM product"
            product_id = str(cursor.execute(que).fetchone()).strip("(,)")
            id_product = int(product_id)
            id_product += 1

            que = "SELECT barcode FROM product WHERE name_product = '"+str(self.nameProduct_linedit.text())+ "' AND id_shipper ='"+ shipper_id + "'"
            res = cursor.execute(que).fetchone()

            if(res == None):
                que = "INSERT INTO product VALUES ('"+str(id_product)+"','" + str(self.barcodeProduct_linedit.text()) + "', '"+ str(self.nameProduct_linedit.text()) + "','" + str(self.serteficateProduct_lineEdit.text()) + "', '"+self.expirDataProduct_datedit.date().toString() +"', '"+str(self.countProduct_lineEdit.text())+"', '"+ str(self.unitProduct_lineEdit.text())+"','"+str(self.placeProduct_linedit.text())+"', '"+str(shipper_id)+"')"
                cursor.execute(que)
                conn.commit()

                que = "SELECT id_employee FROM employee WHERE name = '" + employee.login + "'"
                id_employee = str(cursor.execute(que).fetchone()).strip("(,')")
                que = "SELECT MAX(id_income) FROM income_head"
                id_income = str(cursor.execute(que).fetchone()).strip("(,')")
                if (id_income != None):
                    id_income = int(id_income) + 1
                else:
                    id_income = 1
                que = "INSERT INTO income_head VALUES ('" + str(
                    datetime.datetime.today().replace(microsecond=0)) + "','" + str(id_employee) + "','" + str(
                    id_income) + "','income')"
                cursor.execute(que)
                conn.commit()
                que = "SELECT id_product FROM product WHERE name_product='" + str(self.nameProduct_linedit.text()) + "'"
                id_product = str(cursor.execute(que).fetchone()).strip("(,')")
                que = "INSERT INTO income_list VALUES ('" + str(id_product) + "','" + str(id_income) + "', '"+ str(self.countProduct_lineEdit.text())+"')"
                cursor.execute(que)
                conn.commit()

                item = str(str(id_product) + ", " + str(self.barcodeProduct_linedit.text()) + ", " + str(self.nameProduct_linedit.text()) + ", " + str(self.serteficateProduct_lineEdit.text()) + ", " + self.expirDataProduct_datedit.date().toString() + ", " + str(self.countProduct_lineEdit.text()) + ", " + str(self.unitProduct_lineEdit.text()) + ", " + str(self.placeProduct_linedit.text()) + ", " + str(shipper_id)+"")
                items = QtWidgets.QListWidgetItem()
                items.setText(item)
                self.listWidget.addItem(items)

            else:
                que = "SELECT count FROM product WHERE name_product ='"+str(self.nameProduct_linedit.text())+"'"
                count = int(str(cursor.execute(que).fetchone()).strip("(,)"))
                count += int(self.countProduct_lineEdit.text())
                que = "UPDATE product SET count = '"+str(count)+ "' WHERE name_product = '" + str(self.nameProduct_linedit.text())+"'"
                cursor.execute(que)
                conn.commit()

                que = "SELECT id_employee FROM employee WHERE name = '" + employee.login + "'"
                id_employee = str(cursor.execute(que).fetchone()).strip("(,')")
                que = "SELECT MAX(id_income) FROM income_head"
                id_income = str(cursor.execute(que).fetchone()).strip("(,')")
                if (id_income != None):
                    id_income = int(id_income) + 1
                else:
                    id_income = 1
                que = "INSERT INTO income_head VALUES ('" + str(
                    datetime.datetime.today().replace(microsecond=0)) + "','" + str(id_employee) + "','" + str(
                    id_income) + "','adding')"
                cursor.execute(que)
                conn.commit()
                que = "SELECT id_product FROM product WHERE name_product='" + str(self.nameProduct_linedit.text()) + "'"
                id_product = str(cursor.execute(que).fetchone()).strip("(,')")
                que = "INSERT INTO income_list VALUES ('" + str(id_product) + "','" + str(id_income) + "', '"+ str(self.countProduct_lineEdit.text())+"')"
                cursor.execute(que)
                conn.commit()

                item = str(str(id_product) + ", " + str(self.barcodeProduct_linedit.text()) + ", " + str(self.nameProduct_linedit.text()) + ", " + str(self.serteficateProduct_lineEdit.text()) + ", " + self.expirDataProduct_datedit.date().toString() + ", " + str(self.countProduct_lineEdit.text()) + ", " + str(self.unitProduct_lineEdit.text()) + ", " + str(self.placeProduct_linedit.text()) + ", " + str(shipper_id)+"")
                items = QtWidgets.QListWidgetItem()
                items.setText(item)
                self.listWidget.addItem(items)

            self.serteficateProduct_lineEdit.clear()
            self.unitProduct_lineEdit.clear()
            self.placeProduct_linedit.clear()
            self.countProduct_lineEdit.clear()
            self.nameProduct_linedit.clear()
            self.barcodeProduct_linedit.clear()
            self.placeProduct_linedit.clear()
            self.dateTimeErro_label.clear()


    def addshipper(self):
        AddShipper.show()

    def retranslateUi(self, addProduct):
        _translate = QtCore.QCoreApplication.translate
        addProduct.setWindowTitle(_translate("addProduct", "Додати продукт"))
        self.placeProduct_label.setText(_translate("addProduct", "Мiсце продукту"))
        self.nameProduct_label.setText(_translate("addProduct", "Назва продукту"))
        self.barcodeProduct_label.setText(_translate("addProduct", "Штрих-код"))
        self.serteficateProduct_label.setText(_translate("addProduct", "Сетрифікат"))
        self.countProduct_label.setText(_translate("addProduct", "Кількість"))
        self.countProduct_label_2.setText(_translate("addProduct", "Міра виміру"))
        self.expirDataProduct_label.setText(_translate("addProduct", "Срок придатності"))
        self.shipperProduct_label.setText(_translate("addProduct", "Постачальник"))
        self.addShipper_pushbutton.setText(_translate("addProduct", "Додати постачальника"))
        self.saveProduct_pushbutton.setText(_translate("addProduct", "Зберегти"))
        self.cancel_pushbutton.setText(_translate("addProduct", "Відміна"))

class Ui_LogonWindow(object):
    def setupUi(self, LogonWindow):
        LogonWindow.setWindowIcon(ico)
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
        f = open("loginfo.txt")
        employee.login = f.readline().strip()
        self.nameLine.setText(employee.login)
        self.passLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passLine.setGeometry(QtCore.QRect(10, 80, 180, 20))
        employee.pas = f.readline().strip()
        self.passLine.setObjectName("passLine")
        self.passLine.setText(employee.pas)
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(10, 110, 180, 20))
        self.loginButton.setObjectName("loginButton")
        self.regButton = QtWidgets.QPushButton(self.centralwidget)
        self.regButton.setGeometry(QtCore.QRect(10, 140, 180, 20))
        self.regButton.setObjectName("regButton")
        LogonWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(LogonWindow)
        self.statusbar.setObjectName("statusbar")
        LogonWindow.setStatusBar(self.statusbar)
        self.retranslateUi(LogonWindow)
        QtCore.QMetaObject.connectSlotsByName(LogonWindow)
        self.loginButton.clicked.connect(self.login)
        self.loginButton.setShortcut("Return")
        self.nameLine.setFocus()
        f.close()
        self.regButton.clicked.connect(self.regestration)

    def regestration(self):
        if(self.label.text() == "Введіть операційний пароль"):
            if(self.nameLine.text() == password_for_operation and self.nameLine.text() != " " or not(re.match('\w{2}')) or self.nameLine.text() == "Помилка!"):
                que = "SELECT Max(id_employee) FROM employee"
                id_employee = int(str(cursor.execute(que).fetchone()).strip("(,')")) + 1
                que = "INSERT INTO employee VALUES('"+str(id_employee)+"','','"+employee.pas+"','"+employee.login+"')"
                cursor.execute(que)
                conn.commit()
                self.nameLine.setText("Успішно виконано!")
                f = open("loginfo.txt", "w").close()

                self.passLine.setEnabled(True)
                self.loginButton.setEnabled(True)
                self.retranslateUi(LogonWindow)
            else:
                self.nameLine.setText("Помилка!")


        if(self.label.text() != "Задайте Логін та Пароль" and self.nameLine.text() != "Успішно виконано!"):
            self.loginButton.setDisabled(True)
            self.label.setText("Задайте Логін та Пароль")
            self.regButton.setText("Далі")
            self.nameLine.clear()
            self.passLine.clear()
        else:
            if(self.regButton.text() == "Далі"):
                ch = True
                if(not(re.match('\w',self.nameLine.text())) or self.nameLine.text() == " " or self.nameLine.text() == "Помилка!"):
                    self.nameLine.setText("Помилка!")
                    ch = False

                if(not(re.match('[0-9]{5}', self.passLine.text())) or self.passLine.text() == " " or self.passLine.text() == "Помилка!"):
                    self.passLine.setText("Помилка!")
                    ch = False

                if ch:
                    employee.login = self.nameLine.text()
                    employee.pas = self.passLine.text()
                    self.nameLine.clear()
                    self.passLine.clear()
                    self.passLine.setDisabled(True)
                    self.label.setText("Введіть операційний пароль")


    def loginlabel_errLogin(self):
        self.label.setText('Невірний логін чи пароль')

    def retranslateUi(self, LogonWindow):
        _translate = QtCore.QCoreApplication.translate
        LogonWindow.setWindowTitle(_translate("LogonWindow", "Ввійти"))
        self.label.setText(_translate("LogonWindow", "Введіть логін та пароль"))
        self.loginButton.setText(_translate("LogonWindow", "Логін"))
        self.regButton.setText(_translate("LogonWindow", "Реєстрація"))

    def login(self):
        login = self.nameLine.text()
        pas = self.passLine.text()
        cursor.execute('SELECT id_employee FROM employee WHERE name=? AND password=?', [(login), (pas)])
        a = cursor.fetchone()
        if (a == None):
            self.loginlabel_errLogin()
        else:
            self.closing()

    def closing(self):
        employee.login = self.nameLine.text()
        employee.pas = self.passLine.text()
        f = open("loginfo.txt", "w")
        f.write(str(self.nameLine.text()+"\n"))
        f.write(self.passLine.text())
        f.close()
        LogonWindow.hide()
        MainWindow.show()

class Ui_history(object):
    def setupUi(self, history):
        history.setObjectName("history")
        history.resize(482, 413)
        history.setWindowIcon(ico)
        self.incomeList_table = QtWidgets.QTableWidget(history)
        self.incomeList_table.setGeometry(QtCore.QRect(300, 100, 171, 301))
        self.incomeList_table.setColumnCount(3)
        self.incomeList_table.setObjectName("incomeList_table")
        self.incomeList_table.setRowCount(0)
        self.incomeList_table.horizontalHeader().setDefaultSectionSize(56)
        self.incomeList_table.horizontalHeader().setStretchLastSection(False)
        self.incomeList_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.incomeHead_table = QtWidgets.QTableWidget(history)
        self.incomeHead_table.setGeometry(QtCore.QRect(10, 10, 261, 391))
        self.incomeHead_table.setColumnCount(4)
        self.incomeHead_table.setObjectName("incomeHead_table")
        self.incomeHead_table.setRowCount(0)
        self.incomeHead_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.incomeHead_table.horizontalHeader().setDefaultSectionSize(57)
        self.incomeHead_table.horizontalHeader().setStretchLastSection(False)
        self.label = QtWidgets.QLabel(history)
        self.label.setGeometry(QtCore.QRect(310, 10, 131, 16))
        self.label.setObjectName("label")
        self.nameProduct_label = QtWidgets.QLabel(history)
        self.nameProduct_label.setGeometry(QtCore.QRect(310, 30, 151, 31))
        self.nameProduct_label.setText("")
        self.nameProduct_label.setObjectName("nameProduct_label")
        self.incomeHead_table.setColumnWidth(0,110)
        self.incomeHead_table.setColumnWidth(1,10)
        self.incomeHead_table.setColumnWidth(2,10)
        self.incomeHead_table.setColumnWidth(3,55)
        self.load_head()
        self.incomeHead_table.clicked.connect(self.headItemSelected)
        self.incomeList_table.clicked.connect(self.listItemSelected)

        self.retranslateUi(history)
        QtCore.QMetaObject.connectSlotsByName(history)

    def listItemSelected(self, instance):
        item = self.incomeList_table.itemFromIndex(instance)
        que = "SELECT name_product FROM product WHERE id_product='"+item.text()+"'"
        name = str(cursor.execute(que).fetchone()).strip("(,')")
        self.nameProduct_label.setText(name)

    def headItemSelected(self, instance):
        self.incomeList_table.clear()
        self.incomeList_table.setRowCount(0)
        item = self.incomeHead_table.itemFromIndex(instance)
        que = "SELECT * FROM income_list WHERE id_income IN(SELECT id_income FROM income_head WHERE date_income = '"+item.text()+"')"
        income_list = cursor.execute(que).fetchall()
        for row_count, item in enumerate(income_list):
            self.incomeList_table.insertRow(row_count)
            for col_count, data in enumerate(item):
                self.incomeList_table.setItem(row_count, col_count, QtWidgets.QTableWidgetItem(str(data)))

    def load_head(self):
        que = "SELECT * FROM income_head"
        income_head = cursor.execute(que).fetchall()
        for row_number, item in enumerate(income_head):
            self.incomeHead_table.insertRow(row_number)
            for col_number, data in enumerate(item):
                self.incomeHead_table.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))

    def retranslateUi(self, history):
        _translate = QtCore.QCoreApplication.translate
        history.setWindowTitle(_translate("history", "Журнал"))
        self.label.setText(_translate("history", "Назва продукту:"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(ico)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 466)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(735, 466)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 171, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.mainMenulayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainMenulayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.mainMenulayout.setContentsMargins(5, 0, 5, 0)
        self.mainMenulayout.setSpacing(0)
        self.mainMenulayout.setObjectName("mainMenulayout")
        self.addProduct_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.addProduct_button.setObjectName("addProduct_button")
        self.mainMenulayout.addWidget(self.addProduct_button)
        self.giveProduct_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.giveProduct_button.setObjectName("giveProduct_button")
        self.mainMenulayout.addWidget(self.giveProduct_button)
        self.history_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.history_button.setObjectName("history_button")
        self.mainMenulayout.addWidget(self.history_button)
        self.map_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.map_button.setObjectName("map_button")
        self.mainMenulayout.addWidget(self.map_button)
        self.exit_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_button.setObjectName("exit_button")
        self.mainMenulayout.addWidget(self.exit_button)
        self.mainMenuLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainMenuLabel.setGeometry(QtCore.QRect(0, 0, 161, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainMenuLabel.sizePolicy().hasHeightForWidth())
        self.mainMenuLabel.setSizePolicy(sizePolicy)
        self.mainMenuLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.productListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.productListWidget.setGeometry(QtCore.QRect(180, 40, 421, 401))
        self.productListWidget.setObjectName("productListWidget")

        self.productListWidget.setModelColumn(5)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(610, 40, 121, 350))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.ProductInfo_layuot = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.ProductInfo_layuot.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.ProductInfo_layuot.setContentsMargins(0, 0, 0, 0)
        self.ProductInfo_layuot.setSpacing(0)
        self.ProductInfo_layuot.setObjectName("ProductInfo_layuot")
        self.productName_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productName_label.sizePolicy().hasHeightForWidth())
        self.productName_label.setSizePolicy(sizePolicy)
        self.productName_label.setMaximumSize(QtCore.QSize(16777215, 60))
        self.productName_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.productName_label.setBaseSize(QtCore.QSize(0, 0))
        self.productName_label.setObjectName("productName_label")
        self.ProductInfo_layuot.addWidget(self.productName_label)
        self.productUnit_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productUnit_label.sizePolicy().hasHeightForWidth())
        self.productUnit_label.setSizePolicy(sizePolicy)
        self.productUnit_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.productUnit_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.productUnit_label.setObjectName("productUnit_label")
        self.ProductInfo_layuot.addWidget(self.productUnit_label)
        self.productCount_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productCount_label.sizePolicy().hasHeightForWidth())
        self.productCount_label.setSizePolicy(sizePolicy)
        self.productCount_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.productCount_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.productCount_label.setObjectName("productCount_label")
        self.ProductInfo_layuot.addWidget(self.productCount_label)
        self.productPlace_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productPlace_label.sizePolicy().hasHeightForWidth())
        self.productPlace_label.setSizePolicy(sizePolicy)
        self.productPlace_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.productPlace_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.productPlace_label.setObjectName("productPlace_label")
        self.ProductInfo_layuot.addWidget(self.productPlace_label)
        self.productShipper_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productShipper_label.sizePolicy().hasHeightForWidth())
        self.productShipper_label.setSizePolicy(sizePolicy)
        self.productShipper_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.productShipper_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.productShipper_label.setObjectName("productShipper_label")
        self.ProductInfo_layuot.addWidget(self.productShipper_label)
        self.productSertificate_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productSertificate_label.sizePolicy().hasHeightForWidth())
        self.productSertificate_label.setSizePolicy(sizePolicy)
        self.productSertificate_label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.productSertificate_label.setSizeIncrement(QtCore.QSize(0, 0))
        self.productSertificate_label.setObjectName("productSertificate_label")
        self.ProductInfo_layuot.addWidget(self.productSertificate_label)
        self.Search_line = QtWidgets.QLineEdit(self.centralwidget)
        self.Search_line.setGeometry(QtCore.QRect(180, 10, 341, 20))
        self.Search_line.setObjectName("Search_line")
        self.Search_button = QtWidgets.QPushButton(self.centralwidget)
        self.Search_button.setGeometry(QtCore.QRect(530, 10, 71, 20))
        self.Search_button.setObjectName("Search_button")
        self.Search_button.setDisabled(True)
        self.productInfo_label = QtWidgets.QLabel(self.centralwidget)
        self.productInfo_label.setGeometry(QtCore.QRect(610, 10, 121, 16))
        self.productInfo_label.setObjectName("productInfo_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.addProduct_button.clicked.connect(self.addproduct)
        self.map_button.clicked.connect(self.map_show)
        self.Search_line.textChanged.connect(self.searchTextEdited)
        self.Search_line.setFocus()
        self.item = QtWidgets.QListWidgetItem
        self.productListWidget.itemClicked.connect(self.fillDescription)
        self.giveProduct_button.clicked.connect(lambda : GiveProduct.show())
        self.history_button.clicked.connect(lambda : History.show())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Головна"))
        self.addProduct_button.setText(_translate("MainWindow", "Додати продукт"))
        self.giveProduct_button.setText(_translate("MainWindow", "Видати продукт"))
        self.history_button.setText(_translate("MainWindow", "Продивитися історію"))
        self.map_button.setText(_translate("MainWindow", "Карта складу"))
        self.exit_button.setText(_translate("MainWindow", "Вийти та закрити"))
        self.mainMenuLabel.setText(_translate("MainWindow", "ГОЛОВНЕ МЕНЮ"))
        self.productName_label.setText(_translate("MainWindow", "Назва продукту"))
        self.productUnit_label.setText(_translate("MainWindow", "міра"))
        self.productCount_label.setText(_translate("MainWindow", "(кількість)"))
        self.productPlace_label.setText(_translate("MainWindow", "розположення"))
        self.productShipper_label.setText(_translate("MainWindow", "постачальник"))
        self.productSertificate_label.setText(_translate("MainWindow", "сертефікат"))
        self.Search_button.setText(_translate("MainWindow", "Пошук"))
        self.productInfo_label.setText(_translate("MainWindow", "Інформація"))
        self.exit_button.clicked.connect(self.closeEvent)

    def fillDescription(self, QListWidgetItem):
        i = 1
        j = 0
        name_label = ""
        sert_label = ""
        count_label = ""
        unit_label = ""
        place_label = ""
        st = QListWidgetItem.text()
        while i < len(st)-1:
            while j == 0:
                name_label += st[i]
                i += 1
                if(st[i]== "'"):
                    i += 4
                    j += 1

            while j ==1:
                sert_label += st[i]
                i += 1
                if(st[i]== "'"):
                    i += 3
                    j += 1

            while j ==2:
                count_label += st[i]
                i += 1
                if (st[i] == ","):
                    i += 1
                    j += 1

            while j ==3:
                unit_label +=st[i]
                i += 1
                if (st[i] == ","):
                    i += 2
                    j += 1
            while j == 4:
                    i += 1
                    place_label += st[i]
                    if( i == len(st)-1):
                        j += 1
                        self.productName_label.setText(name_label)
                        self.productCount_label.setText(count_label)
                        self.productPlace_label.setText(place_label.strip("'"))
                        self.productUnit_label.setText(unit_label)
                        self.productSertificate_label.setText(sert_label)
                        que = "SELECT name_shipper FROM shipper WHERE id_shipper IN(SELECT id_shipper FROM product WHERE name_product='" + str(
                            name_label) + "')"
                        cursor.execute(que)
                        shipper = cursor.fetchone()
                        shipper_label = shipper[0]
                        self.productShipper_label.setText(shipper_label)

    def searchTextEdited(self):
        if(self.Search_line.text() == "" or self.Search_line.text() == "  "):
            self.productListWidget.clear()
            self.retranslateUi(MainWindow)
        else:
            self.productListWidget.clear()
            Sql = "SELECT name_product, sertificate, count, unit, place FROM product WHERE name_product LIKE '%" + self.Search_line.text() + "%' "
            res = cursor.execute(Sql).fetchall()
            for row_number, qitem in enumerate(res):
                self.productListWidget.insertItem(row_number, str(qitem).strip("()"))

    def productListUpdate(self):
        for row_number, qitem in enumerate(sql.res):
            self.productListWidget.insertItem(row_number, str(qitem).strip("()"))

    def map_show(self):
        StorageMap.show()

    def addproduct(self):
        AddProduct.show()

    def closeEvent(self):
        log = employee.login
        cursor.execute('UPDATE employee SET last_seen=? WHERE name=?', [(str(datetime.datetime.now().replace(microsecond=0))),(log)])
        conn.commit()
        employee.login = ""
        employee.pas = ""
        f = open("loginfo.txt", "w")
        f.close()
        conn.close()
        sys.exit()

app = QtWidgets.QApplication(sys.argv)
ico = QtGui.QIcon("SkladLogo.png")

StorageMap = QtWidgets.QWidget()
MapUi = Ui_StorageMap()
MapUi.setupUi(StorageMap)

History = QtWidgets.QWidget()
HistyryUI = Ui_history()
HistyryUI.setupUi(History)

GiveProduct = QtWidgets.QWidget()
GiveProductUI = Ui_GiveProduct()
GiveProductUI.setupUi(GiveProduct)

AddShipper = QtWidgets.QMainWindow()
AddShipperUi = Ui_addShipper()
AddShipperUi.setupUi(AddShipper)

AddProduct = QtWidgets.QMainWindow()
AddProductUi = Ui_addProduct()
AddProductUi.setupUi(AddProduct)

MainWindow = QtWidgets.QMainWindow()
MainWindowUi = Ui_MainWindow()
MainWindowUi.setupUi(MainWindow)

LogonWindow = QtWidgets.QMainWindow()
LogonWindowUi = Ui_LogonWindow()
LogonWindowUi.setupUi(LogonWindow)
LogonWindow.show()

sys.exit(app.exec_())
