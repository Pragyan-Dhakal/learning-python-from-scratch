#Write a class vector representing a vector of n dimensions. Overload the + add and * multiply operators which calculates the sum andmthe dor(.) products of them.

class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        # Add corresponding components using zip
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        # Dot product: multiply and sum corresponding components
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        return str(self.components)


# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("Addition:", v1 + v2)
print("Dot product:", v1 * v2)
