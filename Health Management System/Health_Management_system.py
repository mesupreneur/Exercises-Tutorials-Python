#Health Management System
#think that you are the fitness trainer and many clients comesto you to lose their muscles,fat etc.
#think that there are three clients-harry,rohan and hammad
#you have to make total 6 files 3 files to log their food and 3 files to log their exercises
#write a function that executed takes as input clients name and also retreive the log [time]ex or food
''''use this function
def getdate():
    import datetime
    return datetime.datetime.now()
'''
def datetime():
    import datetime
    return datetime.datetime.now() 
print("Health Management system: ")
def take(k):
    if k==1:
        c=int(input("Press 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("type the exercise\n")
            with open("harryexe.txt","a") as op:
                op.write(str(datetime())+":"+ value +"\n")
                print("successfully written")
        elif c==2:
            value=input("type the food\n")
            with open("harryfood.txt","a") as op:
                op.write(str(datetime())+":"+ value +"\n")
                print("successfully written")
    elif k==2:
        c=int(input("Press 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("type the exercise\n")
            with open("rohanexe.txt","a") as op:
                op.write(str(datetime())+ ":"+ value+"\n")
                print("successfully written")
        elif c==2:
            value=input("type the food\n")
            with open("rohanfood.txt","a") as op:
                op.write(str(datetime())+":"+value+"\n")
                print("successfully written")
    elif k==3:
        c=int(input("Press 1 for exercise and 2 for food\n"))
        if c==1:
            value=input("type the exercise\n")
            with open("hamadexe.txt","a") as op:
                op.write(str(datetime())+ ":"+ value+"\n")
                print("successfully written")
        elif c==2:
            value=input("type the food\n")
            with open("hamadfood.txt","a") as op:
                op.write(str(datetime())+":"+value+"\n")
                print("successfully written")
    else:
        print("enter a valid input[1 for harry,2 for rohan,3 for hamad]")
def retrieve(k):
    if k==1:#harry ko reterive
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
           with open("harryexe.txt")as op:
               a=op.read()
               print(a)
        elif c==2:
            with open("harryfood.txt")as op:
                a=op.read()
                print(a)
    elif k==2:
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
           with open("rohanexe.txt")as op:
               a=op.read()
               print(a)
        elif c==2:
            with open("rohanfood.txt")as op:
                a=op.read()
                print(a)
    elif k==3:
        c=int(input("Enter 1 for exercise and 2 for food\n"))
        if c==1:
           with open("hamadexe.txt")as op:
               a=op.read()
               print(a)
        elif c==2:
            with open("hamadfood.txt")as op:
                a=op.read()
                print(a)
    else:
        print("enter a valid input[1 for harry,2 for rohan,3 for hamad]")
a=int(input("Press 1 for log and 2 for retrive:\n"))
if a==1:
    b=int(input("Press 1 for harry, 2 for rohan and 3 for hamad\n"))
    take(b)
else:
    b=int(input("Press 1 for harry, 2 for rohan and 3 for hamad\n"))
    retrieve(b)