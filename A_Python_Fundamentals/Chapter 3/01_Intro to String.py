#Once a string is it's letter cannot be edited as usal, so to do that follow the following steps:
name ="Pragyan"
nameshort = name[0:3] # It is the instruction to only add letters at 0,1 and 2'th position
print (nameshort)

name ="Pragyan"
shortname = name[-4:]  #It is the instruction to only add letters at -1,-2, and -3'th position which are counted from back.
print (shortname)
firstcharacter = name[0]
print (firstcharacter)

name = "0123456789"
print(name [1:7:3])