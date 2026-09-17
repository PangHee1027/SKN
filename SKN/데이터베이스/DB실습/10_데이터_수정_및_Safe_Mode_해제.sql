USE testdb;

UPDATE test_table SET col2 = '데이터 수정' WHERE col1 = 3;

SELECT * FROM test_table;

# SET sql_safe_updates = 0;
# UPDATE test_table SET col2 = '전체 데이터 수정';

# SELECT * FROM test_table;
