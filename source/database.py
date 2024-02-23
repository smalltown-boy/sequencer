from PyQt6 import QtWidgets, QtSql
import sys


class Database():         # Класс для работы с базами данных
    def __init__(self):   # Конструктор класса
        self.cursor = None
        self.obj = QtWidgets.QApplication(sys.argv)  # Создаём объект программы
        self.connection = QtSql.QSqlDatabase.addDatabase(
            'QSQLITE')  # Указываем тип базы данных, с которой будем работать
        self.connection.setDatabaseName('database/users.sqlite')  # Указываем имя базы данных для открытия
        #
        if 'users' not in self.connection.tables():  # Если таблицы users нет в базе данных (в случае, если базы нет)
            self.database_open() # Открываем базу данных
            self.database_create_users_table() # Создаём необходимую нам таблицу
            self.database_close() # Закрываем базу данных

    def database_open(self): # Функция открытия базы данных
        self.connection.open()

    def database_close(self): # Функция закрытия базы данных
        self.connection.close()

    def database_create_users_table(self): # Создание таблицы пользователей
        self.cursor = QtSql.QSqlQuery()    # Создание курсора
        self.cursor.exec("create table users (user_id integer primary key autoincrement, " +
                         "login text, " +
                         "name text, " +
                         "company text, " +
                         "post text, " +
                         "password text, " +
                         "rights text)")



