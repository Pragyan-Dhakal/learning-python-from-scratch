
def main():
    x = int(input("Enter a number: "))
    print(f"The square of the {x} is", square(x))

def square(n):
    return n*n


if __name__=="__main__":
    main()