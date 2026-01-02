import re

url = input("Enter your URL of twitter: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","", url)   #re.sub will substitute will remove https://twitter.com/ with nothing from url.
print(f"Username is: {username}")                     #\. to tolorate . which will mean any charater. ? mean s is optional