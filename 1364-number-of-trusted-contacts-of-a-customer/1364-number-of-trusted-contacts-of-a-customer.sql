# Write your MySQL query statement below
/*
Customers
* customer_id
* customer_name
* email

Contacts
* user_id
* contact_name
* contact_email

Invoices
* invoice_id
* price
* user_id
*/
WITH cte AS
(SELECT user_id, count(contact_email) contacts_cnt, SUM(contact_email IN (SELECT email FROM Customers)) trusted_contacts_cnt
FROM Contacts
GROUP BY 1)

SELECT i.invoice_id, c.customer_name, i.price, IFNULL(contacts_cnt, 0) contacts_cnt, IFNULL(trusted_contacts_cnt, 0) trusted_contacts_cnt
FROM Invoices i
LEFT JOIN Customers c
ON i.user_id = c.customer_id
LEFT JOIN cte
ON i.user_id = cte.user_id
ORDER BY 1;