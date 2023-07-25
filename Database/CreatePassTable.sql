CREATE TABLE User_password (
    UserID int NOT NULL,
    HashedPassword CHAR,
    PRIMARY KEY (UserID)
);

INSERT INTO User_password
VALUES
(1, 'pass1'),
(2, 'pass2'),
(3, 'pass3'),
(4, 'pass4');
