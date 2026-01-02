# Override the _len_() method on vector of problem 5 to display the dimension of the vector.


class Vector:
    def __init__(self, components):
        if len(components) != 4:
            raise ValueError("This vector must have exactly 4 dimensions.")
        self.components = components

    def __add__(self, other):
        # Element-wise addition using zip
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        # Dot product using zip
        return sum(a * b for a, b in zip(self.components, other.components))

    def __str__(self):
        # Format the vector as "7i+8j+10k"
        return f"{self.components[0]}i+{self.components[1]}j+{self.components[2]}k"

    def __len__(self):
        # Returns the dimension of the vector
        return len(self.components)


# Example usage:
v = Vector([7, 8, 10, 12])
print(v)        # Output: 7i+8j+10k
print(len(v))   # Output: 3

