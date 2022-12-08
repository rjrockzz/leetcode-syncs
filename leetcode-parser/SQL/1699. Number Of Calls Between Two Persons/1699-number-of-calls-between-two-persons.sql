# Write your MySQL query statement below
/* 
Calls table
* from_id - user who did the call
* to_id - user to whome the call was made
* duration - total time of the call
\U0001f4de 
*/
/* the catch here is that from and to can be interchanged and we need to take the number of calls as the call_counts*/

# Write your MySQL query statement below
SELECT LEAST(from_id,to_id) as person1,
GREATEST(from_id,to_id) as person2,
COUNT(*) as call_count,
SUM(duration) as total_duration
FROM Calls
GROUP BY person1,person2;