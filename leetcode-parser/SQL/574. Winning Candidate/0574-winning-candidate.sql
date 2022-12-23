# Write your MySQL query statement below
/*
Candidate
* id
* name

Vote
* id
* candidateId
*/

select name from (select c.name, COUNT(*) AS counts from candidate c join vote v on c.id = v.candidateId GROUP BY 1 order by 2 desc) w limit 1 