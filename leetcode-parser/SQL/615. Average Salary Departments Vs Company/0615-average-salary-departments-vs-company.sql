# Write your MySQL query statement below
/*
Salary
* id
* employee_id
* amount
* pay_date

Employee
* employee_id
* department_id
*/
SELECT DISTINCT pay_month, department_id, 
(CASE WHEN department_avg_salary > company_avg_salary THEN 'higher'
     WHEN department_avg_salary < company_avg_salary THEN 'lower'
     WHEN department_avg_salary = company_avg_salary THEN 'same' END) AS comparison
FROM (
SELECT A.employee_id, amount, pay_date,department_id, LEFT(pay_date,7) as pay_month, AVG(amount) OVER(PARTITION BY A.pay_date) AS company_avg_salary,
AVG(amount) OVER(PARTITION BY A.pay_date, B.department_id) AS department_avg_salary
FROM salary AS A
JOIN employee AS B
ON A.employee_id = B.employee_id) AS temp;