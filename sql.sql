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

UPDATE levels
SET divisionTimesTables = "null"
WHERE level = 3;

UPDATE levels
SET multiplicationTimesTables = "null", divisionTimesTables = "null"
WHERE level = 2;

UPDATE levels
SET multiplicationTimesTables = "null", divisionTimesTables = "null"
WHERE level = 1;

INSERT INTO levels
(level, additionMin, additionMax, subtractionMin, subtractionMax,
 multiplicationTimesTables, divisionTimesTables, levelOperations)
VALUES (5, 1, 500, 1, 100, "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]", "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]", "[0, 1, 2, 3]");

INSERT INTO levels
(level, additionMin, additionMax, subtractionMin, subtractionMax,
 multiplicationTimesTables, divisionTimesTables, levelOperations)
VALUES (5, 1, 500, 1, 100, "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]", "[0, 1, 2, 3]");

INSERT INTO levels
(level, additionMin, additionMax, subtractionMin, subtractionMax,
 multiplicationTimesTables, divisionTimesTables, levelOperations)
VALUES (4, 1, 100, 1, 100, "[2, 3, 4, 5, 6, 7, 8, 9, 10]", "[2, 3, 4, 5, 10]", "[0, 1, 2, 3]");

INSERT INTO levels
(level, additionMin, additionMax, subtractionMin, subtractionMax,
 multiplicationTimesTables, divisionTimesTables, levelOperations)
VALUES (3, 1, 50, 1, 50, "[2, 3, 4, 5]", "", "[0, 1, 2]");

INSERT INTO levels
(level, additionMin, additionMax, subtractionMin, subtractionMax,
 multiplicationTimesTables, divisionTimesTables, levelOperations)
VALUES (2, 1, 20, 1, 20, "", "", "[0, 1]");

INSERT INTO levels
(level, additionMin, additionMax, subtractionMin, subtractionMax,
 multiplicationTimesTables, divisionTimesTables, levelOperations)
VALUES (1, 1, 10, 0, 0, "", "", "[0]");