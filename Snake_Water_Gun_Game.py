# Snake water  Gun game 
'''
Create a game using random module and choice function and store Gun,Snake,Water in the variable.
and take the input from the user(s for snake,w for water,g for gun) and the input limit must be 10 
show the user that how much point he/she get while playing with computer. ( use while loop)
'''
'''
water kill Gun
gun kill snake
snake drink water
'''
import random
computer=["w","g","s"]
count_start=1
count_limit=10
computer_point=0
human_point=0
print(''' 
 Snake,Water,Gun Game''')
print(''' 
          s for snake 
          w for water 
          g for gun
        ''')
while count_start<=count_limit:
    user_input=input("Enter what you want[w for water,s for snake and g for gun]: ").lower()
    computer_random=random.choice(computer)
    if user_input == computer_random:
        print("Tie Both 0 point to each \n ")
    elif user_input=="g" and computer_random=="w":
        computer_point=computer_point+1
        print("you guess is gun and computer guess is water")
        print(f"your point is {human_point} and computer point is {computer_point}")
        print("Computer wins 1 point")
    elif user_input=="w" and computer_random=="g":
        human_point=human_point+1
        print("your guess is water and computer guess is gun")
        print(f"your point is {human_point} and computer guess is {computer_point}")
        print("you wins 1 point")
    elif user_input=="g" and computer_random=="s":
        human_point=human_point+1
        print("your guess is gun and computer guess is snake")
        print(f"your point is {human_point} and computer guess is {computer_point}")
        print("you wins 1 point")
    elif user_input=="s" and computer_random=="g":
        computer_point=computer_point+1
        print("you guess is snake and computer guess is Gun")
        print(f"your point is {human_point} and computer point is {computer_point}")
        print("Computer wins 1 point")
    elif user_input=="s" and computer_random=="w":
        human_point=human_point+1
        print("your guess is snake and computer guess is water")
        print(f"your point is {human_point} and computer guess is {computer_point}")
        print("you wins 1 point")
    elif user_input=="w" and computer_random=="s":
        computer_point+=1
        print("your guess is water and computer guess is snake")
        print(f"your point is {human_point} and computer guess is {computer_point}")
        print("computer wins 1 point")           
    else:
        print("you have input wrong \n")
    print(f"{count_limit-count_start}","no of guess left")
    count_start+=1

print("Game over")
if computer_point==human_point:
    print("Tie")

elif computer_point > human_point:
    print("Computer wins and you loose")
elif human_point>computer_point:
    print("You win the game and computer lose")

print(f"your point is {human_point} and computer point is {computer_point}")
