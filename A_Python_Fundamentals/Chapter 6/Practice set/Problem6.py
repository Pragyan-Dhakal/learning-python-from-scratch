#Write a program to calculate the grade of a students from his marks from the following scheme:
a = int(input("Enter your marks: "))
if(a<=100 and a>=90):
    print("Your grade is Ex") #elif can also be used
if(a<=90 and a>=80):
    print("Your grade is A")
if(a<=80 and a>=70):
    print("Your grade is B")
if(a<=70 and a>=60):
    print("Your grade is C")
if(a<=60 and a>=50):
    print("Your grade is D")
if(a<=50):
    print("Your grade is F")