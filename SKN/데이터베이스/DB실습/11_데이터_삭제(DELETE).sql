USE testdb;

DELETE FROM test_table WHERE col1 = 2;
SELECT * FROM test_table;

DELETE FROM test_table;
SELECT * FROM test_table;