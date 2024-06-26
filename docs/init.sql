CREATE DATABASE IF NOT EXISTS outfit_finder;

USE outfit_finder;

CREATE TABLE IF NOT EXISTS Color(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Color (name) VALUES
('Red'),
('Orange'),
('Yellow'),
('Green'),
('Blue'),
('Purple'),
('Pink'),
('Brown'),
('White'),
('Black'),
('Gray'),
('Beige'),
('Other');

CREATE TABLE IF NOT EXISTS Pattern(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Pattern (name) VALUES
('Solid'),
('Ombre'),
('Tie-Dye'),
('Animal Print'),
('Abstract'),
('Geometric'),
('Checkered'),
('Plaid'),
('Floral'),
('Polka Dot'),
('Striped'),
('Other');

CREATE TABLE IF NOT EXISTS Style(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Style (name) VALUES
('Tshirt'),
('Blouse'),
('Tank Top'),
('Crop Top'),
('Sweater'),
('Hoodie'),
('Cardigan'),
('Blazer'),
('Jacket'),
('Coat'),
('Dress'),
('Skirt'),
('Shorts'),
('Jeans'),
('Pants'),
('Leggings'),
('Jumpsuit'),
('Romper'),
('Suit'),
('Other');

CREATE TABLE IF NOT EXISTS Fabric(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Fabric (name) VALUES
('Polyester'),
('Rayon'),
('Nylon'),
('Spandex'),
('Leather'),
('Denim'),
('Fur'),
('Yarn'),
('Blend'),
('Mix'),
('Other');

CREATE TABLE If NOT EXISTS Category(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Category (name) VALUES
('Top'),
('Bottom'),
('Dress'),
('Other');

CREATE TABLE IF NOT EXISTS Occasion(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Occasion (name) VALUES
('Formal'),
('Athletic'),
('Party'),
('Date Night'),
('Wedding'),
('Work'),
('Other');

CREATE TABLE IF NOT EXISTS Season(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Season (name) VALUES
('Spring'),
('Summer'),
('Fall'),
('Winter'),
('Other');

CREATE TABLE IF NOT EXISTS Weather(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Weather (name) VALUES
('Sunny'),
('Rainy'),
('Snowy'),
('Windy'),
('Hot'),
('Cold'),
('Other');

CREATE TABLE IF NOT EXISTS Gender(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Gender (name) VALUES
('Male'),
('Female'),
('Non-Binary'),
('Other');


CREATE TABLE IF NOT EXISTS User(
    id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(50) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    gender VARCHAR(50) NOT NULL,
    FOREIGN KEY (gender) REFERENCES Gender(name)
);


CREATE TABLE IF NOT EXISTS Clothes(
    id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
    image_url VARCHAR(255),
    user_id MEDIUMINT NOT NULL,
    category VARCHAR(50) NOT NULL,
    pattern VARCHAR(50) NOT NULL,
    style VARCHAR(50) NOT NULL,
    fabric VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
    ON DELETE CASCADE,
    FOREIGN KEY (category) REFERENCES Category(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (pattern) REFERENCES Pattern(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (style) REFERENCES Style(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (fabric) REFERENCES Fabric(name)
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS clothes_colors(
    clothes_id MEDIUMINT,
    color_id SMALLINT,
    PRIMARY KEY (clothes_id, color_id),
    FOREIGN KEY (clothes_id) REFERENCES Clothes(id)
    ON DELETE CASCADE,
    FOREIGN KEY (color_id) REFERENCES Color(id)
);

CREATE TABLE IF NOT EXISTS Outfit(
    id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
    user_id MEDIUMINT,
    occasion VARCHAR(50),
    season VARCHAR(50),
    weather VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES User(id)
    ON DELETE CASCADE,
    FOREIGN KEY (occasion) REFERENCES Occasion(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (season) REFERENCES Season(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (weather) REFERENCES Weather(name)
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS outfits_clothes(
    outfit_id MEDIUMINT,
    clothes_id MEDIUMINT,
    PRIMARY KEY (outfit_id, clothes_id),
    FOREIGN KEY (outfit_id) REFERENCES Outfit(id)
    ON DELETE CASCADE,
    FOREIGN KEY (clothes_id) REFERENCES Clothes(id)
);
