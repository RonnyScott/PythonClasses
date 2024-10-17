class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name               # Public attribute
        self._employee_id = employee_id 
        self.__salary = salary          # Private attribute
    
    def display_info(self):
        print(f"Employee Name: {self.name}, Employee ID: {self._employee_id}")
    
    def get_salary(self): # Public method to access private attribute
        return self.__salary

    def set_salary(self, salary): # Public method to modify private attribute
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary!")

# Subclass: Manager (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)  # Call parent constructor
        self.team_size = team_size                   # New attribute for Manager
    
    # Override the display_info method
    def display_info(self):
        super().display_info()  # Call the parent method
        print(f"Team Size: {self.team_size}")
    
# Subclass: Developer (inherits from Employee)
class Developer(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)    # Call parent constructor
        
    
    # Override the display_info method
    def display_info(self):
        super().display_info()  # Call the parent method
        

# Create instances of the base and derived classes
emp1 = Employee("John Doe", 101, 50000)
emp2 = Manager("Jane Smith", 102, 75000, 10)
emp3 = Developer("Alice Johnson", 103, 60000)

# Demonstrating encapsulation: accessing private and protected attributes
print(f"\n=== Accessing and Modifying Salary for emp1 ===")
print(f"Initial Salary: {emp1.get_salary()}")
emp1.set_salary(52000)
print(f"Updated Salary: {emp1.get_salary()}")

print(f"\n=== Display Information for Each Employee ===")
# Calling display_info for each employee (shows polymorphism in action)
emp1.display_info()
emp2.display_info()  # Manager-specific info
emp3.display_info()  # Developer-specific info
