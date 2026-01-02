class employee:
    def __init__(self):
        print("Constructor of employee")
    a=1

class programmer(employee):
    def __init__(self):
        print("Constructor of programmer")
    b=2

class manager(programmer):
    def __init__(self):
        print("Constructor of manager")
    c=3

o=employee() #object
print(o.a)
#print(o.b, o.c) #it will show error because there is no attributes b, c in a but:

p=programmer() #Object
print(p.a, p.b)


p=manager() #Object can be anything p,o etc. does't matter if it is repeated
print(p.a, p.b, p.c)


#Same same but different.


class employee:
    def __init__(self):
        print("Constructor of employee")
    a=1

class programmer(employee):
    def __init__(self):
        print("Constructor of programmer")
    b=2

class manager(programmer):
    def __init__(self):
        super().__init__()   #super is used to call parent class "programmer" it will print the parent also.
        print("Constructor of manager")
    c=3

o=employee() #object
print(o.a)
#print(o.b, o.c) #it will show error because there is no attributes b, c in a but:

p=programmer() #Object
print(p.a, p.b)


p=manager() #Object can be anything p,o etc. does't matter if it is repeated
print(p.a, p.b, p.c)



