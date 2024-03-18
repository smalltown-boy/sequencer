from PyQt6 import QtWidgets

import gui.protocol_view as protocol_viewer
from source.database import Database


class WindowViewProtocol(QtWidgets.QDialog,
                         protocol_viewer.Ui_diaog_viewer):  # Окно редактора протоколов
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.user_data = None
        self.device_data = None
        self.setupUi(self)
        # Настраиваем таблицу
        self.table_protocol.setHorizontalHeaderLabels(
            ["Название команды", "Запрос", "Ответ"])
        # Инициализируем кнопки
        self.btn_exit.clicked.connect(self.exit)  # Кнопка выхода

    def exit(self):
        self.close()

    def show_data(self, data):
        # Открываем базу данных
        db = Database()
        db.open('database/users.db')
        # Читаем данные json
        json_file = db.read_json_data("devices", "protocol", data["device_id"])
        #
        x = len(json_file)
        self.table_protocol.setRowCount(x)
        # Выводим информацию
        row = 0
        for key, value in json_file.items():
            # Заполняем таблицу
            self.table_protocol.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
            self.table_protocol.setItem(row, 1, QtWidgets.QTableWidgetItem(str(value['request'])))
            self.table_protocol.setItem(row, 2, QtWidgets.QTableWidgetItem(str(value['answer'])))
            row += 1
        #
        db.close()
