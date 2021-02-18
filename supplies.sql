USE AVAAS;
CREATE TABLE supplies
(
ProductID INT PRIMARY KEY,
productname VARCHAR(100) NOT NULL,
quantity INT NOT NULL,
FOREIGN KEY (ongoing_project_id) REFERENCES ongoing_projects(ongoing_project_id)
);

INSERT INTO supplies VALUES(1,'Sariya',12);
INSERT INTO supplies VALUES(2,'Cement',10);
INSERT INTO supplies VALUES(3,'Rodhha-pathhar',100000);

