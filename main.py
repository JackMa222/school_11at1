import sqlite3
from datetime import datetime, timedelta
from json import loads
from random import choice, randint

def getQuestion(level):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM levels WHERE level = ? ORDER BY id DESC", (level, ))
    levelData = cursor.fetchone()
    additionMin = levelData[2]
    additionMax = levelData[3]
    subtractionMin = levelData[4]
    subtractionMax = levelData[5]
    multiplicationTimesTables = loads(levelData[6])
    divisionTimesTables = loads(levelData[7])
    levelsOperations = loads(levelData[8])
    
    db.close()
    
    operationOption = choice(levelsOperations)
    # Operation option 0, 1, 2, 3 = Addition, Subtraction, Multiplication, Division respectively
    
    if operationOption == 0:
      number1 = randint(additionMin, additionMax)
      number2 = randint(additionMin, additionMax)
      question = f"{number1} + {number2} = ?"
      answer = number1 + number2
    elif operationOption == 1:
        number1 = randint(subtractionMin, subtractionMax)
        while True:
            number2 = randint(subtractionMin, subtractionMax)
            answer = number1 - number2
            if answer >= 0:
                break
        question = f"{number1} - {number2} = ?"
    elif operationOption == 2:
        number1 = choice(multiplicationTimesTables)
        number2 = choice(multiplicationTimesTables)
        answer = number1 * number2
        question = f"{number1} x {number2} = ?"
    elif operationOption == 3:
        number2 = choice(divisionTimesTables)
        answer = choice(divisionTimesTables)
        number1 = number2 * answer
        question = f"{number1} / {number2} = ?"
    else:
        question = "ERROR - No questions avaliable, press enter to continue"
        answer = ""
    return question, answer

def leaderboard(userID, mode, level):
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute("SELECT score, username FROM leaderboard WHERE mode = ? AND level = ? ORDER BY score DESC LIMIT 5", (mode, level))
    top_scores = cursor.fetchall()
    print(f"Global leaderboard")
    for counter, entry in enumerate(top_scores):
        print(f"#{counter+1}: {entry[1]} ({entry[0]})")
    if not top_scores:
        print("No scores available for this leaderboard.")
        
    cursor.execute("SELECT score, username FROM leaderboard WHERE mode = ? AND level = ? and userID = ? ORDER BY score DESC LIMIT 5", (mode, level, userID))
    top_scores = cursor.fetchall()
    print(f"Personal leaderboard")
    for counter, entry in enumerate(top_scores):
        print(f"#{counter+1}: {entry[1]} ({entry[0]})")
    if not top_scores:
        print("No scores available for this leaderboard.")
    db.close()

def addLeaderboard(userID, mode, level, score):
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        username = cursor.execute("SELECT username FROM users WHERE id = ?", (userID, )).fetchone()
        cursor.execute("INSERT INTO leaderboard (userID, mode, level, score, username) VALUES (?, ?, ?, ?, ?)", (userID, mode, level, score, username[0]))
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
    initialTime = datetime.now()
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
            if intUserAnswer == answer and datetime.now() < endTime:
                score = score + 1
            elif datetime.now() >= endTime:
                print("Out of time, answer will not count")
            else:
                print("Incorrect")
        if datetime.now() >= endTime:
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
            intUserAnswer = int(userAnswer)
        except:
            print("Error - answer must be a number")
            break
        else:
            if intUserAnswer == answer:
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
    menuChoice = input('T for timed, S for streak game and L for leaderboard. Any other key to logout ').upper()
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    minLevel = cursor.execute("SELECT MIN(level) FROM levels").fetchone()[0]
    maxLevel = cursor.execute("SELECT MAX(level) FROM levels").fetchone()[0]
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
                mode = input(f'S for Streak leaderboard or T for timed leaderboard (Level: {level}) ')
                if mode.upper() in ['S', 'T']:
                    if mode.upper() == 'T':
                        mode = 0
                    elif mode.upper() == 'S':
                        mode = 1
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
                db.close()
                if len(user) > 0:
                    print('Username already exists, please try registering again')
                elif len(username) < 1 or len(username) > 12:
                    print('Username must be between 1 and 12 characters')
                elif len(password) > 12:
                    print('Password must be between 0 and 12 characters. (Password can be empty)')
                else:
                    db = sqlite3.connect('database.db')
                    cursor = db.cursor()
                    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                    db.commit()
                    db.close()
                    print('Account created successfully')
    login()       
    
login()