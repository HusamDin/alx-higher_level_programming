-- List all records of the table second_table
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != NULL
ORDER BY `score` DESC;
