create database student;
create table student if not exists(id int, name text ,second text,age real, bahosi real);
insert into student values(1,"akbar","saidov", 18, 80),
            (2,"behruz","shokirov",17,90),
            (3,"avaz","temirov",19,75),
            (4,"fazliddin","jeparov",18,65),
            (5,"hasanboy","dosmatov",25,45);

UPDATE student SET bahosi=95 where id=5;

select * from student where bahosi>90 ORDER by name DESC;

+------+----------+----------+------+--------+
| id   | name     | second   | age  | bahosi |
+------+----------+----------+------+--------+
|    5 | hasanboy | dosmatov |   25 |     95 |
+------+----------+----------+------+--------+
1 row in set (0.01 sec)

select * from student where bahosi BETWEEN 70 and 90 ORDER BY age DESC;
+------+--------+----------+------+--------+
| id   | name   | second   | age  | bahosi |
+------+--------+----------+------+--------+
|    3 | avaz   | temirov  |   19 |     75 |
|    1 | akbar  | saidov   |   18 |     80 |
|    2 | behruz | shokirov |   17 |     90 |
+------+--------+----------+------+--------+
3 rows in set (0.00 sec)



 select * from student where bahosi BETWEEN 60 and 70 ORDER by bahosi;
+------+-----------+---------+------+--------+
| id   | name      | second  | age  | bahosi |
+------+-----------+---------+------+--------+
|    4 | fazliddin | jeparov |   18 |     65 |
+------+-----------+---------+------+--------+
1 row in set (0.00 sec)

-----------------milliy taomlar-------------------
create database if not exists milliy_taomlar;
create table milliy_taomlar(id int, taom_nomi text, taom_masalliqlar text);
insert into milliy_taomlar values(1, 'Osh (Palov)', 'Guruch, sabzi, gosht, piyoz, yog, ziravorlar'),
(2, 'Somsa', 'Un, gosht yoki kartoshka, piyoz, yog'),
(3, 'Manti', 'Un, qiyma gosht, piyoz, ziravorlar'),
(4, 'Lagmon', 'Un, gosht, sabzavotlar, ziravorlar'),
(5, 'Shashlik', 'Gosht, piyoz, sirka, ziravorlar'),
(6, 'Dimlama', 'Gosht, kartoshka, sabzi, karam, piyoz'),
(7, 'Chuchvara', 'Un, qiyma gosht, piyoz, ziravorlar'),
(8, 'Norin', 'Ot goshti, xamir, piyoz'),
(9, 'Qozon kabob', 'Gosht, kartoshka, piyoz, yog'),
(10, 'Moshxorda', 'Mosh, guruch, gosht, sabzi, piyoz');

select * from milliy_taomlar;

+------+-------------+----------------------------------------------+
| id   | taom_nomi   | taom_masalliqlar                             |
+------+-------------+----------------------------------------------+
|    1 | Osh (Palov) | Guruch, sabzi, gosht, piyoz, yog, ziravorlar |
|    2 | Somsa       | Un, gosht yoki kartoshka, piyoz, yog         |
|    3 | Manti       | Un, qiyma gosht, piyoz, ziravorlar           |
|    4 | Lagmon      | Un, gosht, sabzavotlar, ziravorlar           |
|    5 | Shashlik    | Gosht, piyoz, sirka, ziravorlar              |
|    6 | Dimlama     | Gosht, kartoshka, sabzi, karam, piyoz        |
|    7 | Chuchvara   | Un, qiyma gosht, piyoz, ziravorlar           |
|    8 | Norin       | Ot goshti, xamir, piyoz                      |
|    9 | Qozon kabob | Gosht, kartoshka, piyoz, yog                 |
|   10 | Moshxorda   | Mosh, guruch, gosht, sabzi, piyoz            |
+------+-------------+----------------------------------------------+

select * from milliy_taomlar where taom_nomi like "%a";
+------+-----------+---------------------------------------+
| id   | taom_nomi | taom_masalliqlar                      |
+------+-----------+---------------------------------------+
|    2 | Somsa     | Un, gosht yoki kartoshka, piyoz, yog  |
|    6 | Dimlama   | Gosht, kartoshka, sabzi, karam, piyoz |
|    7 | Chuchvara | Un, qiyma gosht, piyoz, ziravorlar    |
|   10 | Moshxorda | Mosh, guruch, gosht, sabzi, piyoz     |
+------+-----------+---------------------------------------+

select * from milliy_taomlar where taom_masalliqlar like "%guruch%";

+------+-------------+----------------------------------------------+
| id   | taom_nomi   | taom_masalliqlar                             |
+------+-------------+----------------------------------------------+
|    1 | Osh (Palov) | Guruch, sabzi, gosht, piyoz, yog, ziravorlar |
|   10 | Moshxorda   | Mosh, guruch, gosht, sabzi, piyoz            |
+------+-------------+----------------------------------------------+

---------------------