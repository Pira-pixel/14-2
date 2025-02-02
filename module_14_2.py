import sqlite3

# Создание подключения к базе данных
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполнение таблицы 10 записями
# users_data = [
#     ('User 1', 'example1@gmail.com', 10, 1000),
#     ('User 2', 'example2@gmail.com', 20, 1000),
#     ('User 3', 'example3@gmail.com', 30, 1000),
#     ('User 4', 'example4@gmail.com', 40, 1000),
#     ('User 5', 'example5@gmail.com', 50, 1000),
#     ('User 6', 'example6@gmail.com', 60, 1000),
#     ('User 7', 'example7@gmail.com', 70, 1000),
#     ('User 8', 'example8@gmail.com', 80, 1000),
#     ('User 9', 'example9@gmail.com', 90, 1000),
#     ('User 10', 'example10@gmail.com', 100, 1000)
# ]

# cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)

# Обновление balance у каждой 2-й записи начиная с 1-й на 500
cursor.execute('UPDATE Users SET balance = ? WHERE id%2 != ?', (500, 0))

# Удаление каждой 3-й записи в таблице начиная с 1-й
cursor.execute("DELETE FROM Users WHERE id in (1, 4, 7, 10) != ?", (0,))

# Выборка всех записей, где возраст не равен 60
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
results = cursor.fetchall()

# Вывод результатов в консоль
# for username, email, age, balance in results:
#     print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total2 = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
sum_balance = cursor.fetchone()[0]

# Сохранение изменений и закрытие соединения
print(sum_balance/total2)
connection.commit()
connection.close()
