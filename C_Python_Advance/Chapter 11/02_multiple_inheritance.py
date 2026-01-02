class employee:  #parent/base class 1 
    company = "Microsoft"
    name="Pragyan Dhakal"
    salary = 1000000
    def info(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class developer:  #parent/base class 2
    language ="Python"
    def dev(self):
        print(f"Your language of coding is {self.language}")


class programmer(employee, developer): #Multiple Inheritance Class 
    name = "Ram Bahadur"
    company = "Apple"       # The information of class employee is stored in it if any changes is required change can be made in base class
    def languageinfo (self):
        print(f"The name is {self.name} and his company is {self.company}")

a =employee()  #Object
b =programmer()

a.info()
b.info()
b.languageinfo()
b.dev()