'''PROGRAM
'''

import re
import json
from cryptography.fernet import Fernet


cipher_suite = Fernet(b'DHML65d-nY3iZL1vsWkrmzf2kSfoHQ9Fnv6IWlyIPzQ=')
print(cipher_suite)
def register_user():
    ''' Register function
    '''

    with open('login.json', 'r', encoding="UTF-8") as file:
        login = json.load(file)
    phone_pattern = r'^\+3749\d{7}$'
    email_pattern =  r'^\w+@gmail\.com$'


    phone_number = input('Enter phone number: ')
    email = input("Enter email: ")

    phone_valid = re.match(phone_pattern, phone_number)
    email_valid = re.match(email_pattern, email)

    if phone_valid and email_valid:
        username = input("Create username: ")
        password = input("Create password: ")
        repeat_pass = input("Repeat password: ")

        if repeat_pass == password:
            encrypt_pass = cipher_suite.encrypt(password.encode()).decode('utf-8')
            login[phone_number] = {
                "username": username,  
                "email": email,  
                "password": encrypt_pass  
            }
            print("User registered successfully!")
        else:
            print("Passwords don't match.")
            return
    else:
        print("Invalid phone number or email. Please enter valid details.")
        return

    with open('login.json', 'w', encoding='utf-8') as file:
        json.dump(login, file, indent=4)

def login_user():
    '''Login function
    '''

    with open('login.json', 'r', encoding="UTF-8") as file:
        login = json.load(file)
    entered_login = input("Enter your phone number: ")
    entered_password = input("Enter password: ")

    if entered_login in login:
        stored_password = login[entered_login]["password"]
        decrypt_pass = cipher_suite.decrypt(bytes(stored_password, 'utf-8')).decode('utf-8')
        login[entered_login]["password"] = decrypt_pass

        if entered_password == decrypt_pass:
            print("Welcome to our page!")
        else:
            print("Wrong password")
    else:
        print("Login not found")

def exit_program():
    ''' Exit function
    '''
    log_out = input("Are you sure you want to leave this page? ")
    if log_out.lower() == "yes":
        print("You have exited the page")
    else:
        print("Link the page one more time")

while True:
    reg_or_log = input("What do you want to do? 1. Register 2. Login 3. Exit: ")
    if reg_or_log == "1":
        register_user()
    elif reg_or_log == "2":
        login_user()
    elif reg_or_log == "3":
        exit_program()
        break
