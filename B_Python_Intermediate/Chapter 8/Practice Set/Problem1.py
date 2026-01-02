#Write a program using functions to find greatest of three numbers.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
def great():
    if(a>b>c):
        print("The greatest number is:", a)

    if(b>c>a):
        print("The greatest number is:", b)

    if(c>b>a):
        print("The greatest number is:", b)

great() #Function Call

#or
a = 5
b = 8
c = 9
def great(a,b,c):
    if(a>b>c):
        print("The greatest number is:", a)

    if(b>c>a):
        print("The greatest number is:", b)

    if(c>b>a):
        print("The greatest number is:", b)

great(a,b,c) #Function Call
