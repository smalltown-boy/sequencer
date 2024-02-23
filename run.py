from PyQt6 import QtWidgets
import gui.login as login
import gui.register as register

class WindowLogin(QtWidgets.QMainWindow, login.Ui_login_form): # Класс, вызывающий окно регистрации и входа
    def __init__(self,parent=None): # Функция инициализации
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.register_dialog = WindowRegister()
        self.register_button.clicked.connect(self.open_register_window) # Соединяем кнопку регистрации пользователя с новым окном

    def open_register_window(self): # Функция вызова окна регистрации нового пользователя
        self.close() # Закрываем окно регистрации
        self.register_dialog.show() # Показываем окно регистрации нового пользователя


class WindowRegister(QtWidgets.QMainWindow, register.Ui_register_form):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin()
    window.show()
    sys.exit(app.exec())