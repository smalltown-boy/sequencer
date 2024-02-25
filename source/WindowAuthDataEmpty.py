# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore

import gui.auth_error_empty as auth_empty


class WindowAuthDataEmpty(QtWidgets.QMainWindow, auth_empty.Ui_auth_dialog_error_form):
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()
