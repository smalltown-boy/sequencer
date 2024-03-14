from PyQt6 import QtWidgets

import gui.show_net_settings as net_settings
import json
from source.database import Database


class WindowShowNetSettings(QtWidgets.QDialog, net_settings.Ui_dialog_net_settings):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # Блокируем окна вывода для редактирования
        self.ip_addr_edit.setReadOnly(True)
        self.mask_edit.setReadOnly(True)
        self.port_edit.setReadOnly(True)
        # Инициализируем кнопки
        self.btn_ok.clicked.connect(self.exit)

    def show_info(self, data):
        # Открываем базу данных
        db = Database()
        db.open('database/users.db')
        # Читаем данные json
        json_file = db.read_json_data("devices", "net_settings", data["device_id"])
        # Выводим информацию
        self.ip_addr_edit.setText(json_file["ip_addr"])
        self.mask_edit.setText(json_file["mask"])
        self.port_edit.setText(json_file["port"])
        #
        db.close()

    def exit(self):
        self.close()
