# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets

import gui.login as login

from source.WindowRegister import WindowRegister
from source.WindowAuthDataEmpty import WindowAuthDataEmpty
from source.WindowsAuthError import WindowAuthError
from source.WindowGuestMode import WindowGuestMode
from source.WindowSequencer import WindowMain
from source.database import Database


class WindowLogin(QtWidgets.QMainWindow, login.Ui_login_form):  # Класс, вызывающий окно регистрации и входа
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # Создаём объекты классов окон, которые мы будем вызывать
        self.register_dialog = WindowRegister()
        self.auth_empty_dialog = WindowAuthDataEmpty()
        self.auth_error_dialog = WindowAuthError()
        self.guest_mode_dialog = WindowGuestMode()
        self.sequencer_dialog = WindowMain()
        # Регистрируем нажатия кнопок
        self.register_button.clicked.connect(
            self.open_register_window)  # Соединяем кнопку регистрации пользователя с новым окном
        self.exit_button.clicked.connect(self.close_register_window)  # Соединяем кнопку выхода из программы с функцией
        self.login_button.clicked.connect(self.authentication)  # Соединяем кнопку входа с функцией аутентификации
        self.guest_button.clicked.connect(self.start_guest_mode)  # Запускаем гостевой режим
        self.db = Database()  # Создаём объект базы данных

    def start_guest_mode(self):
        # Выполняем вход гостевым пользователем
        self.db.open('database/users.db')  # Открываем базу данных
        self.user = self.db.search_user('login', 'Guest', 'USERS')  # Ищем пользователя в поле 'login' таблицы 'users'
        print(self.user)
        self.db.close()  # Закрываем базу данных
        self.close()  # Закрываем окно логина
        # Открываем окно секвенсора и окно предупреждения
        self.sequencer_dialog.show()  # Показываем главное окно
        self.sequencer_dialog.register_user_data(self.user)  # Передаём данные о госте в основное окно
        self.guest_mode_dialog.show()  # Выводим окно предупреждения для гостевого режима

    def open_register_window(self):  # Функция вызова окна регистрации нового пользователя
        self.register_dialog.exec()  # Показываем окно регистрации нового пользователя

    def close_register_window(self):  # Функция выхода из программы
        self.close()  # Закрываем окно регистрации

    def authentication(self):  # Функция аутентификации
        login = self.login_line.text()
        password = self.password_line.text()

        if login == '' or password == '':  # Если логин или пароль не введены
            self.auth_empty_dialog.show()  # Вызвать диалог с ошибкой
        else:  # Если логин и пароль введены
            self.db.open('database/users.db')  # Открываем базу данных
            self.user = self.db.search_user('login', login, 'USERS')  # Ищем пользователя в поле 'login' таблицы 'users'
            self.db.close()  # Закрываем базу данных
            if self.user:  # Если пользователь найден
                # Примитивная проверка пароля на совпадение
                if password == self.user["password"]:
                    self.close()
                    self.sequencer_dialog.show()  # Запускаем рабочее окно программы
                    self.sequencer_dialog.register_user_data(
                        self.user)  # Передаём в главный класс данные о пользователе
                else:
                    self.auth_error_dialog.show()
            else:  # Если записи о таком пользователе нет
                self.auth_error_dialog.show()
