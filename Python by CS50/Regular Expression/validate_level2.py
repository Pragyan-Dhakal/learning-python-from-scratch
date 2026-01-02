import re

email = input("Enter your email: ").strip() #remove extra space in last

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_].+\.com$",email):   # .+means somethings is in there, .* ,means there is either somethings or nothings this sign is from re libary.
    print("Valid")                     # ^ this means  starting of word and $ means end.
                                        
else:
    print("Invalid")