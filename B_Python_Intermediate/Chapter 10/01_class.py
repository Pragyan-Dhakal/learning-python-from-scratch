class employee:
    #name = "Pragyan Dhakal" #This is a class attribute, name can be directly written below. 
    role = "Data Scientist"
    salary = 500000

pragyan = employee()
pragyan.name = "Pragyan Dhakal" #This is a instance attribute, any components in class can be changed here if needed.
print(pragyan.name, pragyan.role, pragyan.salary) 

ram = employee()
ram.name = "Ram the god"
print(ram.name, ram.role, ram.salary)  

