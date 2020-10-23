"""
Harry want to cheat in exam so we are against hari and we want to make hari fail in exam.
Harry want these solution:45*3,56+9=77,56/6 
we have make a calculator that makes hari fail in exam 
Design a calculator which will correctly slove all the problems except the following ones
They are:
45*3=555
56+9=77
56/6=4
Your program should take operator and two numbers from user as input and then return the result."""
print("Enter 1st number:")
num1=int(input())
print("Enter 2nd number:")
num2=int(input())
print("Enter which operator do you want? '+','-','*','/','%','**','//' ")
print("+ means addiction")
print("- means subraction")
print("* means multipication")
print("/ means division")
print("% ,means modulus")
print("** means exponentiation")
print("// means floor division")
operator=input()
if num1== 45 and num2== 3 and operator=="*":#we have kept faulty calculation so that it first check this statement.
    print("Your value is: ","555")
elif num1 ==56 and num2 == 9 and operator =="+":
    print("Your value is: " ,"77")
elif num1 ==56 and num2==6 and operator=="/":
    print("Your value is: ","4")
elif operator=="+":
    print("Your value is: ",num1+num2)
elif operator=="-":
    print("You value is: ",num1-num2)
elif operator=="*":
    print("Your value is: ",num1*num2)
elif operator=="/":
    print("Your value is: ",num1/num2)
elif operator=="%":
    print("Your value is: ",num1%num2)
elif operator=="**":
    print("Your value is: ",num1**num2)
elif operator=="//":
    print("Your value is: ",num1//num2)
else:
    print("Error! please check your input")
    
    

