import random


print("Welcome to my rock, paper, scissors game!")


# USER INPUT
user_choice = input("Please make your selection ('rock', 'paper', 'scissors'):")
user_choice = user_choice.capitalize()
print(f"You chose: '{user_choice}'")


# VALIDATE USER INPUTS
valid_choice = ["Rock", "Paper", "Scissors"]
if user_choice not in valid_choice:
    print("Your choice is invalid")
    exit()


# COMPUTER CHOICE
computer_choice = random.choice(valid_choice)
print(f"The computer chose: '{computer_choice}'")



# DETERMINE THE WINNER
# Adapted from code shared in slack by Bonnie:
#https://nyu-tech-2335.slack.com/archives/C5WPFSB52/p1657672686150239
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock":
    if computer_choice == "Scissors":
        print("Rock crushes scissors. You win!")
    else:
        print("Paper covers rock. You lose.")
elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("Paper covers rock. You win!")
    else:
        print("Scissors cuts paper. You lose.")
elif user_choice == "Scissors":
    if computer_choice == "Paper":
        print("Scissors cuts paper. You win!")
    else:
        print("Rock crushes scissors. You lose.")

print("Thank you for playing. Please play again!")

# DISPLAY RESULTS

#-------------------
#Welcome 'Player One' to my Rock-Paper-Scissors game...
#-------------------
#Please choose either 'rock', 'paper', or 'scissors': rock
#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!


