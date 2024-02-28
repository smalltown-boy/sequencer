# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets
import gui.register_error as register_error
class WindowRegisterError(QtWidgets.QMainWindow, register_error.Ui_reg_error_form):  # Окно ошибки аутентификации
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()
