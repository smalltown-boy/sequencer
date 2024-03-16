from PyQt6 import QtWidgets

import gui.protocol as protocol_manager
from source.database import Database


class WindowProtocolManager(QtWidgets.QDialog,
                            protocol_manager.Ui_diaog_protocol_redactor):  # Окно редактора протоколов
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.user_data = None
        self.setupUi(self)
        # Настраиваем таблицу
        self.table_protocol.setHorizontalHeaderLabels(
            ["Название команды", "Запрос", "Ответ"])
        # Инициализируем кнопки
        self.btn_save_command.clicked.connect(self.save_command)  # Кнопка сохранения команды
        self.btn_delete_command.clicked.connect(self.delete_command)  # Кнопка удаления команды
        self.btn_save_protocol.clicked.connect(self.save_protocol)  # Кнопка сохранения протокола
        self.checkBox_no_answer.stateChanged.connect(self.check_box)  # Функция для вызова чек бокса
        # Переменная для хранения протокола
        command_flow = {}
        # Переменная для чек бокса
        check_box = False

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя

    def save_command(self):
        command_name = self.line_name.text()
        command_request = self.line_request.text()
        command_answer = self.line_answer.text()

        

    def delete_command(self):
        pass

    def save_protocol(self):
        pass

    def update(self):
        pass

    def select_row(self):
        pass

    def check_box(self):
        if self.checkBox_no_answer.isChecked():
            check_box = True
            self.line_answer.setReadOnly(True)  # Делаем окно ввода ответа недоступным
        else:
            check_box = False
            self.line_answer.setReadOnly(False)  # Делаем окно ввода ответа доступным
