import random
import os
import re

#email reg validator
def is_valid_email(email):
    # Define the regular expression pattern for a basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use the re.match() function to check if the entire string matches the pattern
    match = re.match(pattern, email)

    # If match is not None, the email is valid; otherwise, it's invalid
    return match is not None
#welcome 
def welcomeMessage():
    try:
        print("Welcome to Rock, Paper, Scissors")
        print("press (ctrl d or ctrl c)  to quit the game")
        choice = input("(0.Signup), (1, Login): ")
        if not isinstance(choice, int):
            try:
                choice = int(choice)
                if choice == 0:
                   signUp()
                elif choice == 1:
                    userLogin()
                else:
                    print("Invalid Input!")
                    exit(0)
            except ValueError:
                print("Invalid input, Try Again !")
                exit(0)
    except (KeyboardInterrupt, EOFError):
        print("\nExit from Rock🧨 paper📕 scissors Game✂️ ")
        exit(0)

os.system('clear')
  
def signUp():
    try:
        count = 0
        firstName = input("Enter firstName: ").title()
        lastName = input("Enter lastName: ").title()
        email = input("Enter email: ")

        while not is_valid_email(email):
            print(f"{email} is not a valid email address.")
            email = input("email: ")
            count += 1
            if count > 1:
                print("Try Again!")
                exit(0)

        if os.path.isfile(".RPS"):
                validateEmail(email)

        phoneNumber = input("Enter phoneNumber: ")

        if os.path.isfile(".RPS"):
            validatePhone(phoneNumber)

        password = input("Enter password: ")
        confirmPassword  = input("confirm password: ")

        #password validation.
        while not confirmPassword == password:
          print("Sorry, passwords don't match. Please try again.")
          confirmPassword  = input("confirm password: ")
          count += 1
          if count > 2:
              print("sorry you have to try later 🤧")
              exit(0)
            
        if os.path.isfile(".RPS"):
            validatePassword(password)
       
        os.system('clear') # clear the console

        #creating username c
        userName = creatUserName(firstName, lastName, phoneNumber)
        #Writting and saving the users crendentials in a file.
        userData = f"{firstName}\n{lastName}\n{email}\n{phoneNumber}\n{password}\n{userName}\n"
        filePath = open(".RPS", "a")
        
        filePath.write(userData)
        filePath.close()
        print(f"You have Successfully registered for the RPS Game")
        print(f"your username is:{userName}\n")
        # generating username. (using slicing)
       
    except (KeyboardInterrupt, EOFError):
        print("\nGOOD BYE!")
        exit(0)

#creat username
def creatUserName(firstName, lastName, phoneNumber):
        usrFn = firstName[:3]
        usrLn = lastName[:3]
        usrPhoneNo = phoneNumber[-2:]
        userNameList= [usrFn, usrLn, usrPhoneNo]
        userName = "".join(userNameList)

        return userName

#validate email
def validateEmail(email):
    with open(".RPS", "r") as file:
        fileContent = file.read()
        if email in fileContent:
            print("email already registered")
            exit(0)

#validate phoneNumber
def validatePhone(phoneNumber):
    with open(".RPS", "r") as file:
        fileContent = file.read()
        if phoneNumber in fileContent:
            print("phoneNumber already registered")
            exit(0)

#validate password
def validatePassword(password):
    with open(".RPS", "r") as file:
        fileContent = file.read()
    if password in fileContent:
        print("Password already taken")
        exit(0)
    
#Login Message
        
def userLogin():
    usersName =  input("Enter Username: ")
    while not usersName:
        print("sorry input cannot be Empty: ")
        usersName =  input("Enter Username: ")
    password = input("Enter Password: ")
    while not password:
        print("sorry input cannot be Empty: ")
        password = input("Enter Password: ")
    with open(".RPS", "r") as file:
        fileContent = file.read()
        if usersName in fileContent and password  in fileContent:
            print("Login successFul")
            RPS(usersName)
        else:
            print("Invalid UserName or Password")
            exit(0)
    
def printUserHighscore(userName, playerHighScore):
     print(f"{userName} highScore: {playerHighScore}")
    

#Game logic
def RPS(userName):
    count = 0
    playerHighScore = 0
    botHighScore = 0
    print(f"Welcome in {userName}") #Welcome message
    try:        
        while True:
            userInput = input("Select choice (0, Rock), (1, paper), (2, scissors) ")
        
            if not userInput:
                continue
            else:
                if not isinstance(userInput, int):
                    try:
                        userInput = int(userInput) 
                    except ValueError:
                        print(f"Error: user input {userInput} is not a valid integer")
                        break
            randomNumber = random.randint(0,2) #Generate a random number
            choice = ["Rock 🧨", "Paper 📕", "Scissors ✂️"]
            botChoice = choice[randomNumber] #Match botchoice with the random integers generated
        
            if  userInput in [0, 1, 2]:
                usersChoice = choice[userInput] #Match userInput with the choice                
                if (userInput == 0 and randomNumber == 2) or (userInput == 1 and randomNumber ==  0) or (userInput == 2 and randomNumber == 1):
                    print("player won 💃🏽")
                    print(f"player chose {usersChoice}")
                    print(f"bot chose {botChoice}")
                    
                    playerHighScore += 1
                    print(f"player: {playerHighScore}")
                elif botChoice == usersChoice:
                    print("draw 🤝")
                    print(f"bot chose {botChoice}")
                    print(f"player chose {usersChoice}")
                else:
                    print("bot won 💃🏽")
                    print(f"bot chose {botChoice}")
                    print(f"player chose {usersChoice}")
                    botHighScore += 1
                    print(f"Bot highScore: {botHighScore}")
            else:
                userInput = input("Select choice (0, Rock), (1, Scissors), (2, paper) ")
                continue
                #logic to quit or continue game
            count += 1
            if count == 5:
                userInput = input("wish to continue ? (y, continue) or  (any key to quit) ")
                if userInput.lower() == "y":
                    count = 0
                    continue
                else:
                    if playerHighScore > botHighScore:
                        print(f"Player Won the GAME 🚀")
                        printUserHighscore(userName,  playerHighScore)
                    elif botHighScore > playerHighScore:
                        print(f"Bot won the Game🚀")
                        return botHighScore
                    else:
                        print("it was a draw Game 🤝")
                    print(f"Bot highScore: {botHighScore}")
                    printUserHighscore(userName,  playerHighScore)
                    print("Thank you for playing Rock paper scissors Game")
                    exit(0)
    except (EOFError,KeyboardInterrupt):
        if playerHighScore > botHighScore:
            print(f"Player Won the GAME 🚀")
        elif botHighScore > playerHighScore:
            print(f"Bot won the Game🚀")
        else:
            print("\nit was a draw Game 🤝")
        print(f"Bot highScore: {botHighScore}")
        printUserHighscore(userName,  playerHighScore)
    print("Thank you for playing Rock🧨 paper📕 scissors Game✂️ ")
    exit(0)
if __name__ == "__main__":
    welcomeMessage()

###########ERROR HANDLING (edge cases)#########
    #check if the user input is greater than 2.
    #check when theres no input in the stdin
    #check if the user input any other value rather than y or n in the quit or continue logic

    #email validation
    #name validation
    #password validation

#############IMPROVEMENT#############
    # implement user login
    # implement a file to store the details of the user
    # implement forgetten password
    # find a way to know the user that logged in using their username
    # implement real time email messaging after user registered with their email
    # implement real time greating
    # save the highscore of each user