# Form implementation generated from reading ui file 'sequencer_new_card.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_create_card_dialog(object):
    def setupUi(self, create_card_dialog):
        create_card_dialog.setObjectName("create_card_dialog")
        create_card_dialog.resize(468, 434)
        font = QtGui.QFont()
        font.setPointSize(9)
        create_card_dialog.setFont(font)
        self.name_line = QtWidgets.QLabel(parent=create_card_dialog)
        self.name_line.setGeometry(QtCore.QRect(20, 20, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.name_line.setFont(font)
        self.name_line.setObjectName("name_line")
        self.lineEdit = QtWidgets.QLineEdit(parent=create_card_dialog)
        self.lineEdit.setGeometry(QtCore.QRect(240, 20, 211, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(parent=create_card_dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_serial_num = QtWidgets.QLineEdit(parent=create_card_dialog)
        self.line_serial_num.setGeometry(QtCore.QRect(240, 60, 211, 22))
        self.line_serial_num.setObjectName("line_serial_num")
        self.label_2 = QtWidgets.QLabel(parent=create_card_dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_engineer = QtWidgets.QLineEdit(parent=create_card_dialog)
        self.line_engineer.setGeometry(QtCore.QRect(240, 100, 211, 22))
        self.line_engineer.setObjectName("line_engineer")
        self.label_3 = QtWidgets.QLabel(parent=create_card_dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_programmer = QtWidgets.QLineEdit(parent=create_card_dialog)
        self.line_programmer.setGeometry(QtCore.QRect(240, 140, 211, 22))
        self.line_programmer.setObjectName("line_programmer")
        self.label_4 = QtWidgets.QLabel(parent=create_card_dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plain_description = QtWidgets.QPlainTextEdit(parent=create_card_dialog)
        self.plain_description.setGeometry(QtCore.QRect(240, 180, 211, 141))
        self.plain_description.setObjectName("plain_description")
        self.label_5 = QtWidgets.QLabel(parent=create_card_dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 340, 191, 22))
        self.label_5.setObjectName("label_5")
        self.line_hardware_ver = QtWidgets.QLineEdit(parent=create_card_dialog)
        self.line_hardware_ver.setGeometry(QtCore.QRect(240, 340, 211, 22))
        self.line_hardware_ver.setObjectName("line_hardware_ver")
        self.label_6 = QtWidgets.QLabel(parent=create_card_dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 196, 22))
        self.label_6.setObjectName("label_6")
        self.line_software_ver = QtWidgets.QLineEdit(parent=create_card_dialog)
        self.line_software_ver.setGeometry(QtCore.QRect(240, 380, 211, 22))
        self.line_software_ver.setObjectName("line_software_ver")

        self.retranslateUi(create_card_dialog)
        QtCore.QMetaObject.connectSlotsByName(create_card_dialog)

    def retranslateUi(self, create_card_dialog):
        _translate = QtCore.QCoreApplication.translate
        create_card_dialog.setWindowTitle(_translate("create_card_dialog", "Новая карточка"))
        self.name_line.setText(_translate("create_card_dialog", "Название прибора:"))
        self.label.setText(_translate("create_card_dialog", "Серийный номер:"))
        self.label_2.setText(_translate("create_card_dialog", "Разработчик:"))
        self.label_3.setText(_translate("create_card_dialog", "Программист ВПО:"))
        self.label_4.setText(_translate("create_card_dialog", "Описание:"))
        self.label_5.setText(_translate("create_card_dialog", "Версия железа:"))
        self.label_6.setText(_translate("create_card_dialog", "Версия прошивки:"))
