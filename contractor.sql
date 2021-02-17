CREATE DATABASE sample;
USE sample;
CREATE TABLE ongoing_projects
(
ongoing_projects_id INT PRIMARY KEY AUTO_INCREMENT
);
-- inserting dummy ongoing projects
INSERT INTO ongoing_projects VALUES ();
INSERT INTO ongoing_projects VALUES ();
INSERT INTO ongoing_projects VALUES ();
INSERT INTO ongoing_projects VALUES ();
INSERT INTO ongoing_projects VALUES ();
CREATE TABLE contractors
(
contractor_id INT PRIMARY KEY AUTO_INCREMENT,
contractor_name VARCHAR(100) NOT NULL,
dob DATE NOT NULL,
current_project_id INT,
competency_score INT,
phone_number INT NOT NULL,
FOREIGN KEY(current_project_id) REFERENCES ongoing_projects(ongoing_projects_id)
);
INSERT INTO contractors(contractor_name,dob,current_project_id,competency_score,phone_number) 
VALUES ('Boris Singh','1960-01-01',3,90,12456889);
INSERT INTO contractors(contractor_name,dob,current_project_id,competency_score,phone_number)
VALUES ('Dheeraj Singh','1950-01-01',5,99,12456854);
INSERT INTO contractors(contractor_name,dob,current_project_id,competency_score,phone_number)
VALUES ('Tapan Roy','1989-01-01',1,85,124787889);
INSERT INTO contractors(contractor_name,dob,current_project_id,competency_score,phone_number)
VALUES ('Dilip Ghosh','1990-01-01',4,80,242456887);
INSERT INTO contractors(contractor_name,dob,current_project_id,competency_score,phone_number)
VALUES ('Rahul Sinha','1970-01-01',2,70,892456582);



