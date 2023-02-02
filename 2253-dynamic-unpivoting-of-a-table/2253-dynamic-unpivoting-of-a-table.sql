/*
Products
* Column Name
* Type
Each row in this table indicates the product's price in n different stores.
If the product is not available in a store, the price will be null in that store's column.
The names of the stores may change from one testcase to another. There will be at least 1 store and at most 30 stores.
*/
CREATE PROCEDURE UnpivotProducts()
BEGIN
	set session group_concat_max_len = 198742918;
    set @variable = null;
	select group_concat(
        concat(
            'select product_id, "',`column_name`, '" as store, ', `column_name`, ' as price from products where ',`column_name`, ' is not null') separator ' union '
        )
        into @variable
        from `information_schema`.`columns`
        where `table_schema` = 'test' and `table_name` = 'products' and `column_name` != 'product_id';
        prepare sql_query from @variable;
        execute sql_query;
        deallocate prepare sql_query;
END