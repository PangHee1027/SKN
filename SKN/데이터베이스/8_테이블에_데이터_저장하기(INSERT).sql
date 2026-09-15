USE testdb;

INSERT INTO test_table (col2, col3) VALUES ('데이터입력1', '2025-01-01');
INSERT INTO test_table (col2, col3) VALUES ('데이터입력2', '2025-01-02'), ('데이터입력3', '2025-01-03');

SELECT * FROM test_table;
