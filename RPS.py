import random

print("Welcome to Rock, Paper, Scissors")
print("press (ctrl d or ctrl c)  to quit the game")

count = 0

try:        
    while True:
       
        userInput = input("Select choice (0, Rock), (1, Scissors), (2, paper) ")
      
        if not userInput:
            print("Input cannot be empty")
            break
        else:
            if not isinstance(userInput, int):
                try:
                    userInput = int(userInput) 
                except ValueError:
                    print(f"Error: user input {userInput} is not a valid integer")
                    break
        randomNumber = random.randint(0,2) #Generate a random number
        choice = ["Rock", "Paper", "Scissors"]
        botChoice = choice[randomNumber] #Match botchoice with the random integers generated
    
        if  userInput > 2:
            userInput = input("Select choice (0, Rock), (1, Scissors), (2, paper) ")

        else:
            usersChoice = choice[userInput] #Match userInput with the choice
            if (userInput == 0 and randomNumber == 1 or userInput == 2 and randomNumber == 1
            or userInput == 1 and randomNumber == 0):
                print("player won")
                print(f"player chose {usersChoice}")
                print(f"bot chose {botChoice}")
                
            elif userInput == randomNumber:
                print("draw")
                print(f"bot chose {botChoice}")
                print(f"player chose {usersChoice}")
            else:
                print("bot won")
                print(f"bot chose {botChoice}")
                print(f"player chose {usersChoice}")

            #logic to quit or continue game
        count += 1
        if count == 5:
            userInput = input("wish to continue ? (y, continue) or  (or ctrl d or ctrl c to quit) ")
            if userInput.lower() == "y":
                count = 0
                continue
            elif userInput.lower() == "n":
                count = 0
                print("Thank you for playing Rock paper scissors Game")
                break
            else:
                print("Not a valid syntax")
                exit(1)
except (EOFError,KeyboardInterrupt):
    print("\nGoodbye!")
    exit(0)

###########ERROR HANDLING (edge cases)#########
    #check if the user input is greater than 2.
    #check when theres no input in the stdin
    #check if the user input any other value rather than y or n in the quit or continue logic

#############IMPROVEMENT#############
    # implement user login
    # implement a file to store the details of the user
    # implement forgetten password


#activities to carry 2day 
    # finish my email stuff
    # read about alias and evnironment variable 
    # make my git to periodcally update and push