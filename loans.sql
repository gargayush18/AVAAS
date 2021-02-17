USE AVAAS;
create table loans
(
loan_id int primary key auto_increment,
borrower varchar(100) not null,
lender varchar(100) not null,
interest_rate decimal(13,2) not null check(interest_rate<=100.0),
date_of_issue date not null,
loan_amount decimal(13,2) not null check(loan_amount>0.0),
amount_paid_back decimal(13,2) check(amount_paid_back<=loan_amount)
);
