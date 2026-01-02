with open ("names_of_student.csv") as file:
    lines = file.readlines()

for line in lines:
    row=line.rstrip().split(",")
    print(f"{row[0]} works under {row[1]}")
