# Write a program to input eight numbers from the user and display all the unique number once.
s = set ()
n = input("Enter any number:")
s.add(int(n))
n = input("Enter any number:")
s.add(int(n))
n = input("Enter any number:")
s.add(int(n))
n = input("Enter any number:")
s.add(int(n))
n = input("Enter any number:")
s.add(int(n))
n = input("Enter any number:")
s.add(int(n))
n = input("Enter any number:")
s.add(int(n))
n = input("Enter any number:")
s.add(int(n))

print("Unique Number",s)
#or
# Create an empty set to store unique numbers
"""unique_numbers = set()

# Input eight numbers from the user
for i in range(8):
    num = int(input("Enter any number: "))
    unique_numbers.add(num)  # Add the number to the set

# Display the unique numbers
print("Unique numbers entered:", unique_numbers)"""
