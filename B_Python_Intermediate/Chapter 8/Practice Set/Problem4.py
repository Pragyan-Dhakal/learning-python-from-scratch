#Write a recursive function to calculate the sum of first  n natural numbers.
"""
sum(n)= 1+2+3+4......+(n-1)+n
sum(n)=sum(n-1) + n
"""
n = int(input("Enter a nth number: "))
def sum(n):
    if(n==1): #This is ti stop being summ of 0+1+2+n, -2+-1+0+1+2+n, etc.
        return 1
    return sum(n-1)+n
print(sum(n))