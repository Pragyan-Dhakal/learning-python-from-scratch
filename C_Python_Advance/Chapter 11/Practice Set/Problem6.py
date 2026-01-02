#Write a _str_() method to print the vector as follows:
#7i+8j+10k   
#Assume vector of dimension 3 for this problem.

class Vector:
    def __init__(self, components):
        if len(components) != 3:
            raise ValueError("Vector must be of dimension 3")
        self.components = components

    def __str__(self):
        # Formats the vector in the form "7i+8j+10k"
        return f"{self.components[0]}i+{self.components[1]}j+{self.components[2]}k"


# Example usage:
v = Vector([7, 8, 10])
print(v)  # Output: 7i+8j+10k
