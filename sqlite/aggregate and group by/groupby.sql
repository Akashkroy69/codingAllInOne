-- create a table for food deliveries with 20 records
CREATE TABLE food_deliveries(
  id INTEGER PRIMARY KEY,
  name TEXT,
  quantity INTEGER,
  price REAL,
  location TEXT
);
-- insert 20 records into the table
INSERT INTO food_deliveries (name, quantity, price, location) VALUES
('Pizza', 10, 12.99, 'New York'),
('Burger', 15, 5.99, 'Los Angeles'),
('Sushi', 8, 24.99, 'San Francisco'),
('Pasta', 12, 10.99, 'Chicago'),
('Salad', 20, 6.99, 'Houston'),
('Sandwich', 25, 4.99, 'Dallas'),
('Tacos', 18, 8.99, 'San Diego'),
('Noodles', 10, 9.99, 'Seattle'),
('Fried Chicken', 22, 14.99, 'Atlanta'),
('Steak', 5, 29.99, 'Boston'),
('Pizza', 14, 12.99, 'Miami'),
('Burger', 30, 5.99, 'Denver'),
('Sushi', 6, 24.99, 'Portland'),
('Pasta', 9, 10.99, 'Las Vegas'),
('Salad', 18, 6.99, 'Orlando'),
('Sandwich', 20, 4.99, 'Phoenix'),
('Tacos', 25, 8.99, 'San Antonio'),
('Noodles', 15, 9.99, 'Philadelphia'),
('Fried Chicken', 10, 14.99, 'Austin'),
('Steak', 8, 29.99, 'San Jose'),
('Pizza', 20, 12.99, 'Charlotte'),
('Burger', 18, 5.99, 'Columbus'),
('Sushi', 12, 24.99, 'Indianapolis'),
('Pasta', 8, 10.99, 'San Francisco'),
('Salad', 25, 6.99, 'Baltimore'),
('Sandwich', 22, 4.99, 'Milwaukee'),
('Tacos', 12, 8.99, 'Washington D.C.'),
('Noodles', 10, 9.99, 'Detroit'),
('Fried Chicken', 15, 14.99, 'Nashville'),
('Steak', 7, 29.99, 'Jacksonville');
-- ascending order
select '------------';
select * from food_deliveries order by quantity asc;
-- descending order
select '------------';
select * from food_deliveries order by quantity desc;
-- distinct
select '------------';
select avg(price) from food_deliveries;

-- group by
select '-----group by-------';
select name, count(*),sum(quantity) from food_deliveries group by name;


