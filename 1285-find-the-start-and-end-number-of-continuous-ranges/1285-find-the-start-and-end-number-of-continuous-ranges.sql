# “De Mysteriis Dom Sathanas”
with CTE as
     (select log_id,
	         row_number() over(order by log_id) as rownumber
	  from logs)
select min(log_id) as start_id,
       max(log_id) as end_id
from CTE
group by (log_id - rownumber)