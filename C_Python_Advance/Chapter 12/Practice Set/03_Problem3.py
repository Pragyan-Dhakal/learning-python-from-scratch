# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter a number: "))

print(f"The multiplication table of {n} is as follows: ")

for i in range(1, 11):
    print(f"{n}*{i} = {n*i}")