from PyQt6 import QtWidgets
import gui.login as login
import gui.register as register

class WindowLogin(QtWidgets.QMainWindow, login.Ui_login_form): # Класс, вызывающий окно регистрации и входа
    def __init__(self,parent=None): # Функция инициализации
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.register_dialog = WindowRegister()
        self.register_button.clicked.connect(self.open_register_window) # Соединяем кнопку регистрации пользователя с новым окном
        self.exit_button.clicked.connect(self.close_register_window) # Соединяем кнопку выхода из программы с функцией
    def open_register_window(self): # Функция вызова окна регистрации нового пользователя
        self.close() # Закрываем окно регистрации
        self.register_dialog.show() # Показываем окно регистрации нового пользователя

    def close_register_window(self): # Функция выхода из программы
        self.close() # Закрываем окно регистрации


class WindowRegister(QtWidgets.QMainWindow, register.Ui_register_form):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.abort_button.clicked.connect(self.exit_register_window) # Задаём событие для кнопки отмены
    def exit_register_window(self): # Функция выхода из окна регистрации
        self.close()                # Закрываем окно регистрации
        window.show()               # Открываем окно входа


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin()
    window.show()
    sys.exit(app.exec())