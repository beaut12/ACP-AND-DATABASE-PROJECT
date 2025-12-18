INSERT INTO user (fullname, email, username, password, profile_picture) VALUES
('Marga Villanueva', 'marga@email.com', 'marga_v', 'hashedpass123', 'marga.jpg'),
('Vilma Virrey', 'vilma@email.com', 'vilma_v', 'hashedpass234', 'vilma.png'),
('Jonathan Manalo', 'jonathan@email.com', 'jon_manalo', 'hashedpass345', 'jonathan.jpg');

INSERT INTO donation (ref_id, food_type, food_name, status, quantity, expiration, donor_name, contact, delivery, location, user_id, reservation_status) VALUES
('BZ001', 'Cooked Food', 'Chicken Adobo', 'Available', 5, '2025-12-20',
 'Marga Villanueva', '09171234567', 'Pickup', 'Lipa City', 1, 'available'),

('BZ002', 'Packed Food', 'Bread Loaves', 'Available', 10, '2025-12-19',
 'Vilma Virrey', '09221234567', 'Delivery', 'Batangas City', 2, 'reserved'),

('BZ003', 'Canned Goods', 'Sardines', 'Available', 20, '2026-01-10',
 'Jonathan Manalo', '09331234567', 'Pickup', 'Tanauan City', 3, 'available');
