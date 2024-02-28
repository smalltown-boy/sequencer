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
        self.open('database/users.db') # Открываем базу данных
        result = self.check_table('users') # Проверяем наличие таблицы 'users'
        if not result: # Если таблицы не существует
            self.create_table_users() # Создаём таблицу 'users' (продумать эту функцию)
            self.add_user('Guest', 'Гость', 'Нет', 'Нет', 'Нет', 'Limit')
            self.commit() # Сохраняем изменения
        self.close() # Закрываем базу данных

    # Открытие базы данных
    def open(self, db_name):
        try:
            self.connection = sqlite3.connect(db_name) # Открываем бд
            self.cursor = self.connection.cursor()     # Сразу создаём курсор
            return True
        except:
            return False

    # Создание таблицы users (хардкод, потом доработать)
    def create_table_users(self):
        self.table = """CREATE TABLE USERS(
                        user_id integer primary key autoincrement,
                        login text,
                        name text,
                        company text,
                        post text,
                        password text,
                        rights text)"""
        self.cursor.execute(self.table)

    # Чтение базы данных
    def read(self, db_name):
        self.data = self.cursor.execute('''SELECT * FROM users''')
        return self.data

    # Запись массива данных в бд
    def add_user(self, login, name, company, post, password, rights):
        self.cursor.execute("insert into users (login, name, company, post, password, rights) values (?, ?, ?, ?, ?, ?)",(login, name, company, post, password, rights))
       
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
        self.cursor.execute(f"SELECT * FROM {table} WHERE {column}= (?)",(value,))
        self.data = self.cursor.fetchall()
        return self.data

    

if __name__ == "__main__":
    db = Database()
    db.open('new_database.db')
    result = db.check_table('USERS')
    if result:
        #db.add_user('Sasha','spacecow','ME','Programmer','Root','Full')
        #db.commit()
        #db.close()
        user = db.search_user('login', 'Sasha', 'USERS')
        print(user)
    else:
        db.create_table_users()
