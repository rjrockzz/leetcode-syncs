# Write your MySQL query statement below
/*
Managers
* id
* name
* department
* managerId
*/
select name from employee where id in (select managerId from employee group by 1 having(count(*))>=5)