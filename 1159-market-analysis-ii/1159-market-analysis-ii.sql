# Write your MySQL query statement below
select user_id as seller_id, 
        (case 
            when favorite_brand = (
                            select i.item_brand
                            from Orders o left join Items i
                            on o.item_id = i.item_id
                            where o.seller_id = u.user_id 
                            order by o.order_date
                            limit 1 offset 1
                                  ) then "yes" else "no" end
         ) as "2nd_item_fav_brand"   
from Users u   