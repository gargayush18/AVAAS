CREATE DATABASE IF NOT EXISTS AVAAS2;
USE AVAAS2;
CREATE TABLE IF NOT EXISTS Financial_Customers 
(
  f_customer_id VARCHAR(100) PRIMARY KEY,
  name VARCHAR(500) NOT NULL,
  category VARCHAR(50) NOT NULL CHECK( category IN('govt','public','contractor','bank')),
  loans_clear BOOL NOT NULL,
  credibility_score INT CHECK(credibility_score>=-2 AND credibility_score<=100)
);
CREATE TABLE IF NOT EXISTS Banks 
(
  f_institution_id VARCHAR(100) PRIMARY KEY ,
  f_customer_id VARCHAR(100),
  name VARCHAR(100) NOT NULL,
  location VARCHAR(100) NOT NULL,
  FOREIGN KEY(f_customer_id) REFERENCES Financial_Customers(f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE

);
CREATE TABLE IF NOT EXISTS loans_offered 
(
  loan_offer_id varchar(100) PRIMARY KEY,
  f_institution_id VARCHAR(100)  ,
  ROI DECIMAL(13,2) CHECK(ROI>=0.0 AND ROI<=100.0),
  max_loan_amount DECIMAL(13,2) CHECK(max_loan_amount>=0.0 ),
  max_duration DECIMAL(13,2) CHECK(max_duration >=0.0 ),
  no_of_installments INT CHECK(no_of_installments>0),
  loan_type VARCHAR(100) check(loan_type in ('public','contractor')),
  foreign key (f_institution_id) references Banks(f_institution_id) ON DELETE CASCADE ON UPDATE CASCADE
);




CREATE TABLE IF NOT EXISTS Loans
(
loan_id VARCHAR(100) NOT NULL,
borrower varchar(200) NOT NULL, 
lender varchar(200) NOT NULL, 

id_borrower VARCHAR(100) NOT NULL,
id_lender VARCHAR(100) NOT NULL,
interest_rate DECIMAL(13,2) NOT NULL CHECK(interest_rate<=100.0 AND interest_rate>=0),
date_of_issue DATE NOT NULL,
loan_amount DECIMAL(13,2) NOT NULL CHECK(loan_amount>0.0),
amount_paid_back DECIMAL(13,2) ,
loan_maturity_in_years INT NOT NULL,
FOREIGN KEY(id_borrower) REFERENCES Financial_Customers(f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(id_lender) REFERENCES Banks(f_institution_id) ON DELETE CASCADE ON UPDATE CASCADE,

-- Added : A composite primary key 
-- (i, xx, yy) represents the ith loan between
-- the borrower with id xx and receiver with id yy

PRIMARY KEY(loan_id, id_borrower, id_lender)

);

CREATE TABLE IF NOT EXISTS Transactions
(
id_transaction varchar(50) NOT NULL,
date_of_transaction DATE NOT NULL,


sender_id VARCHAR(100) NOT NULL,
receiver_id VARCHAR(100) NOT NULL,
amount DECIMAL(13,2) NOT NULL CHECK(amount>=0.0),
transaction_type varchar(100) not null check(transaction_type in('loan_payment','general')),
FOREIGN KEY(sender_id) REFERENCES Financial_Customers(f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(receiver_id) REFERENCES Financial_Customers(f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE,

-- Added : A composite primary key 
-- (i, xx, yy) represents the ith transcation between
-- the borrower with id xx and receiver with id yy

PRIMARY KEY(id_transaction, sender_id, receiver_id)

);
CREATE TABLE IF NOT EXISTS Government
(
govt_id VARCHAR(100) PRIMARY KEY,
f_customer_id VARCHAR(100),
govt_name VARCHAR(100) NOT NULL,
-- location VARCHAR(100),
-- department VARCHAR(100),
FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS Contractors
(
contractor_id varchar(100) PRIMARY KEY ,
contractor_name VARCHAR(500) NOT NULL,
dob DATE NOT NULL,
contactdetails VARCHAR(500) NOT NULL,
competency_score INT CHECK(competency_score>=0 AND competency_score<=100),
booked VARCHAR(3) CHECK (booked IN('YES','NO')),
phone_number bigint  CHECK(phone_number>999999),
f_customer_id varchar(100) ,
FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS contractor_competency
(
c_competency_id varchar(100) PRIMARY KEY,
exp_years INT CHECK(exp_years>=0),
no_of_completed_projects INT CHECK(no_of_completed_projects>=0),
personal_workforce_available VARCHAR(3) CHECK(personal_workforce_available IN ('YES','NO')),
FOREIGN KEY(c_competency_id) REFERENCES Contractors(contractor_id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS ongoing_projects
(
ongoing_project_id varchar(100) PRIMARY KEY,

p_contractor_id varchar(100) ,
govt_add_id varchar(100) NOT NULL,
name varchar(300),
location VARCHAR(200) NOT NULL,
size DECIMAL(8,3) NOT NULL,
assigned VARCHAR(3) NOT NULL CHECK (assigned IN('YES','NO')),
completion_percentage DECIMAL(8,2) NOT NULL CHECK(completion_percentage<=100 AND completion_percentage>=0),
FOREIGN KEY (govt_add_id) REFERENCES Government(govt_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (p_contractor_id) REFERENCES Contractors(contractor_id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS supplies
(
project_supplies_id varchar(100) PRIMARY KEY,
construction_material INT NOT NULL,
labour int ,
engineers int,  
FOREIGN KEY (project_supplies_id) REFERENCES ongoing_projects(ongoing_project_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS project_requirements
(
project_req_id varchar(100) PRIMARY KEY,
min_exp INT NOT NULL,
preworkforce_needed  varchar(3) check(preworkforce_needed in('YES','NO')), 
min_cost_handled int, 
no_of_projects int , 


FOREIGN KEY (project_req_id) REFERENCES ongoing_projects(ongoing_project_id) ON DELETE CASCADE ON UPDATE CASCADE
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
    FOREIGN KEY (govt_add_id) REFERENCES Government(govt_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (p_contractor_id) REFERENCES Contractors(contractor_id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS Public
(
  public_id varchar(100) PRIMARY KEY,
  f_customer_id varchar(100),
  name VARCHAR(200) NOT NULL,
  location varchar(100) NOT NULL,
   
   competence_score INT ,
   FOREIGN KEY (f_customer_id) REFERENCES Financial_Customers(f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);
create table if not exists public_competence
(
public_id varchar(100) primary key,
financial_category varchar(100),
no_of_female_members int,
loans_cleared varchar(3) check(loans_cleared in('YES','NO')),
foreign key(public_id) references Public(public_id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS houses_in_one_project
(
house_id varchar(100) NOT NULL,
project_id varchar(100) NOT NULL,
assigned VARCHAR(3) NOT NULL CHECK(assigned IN('YES','NO')),
owner_id varchar(100),
FOREIGN KEY(project_id) REFERENCES Completed_Projects(completed_project_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(owner_id) REFERENCES Public(public_id) ON DELETE CASCADE ON UPDATE CASCADE,

-- Added : A composite primary key 
-- (i, xx) represents the ith house of project with id xx

-- Eg. (1,10001) represents the 1st house of proj 10001
-- (1, 10002) represents the 1st house of proj 10002


PRIMARY KEY(house_id, project_id)


);
CREATE TABLE IF NOT EXISTS reviews
(
review_id varchar(100) NOT NULL,
public_id varchar(100) NOT NULL,
project_id varchar(100) NOT NULL,
review_score INT CHECK(review_score>=0 AND review_score<=10),
review_comment VARCHAR(500),
FOREIGN KEY (public_id) REFERENCES Public(public_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (project_id) REFERENCES Completed_Projects(completed_project_id) ON DELETE CASCADE ON UPDATE CASCADE,

-- Added : A composite primary key 
-- (i, xx) represents the ith review of project with id xx

PRIMARY KEY(review_id, project_id)
);
CREATE TABLE IF NOT EXISTS queries
(
query_id varchar(100) NOT NULL,
project_id varchar(100) NOT NULL,



public_id varchar(100) NOT NULL,


actual_query VARCHAR(500),
date_posted DATE NOT NULL,
resolved VARCHAR(3) CHECK(resolved IN ('YES','NO')),
FOREIGN KEY (public_id) REFERENCES Public(public_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (project_id) REFERENCES Completed_Projects(completed_project_id) ON DELETE CASCADE ON UPDATE CASCADE,


-- Added : A composite primary key 
-- (i, xx) represents the ith query of project with id xx

PRIMARY KEY(query_id, project_id)
);
CREATE TABLE IF NOT EXISTS house_applicants
(
public_id varchar(100) NOT NULL,
completed_project_id varchar(100) NOT NULL,
application_status VARCHAR(50) CHECK(application_status IN ('Alloted','Not alloted', 'Under review')),
application_time date not null,
FOREIGN KEY (public_id) REFERENCES Public(public_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (completed_project_id) REFERENCES Completed_Projects(completed_project_id) ON DELETE CASCADE ON UPDATE CASCADE,
primary key(public_id,completed_project_id)
);
CREATE TABLE IF NOT EXISTS project_applicants
(
p_contractor_id varchar(100) NOT NULL,
ongoing_project_id varchar(100) NOT NULL,
application_status VARCHAR(50) CHECK(application_status IN ('Assigned','Not assigned', 'Under review')),
application_time datetime not null,
bid_value decimal(13,2) not null check(bid_value>=0),
FOREIGN KEY (p_contractor_id) REFERENCES Contractors(contractor_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (ongoing_project_id) REFERENCES ongoing_projects(ongoing_project_id) ON DELETE CASCADE ON UPDATE CASCADE,
primary key(p_contractor_id, ongoing_project_id)
);
CREATE TABLE IF NOT EXISTS loan_applicants (
    loan_id VARCHAR(100) NOT NULL,
    f_customer_id VARCHAR(100) NOT NULL,
    application_status VARCHAR(50) CHECK (application_status IN ('Sanctioned' , 'Not sanctioned', 'Under review')),
    application_time DATETIME NOT NULL,
    FOREIGN KEY (f_customer_id)
        REFERENCES Financial_Customers (f_customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (loan_id)
        REFERENCES loans_offered (loan_offer_id) ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (loan_id , f_customer_id)
);
CREATE TABLE IF NOT EXISTS login_details
(
user_id varchar(100) primary key,
user_password varchar(100) not null
);
