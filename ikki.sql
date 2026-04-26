create database course_platform;
create table course_platform(course_id int,
title varchar(200),instructor varchar(100),duraation_hr decimal,
price decimal,rating decimal,enrolled int);

INSERT INTO course_platform VALUES
(1,'Python Basics', 'Ali Karimov', 10.5, 150000, 4.5, 120),
(2,'SQL Mastery', 'Vali Xasanov', 8.0, 120000, 4.7, 95),
(3,'Web Development', 'Sardor Bek', 15.0, 200000, 4.6, 150),
(4,'Cybersecurity Intro', 'Akbar T.', 12.0, 180000, 4.8, 110),
(5,'Java Programming', 'Dilshod R.', 14.5, 170000, 4.4, 80),
(6,'C Programming', 'Jamshid K.', 9.0, 100000, 4.3, 60),
(7,'Data Science', 'Aziza M.', 20.0, 250000, 4.9, 200),
(8,'Machine Learning', 'Bekzod S.', 18.5, 300000, 4.7, 170),
(9,'HTML & CSS', 'Nodir P.', 6.0, 90000, 4.2, 140),
(10,'Networking Basics', 'Sherzod U.', 11.0, 130000, 4.5, 75);

UPDATE course_platform set price=0 where course_id=6;
--1-shart---------------------------
select * from course_platform where price=0;

+-----------+---------------+------------+--------------+-------+--------+----------+
| course_id | title         | instructor | duraation_hr | price | rating | enrolled |
+-----------+---------------+------------+--------------+-------+--------+----------+
|         6 | C Programming | Jamshid K. |            9 |     0 |      4 |       60 |
+-----------+---------------+------------+--------------+-------+--------+----------+

--2-shart------------------------
select * from course_platform order by enrolled desc limit 3;

+-----------+------------------+------------+--------------+--------+--------+----------+
| course_id | title            | instructor | duraation_hr | price  | rating | enrolled |
+-----------+------------------+------------+--------------+--------+--------+----------+
|         7 | Data Science     | Aziza M.   |           20 | 250000 |      5 |      200 |
|         8 | Machine Learning | Bekzod S.  |           19 | 300000 |      5 |      170 |
|         3 | Web Development  | Sardor Bek |           15 | 200000 |      5 |      150 |
+-----------+------------------+------------+--------------+--------+--------+----------+

--3-shart-----------------------------------------

UPDATE course_platform set instructor="muhammad jorayev" where course_id=2;

select * from course_platform where instructor like "muhammad%";

+-----------+-------------+------------------+--------------+--------+--------+----------+
| course_id | title       | instructor       | duraation_hr | price  | rating | enrolled |
+-----------+-------------+------------------+--------------+--------+--------+----------+
|         2 | SQL Mastery | muhammad jorayev |            8 | 120000 |      5 |       95 |
+-----------+-------------+------------------+--------------+--------+--------+----------+

--4-shart-------------------------------------------

select instructor,sum() as miqdori from course_platform group by instructor;

+------------------+---------+
| instructor       | miqdori |
+------------------+---------+
| Ali Karimov      |       1 |
| muhammad jorayev |       1 |
| Sardor Bek       |       1 |
| Akbar T.         |       1 |
| Dilshod R.       |       1 |
| Jamshid K.       |       1 |
| Aziza M.         |       1 |
| Bekzod S.        |       1 |
| Nodir P.         |       1 |
| Sherzod U.       |       1 |
+------------------+---------+

------------------------------2-sql-masala---------------------

