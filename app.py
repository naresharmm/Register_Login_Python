''' new py file
'''
import json

from login import Users

def run_users():
    '''Function 
    '''
    with open('login.json', 'r', encoding="UTF-8") as file:
        login_data = json.load(file)

    users = Users(login_data)

    while True:
        reg_or_log = input("What do you want to do? 1. Register 2. Login 3. Exit: ")
        if reg_or_log == "3":
            users.exit_program()
            break
        else:
            if reg_or_log == "1":
                users.register_user()
            elif reg_or_log == "2":
                users.login_user()

if __name__ == '__main__':
    run_users()
