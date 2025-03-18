import sqlite3

def main(userID):
    print(f'You are now in the main section with userID: {userID}')

def login():
    accountChoice = input("Select L for login, R for register or any other key to exit: ")
    if accountChoice.upper() not in ['L', 'R']:
        return 1
    username = input("Username: ")
    password = input("Password: ")
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    if username == '' or username == None:
        print('Error: username cannot be empty')
        return 0
    if accountChoice.upper() == 'L':
        user = cursor.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()
        if len(user) == 0:
            print('Error user does not exist')
            return 0     
        elif password == user[0][2]:
            userID = user[0][0]
            main(userID)
        
    elif accountChoice.upper() == 'R':
        user = cursor.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()
        if len(user) > 0:
            print('Username already exists, please try registering again')
            return 0
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        print('Account created successfully')
          
    
def welcome():
    while login() != 1:
        pass
    exit()
    
welcome()