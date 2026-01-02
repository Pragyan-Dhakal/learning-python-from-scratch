# Write a program to display a/b where a and b are integers. If b =0, dispaly infinite by handling the "ZeroDivisionError"

try:
    a = int(input("Enter a first number "))
    b = int(input("Enter a second number "))


    print(a/b)

except ZeroDivisionError:
        print("The result is infinite because you cannot divide by 0. ")

except ValueError:
        print("Please enter a valid number")


 
 