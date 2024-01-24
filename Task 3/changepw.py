import os
import getpass
import main

def change_password(username):
    
    current_password = getpass.getpass("Enter your current password: ")
    info_user = main.retrieve_user_data(username)

    if not info_user or main.password_encryption(current_password) != info_user[1]:
        print("Invalid current password or username. Password not changed.\n")
        return

    new_password = getpass.getpass("Enter your new password: ")

    verify_password = getpass.getpass("Re-enter your new password for verification: ")

    if new_password == verify_password:
        lines = main.read_user_data()
        for i, line in enumerate(lines):
            info_user = line.strip().split(":")
            if info_user[0] == username:
                lines[i] = f"{username}:{main.password_encryption(new_password)}\n"
                main.write_user_data(lines)
                print("Password changed successfully.\n")
                return
    else:
        print("Passwords do not match. Password not changed.\n")

    print("Username not found. Password not changed.\n")

username = input("Enter username:").lower()
change_password(username)
