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
        # Инициализируем отслеживание выбранных строк в таблице
        self.table_protocol.selectionModel().selectionChanged.connect(self.select_row)
        # Переменная для хранения протокола
        self.command_flow = {}
        # Переменная для выбранных данных
        self.selected_data = None
        # Переменная для чек бокса
        self.check_box = False

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя

    def save_command(self):
        command_name = self.line_name.text()
        command_request = self.line_request.text().replace('/0x', '').split('/')
        command_answer = self.line_answer.text().replace('/0x', '').split('/')

        print(command_request)
        print(command_answer)

        if not self.check_box:  # Если чек бокс не поставлен
            if all([command_name, command_request, command_answer]):  # Если все поля заполнены
                # Сохраняем данные
                if command_name not in self.command_flow:
                    # Если команды нет в списке, то добавляем её
                    self.command_flow[command_name] = {"request": command_request, "answer": command_answer}
                    print("Данные сохранены.")
                else:
                    # Если нет, то обновим команду
                    self.command_flow[command_name].update({"request": command_request, "answer": command_answer})
                    print("Команда обновлена!")
            else:
                # Выводим сообщение об ошибке
                print("Заглушка для ошибки, если не заполнены все поля.")
        else:  # Если чек бокс поставлен
            if all([command_name, command_request]):  # Если два первых поля заполнены
                # Сохраняем данные
                if command_name not in self.command_flow:
                    # Если команды нет в списке, то добавляем её
                    self.command_flow[command_name] = {"request": command_request, "answer": None}
                    print("Данные сохранены.")
                else:
                    # Если нет, то обновим команду
                    self.command_flow[command_name].update({"request": command_request, "answer": None})
                    print("Команда обновлена!")
            else:
                # Выводим сообщение об ошибке
                print("Заглушка для ошибки, если не заполнены первые два поля.")
        self.update()

    def delete_command(self):
        if self.selected_data:  # Если одна из строк выбрана
            print(self.selected_data[0])
            self.command_flow.pop(self.selected_data[0])
            self.update()
        else:
            print("Нельзя удалить строку: данных нет.")

    def save_protocol(self):
        pass

    def update(self):
        self.table_protocol.clear()  # Очищаем таблицу
        self.table_protocol.setRowCount(0)  # Удаляем все строки

        x = len(self.command_flow)  # Смотрим, сколько ключей находится в словаре, содержащим команды

        for a in range(x):  # Добавляем строки по количеству ключей
            self.table_protocol.insertRow(a)

        self.table_protocol.insertRow(1)  # Добавляем ещё одну строку (на самом деле, это костыль)

        row = 0
        for key, value in self.command_flow.items():
            # Заполняем таблицу
            self.table_protocol.setItem(row, 0, QtWidgets.QTableWidgetItem(key))
            self.table_protocol.setItem(row, 1, QtWidgets.QTableWidgetItem(str(value['request'])))
            self.table_protocol.setItem(row, 2, QtWidgets.QTableWidgetItem(str(value['answer'])))
            row += 1

    def select_row(self):
        self.selected_data = {}
        try:
            selected_row = self.table_protocol.currentItem().row()

            data_column_1 = self.table_protocol.item(selected_row, 0).text()
            data_column_2 = self.table_protocol.item(selected_row, 1).text()
            data_column_3 = self.table_protocol.item(selected_row, 2).text()

            self.selected_data = (data_column_1, data_column_2, data_column_3)
            print(self.selected_data)
        except:
            self.selected_data.clear()
            print(self.selected_data)

    def check_box(self):
        if self.checkBox_no_answer.isChecked():
            self.check_box = True
            self.line_answer.setReadOnly(True)  # Делаем окно ввода ответа недоступным
        else:
            self.check_box = False
            self.line_answer.setReadOnly(False)  # Делаем окно ввода ответа доступным
