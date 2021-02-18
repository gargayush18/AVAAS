CREATE DATABASE AVAAS;
USE AVAAS;
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
contractor_id INT PRIMARY KEY ,
contractor_name VARCHAR(100) NOT NULL,
dob DATE NOT NULL,
current_project_id INT,
competency_score INT,
phone_number INT NOT NULL,
FOREIGN KEY(current_project_id) REFERENCES ongoing_projects(ongoing_projects_id)
);
INSERT INTO contractors VALUES (1,'Boris Singh','1960-01-01',3,90,12456889);
INSERT INTO contractors VALUES (2,'Dheeraj Singh','1950-01-01',5,99,12456854);
INSERT INTO contractors VALUES (3,'Tapan Roy','1989-01-01',1,85,124787889);
INSERT INTO contractors VALUES (4,'Dilip Ghosh','1990-01-01',4,80,242456887);
INSERT INTO contractors VALUES (5,'Rahul Sinha','1970-01-01',2,70,892456582);

CREATE TABLE contractor_competency
(
c_competency_id int primary key,
exp_years int check(exp_years>=0),
no_of_completed_projects int check(no_of_completed_projects>=0),
personal_workforce_available varchar(3) check(personal_workforce_available IN ('YES','NO')),
FOREIGN KEY(c_competency_id) REFERENCES contractors(contractor_id)
);

insert into contractor_competency values(2,5,8,'YES');
insert into contractor_competency values(4,10,15,'NO');



