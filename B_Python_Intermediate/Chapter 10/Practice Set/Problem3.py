#Create a class with a class attribute a :
# create an object from it and set "a" directly using object.a=0. Does this change the class attribute?

#Ans: No, modifying a directly using object.a = 0 does not change the class attribute;
# it only creates or modifies an instance attribute for that specific object

class MyClass:
    a = 10  # class attribute

# Create an object of the class
obj = MyClass()

# Modify 'a' using the object
obj.a = 0

print("Class attribute a:", MyClass.a)  # Will still be 10
print("Instance attribute a:", obj.a)   # Will be 0
