# Write your MySQL query statement below
# In the Where Clause, we can actually check , the two values coupled inside a tuple
select distinct num as ConsecutiveNums from Logs 
where (Id+1, num) in (select * from logs) 
and (id+2, num) in (select * from logs)