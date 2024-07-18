CREATE DATABASE IF NOT EXISTS outfit_finder;

USE outfit_finder;

CREATE TABLE IF NOT EXISTS Color(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Color (name) Values
                             ('navy blue'),
                             ('blue'),
                             ('grey'),
                             ('purple'),
                             ('white'),
                             ('green'),
                             ('brown'),
                             ('pink'),
                             ('black'),
                             ('red'),
                             ('off white'),
                             ('yellow'),
                             ('beige'),
                             ('cream'),
                             ('olive'),
                             ('magenta'),
                             ('burgundy'),
                             ('maroon'),
                             ('grey melange'),
                             ('orange'),
                             ('teal'),
                             ('rust'),
                             ('charcoal'),
                             ('multi'),
                             ('peach'),
                             ('lavender'),
                             ('mustard'),
                             ('khaki'),
                             ('turquoise blue'),
                             ('sea green'),
                             ('coffee brown'),
                             ('mushroom brown'),
                             ('mauve'),
                             ('tan'),
                             ('gold'),
                             ('nude'),
                             ('lime green'),
                             ('fluorescent green');


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



CREATE TABLE IF NOT EXISTS Fabric(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Fabric (name) VALUES
                              ('Cotton'),
                              ('Silk'),
                              ('Wool'),
                              ('Linen'),
                              ('Satin'),
                              ('Velvet'),
                              ('Fleece'),
                              ('Lycra'),
                              ('Mesh'),
                              ('Suede'),
                              ('Polyester'),
                              ('Rayon'),
                              ('Nylon'),
                              ('Spandex'),
                              ('Leather'),
                              ('Denim'),
                              ('Fur'),
                              ('Yarn'),
                              ('Blend'),
                              ('Other');


CREATE TABLE IF NOT EXISTS Style(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Style (name) VALUES
                             ('shirts') ,
                             ('tshirts'),
                             ('tops'),
                             ('sweatshirts'),
                             ('swimwear'),
                             ('jackets'),
                             ('sweaters'),
                             ('tunics'),
                             ('jeans'),
                             ('shorts'),
                             ('skirts'),
                             ('leggings'),
                             ('tights'),
                             ('jeggings'),
                             ('dresses'),
                             ('rompers');


CREATE TABLE If NOT EXISTS Category(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Category (name) VALUES
                                ('Top'),
                                ('Bottom'),
                                ('Dress');

-- For future use
-- ('Jumpsuit'),
-- ('Outerwear'),
-- ('Shoes'),
-- ('Accessories'),
-- ('Other');


CREATE TABLE IF NOT EXISTS 'Usage'(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO 'Usage' (name) VALUES
                                ('casual'),
                                ('formal'),
                                ('sports'),
                                ('smart casual'),
                                ('any'),
                                ('party'),
                                ('travel');


CREATE TABLE IF NOT EXISTS Season(
    id SMALLINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO Season (name) VALUES
                                ('spring'),
                                ('summer'),
                                ('fall'),
                                ('winter'),
                                ('all');

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
                              ('men'),
                              ('women'),
                              ('unisex');

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
    name VARCHAR(50) NOT NULL,
    image_url VARCHAR(255),
    user_id MEDIUMINT NOT NULL,
    category VARCHAR(50) NOT NULL,
    pattern VARCHAR(50) NOT NULL,
    style VARCHAR(50) NOT NULL,
    fabric VARCHAR(50) NOT NULL,
    color VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(id)
    ON DELETE CASCADE,
    FOREIGN KEY (category) REFERENCES Category(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (pattern) REFERENCES Pattern(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (style) REFERENCES Style(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (fabric) REFERENCES Fabric(name)
    ON UPDATE CASCADE,
    FOREIGN KEY (color) REFERENCES Color(name)
    ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS Outfit(
    id MEDIUMINT PRIMARY KEY AUTO_INCREMENT,
    user_id MEDIUMINT,
    'usage' VARCHAR(50),
    season VARCHAR(50),
    weather VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES User(id)
    ON DELETE CASCADE,
    FOREIGN KEY ('usage') REFERENCES `Usage`(name)
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
