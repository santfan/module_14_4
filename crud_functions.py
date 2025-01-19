import sqlite3

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    ''')

    title = ['Спирулина', 'Йохимбе', 'Инозитол', 'Макка']
    description = ['Superfood', 'YOHIMBE', 'Максиферт', 'перуанская']
    price = [1200, 1000, 1470, 1300]

    for i in range(4):
        cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
        (f'{title[i]}', f'{description[i]}', f'{price[i]}'))

    connection.commit()
    connection.close()

# initiate_db()
def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    db = cursor.fetchall()
    return list(db)