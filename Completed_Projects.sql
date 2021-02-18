use AVAAS;
create table Completed_Projects (
    ID int not null,
    location varchar(200) not null,
    size float(2) not null check(size>0.00), 
    price float(2) not null check(price>0.00), /*In crores*/
    primary key(ID)
);
insert into Completed_Projects values(1,'110060 Old Rajinder Nagar',11.23, 1.20);
insert into Completed_Projects values(2,'110008 West Patel Nagar',12.21, 2.10);
insert into Completed_Projects values(3,'110031 Shastri Nagar',15.12, 2.80);
insert into Completed_Projects values(4,'110015 West Ramesh Nagar',14.21, 2.60);
