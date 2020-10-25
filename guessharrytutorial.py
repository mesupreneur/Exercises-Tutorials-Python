"""
create a program that take input as a number from the user and user have to guess the number.
there will be secret no inside the program.
no of guess should be limited that is 9 and it have to tell the user that the input no is greater or smaller than the secret no
if the user enter secret no then we should say the user that how many guess it take to win!
"""
secret_number=48
guess_count=1
guess_limit=9
print("Number of guess is limited to only 9 times")
while guess_count<=guess_limit:
    guess=int(input("Guess the number: "))
    if guess<48:
        print("You have entered smaller number please enter greater number.\n")
    elif guess>48:
        print("You have entered greater number please enter smaller number.\n")
    elif guess==secret_number:
        print("You won!")
        break
    print(9-guess_count,"no of guesses left")
    guess_count+=1
else:
    print("Game Over")

