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
        self.btn_add_device.clicked.connect(self.add_device)  # Кнопка добавления команды
        self.btn_add_command.clicked.connect(self.add_command)  # Кнопка добавления команды
        self.btn_clear_table.clicked.connect(self.clear_table)  # Кнопка очистки таблицы
        # Переменная базы данных
        self.db = None
        # Прочие необходимые переменные
        self.list_of_devices = []
        self.list_of_command = []
        self.database = None
        self.data = None
        self.json_file = None
        self.current_device = None
        self.protocol = None
        self.current_command = None
        # -------------------- Тестовый болк --------------------
        #self.container = {'net_settings' : None, 'protocol' : None}.copy()
        # -------------------------------------------------------
        # Функция инициализации секвенсора
        self.init_list_device()
        # Настраиваем режим выбора строк
        self.list_device.selectionModel().selectionChanged.connect(self.select_device)
        # Настраиваем заголовки таблиц
        self.list_device.setHorizontalHeaderLabels(["Приборы"])
        self.list_command.setHorizontalHeaderLabels(["Команды"])
        #
        self.command_flow = {}
        self.protocol_flow = {}

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
        self.current_device = self.box_select_device.currentText() # Получаем название прибора из списка
        dev_name, dev_serial = self.current_device.split(" №")      # Получаем имя прибора и серийный номер
        self.db = Database()  # Инициализируем базу данных
        self.db.open('database/users.db')  # Открываем базу данных
        search_result = self.db.search_device('devices', dev_name, dev_serial) # Ищем по названию и серийному номеру инфомрацию о приборе
        net_param = self.db.read_json_data('devices', 'net_settings', search_result['device_id']) # Ищем по полученному device_id сетевые настройки
        self.command_flow[self.current_device] = {'net_settings': None, 'protocol': None}.copy()
        self.command_flow[self.current_device]['net_settings'] = net_param.copy()
        self.db.close() #Закрываем базу данных
        #
        self.update_device_table() # Обновляем столбец с коммандами
         
    def add_command(self):
        current_command = self.box_select_command.currentText() # Получаем название комманды из списка
        self.protocol_flow[current_command] = self.json_file.get(current_command) # Добавляем команды в поток команд
        self.command_flow[self.current_device]['protocol'] = self.protocol_flow.copy()
        #
        print(self.command_flow)
        self.update_command_table()

    def clear_table(self):
        pass

    def init_list_device(self):
        self.db = Database()  # Инициализируем базу данных
        self.db.open('database/users.db')  # Открываем базу данных
        self.database = self.db.read_all_data('devices')  # Читаем полностью таблицу 'devices'
        # Собираем имена приборов для списка девайсов
        for i in self.database:
            # Формируем строку выбора элемента
            menu_item = str(i['device_name']) + ' №' + str(i['serial_number']) 
            self.list_of_devices.append(menu_item)
        # Соединаем получанный список с комбобоксом
        self.box_select_device.addItems(self.list_of_devices)
        self.db.close()

    def init_list_command(self, device):
        pass

    def select_device(self):
        self.protocol_flow.clear()
        #
        selected_row = self.list_device.currentItem().row()
        self.current_device = self.list_device.item(selected_row, 0).text()
        dev_name, dev_serial = self.current_device.split(" №")
        #
        self.db = Database()  # Инициализируем базу данных
        self.db.open('database/users.db')  # Открываем базу данных
        #
        search_result = self.db.search_device('devices', dev_name, dev_serial) # Ищем информацию о приборе по имени 
        self.json_file = self.db.read_json_data('devices', 'protocol', search_result['device_id']) # Считываем протокол из базы данных
        #
        self.box_select_command.clear() # Очищаем список выбора команд
        self.list_of_command = [*self.json_file] # Получаем список ключей из файла протокола
        self.box_select_command.addItems(self.list_of_command) # Формируем список команд для выбора 
        # -------------------------------------- TEST ----------------------------------------------
        self.update_command_table()
        
    def update_device_table(self): 
        row_len = len(self.command_flow) # Получаем количество словарей в главном словаре 
        data_item = self.command_flow.keys() # Получаем ключи из стартового словаря (названия приборов)
        #
        self.list_device.clear() # Очищаем таблицу
        self.list_device.setRowCount(row_len) # Устанавливаем количество строк в таблице
        #
        row = 0 # Счётчик заполнения строк
        
        for i in data_item: # Проходимся по названиям приборов
            self.list_device.setItem(row, 0, QtWidgets.QTableWidgetItem(i)) # Добавляем строку в таблицу
            row += 1 # Увеличиваем счётчик строк на 1
            
        self.list_device.setHorizontalHeaderLabels(["Приборы"])
            
    def update_command_table(self):        
        if self.command_flow[self.current_device]['protocol'] != None:
            row_len = len(self.command_flow[self.current_device]['protocol'])
            data_item = self.command_flow[self.current_device]['protocol'].keys()
            
            self.list_command.clear() # Очищаем таблицу
            self.list_command.setRowCount(row_len) # Устанавливаем количество строк в таблице
            
            row = 0
            
            for i in data_item: # Проходимся по названиям приборов
                self.list_command.setItem(row, 0, QtWidgets.QTableWidgetItem(i)) # Добавляем строку в таблицу
                row += 1 # Увеличиваем счётчик строк на 1
        else:
            self.list_command.clear()
            self.list_command.setRowCount(0)
            print("Nothing data.")
        
        self.list_command.setHorizontalHeaderLabels(["Команды"])