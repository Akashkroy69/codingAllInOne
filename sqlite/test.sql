create table if not exists users(
  id integer primary key autoincrement,
  name varchar(20) not null,
  email varchar(20) not null,
  age integer not null
);

-- insert 10 users
insert into users(name, email, age) values('Jack', 'oqibz@example.com', 20), ('Rose', 'rdlnk@example.com', 22), ('Tom', 'plsgq@example.com', 25), ('Jane', 'qpmzj@example.com', 30), ('Mike', 'rdlnk@example.com', 35), ('Lily', 'qpmzj@example.com', 40), ('Jim', 'xcvkp@example.com', 45), ('Jenny', 'qpmzj@example.com', 50), ('Jacky', 'xcvkp@example.com', 55), ('Jason', 'rdlnk@example.com', 60);

select * from users;
-- select users older than 30
select '--------older than 30---------';
select * from users where age > 30;
-- select users older than 30 and name start with J
select '--------older than 30 and name start with J---------';
select * from users where age > 30 and name like 'J%';
-- select users older than 30 and name start with J or name start with M
select '--------older than 30 and name start with J or name start with M---------';
select * from users where age > 30 and name like 'J%' or name like 'M%';
-- select users older than 30 and name start with J or name start with M and name end with n
select '--------older than 30 and name start with J or name start with M and name end with n---------';
select * from users where age > 30 and name like 'J%' or name like 'M%' and name like '%n';