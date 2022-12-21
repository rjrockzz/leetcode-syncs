# Write your MySQL query statement below
# Write your MySQL query statement below
/**

    THREE Table: Members/Visits/Purchases

member_id is the primary key column for Members table.
Members table indicates the name and the ID of a member.

visit_id is the primary key column for Visits table.
Visits table contains information about the date of a visit to the store and the member who visited it.

visit_id is the primary key column for Purchases table.
visit_id is a foreign key to visit_id from the Visits table.
Purchases table contains information about the amount charged in a visit to the store.


PROBLEM:

A store wants to categorize its members. There are three tiers:
    "Diamond": if the conversion rate is greater than or equal to 80.
    "Gold": if the conversion rate is greater than or equal to 50 and less than 80.
    "Silver": if the conversion rate is less than 50.
    "Bronze": if the member never visited the store.
    
The conversion rate of a member is (100 * total number of purchases for the member) / total number of visits for the member.

Report the id, the name, and the category of each member

STEPS:

    conversion rate = COUNT(Purchases.visit_id)/COUNT(Visits.visit_id)*100
    CASE Statement 
    
*/


SELECT
    M.member_id,
    M.name,
    
    CASE WHEN COUNT(V.visit_id) = 0 THEN 'Bronze'
    WHEN (COUNT(P.visit_id)/COUNT(V.visit_id))*100 >= 80 THEN 'Diamond'
    WHEN (COUNT(P.visit_id)/COUNT(V.visit_id))*100 >= 50 AND (COUNT(P.visit_id)/COUNT(V.visit_id))*100 < 80 THEN 'Gold' 
    WHEN (COUNT(P.visit_id)/COUNT(V.visit_id))*100  < 50 THEN 'Silver'
    END AS category
    
FROM Members M

    LEFT JOIN Visits V
        ON M.member_id = V.member_id
    LEFT JOIN Purchases P
        ON V.visit_id = P.visit_id
GROUP BY 1