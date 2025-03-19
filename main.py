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
        login()
    elif menuChoice == 'T':
        level = input(f'Select level between {minLevel} and {maxLevel}: ')
        try:
            level = int(level)
        except:
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
        else:
            if (type(level) != int) or (level < minLevel) or (level > maxLevel):
                print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            else:
                timed(userID, level)
    elif menuChoice == 'S':
        level = input(f'Select level between {minLevel} and {maxLevel}: ')
        try:
            level = int(level)
        except:
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
        else:
            if (type(level) != int) or (level < minLevel) or (level > maxLevel):
                print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
            else:
                streak(userID, level)
    elif menuChoice == 'L':
        level = input(f'Select level between {minLevel} and {maxLevel}: ')
        try:
            level = int(level)
        except:
            print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
        else:
            if (type(level) == int) and (level >= minLevel) and (level <= maxLevel):
                mode = input(f'S for Steak leaderboard or T for timed leaderboard (Level: {level}) ')
                if mode.upper in ['S', 'T']:
                    leaderboard(userID, mode, level)
                else:
                    print('Error, mode must be S or T') 
            else:
                print(f'Error, level must be be a number between {minLevel} and {maxLevel}')
    main(userID)

def login():
    accountChoice = input("Select L for login, R for register or any other key to exit: ")
    if accountChoice.upper() not in ['L', 'R']:
        exit()
    else:
        username = input("Username: ")
        password = input("Password: ")
        if username == '' or username == None:
            print('Error: username cannot be empty')
        else:
            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            if accountChoice.upper() == 'L':
                user = cursor.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()
                db.close()
                if len(user) == 0:
                    print('Error user does not exist')     
                elif password == user[0][2]:
                    userID = user[0][0]
                    main(userID)
            elif accountChoice.upper() == 'R':
                user = cursor.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()
                if len(user) > 0:
                    print('Username already exists, please try registering again')
                else:
                    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                    db.commit()
                    db.close()
                    print('Account created successfully')
    login() 
          
    
login()