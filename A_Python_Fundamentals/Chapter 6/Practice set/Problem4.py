#Write a program to find out wheather a given user name contain less than 10 character or not.
a = (input("Enter your user name: "))
if(len(a)<10):
    print("Your user name has less than 10 character")
else:
    print("Your user name has 10 or more character")