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
    Translation VARCHAR(100) NOT NULL,
    OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (Order_id)
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

SELECT Orders.Order_id, Users.FirstName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.User_id=Users.FirstName;
