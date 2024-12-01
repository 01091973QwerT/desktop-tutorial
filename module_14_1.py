import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Создаем таблицу, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
    )
''')

# Заполняем таблицу данными
for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

conn.commit()


# Обновляем balance у каждой второй записи
cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")
conn.commit()


# Удаляем каждую третью запись
cursor.execute("DELETE FROM Users WHERE id % 3 = 1")
conn.commit()


# Выборка данных и вывод в консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")


conn.close()
