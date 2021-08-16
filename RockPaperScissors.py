import random

computer_wins=0
user_wins=0

states=["rock","paper", "scissors"]

while True:
    users_input=input("Type Rock/Paper/Scissors or Q to Quit the game:  ").lower()
    
    if users_input=="q":
        break

    if users_input not in states:
        continue

    random_generator=random.randint(0,2)
    #rock 0, paper 1, scissors 2

    computer_choice= states[random_generator]

    print("The computer picked" , computer_choice + ".")

    if users_input == "rock" and computer_choice =="scissors":
        print ("You've Won")
        user_wins += 1

    elif users_input == "scissors"  and computer_choice=="paper":
        print ("You've Won")
        user_wins +=1

    elif users_input == "paper" and computer_choice =="rock":
        print ("You've Won")
        user_wins +=1
    
    else:
        print ("Computer Won")
        computer_wins +=1


print ("You've Won", user_wins ,"times.")
print ("Computer Won", computer_wins,"times.")
print ("Goodbye")