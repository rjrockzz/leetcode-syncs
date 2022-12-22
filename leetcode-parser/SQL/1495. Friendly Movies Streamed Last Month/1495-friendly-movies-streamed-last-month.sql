# Write your MySQL query statement below
/*
TVProgram
* program_date
* content_id
* channel

Content
* content_id
* title
* kids_content
* content_type

2020-06
*/
select distinct c.title from content c join tvprogram tv using(content_id) where c.kids_content = "Y" and left(tv.program_date,7)="2020-06" and content_type = "Movies"