class Employee():

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department
    
    def show_details(self):
        print(self.name, self.salary, self.department)


emp = Employee('ram', 10000, 'Mechanical')

emp.show_details()