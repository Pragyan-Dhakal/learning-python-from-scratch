#Write a program to detect spam comment.
p1 = "Make a lots of monry"
p2 = "buy now"
p3 = "Suscribe this"
p4 = "click here"
a = input("Enter your comment: ")
if(p1 in a or p2 in a or p3 in a or p4 in a):
    print("This is a spam")
else:
    print("This comment is not a spam")