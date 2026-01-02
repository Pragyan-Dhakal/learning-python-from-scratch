import re

name =input ("Enter your name: ")
matches=re.search(r"^(.+), *(.+)$",name) #if ? thats means , is necessary but space is optional
if matches:                              #if * that's means same as ? but it will erase extra space after ,
    # last, first = matches.groups()
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"Hello, {name}")