friends = ["apple", "orange", "12", "1.225", "True", "Ram"] 
                                        
print(friends)  #String never change but list does.


friends.append("Shyam") #append means to add at ends
print(friends)

list =[2,4,8,2,90,100,12,15]
list.sort() #sort to arrange in increasing order
print(list)

list.reverse() #reverse to arrange in decreasing order
print(list)

list.insert(5,9) #To add 9 in 5th position
print(list)  #Counting goes like 0,1,2,3,4,5 in all case.

list.pop(3) #It will delete 6th position.
print(list)

list.remove(100) #It will remove certain value from list.
print(list)