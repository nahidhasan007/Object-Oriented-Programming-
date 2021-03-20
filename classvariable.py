from classes import Employee

emp2 = Employee("Hasan","hasan@gh.com","FrontEnd",40000)

print(emp2.impinfo())

emp2.increase_pay()

print(emp2.pay)
print(emp2.__dict__)