CREATE TABLE customers (
    id INT,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Ravi', 25, 'Hyderabad'),
(2, 'Asha', 30, 'Chennai'),
(3, 'Imran', 22, 'Bangalore');


CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 2, 700),
(103, 1, 300);

SELECT * 
FROM customers
WHERE city = 'Hyderabad';
SELECT c.name, o.amount
FROM customers c
JOIN orders o
ON c.id = o.customer_id;
SELECT c.name, SUM(o.amount) AS total_amount
FROM customers c
JOIN orders o
ON c.id = o.customer_id
GROUP BY c.name;
SELECT c.name
FROM customers c
LEFT JOIN orders o
ON c.id = o.customer_id
WHERE o.order_id IS NULL;
