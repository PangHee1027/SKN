USE testdb;

CREATE TABLE emp_tree (
	emp_name VARCHAR(10),
    mgr_name VARCHAR(10)
);
INSERT INTO emp_tree VALUES ('김사원', '박대리'), ('박대리', '최부장');

SELECT A.emp_name AS 사원, A.mgr_name AS 직속상사, B.mgr_name AS 상사의상사
FROM emp_tree A
INNER JOIN emp_tree B ON A.mgr_name = B.emp_name;