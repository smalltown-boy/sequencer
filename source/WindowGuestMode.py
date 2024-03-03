# -*- coding: utf-8 -*-

from PyQt6 import QtWidgets
import gui.guest_mode_ok as guest_mode

class WindowGuestMode(QtWidgets.QMainWindow, guest_mode.Ui_guest_form):  # Окно ошибки аутентификации
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"

    def exit_from_message(self):  # Закрываем сообщение об ошибке
        self.close()
        # Придумать, как вернуться к окну регистрации

    def start_sequencer(self):
        pass
