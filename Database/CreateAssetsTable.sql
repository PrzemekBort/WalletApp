CREATE TABLE Assets (
    Asset_ID INT PRIMARY KEY,
    AssetType CHAR(10) NOT NULL,
    Name CHAR(30) NOT NULL,
    Quantity FLOAT NOT NULL,
    BuyPrice FLOAT NOT NULL,
    BuyDate CHAR(10)
);

INSERT INTO Assets
values
(101, 'Crypto', 'BTC', 11.123, 78954.23, '07-05-2022'),
(201, 'FIAT', 'PLN', 25623, 25623, '12-12-2020'),
(301, 'GOLD', 'GOLD1', 1, 8500, '14-04-2022');