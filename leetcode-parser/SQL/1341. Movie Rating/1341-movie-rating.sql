# Write your MySQL query statement below
/*
Movies
* movie_id
* title
movie_id is the primary key for this table.

Users
* user_id
* name
user_id is the primary key for this table.

MovieRating
* movie_id
* user_id
* rating
* created_at
(movie_id, user_id) is the primary key for this table.

Write an SQL query to:

Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

*/
# Write your MySQL query statement below
SELECT user_name as results FROM
(
    SELECT b.name as user_name,COUNT(*) as counts FROM Movierating as a
    JOIN Users as b
    ON a.user_id=b.user_id
    GROUP BY a.user_id
    ORDER BY counts DESC,user_name ASC LIMIT 1
) first_query #query for the person who rates the greatest number of movies
UNION
SELECT movie_name as results FROM
(
    SELECT d.title as movie_name,AVG(c.rating) as grade FROM Movierating as c
    JOIN Movies as d
    ON c.movie_id=d.movie_id
    WHERE SUBSTR(c.created_at,1,7)="2020-02"
    GROUP BY c.movie_id
    ORDER BY grade DESC,movie_name ASC LIMIT 1
) second_query; #query for the movie with the highest average rating in February