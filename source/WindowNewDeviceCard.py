from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog

import gui.sequencer_new_card as create_card
from source.database import Database


class WindowCreateCard(QtWidgets.QDialog, create_card.Ui_create_card_dialog):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.dev = None
        self.setupUi(self)
        self.user_data = None
        self.btn_exit.clicked.connect(self.exit)  # Задаём событие для кнопки "Отмена"
        self.btn_save.clicked.connect(self.save_card)  # Задаём событие для кнопки "Сохранить"

    def exit(self):  # Отмена записи
        self.close()

    def save_card(self):
        device_name = self.line_name.text()  # Сохраняем имя прибора
        serial_number = self.line_serial_num.text()  # Сохраняем серийный номер
        engineer_name = self.line_engineer.text()  # Сохраняем имя инженера
        programmer_name = self.line_programmer.text()  # Сохраняем имя программиста
        hardware_version = self.line_hardware_ver.text()  # Сохраняем версию железа
        software_version = self.line_software_ver.text()  # Сохраняем версию прошивки
        description = self.plain_description.toPlainText()  # Сохраняем краткое описание прибора
        #description = "suck"

        db = Database()
        db.open('database/users.db')
        if device_name is None and serial_number is None:
            print("Ничего не введено!")
        # Проверяем, всё ли введено (может, проверка корявая, но какая есть)
        else:
            device = db.search_user('serial_number', serial_number, 'DEVICES')  # Смотрим, есть ли такой пользователь
            if device:
                pass
            else:  # В противном случае зарегистрируем пользователя
                print("Пишем в базу данных.")
                db.add_device("X", device_name, serial_number, engineer_name, programmer_name,
                              hardware_version, software_version, description)
                #db.add_device("1", "1", "1", "1", "1",
                #              "1", "1", "1")
                db.commit()  # Сохраняем изменения
                self.close()
        db.close()

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя
