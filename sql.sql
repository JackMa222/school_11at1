CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT
);

CREATE TABLE leaderboard(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    mode INTEGER NOT NULL,
    level INTEGER NOT NULL,
    score INTEGER NOT NULL,
    username TEXT,
    FOREIGN KEY(userID) REFERENCES users(id)
);

CREATE TABLE levels(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    level INTEGER NOT NULL,
    additionMin INTEGER,
    additionMax INTEGER,
    subtractionMin INTEGER,
    subtractionMax INTEGER,
    multiplicationTimesTables TEXT,
    divisionTimesTables TEXT,
    levelOperations TEXT 
);