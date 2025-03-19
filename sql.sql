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
    FOREIGN KEY(userID) REFERENCES users(id)
);