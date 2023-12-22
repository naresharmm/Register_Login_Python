''' Instruments
'''
nat_instr = {"armenia": ["dhol", "zurna"], "greece": ["bouzuki", "lyre"]}


for country, instruments in nat_instr.items():
    country = input("Which country are you from?  ")
    print(f"{country}: {instruments}")