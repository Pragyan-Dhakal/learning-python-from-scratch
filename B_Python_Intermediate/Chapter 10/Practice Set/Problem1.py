#Create a class "Programmer" for storing information of few programmers working at Microsoft.

class programmer:
    company = "Microsoft"
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

p =programmer("Pragyan Dhakal", "data analyst", "500000")
print(p.name, p.role, p.salary)
r =programmer("Ram Bahadur", "Web Developer", "1000000")
print(r.name, r.role, r.salary)