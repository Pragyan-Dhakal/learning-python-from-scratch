# Write a program to printm third, fifth and seventh element from the list using enumerate function.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i, item in enumerate(a):
    if i==2 or i==4 or i==6:
        if(i==2):
            print(f"The {i+1}rd element is: {item}")

    
        else:
            print(f"The {i+1}th element is: {item}")

