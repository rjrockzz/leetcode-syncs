# Write your MySQL query statement below
/*
Student
* student_id
* student_name

Exam
* exam_id
* student_id
* score
*/
WITH cte AS 
(
	SELECT exam_id, student_id, 
	RANK() OVER(partition by exam_id order by score DESC) AS "high_score",
	RANK() OVER(partition by exam_id order by score) AS "low_score"
	FROM Exam 
)

SELECT DISTINCT e.student_id, s.student_name
FROM Exam e LEFT JOIN Student s ON s.student_id = e.student_id
WHERE e.student_id NOT IN (SELECT student_id FROM cte WHERE high_score = 1 OR low_score = 1) order by student_id