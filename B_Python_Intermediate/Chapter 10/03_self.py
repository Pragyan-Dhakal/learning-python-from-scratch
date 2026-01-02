class employee:
    role = "Data Scientist"
    salary = 500000

    def getInfo(self): #self is necessary
        print(f"The role is {self.role}. The salary is {self.salary}")

pragyan = employee()
pragyan.role = "Web developer" #This is a instance attribute, any components in class can be changed here if needed.
print(pragyan.role, pragyan.salary) 

pragyan.getInfo() #call

