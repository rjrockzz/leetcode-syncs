# Write your MySQL query statement below
/*
Books
* book_id
* name
* available_from

Orders
* order_id
* book_id
* quantity
* dispatch_date
*/
SELECT book_id, 
       name
FROM Books
WHERE available_from < '2019-05-23'
AND book_id NOT IN
            (SELECT book_id
             FROM Orders
             WHERE dispatch_date BETWEEN '2018-06-23' AND '2019-06-23'
             GROUP BY book_id
             Having sum(quantity) >= 10) 