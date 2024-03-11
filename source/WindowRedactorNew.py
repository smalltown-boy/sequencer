from PyQt6 import QtWidgets

import gui.redactor_new as redactor
from source.WindowNewDeviceCard import WindowCreateCard
from source.database import Database

class WindowRedactor(QtWidgets.QDialog, redactor.Ui_redactor_second):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        self.database_data = None
        # Настраиваем таблицу
        self.tableWidget.setHorizontalHeaderLabels(["ID прибора", "Название прибора", "Серийный номер", "Автор карточки"])
        # Инициализируем фомы
        self.create_card = WindowCreateCard()
        # Инициализируем кнопки
        self.btn_create.clicked.connect(
            self.create_new_card)  # Задаём событие для кнопки создания новой карточки прибора
        # Инициализируем отслеживание выбранных строк в таблице
        self.tableWidget.selectionModel().selectionChanged.connect(self.select_row)
        #
        self.init_table("device_id", "device_name", "serial_number", "author_name")

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя (для заполнения части БД)

    def create_new_card(self):  # Вызов формы создания новой карты
        self.create_card.show()  # Вызываем форму создания карточки прибора
        self.create_card.register_user_data(
            self.user_data)  # Передаём данные о пользователе в форму регистрации нового прибора

    def select_row(self):
        print("Стркоа выбрана.")

    def init_table(self, *column_names):
        db = Database()
        db.open('database/users.db')
        self.database_data = db.read_all_data('devices')

        for row in self.database_data:
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("author_name"))









