# Write your MySQL query statement below
/*
SchoolA
* student_id
* student_name

SchoolB
* student_id
* student_name

SchoolC
* student_id
* student_name
*/
select a.student_name member_A, b.student_name member_B, c.student_name member_C from SchoolA a, SchoolB b, SchoolC c where a.student_name<> b.student_name and b.student_name<>c.student_name and a.student_name<>c.student_name and 
a.student_id <> b.student_id and b.student_id <> c.student_id and a.student_id <> c.student_id