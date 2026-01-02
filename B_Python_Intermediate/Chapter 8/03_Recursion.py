"""
Factorial (4) = 4*3*2*1
Factorial (n) = n*n-1* ..... 3*2*1
Factorial (n) = n* factorial of n-1

"""
def factorial(n):
    if(n==1 or n ==0): #Rule factorial 1 and 0 is 1, if(n==1 or n ==0): This means if n =1 and n = 0 then consider it as 1
        return 1 
    return n* factorial(n-1)
n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}") #Function call