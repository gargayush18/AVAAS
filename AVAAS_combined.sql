create database AVAAS;
USE AVAAS;
CREATE TABLE IF NOT EXISTS Financial_Institutions 
(
  f_institution_id INT PRIMARY KEY ,
  name VARCHAR(45) NOT NULL,
  location VARCHAR(45) NOT NULL
);
CREATE TABLE IF NOT EXISTS Financial_Customers 
(
  f_customer_id INT PRIMARY KEY,
  name VARCHAR(45) NOT NULL,
  -- f_institution VARCHAR(45) NOT NULL,
  category VARCHAR(50) NOT NULL CHECK( category IN('government','public','contractor')),
  loans_clear BOOL NOT NULL
);
CREATE TABLE IF NOT EXISTS loans
(
loan_id INT PRIMARY KEY,
borrower VARCHAR(100) NOT NULL,
lender VARCHAR(100) NOT NULL,
id_borrower INT NOT NULL,
id_lender INT NOT NULL,
interest_rate DECIMAL(13,2) NOT NULL CHECK(interest_rate<=100.0 AND interest_rate>=0),
date_of_issue DATE NOT NULL,
loan_amount DECIMAL(13,2) NOT NULL CHECK(loan_amount>0.0),
amount_paid_back DECIMAL(13,2) ,
loan_maturity_in_years INT NOT NULL,
FOREIGN KEY(id_borrower) REFERENCES Financial_Customers(f_customer_id),
FOREIGN KEY(id_lender) REFERENCES Financial_Institutions(f_institution_id)
);
-- INSERT INTO loans VALUES(1,'Tapan Roy','SBI',4.8,'2016-12-14',500000.0,200000.0);
-- INSERT INTO loans VALUES(2,'Tapan Roy','City Bank',6.8,'2016-05-14',1000000.0,200000.0);
-- INSERT INTO loans VALUES(3,'Boris Singh','YES Bank',5.8,'2012-05-20',1000000.0,800000.0);
CREATE TABLE IF NOT EXISTS transactions
(
id_transaction INT PRIMARY KEY,
date_of_transaction DATE NOT NULL,
sender VARCHAR(100) NOT NULL,
receiver VARCHAR(100) NOT NULL,
sender_id INT NOT NULL,
receiver_id INT NOT NULL,
amount DECIMAL(13,2) NOT NULL
);
CREATE TABLE IF NOT EXISTS government
(
govt_id INT PRIMARY KEY,
f_customer_id int,
employee_name VARCHAR(100) NOT NULL,
location varchar(100),
department VARCHAR(100),
foreign key (f_customer_id) references Financial_Customers(f_customer_id)
);
CREATE TABLE IF NOT EXISTS contractors
(
contractor_id INT PRIMARY KEY ,
f_customer_id int ,
contractor_name VARCHAR(100) NOT NULL,
dob DATE NOT NULL,
-- current_project_id INT,
booked varchar(3) check (booked in('YES','NO')),
competency_score INT check(competency_score>=0 and competency_score<=100),
phone_number INT NOT NULL check(phone_number>999999),
-- FOREIGN KEY(current_project_id) REFERENCES ongoing_projects(ongoing_projects_id)
foreign key (f_customer_id) references Financial_Customers(f_customer_id)
);

CREATE TABLE IF NOT EXISTS contractor_competency
(
c_competency_id INT PRIMARY KEY,
exp_years INT CHECK(exp_years>=0),
no_of_completed_projects INT CHECK(no_of_completed_projects>=0),
personal_workforce_available VARCHAR(3) CHECK(personal_workforce_available IN ('YES','NO')),
FOREIGN KEY(c_competency_id) REFERENCES contractors(contractor_id)
);
CREATE TABLE IF NOT EXISTS ongoing_projects
(
ongoing_project_id INT PRIMARY KEY,
govt_add_id INT NOT NULL,
location VARCHAR(200) NOT NULL,
size DECIMAL(8,3) NOT NULL,
p_contractor_id INT ,
assigned VARCHAR(3) NOT NULL CHECK (assigned IN('YES','NO')),
completion_percentage DECIMAL(8,2) NOT NULL CHECK(completion_percentage<=100 AND completion_percentage>=0),
FOREIGN KEY (govt_add_id) REFERENCES government(govt_id),
FOREIGN KEY (p_contractor_id) REFERENCES contractors(contractor_id)
);
CREATE TABLE IF NOT EXISTS supplies
(
project_supplies_id INT PRIMARY KEY,
sariya INT NOT NULL,
cement DECIMAL(8,3) NOT NULL,
rodhha_patthar DECIMAL(8,3) NOT NULL,
  
FOREIGN KEY (project_supplies_id) REFERENCES ongoing_projects(ongoing_project_id)
);
CREATE TABLE IF NOT EXISTS Completed_Projects 
(
    completed_project_id INT PRIMARY KEY,
    govt_add_id INT NOT NULL,
    p_contractor_id INT NOT NULL,
    location VARCHAR(200) NOT NULL,
    size FLOAT(2) NOT NULL CHECK(size>0.00), 
    price FLOAT(2) NOT NULL CHECK(price>0.00), /*In crores*/
    FOREIGN KEY (govt_add_id) REFERENCES government(govt_id),
    FOREIGN KEY (p_contractor_id) REFERENCES contractors(contractor_id)
);
CREATE TABLE IF NOT EXISTS Public
(
	public_id INT PRIMARY KEY,
	house_assigned INT ,
    f_customer_id int,
	name VARCHAR(200) NOT NULL,
	competence_score INT ,
    FOREIGN KEY (house_assigned) REFERENCES Completed_Projects(completed_project_id),
   foreign key (f_customer_id) references Financial_Customers(f_customer_id)
);


