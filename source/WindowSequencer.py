from PyQt6 import QtWidgets

import gui.sequencer_main as main_window
from source.WindowRedactorNew import WindowRedactor
from source.database import Database


class WindowMain(QtWidgets.QMainWindow, main_window.Ui_Sequencer):
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        # Инициализируем окна
        self.redactor = WindowRedactor()
        # Инициализируем кнопки
        self.menu_redactor.triggered.connect(self.open_redactor)  # Кнопка открытия редактора
        self.menu_settings.triggered.connect(self.open_settings)  # Кнопка открытия настроек
        self.menu_search.triggered.connect(self.open_search)  # Кнопка открытия поиска
        # Кнопки управления
        self.btn_add_device.clicked.connect(self.add_device) # Кнопка добавления команды
        self.btn_add_command.clicked.connect(self.add_command) # Кнопка добавления команды
        self.btn_clear_table.clicked.connect(self.clear_table) # Кнопка очистки таблицы
        # Переменная базы данных
        self.db = None

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя
        if self.user_data["rights"] == 'Limit':  # Если права пользователя ограничены
            # Делаем кнопку редактора недоступной
            self.menu_redactor.setEnabled(False)

    def open_redactor(self):  # Кнопка открытия редактора
        self.redactor.register_user_data(self.user_data)  # Передаём данные о пользователе в окно редактора
        self.redactor.exec()

    def open_settings(self):
        print("Открываем настройки.")
        pass

    def open_search(self):
        print("Открываем поиск.")
        pass

    def add_device(self):
        pass

    def add_command(self):
        pass

    def clear_table(self):
        pass

    def init_sequencer(self):
        self.db = Database() # Инициализируем базу данных
        self.db.open('database/users.db')  # Открываем базу данных
        database = self.db.read_all_data('devices') # Читаем полностью таблицу 'devices'

