import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Ensure the length is at least 4 characters for each character set
    if length < 4:
        print("Password length should be at least 4.")
        return None

    # Generate password
    password = random.choice(lowercase_letters) + \
               random.choice(uppercase_letters) + \
               random.choice(digits) + \
               random.choice(symbols) + \
               ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

def get_user_requirements():
    length = int(input("Enter the password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, include_uppercase, include_numbers, include_symbols

if __name__ == "__main__":
    print("Password Generator")
    
    length, include_uppercase, include_numbers, include_symbols = get_user_requirements()

    generated_password = generate_password(length, include_uppercase, include_numbers, include_symbols)

    if generated_password:
        print("Generated Password:", generated_password)






















































































































































































































