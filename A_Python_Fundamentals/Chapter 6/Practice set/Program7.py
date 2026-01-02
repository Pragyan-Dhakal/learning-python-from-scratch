#Write a program to find out wheather a given post is talking about "Harry" or not.
#a = "Hey my name is Harry. I live in Nepal." #You can also take input.
a = input("Enter your post: ")
if("Harry".lower() in a.lower() ):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")