USE AVAAS;
CREATE TABLE loans
(
loan_id INT PRIMARY KEY,
borrower VARCHAR(100) NOT NULL,
lender VARCHAR(100) NOT NULL,
interest_rate DECIMAL(13,2) NOT NULL CHECK(interest_rate<=100.0 AND interest_rate>=0),
date_of_issue DATE NOT NULL,
loan_amount DECIMAL(13,2) NOT NULL CHECK(loan_amount>0.0),
amount_paid_back DECIMAL(13,2) 
);
INSERT INTO loans VALUES(1,'Tapan Roy','SBI',4.8,'2016-12-14',500000.0,200000.0);
INSERT INTO loans VALUES(2,'Tapan Roy','City Bank',6.8,'2016-05-14',1000000.0,200000.0);
INSERT INTO loans VALUES(3,'Boris Singh','YES Bank',5.8,'2012-05-20',1000000.0,800000.0);
