# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets

import gui.login as login
import gui.guest_mode_ok as guest_mode

from source.WindowRegister import WindowRegister
from source.WindowAuthDataEmpty import WindowAuthDataEmpty
from source.WindowsAuthError import WindowAuthError
#from source.WindowGuestMode import WindowGuestMode
from source.database import Database

class WindowLogin(QtWidgets.QMainWindow, login.Ui_login_form):  # Класс, вызывающий окно регистрации и входа
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # Создаём объекты классов, которы будем вызывать
        self.register_dialog = WindowRegister()
        self.auth_empty_dialog = WindowAuthDataEmpty()
        self.auth_error_dialog = WindowAuthError()
        self.guest_mode_dialog = WindowGuestMode()
        self.register_button.clicked.connect(
            self.open_register_window)  # Соединяем кнопку регистрации пользователя с новым окном
        self.exit_button.clicked.connect(self.close_register_window)  # Соединяем кнопку выхода из программы с функцией
        self.login_button.clicked.connect(self.authentication)  # Соединяем кнопку входа с функцией аутентификации
        self.guest_button.clicked.connect(self.start_guest_mode) # Запускаем гостевой режим
        self.db = Database()  # Создаём объект базы данных

    def start_guest_mode(self):
        self.close() # Закрываем окно логина
        self.guest_mode_dialog.show() # Выводим окно предупреждения для гостевого режима

    def open_register_window(self):  # Функция вызова окна регистрации нового пользователя
        self.close()  # Закрываем окно регистрации
        self.register_dialog.show()  # Показываем окно регистрации нового пользователя

    def close_register_window(self):  # Функция выхода из программы
        self.close()  # Закрываем окно регистрации

    def authentication(self):  # Функция аутентификации
        self.login = self.login_line.text()
        self.password = self.password_line.text()

        if self.login == '' or self.password == '':  # Если логин или пароль не введены
            self.auth_empty_dialog.show()  # Вызвать диалог с ошибкой
        else:  # Если логин и пароль введены
            self.db.open('database/users.db')  # Открываем базу данных
            self.user = self.db.search_user('login', self.login, 'USERS')  # Ищем пользователя в поле 'login' таблицы 'users'
            self.db.close() # Закрываем базу данных
            if self.user:  # Если пользователь найден
                pass # Проверка пароля и вход в ПО
            else:  # Если записи о таком пользователе нет
                self.auth_error_dialog.show()

class WindowGuestMode(QtWidgets.QMainWindow, guest_mode.Ui_guest_form):  # Окно ошибки аутентификации
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.start_sequencer)  # Задаём событие для кнопки "OK"
        self.back_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "Назад"
        self.window = WindowLogin()

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()
        self.window.show()  # Запускаем окно ввода логина и пароля

    def start_sequencer(self):
        pass
