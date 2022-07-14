import random



print("welcome to rock paper scissors game")

# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")

# USER INPUTS

user_choice = input("please make a selection ('rock', 'paper', 'scissors'): ")
user_choice = user_choice.lower()

print("you chose:", user_choice)
print(f"You chose: {user_choice}")

# Validate User Inputs

#breakpoint()

valid_options = ["rock", "paper", "scissors"]


if user_choice not in valid_options:
    print("sorry invalid entry")
    exit()


# Computer Choice

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("Computer chose:", computer_choice)



# Determine the Winner
#credits to Bonnie Auger at NYU!!!
#https://nyu-tech-2335.slack.com/archives/C5WPFSB52/p1657672686150239

if user_choice == computer_choice:
    print("issa draw!!!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("rock beats scissors, you win! sheeeesh")
    else:
        print("paper beats rock (for some reason; idk i don't make the rules) you lose. wawa")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("paper beats rock, you win! sheeesh")
    else:
        print("scissors beats paper, you lose")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("scissors beats paper, you win! sheeesh")
    else:
        print("rock beats scissors, you lose")



# Display Results


#-------------------

#-------------------
#Thanks for playing. Please play again!
