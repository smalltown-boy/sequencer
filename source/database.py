from PyQt6 import QtWidgets, QtSql
import sys


class Database():         # Класс для работы с базами данных
    def __init__(self):   # Конструктор класса
        self.obj = QtWidgets.QApplication(sys.argv) # Создаём объект программы
        self.connection = QtSql.QSqlDatabase.addDatabase('QSQLITE') # Указываем тип базы данных, с которой будем работать
        self.connection.setDatabaseName('database/users.sqlite') # Указываем имя базы данных для открытия

    def database_open(self): # Функция открытия базы данных
        self.connection.open()

    def database_close(self): # Функция закрытия базы данных
        self.connection.close()

