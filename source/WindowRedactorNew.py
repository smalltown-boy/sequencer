from PyQt6 import QtWidgets

import gui.redactor_new as redactor
from source.WindowNewDeviceCard import WindowCreateCard


class WindowRedactor(QtWidgets.QDialog, redactor.Ui_redactor_second):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        # Инициализируем фомы
        self.create_card = WindowCreateCard()
        # Инициализируем кнопки
        self.btn_create.clicked.connect(self.create_new_card)  # Задаём событие для кнопки создания новой карточки прибора

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя (для заполнения части БД)

    def create_new_card(self): # Вызов формы создания новой карты
        self.create_card.exec() # Вызываем форму создания карточки прибора