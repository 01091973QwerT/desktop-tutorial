import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Удаление записи с id = 6 (если она существует)
cursor.execute("DELETE FROM Users WHERE id = 6")
conn.commit()

# Подсчет общего количества записей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчет суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# Вывод среднего баланса
if total_users > 0:
    average_balance = all_balances / total_users
    print(average_balance)
else:
    print("Таблица Users пуста")

conn.close()
