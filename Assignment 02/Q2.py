class Employee:
    def __init__(self, name, id):
        self.name = name
        self.emp_id = id

    def calculate_salary(self):
        return 0

    def display_details(self):
        print(f"Name: {self.name}")

class FullTimeEmployee(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.monthly_salary = salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Monthly Salary: {self.calculate_salary()}\n")

class PartTimeEmployee(Employee):
    def __init__(self, name, id, hours_worked, hourly_rate):
        super().__init__(name, id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

    def display_details(self):
       print(f"Employee ID: {self.emp_id}")
       print(f"Name: {self.name}")
       print(f"Part-Time Salary: {self.calculate_salary()}\n")

F1 = FullTimeEmployee("Ali", 1, 5000)
F1.display_details()

F2 = FullTimeEmployee("Nauman", 2, 6000)
F2.display_details()

P1 = PartTimeEmployee("Ahmed", 3, 5, 20)
P1.display_details()

P2 = PartTimeEmployee("Kazim", 4, 10, 25)
P2.display_details()
