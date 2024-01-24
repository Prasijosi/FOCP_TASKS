import os
import main

def login(username, password):
    # Check if the username exists before prompting for a password
    info_user = main.retrieve_user_data(username)
    if not info_user:
        print("Username not found. Please try again.\n")
        return False

    # If username exists, proceed with password verification
    if main.password_encryption(password) == info_user[1]:
        return True

    print("Incorrect password. Please try again.\n")
    return False

username = input("Enter username:").lower()
password = input("Enter a password:")

if login(username, password):
        print("Welcome!!")
else:
        print("Incorrect Username or Password")