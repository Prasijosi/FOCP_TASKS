**TASK 1**

  The BPP_Pizza_Calc function is a code for determining the entire cost of pizza orders at Beckett Plaza Pizza. 
  It starts by greeting users with a message and then goes through a sequence of input validations. Users are 
  requested to enter the number of pizzas they want to purchase, and a valid input.
  The function then asks whether delivery is necessary, if it's Tuesday, and if the consumer used the Beckett Plaza Pizza app, 
  requiring acceptable 'yes' or 'no' replies for each question.The pizza pricing is then computed using the user's input, 
  and a delivery fee is established, with free delivery available for purchases of five or more pizzas. Additional discounts
  are offered if it is Tuesday or if the client uses the app. The final total price is rounded to two decimal places and shown,
  resulting in a user-friendly and efficient method of computing pizza expenses at Beckett Plaza Pizza. The feature encompasses the
  full pizza ordering process, offering clients an integrated and efficient service.


**TASK 2**

  This python program , cat_visit_log, analyzes a cat visitation log file using command-line inputs. The script initially determines 
  whether a command line parameter with the location to the log file is provided. If not, it returns an error message. It then attempts
  to read the contents of the chosen log file, handling any possible file not found issues and terminating with an appropriate message 
  if one is detected.
  
  After successfully reading the log file, the script initializes many variables to track data about cat visits. It goes over each line in
  the log file, skipping empty lines and finishing when it sees the "END" keyword. 
  
  Each non-empty line is then divided into event type ("OURS" for visits from the user's own cat and others for invading cats), entry time,
  and exit time. The duration of each visit is computed, and information such as the number of visits by the user's cat, the number of invading 
  cats sprayed with water, the total time spent in the home, the user's cat's average visit length, and the longest and shortest visit durations
  are updated.
  
  The script tackles potential issues due to incorrect log file formats by producing an error notice for each issue. Finally, it calculates the total time
  spent in the house in hours and minutes, the average visit duration of the user's cat, and publishes a summary of the log file analysis findings. The output 
  contains the number of visits by the user's cat, the number of invading cats drenched with water, the total time spent in the home, the user's cat's average 
  visit length, and the longest and shortest visit duration.


**TASK 3**

Overall the code that we have written in Task implements basic user management system where you create an account, delete an account, update password of an account nad login
to the existing account.
There has been use of file handling,loops,conditions,modules,exception handling and functions to make it as required.
In Main.py
The code implements a basic user management system. The create_new_user function takes a username, full name, and password, encrypts the password using ROT13, and stores
the user information in a "password.txt" file.
The retrieve_user_data function checks if a username already exists and returns the corresponding full name and encrypted password. 
The read_user_data and write_user_data functions handle reading from and writing to the "password.txt" file, respectively. 
The password encryption is performed using a simple ROT13 substitution cipher. Note that for real-world applications, more robust encryption methods and error handling would be necessary.

In login.py
It prompts the user to provide a username and password, and then utilizes the login function to confirm the credentials. The login method first verifies if the username is present by
executing main.retrieve_user_data. If the username is discovered, it compares the encrypted password (using ROT13) to the stored encrypted password. If the passwords match, the script
shows "Welcome!!"; else, it displays "Incorrect password." The script utilizes the getpass module to safely enter the password without displaying it on screen.

In deluser.py
Established a function delete_user that removes an existing user profile from the user management system, which is saved in the "password.txt" file. The function first determines whether
a valid username is provided; if not, it generates an error message and leaves. It then reads the existing user data from the file, determines whether the provided username exists, and, 
if so, removes the proper user information from the list of lines. The changed user data is then written back to the file via the main.write_user_data method. If the provided username has 
been found and erased, it displays an OK message; otherwise, it states that the user does not exist. 

In adduser.py
Using the main module, defined a function create_user for interactively creating a new user profile. The function prompts the user to input their login, complete name, and password. The added
data is then sent to the main. The create_new_user function encrypts the password with ROT13 and adds the new user data to the "password.txt" file. The create_user function is called at the 
conclusion of the script, which starts the user creation process when it is executed. Overall, this script allows for the insertion of new user profiles to the system via user input.

In changepw.py
Created a function called change_password to make it easier to change a user's password. The function prompts the user to provide their current password for verification before determining 
if the given password matches the stored encrypted password for the specified username. If the verification is successful, the script invites the user to input a new password, which it validates.
If the new password is accepted, it modifies the user's password in the "password.txt" file, essentially altering it. The program generates feedback messages for a variety of cases, including 
incorrect existing passwords, mismatched new passwords,and successfully changed passwords. The user enters their username at the start of the script, and the change_password function is invoked
to start the password-changing procedure.


