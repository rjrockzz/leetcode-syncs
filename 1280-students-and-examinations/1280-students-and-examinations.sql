# Write your MySQL query statement below
/*
Students
* student_id
* student_name

Subjects
* subject_name

Examinations
* student_id
* subject_name
*/
 select s.student_id,s.student_name, s.subject_name, ifnull(attended_exams, 0) attended_exams from (select * from students, Subjects) s left join (select student_id, subject_name, count(*) as attended_exams from examinations group by 1,2) e on s.student_id=e.student_id and s.subject_name=e.subject_name order by 1,3