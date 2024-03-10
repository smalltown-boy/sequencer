from PyQt6 import QtWidgets

import gui.redactor as device_redactor


class WindowRedactor(QtWidgets.QMainWindow, device_redactor.Ui_Redactor):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        # self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def register_user_data(self, user_data): # Сохраняем данные о пользователе
        self.user_data = user_data # Получаем данные пользователя (для заполнения части БД)