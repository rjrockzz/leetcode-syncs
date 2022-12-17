# Write your MySQL query statement below
/* 
RequestAccepted
* requester_id
* accepter_id
* accept_date
(requester_id, accepter_id) is the primary key for this table.
*/
with requests as
(
    select requester_id from RequestAccepted 
        union all
    select accepter_id from RequestAccepted
)
select requester_id as id, count(*) as num from requests group by 1 order by 2 desc limit 1