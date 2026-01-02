#Write a prpgram to accept the  marks of 6 students and display in sorted manner.
marks =[]
a = int(input("The marks you obtain"))
marks.append(a)
b = int(input("The marks you obtain"))
marks.append(b)
c  = int(input("The marks you obtain"))
marks.append(c)
d = int(input("The marks you obtain"))
marks.append(d) 
e  = int(input("The marks you obtain"))
marks.append(e)
f  = int(input("The marks you obtain"))
marks.append(f)

marks.sort ()
print(marks)