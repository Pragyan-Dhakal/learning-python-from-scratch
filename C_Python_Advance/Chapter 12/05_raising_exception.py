a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

if (b==0):
    raise ZeroDivisionError ("Our program is not meant to divide any number with zero.")

#This program will create error in case of b is 0, this will crash the program in the middle, this is done to know the error in the fast.

else:
    print(f"The division of a by b is {a/b}")

 