# Write your MySQL query statement below
/*
Schools
* school_id
* capacity
school_id is the primary key for this table.


Exam
* score
* student_count
score is the primary key for this table.
*/
select school_id, ifnull(min(score),-1) as score
from Schools left join Exam
on capacity >= student_count
group by school_id