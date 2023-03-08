
# dictionary for abbrevitions
abbreviations = {
    "DAO": "Data Access Objects",
    "DAP": "Direct Access Protocol",
    "DAT": "Digital Audio Tape",
    "DB": "DataBase",
    "DNS": "Domain Name System",
}

# user input 
user_input = input('Please enter addreviation: ')

# loop thru and checks if abbreviations is in dictionary. 
if user_input in abbreviations:
    print(abbreviations[user_input])
else:
    print('Abbreviation not found')

    

