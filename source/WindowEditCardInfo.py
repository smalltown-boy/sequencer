from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog

import gui.sequencer_new_card as create_card
from source.database import Database


class WindowEditCardInfo(QtWidgets.QDialog, create_card.Ui_create_card_dialog):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.dev = None
        self.setupUi(self)
        self.user_data = None
        self.btn_exit.clicked.connect(self.exit)  # Задаём событие для кнопки "Отмена"
        self.btn_save.clicked.connect(self.save_card)  # Задаём событие для кнопки "Сохранить"

    def exit(self):
        pass

    def save_card(self):
        device_name = self.line_name.text()  # Сохраняем имя прибора
        serial_number = self.line_serial_num.text()  # Сохраняем серийный номер
        engineer_name = self.line_engineer.text()  # Сохраняем имя инженера
        programmer_name = self.line_programmer.text()  # Сохраняем имя программиста
        hardware_version = self.line_hardware_ver.text()  # Сохраняем версию железа
        software_version = self.line_software_ver.text()  # Сохраняем версию прошивки
        description = self.plain_description.toPlainText()  # Сохраняем краткое описание прибора

        db = Database()
        db.open('database/users.db')

        if all([device_name, serial_number, engineer_name, programmer_name, hardware_version, software_version,
                description]):
            pass
        else:
            print("Ничего не введено!")

    def show_info(self, data):
        try:
            self.user_data = data
            self.line_name.setText(data["device_name"])
            self.line_serial_num.setText(data["serial_number"])
            self.line_engineer.setText(data["engineer"])
            self.line_programmer.setText(data["programmer"])
            self.plain_description.setPlainText(data["description"])
            self.line_hardware_ver.setText(data["hardware_ver"])
            self.line_software_ver.setText(data["firmware_ver"])
        except:
            print("Ошибка")
