# Write your MySQL query statement below
/* 
Products
* product_id
* price

Purchases
* invoice_id
* product_id
* quantity
*/
# CTEs
WITH details_by_invoices AS (
    # Calculate total spendings for each row from `Purchases` table
    SELECT
        pu.invoice_id
        , pu.product_id
        , pu.quantity
        , pu.quantity * pr.price AS price
    FROM
        Purchases AS pu
            INNER JOIN Products AS pr
                ON pu.product_id = pr.product_id
)
, invoice_with_max_total AS (
    # Find `invoice_id` with max spendings and, in case of tie, with minimal `invoice_id`
    SELECT
        invoice_id
    FROM
        details_by_invoices
    GROUP BY
        invoice_id
    ORDER BY
        SUM(price) DESC
        , invoice_id ASC
    LIMIT 1
)
# Query's body
SELECT
    product_id
    , quantity
    , price
FROM
    details_by_invoices
WHERE
    invoice_id IN (
        SELECT
            invoice_id
        FROM
            invoice_with_max_total
    );