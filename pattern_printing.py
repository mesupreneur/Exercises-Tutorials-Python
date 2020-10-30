#create a program that take input from the user and it must be integer(n)(no of rows) and 
'''
Boolean =True or False
True
*
**
***
****
False
****
***
**
*
'''
print("Pattern Printing:")
try:
    num=int(input("Enter how many rows you want:\n"))
    bool_var=int(input("Enter 1 for True and 2 for False:\n"))
    if bool_var==1:
        pattern=True
        if pattern:
            for i in range(0,num+1):
                print("*"*i)
    if bool_var==2:
        pattern=True
        if  pattern:
            for i in range(num,0,-1):#here -1 print the loop in opposite
                print("*"*i)
except Exception as f:
    f
    print("Hi, it seems that you have given wrong data please enter again")