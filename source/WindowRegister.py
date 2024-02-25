# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
import gui.register as register

from source.WindowUserError import WindowUserError
from source.WindowRegisterError import WindowRegisterError

class WindowRegister(QtWidgets.QMainWindow, register.Ui_register_form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.abort_button.clicked.connect(self.exit_register_window)  # Задаём событие для кнопки отмены
        self.register_button.clicked.connect(self.user_register)  # Задаём событие для кнопки регистрации
        # Устанавливаем для окон ввода параметры валидации
        # Для логина устанавливаем только латинские буквы, цифры и символ "_". Всего - от 3х до 15ти символов.
        self.login_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[A-Za-z0-9_]{3,15}"), self.login_line)
        self.login_line.setValidator(self.login_validator)
        # Для пароля - те же правила, но без нижнего подчёркивания
        self.password_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[A-Za-z0-9]{8,20}"),                                                             self.password_line)
        self.password_line.setValidator(self.password_validator)
        # Для имени - латинские буквы, и кириллица
        self.name_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r'\w+=\p{L}+\s*'), self.name_line)
        self.name_line.setValidator(self.name_validator)
        # Для должности всё то же самое
        self.post_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r'\w+=\p{L}+\s*'), self.post_line)
        self.post_line.setValidator(self.post_validator)
        # И для компании - тоже
        self.company_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(r'\w+=\p{L}+\s*'), self.company_line)
        self.company_line.setValidator(self.company_validator)
        # Создаём объект окна ошибки
        self.register_error_dialog = WindowRegisterError()
        self.user_error_dialog = WindowUserError()

    def exit_register_window(self):  # Функция выхода из окна регистрации
        self.close()  # Закрываем окно регистрации
        window.show()  # Открываем окно входа

    def user_register(self):  # Функция регистрации нового пользователя
        # Получаем пользователем регистрационные данные
        self.login = self.login_line.text()
        self.password = self.password_line.text()
        self.name = self.name_line.text()
        self.company = self.login_line.text()
        self.post = self.post_line.text()
        self.right = "full"
        # Проверяем, всё ли введено (может, проверка корявая, но какая есть)
        if self.login or self.password or self.name or self.company or self.post: # Если всё введено
            self.user = self.db.database_search_user(self.login)  # Смотрим, есть ли такой пользователь
            if self.login != self.user[1]:  # Если пользователи не совпадают, то надо продолжить регистрацию
                self.reg_data = [self.login, self.name, self.company, self.post, self.password, self.right]
                self.db.database_add_user(self.reg_data)
            else:
                self.user_error_dialog.show()  # Покажем ошибку
        else:
            self.register_error_dialog.show()  # Покажем ошибку