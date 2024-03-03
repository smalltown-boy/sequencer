# Form implementation generated from reading ui file 'sequencer_main.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Sequencer(object):
    def setupUi(self, Sequencer):
        Sequencer.setObjectName("Sequencer")
        Sequencer.resize(1222, 801)
        self.centralwidget = QtWidgets.QWidget(parent=Sequencer)
        self.centralwidget.setObjectName("centralwidget")
        self.log_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.log_box.setGeometry(QtCore.QRect(10, 559, 1201, 171))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.log_box.setFont(font)
        self.log_box.setObjectName("log_box")
        self.log_browser = QtWidgets.QTextBrowser(parent=self.log_box)
        self.log_browser.setGeometry(QtCore.QRect(10, 20, 1181, 141))
        self.log_browser.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.log_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.log_browser.setObjectName("log_browser")
        self.control_box = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.control_box.setGeometry(QtCore.QRect(10, 10, 1201, 541))
        self.control_box.setObjectName("control_box")
        self.btn_start_test = QtWidgets.QPushButton(parent=self.control_box)
        self.btn_start_test.setGeometry(QtCore.QRect(450, 280, 161, 28))
        self.btn_start_test.setObjectName("btn_start_test")
        self.btn_stop_test = QtWidgets.QPushButton(parent=self.control_box)
        self.btn_stop_test.setGeometry(QtCore.QRect(810, 280, 161, 28))
        self.btn_stop_test.setObjectName("btn_stop_test")
        self.btn_pause = QtWidgets.QPushButton(parent=self.control_box)
        self.btn_pause.setGeometry(QtCore.QRect(630, 280, 161, 28))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_add_device = QtWidgets.QPushButton(parent=self.control_box)
        self.btn_add_device.setGeometry(QtCore.QRect(50, 100, 161, 28))
        self.btn_add_device.setObjectName("btn_add_device")
        self.box_select_device = QtWidgets.QComboBox(parent=self.control_box)
        self.box_select_device.setGeometry(QtCore.QRect(50, 60, 161, 28))
        self.box_select_device.setObjectName("box_select_device")
        self.box_select_command = QtWidgets.QComboBox(parent=self.control_box)
        self.box_select_command.setGeometry(QtCore.QRect(260, 60, 161, 28))
        self.box_select_command.setObjectName("box_select_command")
        self.btn_add_command = QtWidgets.QPushButton(parent=self.control_box)
        self.btn_add_command.setGeometry(QtCore.QRect(260, 100, 161, 28))
        self.btn_add_command.setObjectName("btn_add_command")
        self.list_device = QtWidgets.QListView(parent=self.control_box)
        self.list_device.setGeometry(QtCore.QRect(50, 150, 161, 361))
        self.list_device.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_device.setObjectName("list_device")
        self.list_command = QtWidgets.QListWidget(parent=self.control_box)
        self.list_command.setGeometry(QtCore.QRect(260, 150, 161, 361))
        self.list_command.setObjectName("list_command")
        self.progress_testing = QtWidgets.QProgressBar(parent=self.control_box)
        self.progress_testing.setGeometry(QtCore.QRect(450, 330, 741, 23))
        self.progress_testing.setProperty("value", 0)
        self.progress_testing.setObjectName("progress_testing")
        self.btn_open_details = QtWidgets.QPushButton(parent=self.control_box)
        self.btn_open_details.setGeometry(QtCore.QRect(990, 280, 161, 28))
        self.btn_open_details.setObjectName("btn_open_details")
        Sequencer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Sequencer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1222, 26))
        self.menubar.setObjectName("menubar")
        self.menu_create = QtWidgets.QMenu(parent=self.menubar)
        self.menu_create.setObjectName("menu_create")
        self.menu_settings = QtWidgets.QMenu(parent=self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        Sequencer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Sequencer)
        self.statusbar.setObjectName("statusbar")
        Sequencer.setStatusBar(self.statusbar)
        self.btn_create_card = QtGui.QAction(parent=Sequencer)
        self.btn_create_card.setObjectName("btn_create_card")
        self.btn_create_protocol = QtGui.QAction(parent=Sequencer)
        self.btn_create_protocol.setObjectName("btn_create_protocol")
        self.menu_create.addAction(self.btn_create_card)
        self.menu_create.addAction(self.btn_create_protocol)
        self.menubar.addAction(self.menu_create.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())

        self.retranslateUi(Sequencer)
        QtCore.QMetaObject.connectSlotsByName(Sequencer)

    def retranslateUi(self, Sequencer):
        _translate = QtCore.QCoreApplication.translate
        Sequencer.setWindowTitle(_translate("Sequencer", "Секвенсер - Версия 1.0"))
        self.log_box.setTitle(_translate("Sequencer", "Лог"))
        self.control_box.setTitle(_translate("Sequencer", "Управление"))
        self.btn_start_test.setText(_translate("Sequencer", "Начать тест"))
        self.btn_stop_test.setText(_translate("Sequencer", "Остановить тест"))
        self.btn_pause.setText(_translate("Sequencer", "Пауза"))
        self.btn_add_device.setText(_translate("Sequencer", "Добавить прибор"))
        self.btn_add_command.setText(_translate("Sequencer", "Добавить команду"))
        self.btn_open_details.setText(_translate("Sequencer", "Детальный лог"))
        self.menu_create.setTitle(_translate("Sequencer", "Создать..."))
        self.menu_settings.setTitle(_translate("Sequencer", "Настройки"))
        self.btn_create_card.setText(_translate("Sequencer", "Карточка прибора"))
        self.btn_create_protocol.setText(_translate("Sequencer", "Протокол обмена"))
