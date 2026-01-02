

class Number:
    def __init__(self, n):
        self.n = n

    # Define the special method for addition
    def __add__(self, num):
        return self.n + num.n

# Create two instances of Number
n = Number(2)
m = Number(1)

# Add them together using the + operator
print(n + m)  # Output will be 3
