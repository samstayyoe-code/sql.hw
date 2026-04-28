CREATE TABLE genre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE author (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE book(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    price INT,
    amount INT,
    a_id INT,
    g_id INT,
    FOREIGN KEY (a_id) REFERENCES author(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (g_id) REFERENCES genre(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO genre VALUES
(1,'badiiy'),
(2,'tarixiy'),
(3,'diniy'),
(4,'sheriyat');

INSERT INTO author VALUES
(1,'Alisher Navoiy'),
(2,'Abdulla Qodiriy'),
(3,'Cholpon'),
(4,'Erkin Vohidov');

INSERT INTO book(name,price,amount,a_id,g_id) VALUES
('Xamsa',100000,10,1,1),
('Lison ut-tayr',80000,5,1,4),
('Mahbub ul-qulub',70000,6,1,3),
('Farhod va Shirin',120000,8,1,1),
('Otkan kunlar',150000,7,2,2),
('Mehrobdan chayon',130000,5,2,2),
('Obid ketmon',90000,4,2,1),
('Baxtsiz kuyov',85000,3,2,1),
('Kecha va kunduz',110000,6,3,1),
('Uygonish',75000,5,3,4),
('Yorqinoy',70000,4,3,4),
('Adabiyot nadir',80000,2,3,3),
('Tong nafasi',90000,4,4,4),
('Ozbegim',100000,6,4,4),
('Ruhlar isyoni',85000,3,4,1),
('Sevgi va nafrat',95000,5,4,1);

--1-masala-------------------
SELECT g.name
FROM book as b
JOIN genre as g ON g.id = b.g_id
JOIN author as a ON a.id = b.a_id
WHERE a.name = 'Alisher Navoiy'
GROUP BY g.name;

+----------+
| name     |
+----------+
| badiiy   |
| sheriyat |
| diniy    |
+----------+

--2-masala-------------------------
SELECT a.name,g.name
from book as b
JOIN genre as g on g.id = b.g_id
JOIN author as a on a.id =b.a_id;

+-----------------+----------+
| name            | name     |
+-----------------+----------+
| Alisher Navoiy  | badiiy   |
| Alisher Navoiy  | badiiy   |
| Abdulla Qodiriy | badiiy   |
| Abdulla Qodiriy | badiiy   |
| Cholpon         | badiiy   |
| Erkin Vohidov   | badiiy   |
| Erkin Vohidov   | badiiy   |
| Abdulla Qodiriy | tarixiy  |
| Abdulla Qodiriy | tarixiy  |
| Alisher Navoiy  | diniy    |
| Cholpon         | diniy    |
| Alisher Navoiy  | sheriyat |
| Cholpon         | sheriyat |
| Cholpon         | sheriyat |
| Erkin Vohidov   | sheriyat |
| Erkin Vohidov   | sheriyat |
+-----------------+----------+

--3-masala------------------------------

SELECT a.name AS author, g.name AS janr, COUNT(b.id) AS kitob_soni
FROM book AS b
INNER JOIN author AS a ON a.id = b.a_id
INNER JOIN genre AS g ON g.id = b.g_id
GROUP BY a.name, g.name;

+-----------------+----------+------------+
| author          | janr     | kitob_soni |
+-----------------+----------+------------+
| Alisher Navoiy  | badiiy   |          2 |
| Alisher Navoiy  | sheriyat |          1 |
| Alisher Navoiy  | diniy    |          1 |
| Abdulla Qodiriy | tarixiy  |          2 |
| Abdulla Qodiriy | badiiy   |          2 |
| Cholpon         | badiiy   |          1 |
| Cholpon         | sheriyat |          2 |
| Cholpon         | diniy    |          1 |
| Erkin Vohidov   | sheriyat |          2 |
| Erkin Vohidov   | badiiy   |          2 |
+-----------------+----------+------------+

--4-masala--------------------------------

select g.name as janr, count(b.id) as soni 
from book as b 
INNER join genre as g on g.id = b.g_id
GROUP by g.name
order by soni desc 
limit 1;

+--------+------+
| janr   | soni |
+--------+------+
| badiiy |    7 |
+--------+------+

--5-masala----------------------------------

select a.name as author, g.name as janr, count(b.id) as soni
from book as b 
INNER join author as a on a.id = b.a_id
INNER join genre as g on g.id = b.g_id
GROUP by a.name, g.name
order by a.name,soni desc;

+-----------------+----------+------+
| author          | janr     | soni |
+-----------------+----------+------+
| Abdulla Qodiriy | tarixiy  |    2 |
| Abdulla Qodiriy | badiiy   |    2 |
| Alisher Navoiy  | badiiy   |    2 |
| Alisher Navoiy  | sheriyat |    1 |
| Alisher Navoiy  | diniy    |    1 |
| Cholpon         | sheriyat |    2 |
| Cholpon         | badiiy   |    1 |
| Cholpon         | diniy    |    1 |
| Erkin Vohidov   | sheriyat |    2 |
| Erkin Vohidov   | badiiy   |    2 |
+-----------------+----------+------+

--6-masala-------------------------------------

select a.name as author, b.name as kitob, b.amount as sotilgan_soni
from book as b 
inner join author as a on a.id = b.a_id
order by b.amount desc 
limit 1;

+----------------+-------+---------------+
| author         | kitob | sotilgan_soni |
+----------------+-------+---------------+
| Alisher Navoiy | Xamsa |            10 |
+----------------+-------+---------------+

