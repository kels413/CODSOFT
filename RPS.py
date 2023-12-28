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
        print("\nGoodbye!")
        exit(0)

os.system('clear')
  
def signUp():
    try:
        count = 0
        firstName = input("firstName: ").title()
        lastName = input("lasttName: ").title()
        email = input("email: ")

        while not is_valid_email(email):
            print(f"{email} is not a valid email address.")
            email = input("email: ")
            count += 1
            if count > 1:
                print("Try Again!")
                exit(0)

        if os.path.isfile(".RPS"):
                validateEmail(email)

        phoneNumber = input("phoneNumber: ")

        if os.path.isfile(".RPS"):
            validatePhone(phoneNumber)

        password = input("password: ")
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
       
        os.system('clear')
        usrFn = firstName[:3]
        usrLn = lastName[:3]
        usrPhoneNo = phoneNumber[-2:]
        userNameList= [usrFn, usrLn, usrPhoneNo]
        userName = "".join(userNameList)
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
    userName =  input("Enter Username: ")
    while not userName:
        print("sorry input cannot be Empty: ")
        userName =  input("Enter Username: ")
    password = input("Enter Password: ")
    while not password:
        print("sorry input cannot be Empty: ")
        password = input("Enter Password: ")
    with open(".RPS", "r") as file:
        fileContent = file.read()
        print(fileContent)
        if userName in fileContent or password  in fileContent:
            print("Login successFul")
            RPS()
        else:
            print("Invalid UserName or Password")
            exit(0)
    
def RPS():
    count = 0
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
        
            if  userInput > 2:
                userInput = input("Select choice (0, Rock), (1, Scissors), (2, paper) ")

            else:
                usersChoice = choice[userInput] #Match userInput with the choice  
                result = (userInput - randomNumber) % 3
                if result == 1:
                    print("player won 💃🏽")
                    print(f"player chose {usersChoice}")
                    print(f"bot chose {botChoice}")
                elif result == 2:
                    print("bot won 💃🏽")
                    print(f"bot chose {botChoice}")
                    print(f"player chose {usersChoice}")
                else:
                    print("draw 🤝")
                    print(f"bot chose {botChoice}")
                    print(f"player chose {usersChoice}")
                     
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

#activities to carry 2day 
    # finish my email stuff
    # read about alias and evnironment variable 
    # make my git to periodcally update and push
