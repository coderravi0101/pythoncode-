#password generator program by Ravi Kumar singh
import random
import string

def generate_password(length=12):
    # Define the available character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password using random.choice()
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # Default password length is 12 characters, you can change it if you want.
    password_length = 12

    password = generate_password(password_length)
    print("Generated Password:", password)