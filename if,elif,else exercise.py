"""
create a progam that take input form the user and that 
input is age(number) and if the age is greater than 18 than print that user can get driver license,
if the age is less than 18 then print that user cannot get driver license,
if the age is equal to 18 than print that user have to come physically at driver center and should show how he drive."""
#age should not be more than 101 and also make a not valid age option
age=int(input("Enter your age: "))
if age>18 and age<101:
    print("you are eligible to get driver license")
elif age<18:
     print("you are not eligible to get driver license")
elif age==18 :
    print("you have to come physically at diver center and you should show how you can you drive")
else:
    print("not a valid age")