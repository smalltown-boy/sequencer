from PyQt6 import QtWidgets, QtSql
import sys

from PyQt6.QtSql import QSqlQuery


class Database():         # Класс для работы с базами данных

    def __init__(self):   # Конструктор класса
        self.row = None
        self.cursor = None
        self.query = None
        self.obj = QtWidgets.QApplication(sys.argv)  # Создаём объект программы
        self.connection = QtSql.QSqlDatabase.addDatabase(
            'QSQLITE')  # Указываем тип базы данных, с которой будем работать
        self.connection.setDatabaseName('database/users.sqlite')  # Указываем имя базы данных для открытия
        #
        if 'users' not in self.connection.tables():  # Если таблицы users нет в базе данных (в случае, если базы нет)
            self.database_open() # Открываем базу данных
            self.database_create_users_table() # Создаём необходимую нам таблицу
            self.database_create_guest_account() # Создаём гостевой аккаунт для тех, кто не хочет регистрироваться
            self.connection.commit()
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
        #self.connection.commit()

    def database_create_guest_account(self): # Создание гостевой учётной записи
        self.query = QtSql.QSqlQuery()  # Создание курсора
        self.query.exec('INSERT INTO users (login, name, rights) VALUES ("guest", "Гость", "limited")') # Добавление записей для гостевой учётноё записи

    def database_search_user(self, login):
        try:
            self.cursor = QtSql.QSqlQuery()    # Создание курсора
            self.cursor.prepare('SELECT * FROM users WHERE login=?') # Поиск строки с данными о пользователе по логину
            self.cursor.addBindValue(login)
            self.row = self.cursor.first()
            return self.row
        except:
            return False

