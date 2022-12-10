# Write your MySQL query statement below
/*
Variables
* name
* value

Expressions
* left_operand
* operator
* right_operand
*/

SELECT e.left_operand, e.operator, e.right_operand,
       CASE WHEN operator = '>' THEN IF(v1.value > v2.value, 'true', 'false')
            WHEN operator = '<' THEN IF(v1.value < v2.value, 'true', 'false')
            ELSE IF(v1.value = v2.value, 'true', 'false')
       END AS value
FROM Expressions e
JOIN Variables v1 ON v1.name = e.left_operand
JOIN Variables v2 ON v2.name = e.right_operand;