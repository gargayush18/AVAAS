CREATE DATABASE sample;
USE sample;
CREATE TABLE ongoing_projects
(
ongoing_projects_id INT PRIMARY KEY AUTO_INCREMENT
);
INSERT INTO ongoing_projects VALUES ();
CREATE TABLE contractors
(
contractor_id INT PRIMARY KEY AUTO_INCREMENT,
contractor_name VARCHAR(100) NOT NULL,
dob DATE NOT NULL,
current_project_id INT,
competency_score INT,
phone_number INT NOT NULL,
email VARCHAR(40),
FOREIGN KEY(current_project_id) REFERENCES ongoing_projects(ongoing_projects_id)
);
INSERT INTO contractors(contractor_name,dob,current_project_id,phone_number,email) 
VALUES ('Contractor 1','2001-01-01',1,12456889,'abc@xyz.com');
INSERT INTO contractors(contractor_name,dob,current_project_id,phone_number,email) 
VALUES ('Contractor 2','2001-01-01',4,12456889,'abc@xyz.com');

