CREATE DATABASE IF NOT EXISTS AVAAS2;
USE AVAAS2;
CREATE TABLE IF NOT EXISTS Banks 
(
  f_institution_id VARCHAR(100) PRIMARY KEY ,
  name VARCHAR(100) NOT NULL,
  location VARCHAR(100) NOT NULL,
  ROI DECIMAL(13,2) CHECK(ROI>=0.0 AND ROI<=100.0),
  max_loan_amount DECIMAL(13,2) CHECK(max_loan_amount>=0.0 ),
  max_duration DECIMAL(13,2) CHECK(max_duration >=0.0 ),
  no_of_installments INT CHECK(no_of_installments>0)
);

CREATE TABLE IF NOT EXISTS Financial_Customers 
(
  f_customer_id VARCHAR(100) PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  category VARCHAR(50) NOT NULL CHECK( category IN('government','public','contractor','bank')),
  loans_clear BOOL NOT NULL,
  credibility_score INT CHECK(credibility_score>=0 AND credibility_score<=100)
);

CREATE TABLE IF NOT EXISTS Loans
(
loan_id VARCHAR(100) PRIMARY KEY,
borrower VARCHAR(200) NOT NULL,
lender VARCHAR(200) NOT NULL,
id_borrower VARCHAR(100) NOT NULL,
id_lender VARCHAR(100) NOT NULL,
interest_rate DECIMAL(13,2) NOT NULL CHECK(interest_rate<=100.0 AND interest_rate>=0),
date_of_issue DATE NOT NULL,
loan_amount DECIMAL(13,2) NOT NULL CHECK(loan_amount>0.0),
amount_paid_back DECIMAL(13,2) ,
loan_maturity_in_years INT NOT NULL,
FOREIGN KEY(id_borrower) REFERENCES Financial_Customers(f_customer_id),
FOREIGN KEY(id_lender) REFERENCES Banks(f_institution_id)
);
CREATE TABLE IF NOT EXISTS Transactions
(
id_transaction INT PRIMARY KEY,
date_of_transaction DATE NOT NULL,
sender VARCHAR(100) NOT NULL,
receiver VARCHAR(100) NOT NULL,
sender_id VARCHAR(100) NOT NULL,
receiver_id VARCHAR(100) NOT NULL,
amount DECIMAL(13,2) NOT NULL CHECK(amount>=0.0),
transaction_type varchar(100) not null check(transaction_type in('loan_payment','general')),
FOREIGN KEY(sender_id) REFERENCES Financial_Customers(f_customer_id),
FOREIGN KEY(receiver_id) REFERENCES Financial_Customers(f_customer_id)
);
CREATE TABLE IF NOT EXISTS Government
(
govt_id VARCHAR(100) PRIMARY KEY,
f_customer_id VARCHAR(100),
govt_name VARCHAR(100) NOT NULL,
-- location VARCHAR(100),
-- department VARCHAR(100),
FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id)
);
CREATE TABLE IF NOT EXISTS Contractors
(
contractor_id varchar(100) PRIMARY KEY ,
contractor_name VARCHAR(500) NOT NULL,
dob DATE NOT NULL,
contactdetails VARCHAR(500) NOT NULL,
competency_score INT CHECK(competency_score>=0 AND competency_score<=100),
booked VARCHAR(3) CHECK (booked IN('YES','NO')),
phone_number INT  CHECK(phone_number>999999),
f_customer_id varchar(100) ,
FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id)
);
CREATE TABLE IF NOT EXISTS contractor_competency
(
c_competency_id varchar(100) PRIMARY KEY,
exp_years INT CHECK(exp_years>=0),
no_of_completed_projects INT CHECK(no_of_completed_projects>=0),
personal_workforce_available VARCHAR(3) CHECK(personal_workforce_available IN ('YES','NO')),
FOREIGN KEY(c_competency_id) REFERENCES Contractors(contractor_id)
);
CREATE TABLE IF NOT EXISTS ongoing_projects
(
ongoing_project_id varchar(100) PRIMARY KEY,
govt_add_id varchar(100) NOT NULL,
name varchar(300),
location VARCHAR(200) NOT NULL,
size DECIMAL(8,3) NOT NULL,
p_contractor_id varchar(100) ,
assigned VARCHAR(3) NOT NULL CHECK (assigned IN('YES','NO')),
completion_percentage DECIMAL(8,2) NOT NULL CHECK(completion_percentage<=100 AND completion_percentage>=0),
FOREIGN KEY (govt_add_id) REFERENCES Government(govt_id),
FOREIGN KEY (p_contractor_id) REFERENCES Contractors(contractor_id)
);
CREATE TABLE IF NOT EXISTS supplies
(
project_supplies_id varchar(100) PRIMARY KEY,
construction_material INT NOT NULL,
labour int ,
engineers int,  
FOREIGN KEY (project_supplies_id) REFERENCES ongoing_projects(ongoing_project_id)
);
CREATE TABLE IF NOT EXISTS Completed_Projects 
(
    completed_project_id varchar(100) PRIMARY KEY,
    govt_add_id varchar(100) NOT NULL,
    p_contractor_id varchar(100) NOT NULL,
    name varchar(200),
    date_of_completion DATE NOT NULL,
    location VARCHAR(200) NOT NULL,
    size decimal(13,2) NOT NULL CHECK(size>0.00), 
    price decimal(13,2) NOT NULL CHECK(price>0.00), /*In crores*/
    FOREIGN KEY (govt_add_id) REFERENCES Government(govt_id),
    FOREIGN KEY (p_contractor_id) REFERENCES Contractors(contractor_id)
);
CREATE TABLE IF NOT EXISTS Public
(
  public_id varchar(100) PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
   f_customer_id varchar(100),
   competence_score INT ,
   FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id)
);
create table if not exists public_competence
(
public_id varchar(100) primary key,
financial_category varchar(100),
no_of_female_members int,
loans_cleared varchar(3) check(loans_cleared in('YES','NO')),
foreign key(public_id) references Public(public_id)
);
CREATE TABLE IF NOT EXISTS houses_in_one_project
(
house_id varchar(100) PRIMARY KEY,
project_id varchar(100) NOT NULL,
assigned VARCHAR(3) NOT NULL CHECK(assigned IN('YES','NO')),
owner_id varchar(100),
FOREIGN KEY(project_id) REFERENCES Completed_Projects(completed_project_id),
FOREIGN KEY(owner_id) REFERENCES Public(public_id)
);
CREATE TABLE IF NOT EXISTS reviews
(
review_id varchar(100) PRIMARY KEY,
public_id varchar(100) NOT NULL,
project_id varchar(100) NOT NULL,
review_score INT CHECK(review_score>=0 AND review_score<=10),
review_comment VARCHAR(500),
FOREIGN KEY (public_id) REFERENCES Public(public_id),
FOREIGN KEY (project_id) REFERENCES Completed_Projects(completed_project_id)
);
CREATE TABLE IF NOT EXISTS queries
(
query_id varchar(100) PRIMARY KEY,
public_id varchar(100) NOT NULL,
house_id varchar(100) NOT NULL,
actual_query VARCHAR(500),
date_posted DATE NOT NULL,
resolved VARCHAR(3) CHECK(resolved IN ('YES','NO')),
FOREIGN KEY (public_id) REFERENCES Public(public_id),
FOREIGN KEY (house_id) REFERENCES houses_in_one_project(house_id)
);
CREATE TABLE IF NOT EXISTS house_applicants
(
public_id varchar(100) NOT NULL,
completed_project_id varchar(100) NOT NULL,
application_status VARCHAR(50) CHECK(application_status IN ('Alloted','Not alloted', 'Under review')),
application_time datetime not null,
FOREIGN KEY (public_id) REFERENCES Public(public_id),
FOREIGN KEY (completed_project_id) REFERENCES Completed_Projects(completed_project_id),
primary key(public_id,completed_project_id)
);
CREATE TABLE IF NOT EXISTS project_applicants
(
p_contractor_id varchar(100) NOT NULL,
ongoing_project_id varchar(100) NOT NULL,
application_status VARCHAR(50) CHECK(application_status IN ('Assigned','Not assigned', 'Under review')),
application_time datetime not null,
FOREIGN KEY (p_contractor_id) REFERENCES Contractors(contractor_id),
FOREIGN KEY (ongoing_project_id) REFERENCES ongoing_projects(ongoing_project_id),
primary key(p_contractor_id, ongoing_project_id)
);
CREATE TABLE IF NOT EXISTS loan_applicants
(
f_customer_id varchar(100) NOT NULL,
bank_id varchar(100) NOT NULL,
application_status VARCHAR(50) CHECK(application_status IN ('Sanctioned','Not sanctioned', 'Under review')),
application_time datetime not null,
FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id),
FOREIGN KEY(bank_id) REFERENCES Banks(f_institution_id),
primary key(f_customer_id, bank_id)
);
CREATE TABLE IF NOT EXISTS login_details
(
user_id varchar(100) primary key,
user_password varchar(100) not null
);


