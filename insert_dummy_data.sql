-- SQL: USER TABLE
INSERT INTO user_table (user_id, username, isSubscribed, channels_created, channel_subscribed, polls, followers, followings, photoURL, subscription_data, about_me, visibility, score)
VALUES ('U001', 'RajeshKumar', 0, NULL,'CH001','P005,P009', NULL, 'U004', 'PH001', NULL, 'Movie Lover', 1, 0),
('U002', 'PriyaVerma', 0,'CH001', NULL,'P001,P008', 'U003, U004, U005 ', 'U003, U004','PH002',NULL, 'Studious Girl', 1, 0),
('U003', 'ArjunSingh', 0, NULL,'CH001', 'P002,P004', 'U002, U005', 'U002, U004','PH003',NULL, 'Football Guy', 1, 0),
('U004', 'NehaPatel', 0, NULL, NULL, 'P003,P006', 'U001, U002, U003, U005', NULL, 'PH004', NULL, 'Influencer', 1, 0),
('U005', 'RohanSharma', 0, NULL,'CH001', 'P007,P010', NULL,'U002, U003, U004','PH005',NULL, 'GK Boy', 1, 0);


-- POLL TABLE
INSERT INTO poll_table (poll_id, question, options, tags, user_created, created_time, created_date, ends_at, comment_list)
VALUES 
('P001', 'What is the atomic number of carbon?', 'OP011, OP012, OP013, OP014', 'Science', 'PriyaVerma', '08:00:00', '2024-04-17', '2024-05-01', NULL),
('P002', 'Which planet is known as the "Red Planet"?', 'OP021, OP022, OP023, OP024', 'Space', 'ArjunSingh', '09:00:00', '2024-04-17', '2024-05-01', NULL),
('P003', 'Which company is the worlds largest online retailer by revenue?', 'OP031, OP032, OP033, OP034', 'Business', 'NehaPatel', '10:00:00', '2024-04-17', '2024-05-01', 'ArjunSingh'),
('P004', 'Who won the FIFA World Cup in 2018?', 'OP041, OP042, OP043, OP044', 'Football', 'ArjunSingh', '11:00:00', '2024-04-17', '2024-05-01', NULL),
('P005', 'What is the capital city of Australia?', 'OP051, OP052, OP053, OP054', 'Geography', 'RajeshKumar', '12:00:00', '2024-04-17', '2024-05-01', NULL),
('P006', 'Which company is leading the development of self-driving cars?', 'OP061, OP062, OP063, OP064', 'Technology', 'NehaPatel', '13:00:00', '2024-04-17', '2024-05-01', NULL),
('P007', 'What is the main greenhouse gas responsible for global warming?', 'OP071, OP072, OP073, OP074', 'Environment', 'RohanSharma', '14:00:00', '2024-04-17', '2024-05-01', 'PriyaVerma'),
('P008', 'Which vaccine has been developed to combat COVID-19?', 'OP081, OP082, OP083, OP084', 'Health', 'PriyaVerma', '15:00:00', '2024-04-17', '2024-05-01', NULL),

-- Option TABLE:
INSERT INTO option_table (option_id, option)
VALUES 
('OP011', '6'),
('OP012', '12'),
('OP013', '14'),
('OP014', '22'),
('OP021', 'Venus'),
('OP022', 'Mars'),
('OP023', 'Jupiter'),
('OP024', 'Saturn'),
('OP031', 'Walmart'),
('OP032', 'Alibaba Group'),
('OP033', 'Amazon'),
('OP034', 'eBay'),
('OP041', 'Germany'),
('OP042', 'Brazil'),
('OP043', 'France'),
('OP044', 'Argentina'),
('OP051', 'Sydney'),
('OP052', 'Melbourne'),
('OP053', 'Canberra'),
('OP054', 'Brisbane'),
('OP061', 'Tesla'),
('OP062', 'Google (Waymo)'),
('OP063', 'Uber'),
('OP064', 'General Motors'),
('OP071', 'Carbon dioxide (CO2)'),
('OP072', 'Methane (CH4)'),
('OP073', 'Nitrous oxide (N2O)'),
('OP074', 'Chlorofluorocarbons (CFCs)'),
('OP081', 'Pfizer-BioNTech'),
('OP082', 'Moderna'),
('OP083', 'Oxford-AstraZeneca'),
('OP084', 'Johnson & Johnson'),
('OP091', 'Nomadland'),
('OP092', 'The Trial of the Chicago 7'),
('OP093', 'Mank'),
('OP094', 'Minari'),
('OP101', 'Madrid'),
('OP102', 'Berlin'),
('OP103', 'Rome'),
('OP104', 'Paris');


-- Channel TABLE:

INSERT INTO channel_table (channel_id, channel_name, subscriber_count, polls_in_it)
VALUES ('CH001', 'Basic Science', 3, 'P001,P008');

