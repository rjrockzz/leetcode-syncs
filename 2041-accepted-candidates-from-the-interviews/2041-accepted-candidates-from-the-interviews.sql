# Write your MySQL query statement below
/*
Candidates
* candidate_id
* name
* years_of_exp
* interview_id

Rounds
* interview_id
* round_id
* score
*/
with cte as (
select c.candidate_id, c.years_of_exp, sum(r.score) sums from candidates c join rounds r using(interview_id) group by 1,2
)
select candidate_id from cte where sums>15 and years_of_exp>=2