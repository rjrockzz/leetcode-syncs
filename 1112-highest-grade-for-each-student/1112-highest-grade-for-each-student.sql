# Write your MySQL query statement below
/*
Enrollments
* student_id
* course_id
* grade
(student_id, course_id) is the PK for the table
*/
with cte as(select *, rank() over (partition by student_id order by grade desc, course_id) `ranks` from enrollments) select student_id, course_id, grade from cte where ranks = 1 order by student_id 