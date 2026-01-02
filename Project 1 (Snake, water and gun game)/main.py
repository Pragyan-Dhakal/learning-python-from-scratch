import random
computer =random.choice([-1,0,1])
youstr =  input("Enter your choice in the form 's' for snake, 'w' for water, and 'g' for gun: ")

'''1 for snake
-1 for water
0 for gun'''
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake",-1:"water", 0:"gun"}

you = youDict[youstr]

print(f"You choice{reverseDict[you]}\n computer choose {reverseDict[computer]}")

if(computer==you):
    print("It's a Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Loose!")
    elif(computer==1 and you==-1):
        print("You Loose!")
    elif(computer==-1 and you==0):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You Wi23n")
    elif(computer==0 and you==1):
        print("You Loose!")
    else:
        print("There is error in code") #If it occur then there is some mistake in code
    

# import random

# # Computer randomly chooses -1 (water), 0 (gun), or 1 (snake)
# computer = random.choice([-1, 0, 1])

# # Take input from the user
# youstr = input("Enter your choice in the form 's' for snake, 'w' for water, and 'g' for gun: ")

# # Define dictionary for user choices
# youDict = {"s": 1, "w": -1, "g": 0}
# reverseDict = {1: "snake", -1: "water", 0: "gun"}

# # Fetch the user input and map it to the corresponding choice
# you = youDict[youstr]

# # Display both choices
# print(f"You chose {reverseDict[you]}.\nComputer chose {reverseDict[computer]}.")

# # Determine the outcome
# if computer == you:
#     print("It's a Draw!")
# elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
#     print("You Win!")
# else:
#     print("You Lose!")

