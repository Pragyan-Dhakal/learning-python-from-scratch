name = input("Enter your name: ").strip()

if "," in name :
    last, first = name.split(", ") 
    name = f"{first} {last}" #updating name

print(f"Hello, {name}")