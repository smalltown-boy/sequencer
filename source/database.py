# Импорт модуля
import sqlite3


# Класс для работы с базами данных
class Database:
    # Конструктор
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.table = None
        self.data = None

        # Инициализация базы данных в конструкторе класса
        self.open('database/users.db')  # Открываем базу данных
        result = self.check_table('users')  # Проверяем наличие таблицы 'users'

        if result:  # Если таблица существует
            pass
        else:
            self.create_table_users()  # Создаём таблицу 'users' (продумать эту функцию)
            self.add_user('Guest', 'Гость', 'Нет', 'Нет', 'Нет', 'Limit')
            self.commit()  # Сохраняем изменения

        result = self.check_table(
            'devices')  # Проверяем наличие таблицы 'devices' (для хранения информации о устройствах)

        if result:
            pass
        else:
            self.create_table_devices()
            self.commit()

        self.close()  # Закрываем базу данных

    # Открытие базы данных
    def open(self, db_name):
        try:
            self.connection = sqlite3.connect(db_name)  # Открываем бд
            self.cursor = self.connection.cursor()  # Сразу создаём курсор
            return True
        except:
            return False

    # Создание таблицы users (хардкод, потом доработать)
    def create_table_users(self):
        self.table = """CREATE TABLE users(
                        user_id integer primary key autoincrement,
                        login text,
                        name text,
                        company text,
                        post text,
                        password text,
                        rights text);"""
        self.cursor.execute(self.table)

    def create_table_devices(self):
        self.table = """CREATE TABLE devices(
                      device_id integer primary key autoincrement,
                      author_id integer,
                      author_name text,
                      device_name text,
                      serial_number integer,
                      engineer text,
                      programmer text,
                      hardware_ver text,
                      firmware_ver text,
                      description text,
                      net_settings blob,
                      protocol blob);"""
        self.cursor.execute(self.table)

    # Чтение базы данных
    def read(self, db_name):
        self.data = self.cursor.execute('''SELECT * FROM users''')
        return self.data

    # Запись массива данных в бд
    def add_user(self, login, name, company, post, password, rights):
        self.cursor.execute(
            "insert into users (login, name, company, post, password, rights) values (?, ?, ?, ?, ?, ?)",
            (login, name, company, post, password, rights))

    def add_device(self, author_id, author_name, device_name, serial_number, engineer, programmer, hardware_ver, software_ver,
                   description):
        try:
            data = (author_id, author_name, device_name, serial_number, engineer, programmer, hardware_ver, software_ver, description)
            sqlite_param = """insert into devices (author_id, author_name, device_name, serial_number, engineer, programmer, 
            hardware_ver, firmware_ver, description) values (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            self.cursor.execute(sqlite_param, data)
        except sqlite3.Error as error:
            print("Что-то произошло", error)

    # Подверждение изменений
    def commit(self):
        self.connection.commit()

    # Закрытие базы данных
    def close(self):
        self.connection.close()

    # Проверка таблицы на присутствие в базе данных
    def check_table(self, table_name):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        self.result = self.cursor.fetchone()

        if self.result:
            return True
        else:
            return False

    # Поиск пользователя по имени или id
    def search_user(self, column, value, table):
        try:
            self.cursor.execute(f"SELECT * FROM {table} WHERE {column}= (?)", (value,))
            self.data = self.cursor.fetchone()
            return dict(zip([description[0] for description in self.cursor.description], self.data))
        except:
            return False

    def search_device(self, column, value, table):
        try:
            self.cursor.execute(f"SELECT * FROM {table} WHERE {column}= (?)", (value,))
            self.data = self.cursor.fetchone()
            return dict(zip([description[0] for description in self.cursor.description], self.data))
        except:
            return False


