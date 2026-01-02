#Write a python function to multipliation table of a given number.
n = int(input("Enter a number: "))    
def table(n):
    for i in range(1,11):
        print(f"{n}*{i}={n*i}")
table(n)