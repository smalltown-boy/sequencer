# Form implementation generated from reading ui file 'user_error.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_user_error_form(object):
    def setupUi(self, user_error_form):
        user_error_form.setObjectName("user_error_form")
        user_error_form.resize(571, 138)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(user_error_form.sizePolicy().hasHeightForWidth())
        user_error_form.setSizePolicy(sizePolicy)
        self.ok_button = QtWidgets.QPushButton(parent=user_error_form)
        self.ok_button.setGeometry(QtCore.QRect(240, 80, 93, 28))
        self.ok_button.setObjectName("ok_button")
        self.label_2 = QtWidgets.QLabel(parent=user_error_form)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 411, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(user_error_form)
        QtCore.QMetaObject.connectSlotsByName(user_error_form)

    def retranslateUi(self, user_error_form):
        _translate = QtCore.QCoreApplication.translate
        user_error_form.setWindowTitle(_translate("user_error_form", "Ошибка пользователя"))
        self.ok_button.setText(_translate("user_error_form", "OK"))
        self.label_2.setText(_translate("user_error_form", "Пользователь с указанным именем уже существует."))
