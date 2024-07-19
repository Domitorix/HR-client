import sqlite3
#import clients
kkk = 27



connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTAGER    
    )
    
    ''')

#cursor.execute('CREATE INDEX idx_email ON Users (email)')

#cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', ('newuser', 'newuser@example.com', 28))
cur = cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

users_list = []
for user in users:
    user_dict ={
        'id': user[0],
        'username': user[1],
        'email': user[2],
        'age': user[3]
        }
users_list.append(user_dict)
print(users_list)
for i in users_list:
    print(i)
    
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