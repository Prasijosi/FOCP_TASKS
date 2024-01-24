import main

def create_user():
    username = input("Enter username:").lower()
    full_name = input("Enter user's real full name:")
    password = input("Enter a password:")
    main.create_new_user(username, full_name, password)

create_user()
