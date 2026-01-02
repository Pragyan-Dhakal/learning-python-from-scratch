# names =[]

# for i in range(3):
#     name = input("Enter a name: ")
#     names.append(name)


# with open("names_of_people.txt","a") as file: #no need to close when withj open is used
#     for name in names:
#         file.write(f"Hello, {name}\n")


names =[]

for i in range(3):
    name = input("Enter a name and home with soma separation: ")
    names.append(name)

                                            # .csv is called coma separated values
with open("names_of_student.csv","a") as file: #no need to close when withj open is used
    for name in names:
        file.write(f"{name}\n")


    



 

    



 