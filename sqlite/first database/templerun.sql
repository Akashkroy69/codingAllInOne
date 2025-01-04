-- comment

-- creating table 
create table if not exists templerun(
  serialName int,
  playerName varchar(255),
  score int
);
-- inserting data
insert into templerun(serialName,playerName,score) values(1,'Bello Halle',100);

insert into templerun(serialName,playerName,score) values(2,'Deborah',200);

insert into templerun(serialName,playerName,score) values(3,'Akash',300);

-- displaying data from table
select * from templerun;

