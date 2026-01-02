#Add a static method in ptoblem no. 2, to greet the user with hello.

class calculator:
    def __init__(self, n):
        self.n = n

    def square (self):
        print(f"The square of {self.n} is {self.n*self.n}")
 

    def cube (self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")

    def squareroot (self):
        print(f"The squareroot of {self.n} is {self.n**1/2}")

    @staticmethod
    def greet():
        print("Hello there!")

a=calculator(4)
a.square()
a.cube()
a.squareroot()
a.greet()