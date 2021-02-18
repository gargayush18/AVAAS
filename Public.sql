
USE AVAAS;
create table Public(
ID int not null,
houseAssinged varchar(200) not null,
AadharNo int not null unique,
Name varchar(200) not null,
CompetenceScore int not null,
Constraint CompetenceScore check(CompetenceScore between 50 and 100),
TransactionalID int not null unique,
Queries int not null,
Reviews int not null,
Constraint Reviews check(Reviews between 1 and 5),
primary key(ID)
);

Insert into Public values(1, "1A", 12345678, "Hari Prakash", 55, 12, 4, 5);
Insert into Public values(2, "2A", 23456789, "Ram Prakash", 62, 3, 7, 2);
Insert into Public values(3, "3A", 12341234, "Om Prakash", 75, 11, 5, 4);
 

