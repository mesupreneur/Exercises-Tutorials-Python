#create a list with numbers,strings,symbols(junk items)and only print the numbers that is grater than 6 
list1=["mesup",24,4,7,9,"abhiskar",5,18,"Django",0,10,6,"apple",3,70,"/"]
for item in list1:
   if str(item).isnumeric() and item>6:
      print(item)
