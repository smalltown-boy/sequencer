from PyQt6 import QtWidgets

import gui.sequencer_main as main_window


class WindowMain(QtWidgets.QMainWindow, main_window.Ui_Sequencer):
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None

    def register_user_data(self, user_data): # Сохраняем данные о пользователе
        self.user_data = user_data
