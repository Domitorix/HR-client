#21import main




class worker:

    
    prof = {'prog': 1000, 'svar': 1500, 'med': 2000}
    
    def __init__(self, age, male, profesional):
        self.age = age
        self.male = male
        self.profesional = profesional
        
    prof = {'prog': 1000, 'svar': 1500, 'med': 2000}
        
    def ages(self):
        print(f'Age worker {self.age}')
        
    def males(self):
        print(f'Male worker {self.male}')
        
    def profes(self):
        print(f'Profesional = {self.profesional}')
        
    def cash_work(self):
        print(f'Cash work = {self.prof[self.profesional]}')
        
        
        
    
       
say_worker_1 = input("Введите возраст работника: ")
say_worker_2 = input("Введите пол работника: ")
say_worker_3 = input("Введите должность работника: ")

worker_1 = worker(say_worker_1, say_worker_2, say_worker_3)

worker_1.ages() 
worker_1.males()
worker_1.profes()
worker_1.cash_work()

def iii():
    print('lol')

#print(main.users)