with open("names_of_people.txt",) as file:
    lines = file.readlines()

for line in sorted(lines): #sorted will arrange in order
    print(line.rstrip())