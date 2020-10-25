#create a program that takes input(number) from the user unless the input(number) is greater than 100
#if the user gives the input(number)less than 100 then it print try again!and ask to input again.
#if the user gives the input that is greater than 100 than print congratulate you have entered the no greater than 100
while(True):
    num=int(input("Guess a number:"))
    if num>100:
        print("congrats! you have entered number greater than 100")
        break
    else:
        print("Try again!")
        continue
