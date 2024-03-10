# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtWidgets import QMessageBox
import gui.register as register

from source.WindowUserError import WindowUserError
from source.WindowRegisterError import WindowRegisterError
from source.WindowSequencer import WindowMain

from source.database import Database

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
        # Создаём объект окна секвенсора
        self.sequencer_dialog = WindowMain()

    def exit_register_window(self):  # Функция выхода из окна регистрации
        self.close()  # Закрываем окно регистрации
        #window.show()  # Открываем окно входа
        Window.show()

    def user_register(self):  # Функция регистрации нового пользователя
        # Получаем пользователем регистрационные данные
        login = self.login_line.text()
        password = self.password_line.text()
        name = self.name_line.text()
        company = self.company_line.text()
        post = self.post_line.text()
        rights = "Full"
        # Открываем базу данных
        db = Database()
        db.open('database/users.db')
        if login is None and password is None:
            self.register_error_dialog.show()  # Покажем ошибку
        # Проверяем, всё ли введено (может, проверка корявая, но какая есть)
        else:
            user = db.search_user('login', login, 'USERS')  # Смотрим, есть ли такой пользователь
            if user: # Если пользователь найден
                self.user_error_dialog.show()  # Покажем ошибку
            else: # В противном случае зарегистрируем пользователя
                db.add_user(login, name, company, post, password, rights)  # Записываем пользователя в базу данных
                db.commit()  # Сохраняем изменения
                self.close() # Закрываем окно регистрации
                self.sequencer_dialog.show() # Вызываем окно секвенсора
                # Это костыль. Мы ищем в базе только что созданного пользователя
                user = db.search_user('login', login, 'USERS')
                # И передаём в секвенсор данные о нём
                self.sequencer_dialog.register_user_data(user)

        db.close()  # Закрываем базу данных (или оставить её открытой до закрытия программы?)