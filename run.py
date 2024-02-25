# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
import gui.login as login
import gui.register as register
from source.database import Database
import gui.auth_error_empty as auth_empty
import gui.auth_error as auth_error
import gui.guest_mode_ok as guest_mode
import gui.register_error as register_error
import gui.user_error as user_error



class WindowLogin(QtWidgets.QMainWindow, login.Ui_login_form):  # Класс, вызывающий окно регистрации и входа
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
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
            self.db.database_open()  # Открываем баз данных
            self.user = self.db.database_search_user(self.login)  # Ищем пользователя
            self.db.database_close()
            if self.user:  # Если пользователь найден
                pass # Показать окно, что воход выполнен успешно
            else:  # Если записи о таком пользователе нет
                self.auth_error_dialog.show()


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
            self.db = Database()  # Создаём объект базы данных
            self.db.database_open()  # Открываем баз данных
            self.user = self.db.database_search_user(self.login)  # Смотрим, есть ли такой пользователь
            if self.login != self.user[1]:  # Если пользователи не совпадают, то надо продолжить регистрацию
                self.reg_data = [self.login, self.name, self.company, self.post, self.password, self.right]
                self.db.database_add_user(self.reg_data)
                self.db.database_close()
            else:
                self.user_error_dialog.show()  # Покажем ошибку
        else:
            self.register_error_dialog.show()  # Покажем ошибку


class WindowAuthDataEmpty(QtWidgets.QMainWindow, auth_empty.Ui_auth_dialog_error_form):
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()


class WindowAuthError(QtWidgets.QMainWindow, auth_error.Ui_auth_error_form): # Окно ошибки аутентификации
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()

class WindowGuestMode(QtWidgets.QMainWindow, guest_mode.Ui_guest_form): # Окно ошибки аутентификации
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.start_sequencer)  # Задаём событие для кнопки "OK"
        self.back_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "Назад"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()
        window.show() # Запускаем окно ввода логина и пароля

    def start_sequencer(self):
        pass

class WindowRegisterError(QtWidgets.QMainWindow, register_error.Ui_reg_error_form): # Окно ошибки аутентификации
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()

class WindowUserError(QtWidgets.QMainWindow, user_error.Ui_user_error_form): # Окно ошибки аутентификации
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin()
    window.show()
    sys.exit(app.exec())
