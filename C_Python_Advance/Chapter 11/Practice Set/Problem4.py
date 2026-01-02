#Write a "Comlex" to represent complex number, along with overload operators '+' and '*' which add and multiply them.

class Comlex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return Comlex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        real_part = self.r * other.r - self.i * other.i
        i_part = self.r * other.i + self.i * other.r
        return Comlex(real_part, i_part)

    def __repr__(self):
        return f'{self.r} + {self.i}i'

# Example usage
c1 = Comlex(2, 3)
c2 = Comlex(4, 5)

# Addition
c3 = c1 + c2
print("Addition:", c3)

# Multiplication
c4 = c1 * c2
print("Multiplication:", c4)
