# Store the multiplication tables generated in problem 3 in a file named tables.txt.

n = int(input("Enter a number: "))

print(f"The multiplication table of {n} is as follows: ")
 

with open("Table.txt","a") as f:
    for i in range(1, 11):

        a =f"{n}*{i} = {n*i}\n"
        print(a)


        f.write(a)