#Write a program to find out wheather a student has passed or failed if it requires a total of 40%
#and at least 33% in each subjects to pass. Assume 3 subjects and take marks as an input from the users.
marks1 = int(input("Enter your marks")) #may be not according to question ask ChatGPT make sure.
marks2 = int(input("Enter your marks"))
marks3 = int(input("Enter your marks"))
#check for total percentage:
total_percentage= ((marks1+marks2+marks3)/300)*100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You have passed")
else:
    print("You backbencher, you have failed")