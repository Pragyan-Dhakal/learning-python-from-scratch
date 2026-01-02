marks = {"Pragyan":99, "Rohan" :55, "Hari" :68 }
print(marks.items()) #It will show the list in the dictionary.
print(marks.keys()) #It will show elements in left.
print(marks.values()) #It will show the elements in right.
marks.update({"Rohan":88}) #You can also add the value which is not originally there like : marks.update({"Rohan":88, "Ram":75}) 
print(marks)
marks.update({"Rohan":88, "Ram":75})
print (marks)
print(marks.get("Hari")) #same like print(marks["Hari"]) but one difference is .get give none when name did't exists but ["hari"], if does't exists it give error.