from classes import Employee
import datetime

emp3 = Employee('Sarah','srah@gmail.com','backend',48000)

Employee.set_period_bonus(6000)
print(emp3.impinfo())
emp3.increase_pay()
print(emp3.pay)

date = datetime.date(2021,3,20)
Employee.is_working_day(date)