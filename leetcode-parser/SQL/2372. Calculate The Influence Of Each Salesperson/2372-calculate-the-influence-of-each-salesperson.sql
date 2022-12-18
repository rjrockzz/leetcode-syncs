# Write your MySQL query statement below
/*
Salesperson
* salesperson_id
* name

Customer
* customer_id
* salesperson_id

Sales
* sale_id
* customer_id
* price
*/
# Write your MySQL query statement below
/**
Three tables: Salesperson/Customer/Sales

salesperson_id is the primary key for Salesperson table.
Salesperson table shows the ID of a salesperson.

customer_id is the primary key for Customer table.
salesperson_id is a foreign key from the Salesperson table.
Customer table shows the ID of a customer and the ID of the salesperson. 

sale_id is the primary key for Sales table.
customer_id is a foreign key from the Customer table.
Sales table shows ID of a customer and the price they paid for the sale with sale_id.


PROBLEM:report the sum of prices paid by the customers of each salesperson. If a salesperson does not have any customers, the total value should be 0.

STEPS:
    IFNULL(,0)
    LEFT JOIN Customer ON salesperson_id
    LEFT JOIN Sales ON customer_id
    SUM(price)
    GROUP BY salesperson_id
    
*/

SELECT
    P.salesperson_id,
    P.name,
    IFNULL(SUM(price),0) AS total
FROM Salesperson P
LEFT JOIN Customer C
    ON P.salesperson_id = C.salesperson_id
LEFT JOIN Sales S
    ON C.customer_id = S.customer_id
GROUP BY 1
