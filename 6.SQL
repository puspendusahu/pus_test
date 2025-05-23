-- 6. TransacƟon Query (10 minutes)
-- Task:
-- Given the tables:
--  orders (order_id, user_id, total_amount, created_at)
--  users (user_id, name, email)
-- Write a query to fetch all users who placed more than 5 orders with a total spending greater than ₹10000.




-- Write a query to fetch all users who placed more than 5 orders with a total spending greater than ₹10000.
SELECT u.user_id, u.name, u.email
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id
HAVING COUNT(o.order_id) > 5 AND SUM(o.total_amount) > 10000;

