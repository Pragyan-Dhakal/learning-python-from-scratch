#Write a program to find the greatest of four number entered by the user.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
if(a>b and a>c and a>d):
    print("Greatest number is:",a)
elif(b>a and b>c and b>d):
    print("Greatest number is:",b )
elif(c>b and c>a and c>d):
    print("Greatest number is:",c )
elif(d>b and d>c and d>a):
    print("Greatest number is:",d )