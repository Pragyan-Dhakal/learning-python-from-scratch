email = input("Enter your email: ").strip() #remove extra space in last


try:
    username, domain = email.split("@") #defining two variable at a time.


    if username and domain =="gmail.com":
        print("Valid email address")

    else:
        print("Invalid email address")

except ValueError:
    print("Invalid email format")