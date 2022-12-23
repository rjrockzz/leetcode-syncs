# Write your MySQL query statement below
/*
SurveyLog
* id
* action
* question_id
* answer_id
* q_num
* timestamp
*/
with cte as 
(select 
    question_id,
    sum(case when answer_id is not null then 1 else 0 end) as answered_times,
    sum(case when action = 'show' then 1 else 0 end) as showed_times
from SurveyLog
group by question_id)

select question_id as survey_log
from cte
order by answered_times/showed_times desc, question_id asc
limit 1