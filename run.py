from PyQt6 import QtWidgets
import gui.login as login
import gui.register as register
from source.database import Database
import gui.auth_error_empty as auth_empty
import gui.auth_error as auth_error


class WindowLogin(QtWidgets.QMainWindow, login.Ui_login_form):  # Класс, вызывающий окно регистрации и входа
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.register_dialog = WindowRegister()
        self.auth_empty_dialog = WindowAuthDataEmpty()
        self.auth_error_dialog = WindowAuthError()
        self.register_button.clicked.connect(
            self.open_register_window)  # Соединяем кнопку регистрации пользователя с новым окном
        self.exit_button.clicked.connect(self.close_register_window)  # Соединяем кнопку выхода из программы с функцией
        self.login_button.clicked.connect(self.authentication)  # Соединяем кнопку входа с функцией аутентификации
        self.db = Database()  # Создаём объект базы данных

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
                pass
            else:  # Если записи о таком пользователе нет
                self.auth_error_dialog.show()


class WindowRegister(QtWidgets.QMainWindow, register.Ui_register_form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.abort_button.clicked.connect(self.exit_register_window)  # Задаём событие для кнопки отмены
        self.register_button.clicked.connect(self.user_register)  # Задаём событие для кнопки регистрации

    def exit_register_window(self):  # Функция выхода из окна регистрации
        self.close()  # Закрываем окно регистрации
        window.show()  # Открываем окно входа

    def user_register(self):  # Функция регистрации нового пользователя
        self.db = Database()  # Создаём объект базы данных
        self.db.database_open()  # Открываем баз данных
        pass


class WindowAuthDataEmpty(QtWidgets.QMainWindow, auth_empty.Ui_auth_dialog_error_form):
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()


class WindowAuthError(QtWidgets.QMainWindow, auth_error.Ui_auth_error_form):
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
