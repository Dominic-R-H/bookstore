DROP DATABASE IF EXISTS bookstore;

CREATE DATABASE bookstore;
USE bookstore;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    image VARCHAR(255) NOT NULL
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    title VARCHAR(200) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO books (category, subcategory, title, price, image) VALUES

-- Populate some books

('kids', 'Infants', 'Babys First Colors', 9.99, 'https://m.media-amazon.com/images/I/61G+lerftLL._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Infants', 'My First Animal Book', 8.49, 'https://m.media-amazon.com/images/I/81e4cuTihzL._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Infants', 'Shapes and Sounds', 7.99, 'https://i0.wp.com/www.themarginalian.org/wp-content/uploads/2011/06/shapesforsounds_cover.jpg?w=680&ssl=1'),
('kids', 'Infants', 'Little Hands Big World', 10.50, 'https://m.media-amazon.com/images/I/61sZ0P9m8cL._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Infants', 'Bedtime Stories for Babies', 11.25, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS015-WJKmDrL3YmBixd017i8_hr3kbc_j3Hg&s'),

('kids', 'Junior', 'Charlotte''s Web', 10.99, 'https://m.media-amazon.com/images/I/91B3luFcjwL._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Junior', 'The Cat in the Hat', 9.50, 'https://m.media-amazon.com/images/I/61n2olkhm8L._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Junior', 'Diary of a Wimpy Kid', 13.25, 'https://m.media-amazon.com/images/I/81hSQ3rGPiL._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Junior', 'Green Eggs and Ham', 8.99, 'https://m.media-amazon.com/images/I/61dryn3pXbL._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Junior', 'The Very Hungry Caterpillar', 7.99, 'https://m.media-amazon.com/images/I/81qsstEtrgL._AC_UF1000,1000_QL80_.jpg'),

('kids', 'Young', 'Harry Potter and the Sorcerer''s Stone', 14.99, 'https://rukminim2.flixcart.com/image/300/300/xif0q/book/6/t/7/harry-potter-and-the-sorcerer-s-stone-book-1-original-imah9b3wjbvvq2wf.jpeg'),
('kids', 'Young', 'Percy Jackson & the Olympians: The Lightning Thief', 15.50, 'https://m.media-amazon.com/images/I/91WN6a6F3RL._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Young', 'The Hunger Games', 13.75, 'https://m.media-amazon.com/images/I/61I24wOsn8L._AC_UF1000,1000_QL80_.jpg'),
('kids', 'Young', 'The Maze Runner', 12.99, 'https://upload.wikimedia.org/wikipedia/en/d/db/The_Maze_Runner_cover.png'),
('kids', 'Young', 'Divergent', 16.25, 'https://m.media-amazon.com/images/I/71Fk8wjQHDL._UF1000,1000_QL80_.jpg'),

('adults', 'Classic Novels', 'Pride and Prejudice', 18.99, 'https://m.media-amazon.com/images/I/81a3sr-RgdL.jpg'),
('adults', 'Classic Novels', 'Great Expectations', 17.50, 'https://m.media-amazon.com/images/I/81elBAS5LcL._UF1000,1000_QL80_.jpg'),
('adults', 'Classic Novels', 'Moby Dick', 19.25, 'https://m.media-amazon.com/images/I/71K4OH9CqOL._UF1000,1000_QL80_.jpg'),
('adults', 'Classic Novels', 'Wuthering Heights', 16.99, 'https://m.media-amazon.com/images/I/914H-L6bWsL._AC_UF1000,1000_QL80_.jpg'),
('adults', 'Classic Novels', 'Jane Eyre', 18.25, 'https://m.media-amazon.com/images/I/91zU70Aw9IS._AC_UF1000,1000_QL80_.jpg'),

('adults', 'Fiction', 'The Silent City', 14.99, 'https://m.media-amazon.com/images/I/71aN9pjBCZL._AC_UF1000,1000_QL80_.jpg'),
('adults', 'Fiction', 'Echoes of Tomorrow', 15.75, 'https://m.media-amazon.com/images/I/61Wb2sa60hL._AC_UF1000,1000_QL80_.jpg'),
('adults', 'Fiction', 'The Last Letter', 13.99, 'https://m.media-amazon.com/images/I/81mrHyhbtTL._AC_UF1000,1000_QL80_.jpg'),
('adults', 'Fiction', 'Beneath the Blue Sky', 12.50, 'https://m.media-amazon.com/images/I/910BIQgMH0L._UF1000,1000_QL80_.jpg'),
('adults', 'Fiction', 'A Life Unwritten', 16.00, 'https://images-eu.ssl-images-amazon.com/images/I/71ihVsbgixL._AC_UL210_SR210,210_.jpg'),

('adults', 'Comic', 'Watchmen', 9.99, 'https://m.media-amazon.com/images/I/81Hf9W0uoxL.jpg'),
('adults', 'Comic', 'Batman: The Killing Joke', 10.50, 'https://m.media-amazon.com/images/I/91OjBx3hSNL._AC_UF1000,1000_QL80_.jpg'),
('adults', 'Comic', 'Spider-Man: Blue', 11.25, 'https://m.media-amazon.com/images/I/81PHzU0nPpL._UF1000,1000_QL80_.jpg'),
('adults', 'Comic', 'X-Men: Days of Future Past', 8.99, 'https://m.media-amazon.com/images/I/A1d9ajwM3mL._UF1000,1000_QL80_.jpg'),
('adults', 'Comic', 'V for Vendetta', 10.99, 'https://m.media-amazon.com/images/I/612jURJ-GGL._AC_UF1000,1000_QL80_.jpg'),

('adults', 'Crime and Thriller', 'The Da Vinci Code', 17.99, 'https://upload.wikimedia.org/wikipedia/en/6/6b/DaVinciCode.jpg'),
('adults', 'Crime and Thriller', 'Gone Girl', 18.50, 'https://m.media-amazon.com/images/I/71DD0CjO86L.jpg'),
('adults', 'Crime and Thriller', 'The Girl with the Dragon Tattoo', 16.75, 'https://m.media-amazon.com/images/I/81YW99XIpJL._UF1000,1000_QL80_.jpg'),
('adults', 'Crime and Thriller', 'The Silence of the Lambs', 15.99, 'https://m.media-amazon.com/images/I/71wytopNhPL._AC_UF1000,1000_QL80_.jpg'),
('adults', 'Crime and Thriller', 'Angels & Demons', 19.00, 'https://m.media-amazon.com/images/I/61ZnQqg8xzL._AC_UF1000,1000_QL80_.jpg');
