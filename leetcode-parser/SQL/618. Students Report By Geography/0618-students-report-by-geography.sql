# Write your MySQL query statement below
/*
Student
* name
* continent
*/
WITH A AS (SELECT name AS 'America', ROW_NUMBER() OVER (ORDER BY name) AS 'america_rn' FROM student WHERE continent = 'America'),
     B AS (SELECT name AS 'Asia', ROW_NUMBER() OVER (ORDER BY name) AS 'asia_rn' FROM student WHERE continent = 'Asia'),
     C AS (SELECT name AS 'Europe', ROW_NUMBER() OVER (ORDER BY name) AS 'europe_rn' FROM student WHERE continent = 'Europe')


SELECT America, Asia, Europe
FROM A
LEFT JOIN B
ON A.america_rn = B.asia_rn
LEFT JOIN C
ON A.america_rn = C.europe_rn;