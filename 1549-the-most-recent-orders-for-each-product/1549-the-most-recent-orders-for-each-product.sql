# Write your MySQL query statement below
SELECT
    p.product_name,
    p.product_id,
    o.order_id,
    o.order_date
FROM
    Products p
INNER JOIN Orders o ON p.product_id = o.product_id
INNER JOIN (SELECT product_id, MAX(order_date) AS max_date FROM Orders GROUP BY product_id) o2
    ON o.product_id = o2.product_id AND o.order_date = o2.max_date
ORDER BY
    p.product_name ASC,
    p.product_id ASC,
    o.order_id ASC
