# Write your MySQL query statement below
/*
Employee
* empId
* name
* supervisor
* salary
empId is the primary key column for this table.

Bonus
* empId
* bonus
*/
select e.name, b.bonus from employee e left join bonus b on e.empId = b.empId where b.bonus<1000 or b.bonus is null