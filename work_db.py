import sqlite3
#from clients import worker_1



connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone INTAGER,
    age INTAGER    
    )
    
    ''')

#cursor.execute('CREATE INDEX idx_email ON Users (email)')

#cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))
cur = cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
'''
def dm_append():
    
    l_name = worker_1.first_name
    f_name = worker_1.last_name
    e_mail = worker_1.email
    p_hone = worker_1.phone
    a_ge = worker_1.age
    
    cursor.execute('INSERT INTO Users (first_name, last_name, email, phone, age) VALUES (?, ?, ?, ?, ?)', (l_name, f_name, e_mail, p_hone, a_ge))
'''
#dm_append()
'''
while True:
    say = input("Добавить нового работника?")
    if say == 'да':
        say_1 = input("Введите имя:")
        say_2 = input("Введите почту: ")
        say_3 = input("Введите возраст: ")
        
        cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (say_1, say_2, say_3))
    
    if say == 'нет':
        break

'''
connection.commit()
connection.close()
'''

'''