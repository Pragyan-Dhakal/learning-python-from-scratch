def main():
    name = input("Enter your name: ")
    hello(name)

def hello(a="Word"):
    print ("Hello,",a)

if __name__=="__main__":
    main()