# Write your MySQL query statement below
select person_id, concat(name, "(", left(profession,1),")") as name from person order by 1 desc