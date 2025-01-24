CREATE DATABASE IF NOT EXISTS TranslateService;

USE TranslateService;

CREATE TABLE Users (
    User_id INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(80) NOT NULL,
    LastName VARCHAR(80) NOT NULL,
    Password_hash VARCHAR(300) NOT NULL, 
    Email VARCHAR(100) NOT NULL, 
    CreationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (User_id)
);

CREATE TABLE Orders (
    Order_id INT NOT NULL AUTO_INCREMENT,
    User_id INT NOT NULL,
    Book VARCHAR(100) NOT NULL,
    Language VARCHAR(100) NOT NULL,
    Note VARCHAR(300),
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Order_id),
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

SELECT 
    Users.User_id, 
    Users.FirstName, 
    Users.LastName, 
    Users.Email, 
    Orders.Order_id, 
    Orders.Book, 
    Orders.Language, 
    Orders.Note, 
    Orders.OrderDate
FROM 
    Users
INNER JOIN 
    Orders
ON 
    Users.User_id = Orders.User_id;
