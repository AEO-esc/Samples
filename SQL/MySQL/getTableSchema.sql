SELECT DISTINCT TABLE_NAME 
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME IN ('column_name')
	AND TABLE_SCHEMA='you_table';