import os

def create_new_user(username, full_name, password):
    # Encrypt the password and create a new user
    if not username or not full_name or not password:
        print("Error: Fill every informations required\n")
        return

    password = password_encryption(password)
    info_user = f"{username}:{full_name}:{password}\n"

    if retrieve_user_data(username):
        print("Username already exists\n")
        return

    with open("password.txt", "a") as f:
        f.write(info_user)
    print("Welcome. Your profile has been created\n")

def password_encryption(password):
    # Encrypt the password using a simple substitution cipher (ROT13)
    encrypted_characters = []
    for p in password:
        if p.isalpha():
            encrypted_characters.append(chr((ord(p) - ord('A' if p.isupper() else 'a') + 13) % 26 + ord('A' if p.isupper() else 'a')))
        else:
            encrypted_characters.append(p)

    encrypted_password = "".join(encrypted_characters)
    return encrypted_password

def retrieve_user_data(username):
    with open("password.txt", "r") as f:
        for line in f:
            info_user = line.strip().split(":")
            if len(info_user) >= 3 and info_user[0] == username:
                return info_user[1], info_user[2]  # Return full name and encrypted password

    return None  # Return None if user not found

def read_user_data():
    # Read user data from the password file
    try:
        with open("password.txt", "r") as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        return []

def write_user_data(lines):
    # Write user data to the password file
    with open("password.txt", "w") as f:
        f.writelines(lines)
        
