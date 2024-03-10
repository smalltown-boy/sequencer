from PyQt6 import QtWidgets

import gui.sequencer_new_card as create_card
from source.database import Database

class WindowCreateCard(QtWidgets.QDialog, create_card.Ui_create_card_dialog):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        self.btn_exit.clicked.connect(self.exit)  # Задаём событие для кнопки "Отмена"
        self.btn_save.clicked.connect(self.save_card) # Задаём событие для кнопки "Сохранить"

    def exit(self): # Отмена записи
        self.close()

    def save_card(self):
        device_name = self.line_name # Сохраняем имя прибора
        serial_number = self.line_serial_num # Сохраняем серийный номер
        engineer_name = self.line_engineer # Сохраняем имя инженера
        programmer_name = self.line_programmer # Сохраняем имя программиста
        hardware_version = self.line_hardware_ver # Сохраняем версию железа
        software_version = self.line_software_ver # Сохраняем версию прошивки
        description = self.plain_description # Сохраняем краткое описание прибора

        db = Database() # Создаём объект для доступа к базе данных
        db.open('database/users.db') # Открываем базу данных

        if serial_number is None: # Если хотя бы имя прибора и серийный номер пусты
            pass # Показать ошибку (здесь пока заглушка)
        else: # В противном случае
            s_number = db.search_device('serial_number', serial_number, 'devices')  # Смотрим, есть прибор с такийм серийным номером
            if s_number: # Если прибор с таким серийным номером найден, показать ошибку
                pass
            else: # В противном случае необходимо всё записать
                pass
        db.close()