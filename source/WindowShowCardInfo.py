from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPlainTextEdit
import gui.show_card_info as card_info


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

    def show_info(self, data):
        try:
            self.line_name.setText(data["device_name"])
            self.line_serial_num.setText(data["serial_number"])
            self.line_engineer.setText(data["engineer"])
            self.line_programmer.setText(data["programmer"])
            self.plain_description.setPlainText(data["description"])
            self.line_hardware_ver.setText(data["hardware_ver"])
            self.line_software_ver.setText(data["firmware_ver"])

            if data["net_settings"]:
                self.line_net_settings.setText("Есть")
            else:
                self.line_net_settings.setText("Отсутствует")

            if data["protocol"]:
                self.line_protocol.setText("Есть")
            else:
                self.line_protocol.setText("Отсутствует")
        except:
            print("Ошибка")

    def exit(self):
        self.close()


