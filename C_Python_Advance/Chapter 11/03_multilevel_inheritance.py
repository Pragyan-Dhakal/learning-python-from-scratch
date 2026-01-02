class employee:
    a=1

class programmer(employee):  #multilevel_inheritance
    b=2

class manager(programmer):
    c=3

o=employee() #object
print(o.a)
#print(o.b, o.c) #it will show error because there is no attributes b, c in a but:

p=programmer() #Object
print(p.a, p.b)


p=manager() #Object can be anything p,o etc. does't matter if it is repeated
print(p.a, p.b, p.c)