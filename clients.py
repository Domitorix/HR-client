#21import main

io = False


class worker:

    
    prof = {'prog': 1000, 'svar': 1500, 'med': 2000}
    
    def __init__(self, first_name, last_name, email, phone, age):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.age = age
        
    prof = {'prog': 1000, 'svar': 1500, 'med': 2000}
        
    def p_first_name(self):
        print(f'First name: {self.first_name}')
        
    def p_last_name(self):
        print(f'last name: {self.last_name}')
        
    def p_email(self):
        print(f'email: {self.email}')
        
    def p_phone(self):
        print(f'phone: {self.phone}')
        
    def p_age(self):
        print(f"age: {self.age}")
        
    def go(self):
        return worker_1.first_name
    def go_1(self):
        return worker_1.last_name
    def go_2(self):
        return worker_1.email
    def go_3(self):
        return worker_1.phone
    def go_4(self):
        return worker_1.age
        
    
if io == True:
    say_worker_1 = input("Введите имя: ")
    say_worker_2 = input("Введите фамилию: ")
    say_worker_3 = input("Введите почту: ")
    say_worker_4 = input("Введите номер: ")
    say_worker_5 = input("Введите возраст: ")     
    worker_1 = worker(say_worker_1, say_worker_2, say_worker_3, say_worker_4, say_worker_5)
else:
    pass
'''

worker_1.p_first_name()
worker_1.p_last_name()
worker_1.p_email()
worker_1.p_phone()
worker_1.p_age()
'''



#print(main.users)