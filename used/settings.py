# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(161, 210)
        self.sidePanelSettings_label = QtWidgets.QLabel(Settings)
        self.sidePanelSettings_label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.sidePanelSettings_label.setObjectName("sidePanelSettings_label")
        self.languageSettings_label = QtWidgets.QLabel(Settings)
        self.languageSettings_label.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.languageSettings_label.setObjectName("languageSettings_label")
        self.languageSettings_combox = QtWidgets.QComboBox(Settings)
        self.languageSettings_combox.setGeometry(QtCore.QRect(20, 130, 111, 22))
        self.languageSettings_combox.setObjectName("languageSettings_combox")
        self.saveSettings_pushbutton = QtWidgets.QPushButton(Settings)
        self.saveSettings_pushbutton.setGeometry(QtCore.QRect(10, 160, 141, 41))
        self.saveSettings_pushbutton.setObjectName("saveSettings_pushbutton")
        self.widget = QtWidgets.QWidget(Settings)
        self.widget.setGeometry(QtCore.QRect(20, 40, 84, 42))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sidePanelCheckButton_true = QtWidgets.QRadioButton(self.widget)
        self.sidePanelCheckButton_true.setChecked(True)
        self.sidePanelCheckButton_true.setObjectName("sidePanelCheckButton_true")
        self.verticalLayout.addWidget(self.sidePanelCheckButton_true)
        self.sidePanelCheckButton_false = QtWidgets.QRadioButton(self.widget)
        self.sidePanelCheckButton_false.setObjectName("sidePanelCheckButton_false")
        self.verticalLayout.addWidget(self.sidePanelCheckButton_false)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Form"))
        self.sidePanelSettings_label.setText(_translate("Settings", "Бокова панель інформації:"))
        self.languageSettings_label.setText(_translate("Settings", "Мова:"))
        self.saveSettings_pushbutton.setText(_translate("Settings", "Зберегти"))
        self.sidePanelCheckButton_true.setText(_translate("Settings", "Вкл"))
        self.sidePanelCheckButton_false.setText(_translate("Settings", "Викл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QWidget()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())

