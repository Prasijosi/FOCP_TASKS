import main

def delete_user(username):
    # Delete an existing user from the password file
    if not username:
        print("Error: Please provide a username to delete.\n")
        return

    lines = main.read_user_data()

    user_exists = any(info_user[0] == username for info_user in (line.strip().split(":") for line in lines))

    if user_exists:
        lines = [line for line in lines if line.strip().split(":")[0] != username]
        main.write_user_data(lines)
        print("Account has been deleted successfully.\n")
    else:
        print("User doesn't exist.")

# Prompt for username and call the delete_user function
username = input("Enter username:").lower()
delete_user(username)
