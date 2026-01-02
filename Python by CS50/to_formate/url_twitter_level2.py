import re

url = input("Enter your URL of twitter: ").strip()  
if username := re.search(r"^https?://(www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE): # www. is group 1 and .+ is 2, () indicate group.
    print(f"Username is: {username.group(2)}")