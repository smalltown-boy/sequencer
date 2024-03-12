from PyQt6 import QtWidgets
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

    def show_info(self, data):
        pass
