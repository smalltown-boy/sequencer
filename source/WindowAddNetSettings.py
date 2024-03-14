from PyQt6 import QtWidgets
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
import json

import gui.net_settings as create_net_settings
from source.database import Database


class WindowAddNetSettings(QtWidgets.QDialog, create_net_settings.Ui_dialog_net_settings):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # Устанавливаем валидаторы на поля ввода ip адреса и маски
        ip_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{"
                                                                                   "1,3}\\.[0-9]{1,3}"),
                                                         self.ip_addr_edit)
        netmask_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(
            "[0-2]?[0-5]?[0-5]?\\.[0-2]?[0-5]?[0-5]?\\.[0-2]?[0-5]?[0-5]?\\.[0-2]?[0-5]?[0-5]?"),
            self.mask_edit)
        self.ip_addr_edit.setValidator(ip_validator)
        self.mask_edit.setValidator(netmask_validator)
        # Инициализируем кнопки
        self.btn_exit.clicked.connect(self.exit)
        self.btn_save_data.clicked.connect(self.save_net_settings)
        # Переменная для хранения переданных извне пользовательских данных
        self.device_data = None

    def exit(self):
        self.close()

    def save_net_settings(self):
        ip_addr = self.ip_addr_edit.text()
        mask = self.mask_edit.text()
        port = self.port_edit.text()

        if all([ip_addr, mask, port]):  # Если все поля заполнены
            db = Database()
            db.open("database/users.db")
            # Проверяем, является ли пустым поле для хранения настроек
            data_status = db.check_data_empty("net_settings", "devices", self.device_data["ID прибора"])
            
            if data_status: # Если данных в поле нету
                # Формируем json-документ
                net_settngs = {"ip_addr": ip_addr, "mask": mask, "port": port}
                # Преобразуем словарь в json
                json_file = json.dumps(net_settngs)
                # Записываем файл в базу
                db.write_json_data("devices", "net_settings", self.device_data["ID прибора"], json_file)
                db.commit()
                self.close()
            else: # Если они там есть
                print("Тут должно быть предупреждение, что данные будут перезаписаны.")
                
            db.close()
        else:
            print("Ошибка. Заполните все поля.")

