from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPlainTextEdit
import gui.show_card_info as card_info

from source.WindowShowNetSettings import WindowShowNetSettings


class WindowShowCardInfo(QtWidgets.QDialog, card_info.Ui_dialog_show_card):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        # Блокируем все QLineEdit и QPlainTextEdit для редактирования
        self.line_name.setReadOnly(True)
        self.line_serial_num.setReadOnly(True)
        self.line_engineer.setReadOnly(True)
        self.line_programmer.setReadOnly(True)
        self.plain_description.setReadOnly(True)
        self.line_hardware_ver.setReadOnly(True)
        self.line_software_ver.setReadOnly(True)
        self.line_net_settings.setReadOnly(True)
        self.line_protocol.setReadOnly(True)
        # Инициализируем кнопки
        self.btn_exit.clicked.connect(self.exit)
        self.btn_show_settings.clicked.connect(self.show_net_settings)
        self.btn_show_protocol.clicked.connect(self.show_protocol)
        # Инициализируем формы
        self.net_info = WindowShowNetSettings()
        # Переменная для хранения данных
        self.device_data = None

    def show_info(self, data):
        try:
            self.device_data = data
            #
            self.line_name.setText(data["device_name"])
            self.line_serial_num.setText(data["serial_number"])
            self.line_engineer.setText(data["engineer"])
            self.line_programmer.setText(data["programmer"])
            self.plain_description.setPlainText(data["description"])
            self.line_hardware_ver.setText(data["hardware_ver"])
            self.line_software_ver.setText(data["firmware_ver"])

            if data["net_settings"]:
                self.line_net_settings.setText("Есть")
                self.btn_show_settings.setEnabled(True)
            else:
                self.line_net_settings.setText("Отсутствует")
                self.btn_show_settings.setEnabled(False)

            if data["protocol"]:
                self.line_protocol.setText("Есть")
                self.btn_show_protocol.setEnabled(True)
            else:
                self.line_protocol.setText("Отсутствует")
                self.btn_show_protocol.setEnabled(False)
        except:
            print("Ошибка")

    def show_net_settings(self):
        self.net_info.show_info(self.device_data)
        self.net_info.exec()

    def show_protocol(self):
        pass

    def exit(self):
        self.close()


