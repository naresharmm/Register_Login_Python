'''Register/Login/Exit
'''
import re
import json
from cryptography.fernet import Fernet

class Users:
    ''' Declaring class Users with it's methods
    '''
    def __init__(self, login_data: dict):
        self.cipher_suite = Fernet(b'DHML65d-nY3iZL1vsWkrmzf2kSfoHQ9Fnv6IWlyIPzQ=')
        self.login_data = login_data
        self.phone_pattern = r'^\+374\d{8}$'
        self.email_pattern = r'^\w+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$'
        self.password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"

    def validate_input(self, value: str):
        ''' Validating given data
        '''
        input_value = input(f"Enter {value}: ")
        while not re.match(getattr(self, f'{value}_pattern'), input_value):
            print(f'Invalid {value} input')
            input_value = input(f"Please enter {value} again: ")

        return input_value

    def input_data(self, input_value:str):
        ''' Matching data function
        '''
        return self.validate_input(input_value)

    def get_user_input(self):
        ''' Getting input of user
        '''
        phone_number = self.input_data('phone')
        email = self.input_data('email')
        password = self.input_data('password')

        repeat_pass = input("Repeat password: ")

        while repeat_pass != password:
            print("Passwords don't match.")
            repeat_pass = input("Repeat password: ")

        return phone_number, email, password

    def encrypt_pass(self, password:str):
        ''' Password encryption
        '''
        return self.cipher_suite.encrypt(password.encode()).decode('utf-8')

    def write_file(self):
        ''' Writing in json file
        '''
        with open('login.json', 'w', encoding='utf-8') as file:
            json.dump(self.login_data, file, indent=4)

    def register_user(self):
        ''' Registering user
        '''
        phone, email, password = self.get_user_input()
        if phone in self.login_data:
            print("Another account has registered this phone number")
            return

        input_username = input("Create username: ")
        input_country = input("Which country are you from? ")
        encrypt_pass_val = self.encrypt_pass(password)
        self.login_data[phone] = {
            "username": input_username, 
            "email": email, 
            "password": encrypt_pass_val, 
            "country": input_country 
        }
        with open('instruments.json', 'r', encoding='utf-8') as file:
            nat_instr = json.load(file)

        if input_country.capitalize() in nat_instr:
            print(f"{', '.join(nat_instr[input_country.capitalize()])}")
        else:
           print("Country not found on the list")

        instr_choice = input("Do you want to make an instrument global? ")
        if instr_choice == "yes":
            with open('international_instr.json', 'r', encoding='utf-8') as file:
                international_instruments_data = json.load(file)

            available_instr = ', '.join(nat_instr[input_country])
            print(f"Choose one of them: {available_instr}")
            chosen_instrument = input("Enter the instrument: ")

            if chosen_instrument in available_instr:
                if chosen_instrument in international_instruments_data:
                    print(f"{international_instruments_data[chosen_instrument]} has already chosen it")
                if phone not in international_instruments_data:
                    international_instruments_data[chosen_instrument] = phone
 
                with open('international_instr.json', 'w', encoding='utf-8') as file:
                    json.dump(international_instruments_data, file, indent=4)

        print("User registered successfully!")
        self.write_file()

    def check_login(self, entered_login, decrypt_pass):
        ''' Check login '''
        for _ in range(3):
            entered_password = input("Enter password: ")
            if entered_password != decrypt_pass:
                print("Wrong password entered, try again.")
                continue
            print("Welcome to our page!")
            return

        self.login_data[entered_login]["suspended"] = True
        self.write_file()
        print("Three incorrect password attempts. Account suspended.")

    def login_user(self):
        ''' User login '''
        entered_login = input("Enter your phone number: ")

        if entered_login not in self.login_data:
            print("Login not found, something went wrong")
            return

        decrypt_pass = self.cipher_suite.decrypt(
            bytes(self.login_data[entered_login]["password"], 'utf-8')
        ).decode('utf-8')

        self.check_login(entered_login, decrypt_pass)

    def exit_program(self):
        ''' exiting the page
        '''
        log_out = input("Are you sure you want to leave this page? ")
        if log_out.lower() == "yes":
            print("You have exited the page")
        else:
            print("Link the page one more time")
