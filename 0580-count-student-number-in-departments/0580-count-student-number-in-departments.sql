# Write your MySQL query statement below
/*
Student 
* student_id
* student_name
* gender
* dept_id
student_id is the PK

Department
* dept_id
* dept_name
*/
select d.dept_name, ifnull(s.student_number,0) student_number from department d left join (select dept_id, count(*) as student_number from student group by 1) s on s.dept_id = d.dept_id order by 2 desc, 1