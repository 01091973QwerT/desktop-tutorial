import sqlite3


def initiate_db():
    # Создание базы данных и таблицы Products
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создание таблицы Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создание таблицы Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL DEFAULT 1000
        )
    ''')

    conn.commit()
    conn.close()


def add_user(username, email, age):
    # Добавление нового пользователя
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance) 
        VALUES (?, ?, ?, ?)''', (username, email, age, 1000))
    conn.commit()
    conn.close()


def is_included(username):
    # Проверка, существует ли пользователь
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(1) FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()[0]
    conn.close()
    return result > 0


# Запуск инициализации базы данных
initiate_db()


def get_all_products():
    return None