# Write your MySQL query statement below
/*
Events
* business_id
* event_type
* occurences
(business_id, event_type) is the primary key of this table.

Step 1 : Find the average of events, the we can proceed forward
*/
with avg_events as 
(
select event_type as events, avg(occurences) as average_event from events group by 1
)
select b.business_id from (select business_id, event_type from events where occurences > (select average_event from avg_events where event_type = events)) b group by 1 having count(*)>1