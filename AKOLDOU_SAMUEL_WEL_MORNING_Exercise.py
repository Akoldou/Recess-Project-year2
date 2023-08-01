
class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
    def get_payment1(self,):
      return self.salary
      print("the salary is: " + self.salary)
    def get_payment2(self):
      return self.salary*0.2
      print("the increased salary is: " + self.salary)

my_employee = Employee("Samuel", 500000)
print(my_employee.name)
print(my_employee.get_payment1())
print(my_employee.get_payment2())