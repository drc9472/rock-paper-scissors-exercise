# Rock Paper Scissors Exercise

## Purpose 
The purpose of this project is to allow a user to play rock, paper, 
scissors against a computer and show the user the results of the game. 

## Input Process
The game begins with a welcome message to the user then asks the user to 
select either rock, paper, or scissors. 

The code for collecting the user input is:

```
user_choice = input("Please make your selection ('rock', 'paper', 'scissors'):")
```

Once the user has made their selection, the input is standardized and 
vaildated for simplicity.

### Input Standardization
To allow the user to submit a response that isn't case sensitive, the user input is formatted to be capitalized using the following code:

```
user_choice = user_choice.capitalize()
```

### Input Validation
To validate whether the user submitted a valid response, I first created a list containing valid responses:

```
valid_choice = ["Rock", "Paper", "Scissors"]
```

I then uses a conditional statement to verify if the user input matched one of these valid statements. If the user input did not, I informed the user their response is not valid and ended the game:

```
if user_choice not in valid_choice:
    print("Your choice is invalid, please restart the game to try again")
    exit()
```

## Randomized Computer Choice
After user input validation, I used a random choice command to randomly select the computer choice from the list of valid responses:

```
computer_choice = random.choice(valid_choice)
```

## Determine the winner
To determine the winner, I needed to set the rules of the game:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
- Any matching choice is a tie

Using nested conditional statements, the following code was used based off of collaboration during class:

```
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

print("------------------------------------")
print("Thank you for playing. Please play again!")
```







