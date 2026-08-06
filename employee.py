class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12

employee = Employee("Sarah", 250000)

print(employee.yearly_salary())