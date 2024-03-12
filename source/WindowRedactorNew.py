from PyQt6 import QtWidgets

import gui.redactor_new as redactor
from source.WindowNewDeviceCard import WindowCreateCard
from source.WindowShowCardInfo import WindowShowCardInfo
from source.database import Database


class WindowRedactor(QtWidgets.QDialog, redactor.Ui_redactor_second):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        self.database_data = None
        self.device_data = None
        # Настраиваем таблицу
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID прибора", "Название прибора", "Серийный номер", "Автор карточки"])
        # Инициализируем фомы
        self.create_card = WindowCreateCard()
        self.show_info = WindowShowCardInfo()
        # Инициализируем кнопки
        self.btn_create.clicked.connect(self.create_new_card)  # Задаём событие создания новой карточки прибора
        self.btn_about.clicked.connect(self.about_device)  # Событие для подробного описания прибора
        self.btn_refresh.clicked.connect(self.update)  # Событие для кнопки обновления таблицы
        # Инициализируем отслеживание выбранных строк в таблице
        self.tableWidget.selectionModel().selectionChanged.connect(self.select_row)
        #
        self.update()

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя (для заполнения части БД)

    def create_new_card(self):  # Вызов формы создания новой карты
        self.create_card.show()  # Вызываем форму создания карточки прибора
        self.create_card.register_user_data(
            self.user_data)  # Передаём данные о пользователе в форму регистрации нового прибора

    def select_row(self):
        selected_row = self.tableWidget.currentRow()
        try:
            selected_data = {}
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(selected_row, column)
                selected_data[self.tableWidget.horizontalHeaderItem(column).text()] = item.text()

            self.device_data = selected_data
        except:
            print("Data empty")

    def update(self):
        #self.tableWidget.clear()
        # Открывем базу данных
        db = Database()
        db.open('database/users.db')
        data = db.read_all_data('devices')

        for row, item in enumerate(data):
            # self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item["device_id"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item["device_name"]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(item["serial_number"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item["author_name"]))

        db.close()

    def about_device(self):
        db = Database()
        db.open('database/users.db')

        id_device = self.device_data["ID прибора"]

        device_info = db.search_user('device_id', id_device, 'devices')
        if device_info:
            self.show_info.show()
            self.show_info.show_info(device_info)
        else:
            print("Вы выбрали пустую строку!")
