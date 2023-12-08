instruments = []
musicians = ['nare', 'ruben', 'tigran']
add_exec = input("add or exec:::")
if add_exec == "add":
    print("Code continues")
    for i in range(7):
        instruments.append(input("Enter an instrument:"))
    instruments_str = ', '.join(instruments)
    users = {}
    for musician in musicians:
        user_choice = input(f"What instrument does {musician.capitalize()} choose? {instruments_str}:: ")
        if user_choice in instruments:
            users[musician.capitalize()] = user_choice
        else:
            print(f"Please enter a valid instrument from {instruments_str}")
    print(users)
elif add_exec == "exec":
        print("INSTRUMENT REQUIRED-----PAGE CLOSED")

         

