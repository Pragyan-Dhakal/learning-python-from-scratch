class employee:  #parent/base class
    company = "Microsoft"
    name="Pragyan Dhakal"
    salary = 1000000
    def info(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class programmer(employee): #Inheritance Class 
    name = "Ram Bahadur"
    language ="Python"
    company = "Apple"       # The information of class employee is stored in it if any changes is required change can be made in base class
    def languageinfo (self):
        print(f"The name is {self.name} and his language is {self.language}")

a =employee()   #Object
b =programmer()
print(a.company, b.company)
a.info()
b.languageinfo()