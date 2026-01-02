# try:
#     a=int(input("Enter a number: "))
#     print(f"The number you have entered is {a}")

# except ValueError:
#     print("Please input a number.")

#Or

def main():
    x = get_int()
    print(f"The number you have entered is {x}")


def get_int():
    while True:
        try:
            return int(input("Enter a number: "))

        except ValueError:
            # print("Please input a number.") #If you want you can remove # from this line
            pass

    
main()


