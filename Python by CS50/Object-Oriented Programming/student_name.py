def main():
    name = get_name()
    agency = get_agency()
    print (f"{name} works under {agency}")

def get_name():
    return input("Enter you name: ")

def get_agency():
    return input("Enter your agency: ")

if __name__=="__main__":
    main()
