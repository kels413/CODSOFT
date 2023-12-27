def signUp():
    while True:
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        email = input("Email: ")
        gender = input("Gender: ")
        phoneNumber = input("Phone Number: ")
        password = input("Password: ")
        confirmPassword = input("Confirm Password: ")

        if confirmPassword == password:
            break  # Exit the loop if passwords match
        else:
            print("Sorry, passwords don't match. Please try again.")

    userData = f"{firstName}, {lastName}, {email}, {gender}, {phoneNumber}, {password}\n"
    
    filename = ".RPS"
    filePath = open(filename, "a")

    filePath.write(userData)

    filePath.close()

    print("You have successfully registered for the RPS Game.")

# Call the signUp function to test
signUp()
