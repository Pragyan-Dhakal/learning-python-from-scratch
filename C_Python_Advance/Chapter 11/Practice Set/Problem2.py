#Create a class 'pets' from a class 'animal' and further create a class 'Dog' from 'pets'. Add a method 'bark' to class 'Dog'.

class animals:
    pass

class pets(animals):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow")

d=dog()
d.bark()