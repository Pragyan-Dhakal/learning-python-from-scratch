class Employee:
    def __init__(self, first_name, last_name):
        self._first_name = first_name  # Private variable (conventionally)
        self._last_name = last_name    # Private variable (conventionally)
    
    # Getter for full_name
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
    # Setter for full_name
    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ')
        self._first_name = first_name
        self._last_name = last_name
    
    # Deleter for full_name
    @full_name.deleter
    def full_name(self):
        print("Deleting name...")
        self._first_name = None
        self._last_name = None

# Usage
emp = Employee("John", "Doe")
print(emp.full_name)  # Access full_name using getter

emp.full_name = "Jane Smith"  # Update full_name using setter
print(emp.full_name)

del emp.full_name  # Delete full_name using deleter
print(emp.full_name)  # Will print "None None" since names are reset
