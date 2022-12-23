# Write your MySQL query statement below
/*
Elements
* symbol
* type
* electrons


Two elements can form a bond if one of them is 'Metal' 
and the other is 'Nonmetal'.
*/
select m.symbol as metal, n.symbol as nonmetal from elements m, elements n where m.type = "Metal" and n.type = "Nonmetal"