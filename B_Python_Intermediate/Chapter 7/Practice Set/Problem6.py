#Write a program to calculate the factorial of a given number using for loop.
# 5! = 1*2*3*4*5 this is a defination of factorial, it means to multiply any number from 1 to that number.
n = int(input("Enter a number: "))
product = 1
for i in range(1, n+1):
    product = product*i

print(f"The factorial of {n} is {product}")
