# Write your MySQL query statement below
with new_event_start AS (
  SELECT
  	hall_id,
    start_day,
    end_day,
    ifnull(START_DAY>(MAX(end_day) OVER (PARTITION BY hall_id order by start_day, end_day desc rows between unbounded preceding and 1 preceding)), 1) if_start_greater_than_end_previous_max  	
  FROM
  	HallEvents
), event_id AS (
  SELECT
  	if_start_greater_than_end_previous_max,
    SUM(if_start_greater_than_end_previous_max) OVER (PARTITION BY hall_id ORDER BY start_day, end_day desc) AS events_id,
    -- SINCE THE FIRST EVENT IS GONNA BE ALWAYS TRUE; IT'S SAFE TO START OUR CALCULATIONS BY CASTING THE BOOLEAN -> INT62 (ie. 1 for TRUE, 0 for FALSE)
    hall_id,
    start_day,
    end_day
  FROM
  	new_event_start
)select hall_id, min(start_day) as start_day, max(end_day) as end_day from event_id group by hall_id, events_id
