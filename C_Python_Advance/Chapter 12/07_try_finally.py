def main():
    try:
        a = int(input("Enter a number: "))
        print(a)

    except ValueError:  
        print("Please enter a valid number")
    

    finally:
        print("Hey, I am inside finally.")  #Finally will print at the last of the function even if it is a error.

main()

