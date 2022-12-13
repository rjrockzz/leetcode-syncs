# Write your MySQL query statement below
SELECT
    p.product_name,
    p.product_id,
    o.order_id,
    o.order_date
FROM
    Products p
INNER JOIN (
    SELECT
        order_id,
        product_id,
        order_date,
        RANK() OVER (PARTITION BY product_id ORDER BY order_date DESC) `rank`
    FROM Orders
) o
    ON p.product_id = o.product_id
WHERE
    o.rank = 1
ORDER BY
    p.product_name ASC,
    p.product_id ASC,
    o.order_id ASC
