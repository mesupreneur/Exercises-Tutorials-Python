#create a program that take input as a command that may be lower or upercase.
#help command gives the list of commands that we can used in the car.(start,stop,quit)
#if the user type something different than the command then it says I don't understand that...
#if we write start then it says Car started...Ready to go!
#if we write stop then it says Car stopped.
#if we write quit then it quit the game.
"""The lower() methods returns the lowercased string from the given string. It converts all uppercase characters to lowercase.
If no uppercase characters exist, it returns the original string."""
"""The upper() methods returns the uppercased string from the given string.
If no lowercase characters exist, it returns the original string.""" 
"""
if we want to write everywhere lower() then we simply can write with input 
like command=input().lower()

"""
command=""#if w not write this step also the program runs.
while(True):
    command=input("> ").lower()
    if command=="start":
        print("Car started...")
    elif command=="stop":
        print("Car stopped")
    elif command=="help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit the game
        """)
    elif command=="quit":
        break
    else:
        print("I don't understand")

