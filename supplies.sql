USE AVAAS;
CREATE TABLE supplies
(
project_supplies_id INT PRIMARY KEY,
sariya INT NOT NULL,
cement DECIMAL(8,3) NOT NULL,
rodhha_patthar DECIMAL(8,3) NOT NULL,
  
FOREIGN KEY (project_supplies_id) REFERENCES ongoing_projects(ongoing_project_id)
);

INSERT INTO supplies VALUES(1, 1000, 500.40, 2000.5);
INSERT INTO supplies VALUES(2, 2000, 680.69, 1234.5);
INSERT INTO supplies VALUES(3, 1549, 420.42, 78989.6);

