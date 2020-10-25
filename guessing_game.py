#create a program that takes input as a guessing no and there must have only three changes to guess a no
#there must be a secret no and if guess is not correct in three times it says Sorry you failed !
#if the user enter the secret no then print You win! and donot takes the input again
secret_number=10
guess_count=0
guess_chances=3
while guess_count<guess_chances:
    guess=int(input("Guess: "))
    guess_count+=1
    if guess==secret_number:
        print("You win!")
        break
else:
    print("Sorry! you failed")
#we have to write else statement sepretely so that it donot executes in the middle of the program
#when while loop entirely complete then it helps to write sorry you failed after 3 chances.
    
        
