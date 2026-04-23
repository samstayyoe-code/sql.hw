create database computers;
create table computers(id text,model text,cpu text,frequency real,ram int,os text,price real);
INSERT INTO computers VALUES
('Apple','MacBook Pro','Intel i7',3.2,16,'macOS',2500),
('Apple','MacBook Air','Intel i5',2.5,8,'macOS',1500),
('ASUS','ZenBook','Intel i7',3.1,16,'Windows',1800),
('ASUS','VivoBook','Intel i5',2.4,8,'Windows',900),
('HP','Pavilion','Intel i5',2.8,8,'Windows',800),
('HP','Envy','Intel i7',3.0,16,'Windows',1600),
('Dell','XPS 13','Intel i7',3.5,16,'Ubuntu',2000),
('Dell','Inspiron','Intel i5',2.6,8,'Windows',850),
('Lenovo','ThinkPad','Intel i7',3.3,16,'Windows',1700),
('Lenovo','IdeaPad','Intel i5',2.5,8,'Windows',750),
('Acer','Aspire','Intel i5',2.7,8,'Windows',700),
('Acer','Swift','Intel i7',3.2,16,'Windows',1400),
('Apple','Mac Mini','Intel i5',2.6,8,'macOS',1200),
('ASUS','ROG','Intel i7',3.8,32,'Windows',2800),
('HP','EliteBook','Intel i7',3.4,16,'Windows',1900),
('Dell','Latitude','Intel i5',2.5,8,'Windows',950),
('Lenovo','Yoga','Intel i7',3.1,16,'Windows',1600),
('Acer','Nitro','Intel i7',3.6,16,'Windows',1500),
('Apple','iMac','Intel i7',3.7,16,'macOS',2700),
('ASUS','TUF','Intel i5',2.9,8,'Windows',1000);

-- 1-shart-----------
select * from computers order by price DESC limit 1;

+------+-------+----------+-----------+------+---------+-------+
| id   | model | cpu      | frequency | ram  | os      | price |
+------+-------+----------+-----------+------+---------+-------+
| ASUS | ROG   | Intel i7 |       3.8 |   32 | Windows |  2800 |
+------+-------+----------+-----------+------+---------+-------+

--2-shart---------------------
select * from computers order by price limit 1;

+------+--------+----------+-----------+------+---------+-------+
| id   | model  | cpu      | frequency | ram  | os      | price |
+------+--------+----------+-----------+------+---------+-------+
| Acer | Aspire | Intel i5 |       2.7 |    8 | Windows |   700 |
+------+--------+----------+-----------+------+---------+-------+

--3-shart-------------------
select frequency from computers where price between 400 and 1000 and cpu like "%intel%";

+-----------+
| frequency |
+-----------+
|       2.4 |
|       2.8 |
|       2.6 |
|       2.5 |
|       2.7 |
|       2.5 |
|       2.9 |
+-----------+

--4-shart-----------------------
select * from computers where id="Apple";

+-------+-------------+----------+-----------+------+-------+-------+
| id    | model       | cpu      | frequency | ram  | os    | price |
+-------+-------------+----------+-----------+------+-------+-------+
| Apple | MacBook Pro | Intel i7 |       3.2 |   16 | macOS |  2500 |
| Apple | MacBook Air | Intel i5 |       2.5 |    8 | macOS |  1500 |
| Apple | Mac Mini    | Intel i5 |       2.6 |    8 | macOS |  1200 |
| Apple | iMac        | Intel i7 |       3.7 |   16 | macOS |  2700 |
+-------+-------------+----------+-----------+------+-------+-------+

qanaqa qib sanashni bilmadim gpt count(*) db chiqardi qigim kemadi 

--5-shart----------------------
select price from computers where id="ASUS" and os='Windows' and ram>8 order by price;

+-------+
| price |
+-------+
|  1800 |
|  2800 |
+-------+
