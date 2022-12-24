select ROUND(SQRT(min((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y))),2) as shortest
from point2d p1,point2d p2
where p1.x <> p2.x or p1.y <> p2.y;