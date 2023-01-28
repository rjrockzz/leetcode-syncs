# Write your MySQL query statement below
# This is the same question that AB solved in his videos:)))

with cte AS (
    SELECT
        *,
        SUM(IF(drink IS NOT NULL, 1, 0)) over win AS grp
    FROM
        CoffeeShop 
    WINDOW win AS (
        ROWS BETWEEN UNBOUNDED preceding
        AND CURRENT ROW
        )
)
SELECT
    id,
    first_value(drink) over(PARTITION by grp order by grp) AS drink
FROM
    cte;