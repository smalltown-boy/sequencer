# Form implementation generated from reading ui file 'redactor_new.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_redactor_second(object):
    def setupUi(self, redactor_second):
        redactor_second.setObjectName("redactor_second")
        redactor_second.resize(1131, 528)
        self.btn_about = QtWidgets.QPushButton(parent=redactor_second)
        self.btn_about.setGeometry(QtCore.QRect(10, 490, 171, 28))
        self.btn_about.setObjectName("btn_about")
        self.groupBox = QtWidgets.QGroupBox(parent=redactor_second)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 551, 80))
        self.groupBox.setObjectName("groupBox")
        self.btn_create = QtWidgets.QPushButton(parent=self.groupBox)
        self.btn_create.setGeometry(QtCore.QRect(10, 30, 171, 28))
        self.btn_create.setObjectName("btn_create")
        self.create_net = QtWidgets.QPushButton(parent=self.groupBox)
        self.create_net.setGeometry(QtCore.QRect(190, 30, 171, 28))
        self.create_net.setObjectName("create_net")
        self.create_protocol = QtWidgets.QPushButton(parent=self.groupBox)
        self.create_protocol.setGeometry(QtCore.QRect(370, 30, 171, 28))
        self.create_protocol.setObjectName("create_protocol")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=redactor_second)
        self.groupBox_2.setGeometry(QtCore.QRect(570, 10, 551, 80))
        self.groupBox_2.setObjectName("groupBox_2")
        self.edit_device = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.edit_device.setGeometry(QtCore.QRect(10, 30, 171, 28))
        self.edit_device.setObjectName("edit_device")
        self.edit_settings = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.edit_settings.setGeometry(QtCore.QRect(190, 30, 171, 28))
        self.edit_settings.setObjectName("edit_settings")
        self.edit_protocol = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.edit_protocol.setGeometry(QtCore.QRect(370, 30, 171, 28))
        self.edit_protocol.setObjectName("edit_protocol")
        self.tableWidget = QtWidgets.QTableWidget(parent=redactor_second)
        self.tableWidget.setGeometry(QtCore.QRect(10, 100, 1111, 381))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(270)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.btn_refresh = QtWidgets.QPushButton(parent=redactor_second)
        self.btn_refresh.setGeometry(QtCore.QRect(190, 490, 171, 28))
        self.btn_refresh.setObjectName("btn_refresh")
        self.pushButton_2 = QtWidgets.QPushButton(parent=redactor_second)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 490, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(redactor_second)
        QtCore.QMetaObject.connectSlotsByName(redactor_second)

    def retranslateUi(self, redactor_second):
        _translate = QtCore.QCoreApplication.translate
        redactor_second.setWindowTitle(_translate("redactor_second", "Редактор"))
        self.btn_about.setText(_translate("redactor_second", "Подробнее"))
        self.groupBox.setTitle(_translate("redactor_second", "Создать"))
        self.btn_create.setText(_translate("redactor_second", "Новую карточку прибора"))
        self.create_net.setText(_translate("redactor_second", "Новые настройки"))
        self.create_protocol.setText(_translate("redactor_second", "Новый протокол"))
        self.groupBox_2.setTitle(_translate("redactor_second", "Редактировать"))
        self.edit_device.setText(_translate("redactor_second", "Карточку прибора"))
        self.edit_settings.setText(_translate("redactor_second", "Настройки"))
        self.edit_protocol.setText(_translate("redactor_second", "Протокол"))
        self.btn_refresh.setText(_translate("redactor_second", "Обновить таблицу"))
        self.pushButton_2.setText(_translate("redactor_second", "Удалить запись"))
