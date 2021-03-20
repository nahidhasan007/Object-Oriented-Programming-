from classes import Employee

class Developer(Employee):
    period_bonus = 10000

    def __init__(self,name,email,major,pay,prog_language):
        super().__init__(name,email,major,pay)
        self.prog_language = prog_language

class Manager(Employee):
    def __init__(self,name,email,major,pay,employees=None):
        super().__init__(name,email,major,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employess.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->",emp.name)                       


developer1 = Developer("Alexa","exa@email.com","Full Stack",70000,"Python")
developer2 = Developer("Alex","ex@email.com","half Stack",70000,"java")
print(developer1.impinfo())

#will give us how python search methods, variables, characteristics from newly created inheritance Develper method
#print(help(Developer))

developer1.increase_pay()
print(developer1.pay)
print(developer1.prog_language)

mngr1 = Manager("Boss","boss@gmail.com","all above",100000,[developer1])
print(mngr1.impinfo())
mngr1.add_emp(developer1)
mngr1.print_emps()
