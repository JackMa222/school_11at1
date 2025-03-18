import sqlite3

def getQuestion(level):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    
    pass

def leaderboard(userID, mode, level):
    pass

def timed(userID, level):
    pass

def streak(userID, level):
    pass

def main(userID):
    #TODO Finish display options
    menuChoice = input('T for timed, S for streak game and L for leaderboard. Any other key to logout ').upper()
    minLevel = 1
    maxLevel = 6
    if menuChoice not in ['T', 'S', 'L']:
        return 1
    elif menuChoice == 'T':
        level = input(f'Select level between {minLevel} and {maxLevel}: ')
        try:
            level = int(level)
        except:
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            return 0
        if (type(level) != int) or (level < minLevel) or (level > maxLevel):
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            return 0
        timed(userID, level)
    elif menuChoice == 'S':
        level = input(f'Select level between {minLevel} and {maxLevel}: ')
        try:
            level = int(level)
        except:
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            return 0
        if (type(level) != int) or (level < minLevel) or (level > maxLevel):
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            return 0
        streak(userID, level)
    elif menuChoice == 'L':
        level = input(f'Select level between {minLevel} and {maxLevel}: ')
        try:
            level = int(level)
        except:
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            return 0
        if (type(level) != int) or (level < minLevel) or (level > maxLevel):
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            return 0
        mode = input(f'S for Steak leaderboard or T for timed leaderboard (Level: {level}) ')
        if mode.upper() not in ['S', 'T']:
            print('Error, mode must be S or T')
            return 0
        leaderboard(userID, mode, level)
    

def login():
    accountChoice = input("Select L for login, R for register or any other key to exit: ")
    if accountChoice.upper() not in ['L', 'R']:
        return 1
    username = input("Username: ")
    password = input("Password: ")
    if username == '' or username == None:
        print('Error: username cannot be empty')
        return 0
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    if accountChoice.upper() == 'L':
        user = cursor.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()
        db.close()
        if len(user) == 0:
            print('Error user does not exist')
            return 0     
        elif password == user[0][2]:
            userID = user[0][0]
            while main(userID) != 1:
                pass
                    
    elif accountChoice.upper() == 'R':
        user = cursor.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()
        if len(user) > 0:
            print('Username already exists, please try registering again')
            db.close()
            return 0
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        db.commit()
        db.close()
        print('Account created successfully')
        
          
    
def welcome():
    while login() != 1:
        pass
    exit()
    
welcome()