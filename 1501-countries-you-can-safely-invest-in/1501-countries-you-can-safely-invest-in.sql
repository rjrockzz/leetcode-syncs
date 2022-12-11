# Write your MySQL query statement below
/*
Person
* id
* name
* phone_number
Phone number will be in the form 'xxx-yyyyyyy' where xxx is the country code (3 characters) and yyyyyyy is the phone number (7 characters) where x and y are digits. Both can contain leading zeros.

Country
* name
* country_code
country_code will be in the form 'xxx' where x is digits.

Calls
* caller_id
* callee_id
* duration
caller_id != callee_id

The company intends to invest in the countries where the average call duration of the calls in this country is strictly greater than the global average call duration.
*/
with  calls_union as
(
select caller_id, callee_id, duration from calls union all
select callee_id, caller_id, duration from calls 
), country_durations as 
(
select n.name, c.duration from calls_union c left join (select p.id, c.name from person p join country c on left(p.phone_number, 3)=c.country_code) n on c.caller_id = n.id
)
 select c.name as country from (select name, avg(duration) average from country_durations c group by 1) c where c.average>(select avg(duration) from country_durations)