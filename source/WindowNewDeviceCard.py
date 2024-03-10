from PyQt6 import QtWidgets

import gui.sequencer_new_card as create_card


class WindowCreateCard(QtWidgets.QDialog, create_card.Ui_create_card_dialog):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        # self.ok_button.clicked.connect(self.exit_from_message)  # Задаём событие для кнопки "OK"
