class employee:
    role = "Data Scientist"
    salary = 500000

pragyan = employee()
pragyan.role = "Web developer" #This is a instance attribute, any components in class can be changed here if needed.
print(pragyan.role, pragyan.salary) 

