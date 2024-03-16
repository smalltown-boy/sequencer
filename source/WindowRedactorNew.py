from PyQt6 import QtWidgets

import gui.redactor_new as redactor
from source.WindowNewDeviceCard import WindowCreateCard
from source.WindowShowCardInfo import WindowShowCardInfo
from source.WindowAddNetSettings import WindowAddNetSettings
from source.WindowEditCardInfo import WindowEditCardInfo
from source.WindowEditNetInfo import WindowEditNetSettings
from source.WindowProtocolManager import WindowProtocolManager
from source.database import Database


class WindowRedactor(QtWidgets.QDialog, redactor.Ui_redactor_second):  # Окно редактора
    def __init__(self, parent=None):  # Функция инициализации
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.user_data = None
        self.database_data = None
        self.device_data = None
        # Настраиваем таблицу
        self.tableWidget.setHorizontalHeaderLabels(
            ["ID прибора", "Название прибора", "Серийный номер", "Автор карточки"])
        # Инициализируем фомы
        self.create_card = WindowCreateCard()
        self.show_info = WindowShowCardInfo()
        self.create_net_settings = WindowAddNetSettings()
        self.edit_card_info = WindowEditCardInfo()
        self.edit_net_parameters = WindowEditNetSettings()
        self.protocol_manager = WindowProtocolManager()
        # Инициализируем кнопки
        self.btn_create.clicked.connect(self.create_new_card)  # Задаём событие создания новой карточки прибора
        self.btn_about.clicked.connect(self.about_device)  # Событие для подробного описания прибора
        self.btn_refresh.clicked.connect(self.update)  # Событие для кнопки обновления таблицы
        self.btn_create_net.clicked.connect(self.create_new_settings) # Событие для создания сетевых настроек
        self.btn_edit_device.clicked.connect(self.edit_card) # Событие для редактирования карточки
        self.btn_edit_settings.clicked.connect(self.edit_net_settings) # Событие для редактирования настроек
        self.btn_create_protocol.clicked.connect(self.create_protocol) # Событие для создания протокола
        # Инициализируем отслеживание выбранных строк в таблице
        self.tableWidget.selectionModel().selectionChanged.connect(self.select_row)
        #
        self.update()

    def register_user_data(self, user_data):  # Сохраняем данные о пользователе
        self.user_data = user_data  # Получаем данные пользователя (для заполнения части БД)

    def create_new_card(self):  # Вызов формы создания новой карты
        self.create_card.register_user_data(self.user_data)  # Передаём данные о пользователе в форму регистрации нового прибора
        self.create_card.exec()  # Вызываем форму создания карточки прибора

    def edit_card(self): # Функция редактирования уже существующей карты
        data_len = len(self.device_data)
        if data_len == 0:
            print("Нельзя редактировать карточку прибора, если её нет!")
        else:
            db = Database()
            db.open('database/users.db')
            
            dev_info = db.search_device('devices', self.device_data["Название прибора"], self.device_data["Серийный номер"]) # Получаем подробную инфомрацию о приборе, который мы выбрали
            self.edit_card_info.show_info(dev_info)               # Передаём подробную информацию о приборе в форму 
            self.edit_card_info.user_data = self.user_data        # Передаём подробную информацию о пользователи в форму
            
            device_author_id = dev_info["author_id"]
            user_id = self.user_data["user_id"]
            
            if device_author_id == user_id:
                db.close()
                self.edit_card_info.exec()
            else:
                print("Вы не можете редактировать карточку чужого авторства!")
                db.close()

    def create_new_settings(self): # Создаём новые сетевые настройки
        data_len = len(self.device_data)
        if data_len == 0:
            print("Нельзя создать файл с настройками, если нет карточки прибора!")
        else:
            self.create_net_settings.device_data = self.device_data # Передаём настройки в форму
            self.create_net_settings.exec()

    def edit_net_settings(self): # Редактируем уже существущие сетевые настройки
        data_len = len(self.device_data)
        if data_len == 0:
            print("Выберите прибор, чьи настройки вы хотите отредактировать!")
        else:
            print(self.device_data)
            try:
                # Открываем базу данных
                db = Database()
                db.open('database/users.db')
                # Читаем данные json
                json_file = db.read_json_data("devices", "net_settings", self.device_data["ID прибора"])
                #
                db.close()
                self.edit_net_parameters.device_data = self.device_data
                self.edit_net_parameters.show_info(json_file)
                self.edit_net_parameters.exec()
            except EOFError:
                print(EOFError)

    def select_row(self):
        selected_row = self.tableWidget.currentRow()
        try:
            selected_data = {}
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(selected_row, column)
                selected_data[self.tableWidget.horizontalHeaderItem(column).text()] = item.text()

            self.device_data = selected_data
            # Так как тут есть карточка прибора, делаем кнопку создания недоступной
            self.btn_create.setEnabled(False)
            # Открываем базу данных, чтобы узнать состояние интересующих нас полей
            db = Database()
            db.open('database/users.db')
            # Смотрим состояние интересующих нас полей
            file_net = db.check_data_empty("net_settings", "devices", self.device_data["ID прибора"])
            file_protocol = db.check_data_empty("protocol", "devices", self.device_data["ID прибора"])
            
            if not file_net: # Если файл с сетевыми настройками существует
                self.btn_create_net.setEnabled(False)
            else:
                self.btn_create_net.setEnabled(True)
                
            if not file_protocol: # Если файл с протоколом существует
                self.btn_create_protocol.setEnabled(False)
            else:
                self.btn_create_protocol.setEnabled(True)
                
            db.close() # Закрываем базу данных
        except:
            self.device_data.clear()
            # Так как все поля пустые, делаем кнопки создания доступными
            self.btn_create.setEnabled(True)
            self.btn_create_net.setEnabled(True)
            self.btn_create_protocol.setEnabled(True)

    def update(self):
        # self.tableWidget.clear()
        # Открывем базу данных
        db = Database()
        db.open('database/users.db')
        data = db.read_all_data('devices')

        for row, item in enumerate(data):
            # self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(item["device_id"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(item["device_name"]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(item["serial_number"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(item["author_name"]))

        db.close()

    def about_device(self):
        db = Database()
        db.open('database/users.db')

        data_len = len(self.device_data)
        if data_len == 0:
            print("Данных для отображения нет")
        else:
            id_device = self.device_data["ID прибора"]
            device_info = db.search_user('device_id', id_device, 'devices')
            self.show_info.show_info(device_info)
            self.show_info.exec()

        db.close()

    def create_protocol(self):
        self.protocol_manager.register_user_data(self.user_data)
        self.protocol_manager.exec()
