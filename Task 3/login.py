import main
import getpass

def login(username, password):
    # Check if the username exists before prompting for a password
    info_user = main.retrieve_user_data(username)
    if not info_user:
        print("Error:Invalid user id or password.")
        return False

    # If username exists, proceed with password verification
    if main.password_encryption(password) == info_user[1]:
        return True

username = input("Enter username:").lower()
password = getpass.getpass("Enter a password:")

if login(username, password):
        print("Welcome!!")
else:
        print("Incorrect password\n")
