try:
    a = int(input("Enter a number: "))
    print (a)

except Exception as p:  # If a user enter a invalid number, let's say a letter, the program will not crash or show a error it will print
    print(p)            # something else to show that the user has enter a invald number.

# Or it can be done as:

try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError:  # This specifically catches invalid input (non-integers)
    print("Please enter a valid number")
 