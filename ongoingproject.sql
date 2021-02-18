USE AVAAS; 
CREATE TABLE ongoing_projects
(
ongoing_project_id INT PRIMARY KEY,
location VARCHAR(200) NOT NULL,
size DECIMAL(8,3) NOT NULL,
contractor_id INT NOT NULL,
completion_percentage DECIMAL(8,2) NOT NULL CHECK(completion_percentage<=100 AND completion_percentage>=0)
/*transactions   
supplies*/ 
);

INSERT INTO ongoing_projects VALUES(1,'110045 Dwarka Sector 1a',10.2,3,12.5);
INSERT INTO ongoing_projects VALUES(2,'110022 Okhla Opposite GGSIPU ',5.2,2,10.78);
INSERT INTO ongoing_projects VALUES(3,'110044 Dwarka Sector 5',20.3,4,54.90);
INSERT INTO ongoing_projects VALUES(4,'110040 Dwarka Sector 8',8.6,1,96.3);

