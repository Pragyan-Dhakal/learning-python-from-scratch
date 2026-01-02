#Write a program using function to convert Fahrenheit to celsius.
#Without function
# f = int(input("Enter a Fahrenheit: "))
# c = 5*(f-32)/9
# print(c)

f = int(input("Enter a Fahrenheit: "))

def f_to_c(f):
    return 5 * (f - 32) / 9

print(f_to_c(f))
