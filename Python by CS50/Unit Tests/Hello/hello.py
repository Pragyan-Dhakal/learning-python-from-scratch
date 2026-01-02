def main():
    name = input("Enter your name: ") #If this line is removed it will print hello, world
    print(hello(name))

def hello(a="World"):
    return (f"Hello, {a}")

if __name__=="__main__":
    main()