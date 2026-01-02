#Write a program to open three files 1.txt, 2.txt, and 3.txt if any these files are not present, a massage without exiting the program must be print promiting the same.

files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        with open (file) as f:
            print(f.read())
            print(f"The file {file} is open successfully.")

    except FileNotFoundError:
        print ("The file {file} you are looking for doesn't exist.")

print("Thank You")
