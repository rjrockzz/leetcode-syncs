CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
    select distinct user_id
    from purchases
    where time_stamp >= startDate and time_stamp <= endDate
    and amount >= minAmount
    order by user_id;
END
/*
--Note: Here we need the endDate ending with 00:00:00. Ex: 2022-03-03 00:00:00. 
--For testcases to be successfull.
*/