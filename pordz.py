'''PROGRAM
'''

import json


def modify_user_instrum(user_data: dict, phone_number: str):
    '''
   this is a function which gives an opportunity to change instrument field

    '''
    user_data[phone_number]["instrument"] = input("Enter new instrument: ")

with open('users.json', 'r', encoding = "UTF-8") as file:
    users = json.load(file)

while True:
    add_exit = input("Add or Exit: ")

    if add_exit == "add":
        phone_number = input("Enter phone number: ")
        if phone_number in users:
            change_type = input('what do you want to change? 1. Instruments / 2. Username: ')
            if change_type == '1':
                modify_user_instrum(users, phone_number)
            elif change_type == '2':
                new_name = input("Enter new username: ")
                users[phone_number]["name"] = new_name
        else:
            user_name = input("Enter username: ")
            instruments = input("Enter instruments: ")

            users[phone_number] = {
                "name": user_name,
                "instrument": instruments
            }
    elif add_exit == "exit" or len(users) > 4:
        print("Exiting or user limit reached.")
        break
with open('users.json', 'w', encoding = 'utf-8') as file:
    json.dump(users, file, indent=4)
























# while True:
#     instruments_str = ', '.join(instruments)
#     users = {}
#     for musician in musicians:
#user_choice = input(f"What instrument does {musician.capitalize()} choose? {instruments_str}:: ")
#         if user_choice in instruments:
#             users[musician.capitalize()] = user_choice
#         else:
#             print(f"Please enter a valid instrument from {instruments_str}")

#     print(users)
