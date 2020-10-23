"""
Create a dictionary and take input from the user and return the meaning of the word form dictionary """ 
d1={"coding":"the process of assigning a code to something for classification","python":" a general purpose language","Django": "is a high level python framework","facebook":"social networking site"}
print("coding")
print("python")
print("facebook")
a= input("Enter which meaning you want from up: ")
print("The word " + a + " means",d1[a])
