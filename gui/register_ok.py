# Form implementation generated from reading ui file 'register_ok.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_reg_complete_form(object):
    def setupUi(self, reg_complete_form):
        reg_complete_form.setObjectName("reg_complete_form")
        reg_complete_form.resize(571, 138)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(reg_complete_form.sizePolicy().hasHeightForWidth())
        reg_complete_form.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(parent=reg_complete_form)
        self.label.setGeometry(QtCore.QRect(170, 10, 251, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ok_button = QtWidgets.QPushButton(parent=reg_complete_form)
        self.ok_button.setGeometry(QtCore.QRect(240, 80, 93, 28))
        self.ok_button.setObjectName("ok_button")
        self.label_2 = QtWidgets.QLabel(parent=reg_complete_form)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 531, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(reg_complete_form)
        QtCore.QMetaObject.connectSlotsByName(reg_complete_form)

    def retranslateUi(self, reg_complete_form):
        _translate = QtCore.QCoreApplication.translate
        reg_complete_form.setWindowTitle(_translate("reg_complete_form", "Завершение регистрации"))
        self.label.setText(_translate("reg_complete_form", "Регистрация прошла успешно!"))
        self.ok_button.setText(_translate("reg_complete_form", "OK"))
        self.label_2.setText(_translate("reg_complete_form", "Войдите в программу, используя указанный вами логин и пароль."))
