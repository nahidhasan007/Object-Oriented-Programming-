class Employee:

    period_bonus = 5000

    def __init__(self,name,email,major,pay):
        self.name = name
        self.email = email
        self.major = major
        self.pay = pay

    def impinfo(self):
        print("Department:"+ self.major + "\n" +"Earning:"+str(self.pay))    

    def increase_pay(self):
        self.pay = self.pay + self.period_bonus

    @classmethod
    def set_period_bonus(cls,amount):
        cls.period_bonus = amount

    @staticmethod
    def is_working_day(day):
        if day.weekday == 6 or day.weekday == 7:
            print("Holiday!")
        else:
            print("Working Day!")
    
    def __repr__(self):
       return "Employee('{}', '{}', '{}')".format(self.name, self.email, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.name,self.major)

    def __add__(self,other):
        return self.pay + other.pay

emp1 = Employee('Nahid','nhs@gmail.com','backend',50000)

print(emp1.name)
print(emp1.impinfo())


