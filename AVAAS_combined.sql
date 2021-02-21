CREATE DATABASE AVAAS;
USE AVAAS;
CREATE TABLE IF NOT EXISTS Financial_Institutions 
(
  f_institution_id INT PRIMARY KEY ,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Financial_Customers 
(
  f_customer_id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  -- f_institution VARCHAR(45) NOT NULL,
  category VARCHAR(50) NOT NULL CHECK( category IN('government','public','contractor')),
  loans_clear BOOL NOT NULL
);
CREATE TABLE IF NOT EXISTS loans
(
loan_id INT PRIMARY KEY,
borrower VARCHAR(200) NOT NULL,
lender VARCHAR(200) NOT NULL,
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
CREATE TABLE IF NOT EXISTS transactions
(
id_transaction INT PRIMARY KEY,
date_of_transaction DATE NOT NULL,
sender VARCHAR(100) NOT NULL,
receiver VARCHAR(100) NOT NULL,
sender_id INT NOT NULL,
receiver_id INT NOT NULL,
amount DECIMAL(13,2) NOT NULL,
-- new addition
foreign key (f_customer_id) references Financial_Customers(f_customer_id)
);
CREATE TABLE IF NOT EXISTS government
(
govt_id INT PRIMARY KEY,
f_customer_id INT,
employee_name VARCHAR(100) NOT NULL,
location VARCHAR(100),
department VARCHAR(100),
FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id)
);

CREATE TABLE IF NOT EXISTS contractors
(
contractor_id INT PRIMARY KEY ,

contractor_name VARCHAR(500) NOT NULL,
dob DATE NOT NULL,
-- current_project_id INT,
contactdetails VARCHAR(500) NOT NULL,
competency_score INT CHECK(competency_score>=0 AND competency_score<=100),
booked VARCHAR(3) CHECK (booked IN('YES','NO')),

phone_number INT  CHECK(phone_number>999999),
f_customer_id INT ,

-- FOREIGN KEY(current_project_id) REFERENCES ongoing_projects(ongoing_projects_id)
FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id)
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
name varchar(300),
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
construction_material INT NOT NULL,
labour int ,
engineers int,  
FOREIGN KEY (project_supplies_id) REFERENCES ongoing_projects(ongoing_project_id)
);
CREATE TABLE IF NOT EXISTS Completed_Projects 
(
    completed_project_id INT PRIMARY KEY,
    govt_add_id INT NOT NULL,
    p_contractor_id INT NOT NULL,
    name varchar(200),
    location VARCHAR(200) NOT NULL,
    size decimal(13,2) NOT NULL CHECK(size>0.00), 
    price decimal(13,2) NOT NULL CHECK(price>0.00), /*In crores*/
    FOREIGN KEY (govt_add_id) REFERENCES government(govt_id),
    FOREIGN KEY (p_contractor_id) REFERENCES contractors(contractor_id)
);

CREATE TABLE IF NOT EXISTS Public
(
  public_id INT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  house_assigned INT ,
    f_customer_id INT,
  competence_score INT ,
    FOREIGN KEY (house_assigned) REFERENCES Completed_Projects(completed_project_id),
   FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id)
);

create table if not exists public_competence
(
public_id int primary key,
financial_category varchar(100),
no_of_female_members int,
loans_cleared varchar(3) check(loans_cleared in('YES','NO')),
foreign key(public_id) references Public(public_id)
);

CREATE TABLE IF NOT EXISTS houses_in_one_project
(
house_id INT PRIMARY KEY,
project_id INT NOT NULL,
assigned VARCHAR(3) NOT NULL CHECK(assigned IN('YES','NO')),
owner_id INT,
FOREIGN KEY(project_id) REFERENCES Completed_Projects(completed_project_id),
FOREIGN KEY(owner_id) REFERENCES Public(public_id)
);
CREATE TABLE IF NOT EXISTS reviews
(
review_id INT PRIMARY KEY,
public_id INT NOT NULL,
project_id INT NOT NULL,
review_score INT CHECK(review_score>=0 AND review_score<=10),
review_comment VARCHAR(500),
FOREIGN KEY (public_id) REFERENCES Public(public_id),
FOREIGN KEY (project_id) REFERENCES Completed_Projects(completed_project_id)
);
CREATE TABLE IF NOT EXISTS queries
(
query_id INT PRIMARY KEY,
public_id INT NOT NULL,
house_id INT NOT NULL,
actual_query VARCHAR(500),
date_posted DATE NOT NULL,
resolved VARCHAR(3) CHECK(resolved IN ('YES','NO')),
FOREIGN KEY (public_id) REFERENCES Public(public_id),
FOREIGN KEY (house_id) REFERENCES houses_in_one_project(house_id)
);



