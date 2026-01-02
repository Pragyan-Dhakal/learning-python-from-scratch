#Write a python function to print first n lines of the function pattern:
# ***
# **
# *
# for n =3
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(3)