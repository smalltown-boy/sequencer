# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.resize(406, 245)
        self.centralwidget = QtWidgets.QWidget(parent=login_form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.login_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.login_line.setObjectName("login_line")
        self.gridLayout.addWidget(self.login_line, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password_line.setObjectName("password_line")
        self.gridLayout.addWidget(self.password_line, 1, 1, 1, 2)
        self.login_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_button.sizePolicy().hasHeightForWidth())
        self.login_button.setSizePolicy(sizePolicy)
        self.login_button.setObjectName("login_button")
        self.gridLayout.addWidget(self.login_button, 2, 1, 1, 1)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)
        self.register_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_button.sizePolicy().hasHeightForWidth())
        self.register_button.setSizePolicy(sizePolicy)
        self.register_button.setObjectName("register_button")
        self.gridLayout.addWidget(self.register_button, 4, 0, 1, 1)
        self.guest_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guest_button.sizePolicy().hasHeightForWidth())
        self.guest_button.setSizePolicy(sizePolicy)
        self.guest_button.setObjectName("guest_button")
        self.gridLayout.addWidget(self.guest_button, 4, 1, 1, 1)
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)
        self.exit_button.setObjectName("exit_button")
        self.gridLayout.addWidget(self.exit_button, 4, 2, 1, 1)
        login_form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=login_form)
        self.statusbar.setObjectName("statusbar")
        login_form.setStatusBar(self.statusbar)

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "Секвенсер - Вход"))
        self.label.setText(_translate("login_form", "Логин:"))
        self.label_2.setText(_translate("login_form", "Пароль:"))
        self.login_button.setText(_translate("login_form", "Войти"))
        self.register_button.setText(_translate("login_form", "Регистрация"))
        self.guest_button.setText(_translate("login_form", "Гость"))
        self.exit_button.setText(_translate("login_form", "Выход"))
