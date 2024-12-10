import sqlite3

def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products
for x in range(1,5):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Products(title, description, price) VALUES (?, ?, ?)
        """, (f"Название:{x}", f"Описание:{x}", f"Цена:{x * 100}")
    )
    conn.commit()
    conn.close()
initiate_db()