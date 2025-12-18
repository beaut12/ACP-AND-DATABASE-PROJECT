CREATE DATABASE beyond_zero;

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
          fullname VARCHAR(150),
          email VARCHAR(150) UNIQUE,
          username VARCHAR(150) UNIQUE,
          password VARCHAR(200),
          profile_picture VARCHAR(300)
);

INSERT INTO users (fullname, email, username, password, profile_picture) VALUES
('Marga Villanueva', 'marga@email.com', 'marga_v', 'hashedpass123', 'marga.jpg'),
('Vilma Virrey', 'vilma@email.com', 'vilma_v', 'hashedpass234', 'vilma.png'),
('Jonathan Manalo', 'jonathan@email.com', 'jon_manalo', 'hashedpass345', 'jonathan.jpg');

CREATE TABLE donation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ref_id VARCHAR(10) UNIQUE,
    food_type VARCHAR(100),
    food_name VARCHAR(100),
    status VARCHAR(50),
    quantity INT,
    expiration VARCHAR(50),
    donor_name VARCHAR(100),
    contact VARCHAR(100),
    delivery VARCHAR(50),
    location VARCHAR(100),
    user_id INT,
    reservation_status VARCHAR(20) DEFAULT 'available',
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO donation (ref_id, food_type, food_name, status, quantity, expiration, donor_name, contact, delivery, location, user_id, reservation_status) VALUES
('BZ001', 'Cooked Food', 'Chicken Adobo', 'Available', 5, '2025-12-20',
 'Marga Villanueva', '09171234567', 'Pickup', 'Lipa City', 1, 'available'),

('BZ002', 'Packed Food', 'Bread Loaves', 'Available', 10, '2025-12-19',
 'Vilma Virrey', '09221234567', 'Delivery', 'Batangas City', 2, 'reserved'),

('BZ003', 'Canned Goods', 'Sardines', 'Available', 20, '2026-01-10',
 'Jonathan Manalo', '09331234567', 'Pickup', 'Tanauan City', 3, 'available');

SELECT * FROM users;

SELECT * FROM donation
WHERE reservation_status = 'available';

SELECT food_name, quantity, location
FROM donation
WHERE location = 'Lipa City';

SELECT users.fullname, users.email, donation.food_name, donation.quantity, donation.location
FROM users
INNER JOIN donation ON users.id = donation.user_id;

SELECT users.fullname, donation.food_name, donation.reservation_status
FROM users
INNER JOIN donation ON users.id = donation.user_id
WHERE donation.reservation_status = 'reserved';

SELECT food_name, donor_name, location, delivery
FROM donation
WHERE delivery = 'Pickup';

SELECT users.fullname, COUNT(donation.id) AS total_donations
FROM users
LEFT JOIN donation ON users.id = donation.user_id
GROUP BY users.fullname;

SELECT users.fullname, SUM(donation.quantity) AS total_quantity
FROM users
INNER JOIN donation ON users.id = donation.user_id
GROUP BY users.fullname;

SELECT food_name, expiration, donor_name
FROM donation
WHERE expiration < '2025-12-21';
