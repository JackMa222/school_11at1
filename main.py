import sqlite3
from datetime import datetime, timedelta

def getQuestion(level):
    
    pass

def leaderboard(userID, mode, level):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT score, username FROM leaderboard WHERE mode = ? AND level = ? ORDER BY score DESC LIMIT 5", (level, ))
    top_scores = cursor.fetchall()
    print(top_scores)
    db.closer()
    # TODO UNFINISHIED

def addLeaderboard(userID, mode, level, score):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO leaderboard (userID, mode, level, score) VALUES (?, ?, ?, ?)", userID, mode, level, score)
        db.commit()
        cursor.execute("""SELECT COUNT(*) + 1 FROM leaderboard WHERE mode = ? AND level = ? AND score > ?""", (mode, level, score))
        position = cursor.fetchone()[0]
        cursor.execute("""SELECT COUNT(*) + 1 FROM leaderboard WHERE userID = ? AND mode = ? AND level = ? AND score > ?""", (userID, mode, level, score))
        personalPosition = cursor.fetchone()[0]
        db.close()
        return position, personalPosition

def timed(userID, level):
    time = 30
    score = 0
    initialTime = datetime.datetime.now()
    endTime = initialTime + timedelta(seconds=time)
    while True:
        question, answer = getQuestion(level)
        print(question)
        userAnswer = input("Answer: ")
        try:
            intUserAnswer = int(userAnswer)
        except:
            print("Error - answer must be a number")
        else:
            if intUserAnswer == answer and datetime.datetime.now() < endTime:
                score = score + 1
            elif datetime.datetime.now() >= endTime:
                print("Out of time, answer will not count")
            else:
                print("Incorrect")
        if datetime.datetime.now() >= endTime:
            break
    print('Times up')
    print(f"Score {score}")
    position, personalPosition = addLeaderboard(userID, 0, level, score)
    print(f"You ranked #{position} on the global leaderboard for Level {level} for the Timed mode")
    print(f"You ranked #{personalPosition} on your personal leaderboard for Level {level} for the Time mode")
    

def streak(userID, level):
    score = 0
    while True:
        question, answer = getQuestion(level)
        print(question)
        userAnswer = input("Answer: ")
        try:
            intUsernswer = int(userAnswer)
        except:
            print("Error - answer must be a number")
            break
        else:
            if userAnswer == answer:
                score += 1
                print("Correct")
            else:
                print("Incorrect")
                break
    print("Game over")
    print(f"Score {score}")
    position, personalPosition = addLeaderboard(userID, 1, level, score)
    print(f"You ranked #{position} on the global leaderboard for Level {level} for the Streak mode")
    print(f"You ranked #{personalPosition} on your personal leaderboard for Level {level} for the Streak mode")

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