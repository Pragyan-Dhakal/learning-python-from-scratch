#What would be the length in following condition
s= set ()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
#Ans is 2 but

s= set ()
s.add(20)
s.add(20.1)
s.add("20")
print(len(s))
#Ans is 3 because of 20.0 and 20.1