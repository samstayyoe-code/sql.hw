# # AA3-masala------------------------------
# import pymysql

# class MySQL:
#     def __init__(self):
#         self.ConnectDB()
#         self.CreateDB()
#         self.CreateTB()

#     def ConnectDB(self):
#         self.db = pymysql.connect(
#             host="localhost",
#             user="root",
#             password="1234"
#         )
#         self.c = self.db.cursor()

#     def CreateDB(self):
#         self.c.execute("CREATE DATABASE IF NOT EXISTS gilos")
#         self.c.execute("USE gilos")

#     def CreateTB(self):
#         self.c.execute('''
#             CREATE TABLE IF NOT EXISTS restaurants(
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(50),
#                 address VARCHAR(100),
#                 maxFoodPrice INT,
#                 minFoodPrice INT,
#                 employeesCount INT,
#                 experience INT
#             )
#         ''')

#     def InsertData(self):
#         self.c.execute('''
#             INSERT INTO restaurants(name, address, maxFoodPrice, minFoodPrice, employeesCount, experience)
#             VALUES
#             ('Magic Burger', 'Chilonzor', 50000, 20000, 15, 5),
#             ('Mega Center', 'Yunusobod', 70000, 30000, 20, 7),
#             ('Master Chef', 'Sergeli', 90000, 40000, 25, 10),
#             ('Minor Cafe', 'Olmazor', 60000, 25000, 18, 6),
#             ('Mister Food', 'Chilonzor', 80000, 35000, 22, 8),
#             ('Burger King', 'Yakkasaroy', 75000, 30000, 19, 9),
#             ('Pizza Max', 'Yunusobod', 65000, 28000, 17, 4),
#             ('Royal Diner', 'Sergeli', 100000, 50000, 30, 12),
#             ('City Grill', 'Olmazor', 55000, 20000, 14, 3),
#             ('Fast Fooder', 'Chilonzor', 60000, 25000, 16, 5)
#         ''')
#         self.db.commit()
# # --1-shart----------------------------------------------------

#     def FirstQuery(self):
#         self.c.execute('''
#             SELECT name, maxFoodPrice 
#             FROM restaurants
#             WHERE name LIKE 'm%r'
#             ORDER BY maxFoodPrice ASC
#         ''')
#         natija=self.c.fetchall()
#         for i in natija:
#             print(i)

# # --2-shart---------------------------------------------------
#     def SecondQuery(self):
#         self.c.execute('''
#             SELECT name, minFoodPrice 
#             FROM restaurants
#             ORDER BY minFoodPrice ASC
#             LIMIT 3
#         ''')
#         natija=self.c.fetchall()
#         for i in natija:
#             print(i)

# # --3-shart---------------------------------------------------
#     def ThirdQuery(self):
#         self.c.execute('''
#             SELECT name, maxFoodPrice 
#             FROM restaurants
#             ORDER BY experience DESC, maxFoodPrice DESC
#             LIMIT 4
#         ''')
#         natija=self.c.fetchall()
#         for i in natija:
#             print(i)



# mysql = MySQL()

# mysql.InsertData()
# mysql.FirstQuery()
# mysql.SecondQuery()
# mysql.ThirdQuery()



# AA1-MASALA-----------------------------------------------

import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234"
        )
        self.c = self.db.cursor()

    def CreateDB(self):
        self.c.execute("CREATE DATABASE IF NOT EXISTS School")
        self.c.execute("USE School")

    def CreateTB(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS teachers(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                surname VARCHAR(50),
                salary INT,
                experience INT,
                branch VARCHAR(50)
            )
        ''')

        self.c.execute('''
            CREATE TABLE IF NOT EXISTS students(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                surname VARCHAR(50),
                monthly_payment INT,
                course_duration INT,
                branch VARCHAR(50)
            )
        ''')

    def insert_data(self):
        self.c.execute('''
            INSERT INTO teachers(name,surname,salary,experience,branch) VALUES
            ('Ali','Karimov',1000,3,'Chilonzor'),
            ('Vali','Aliyev',1500,5,'Yunusobod'),
            ('Hasan','Hasanov',1200,4,'Chilonzor'),
            ('Husan','Husanov',2000,7,'Sergeli'),
            ('Akmal','Akmalov',1800,6,'Olmazor'),
            ('Sardor','Saidov',1300,2,'Yunusobod'),
            ('Jasur','Jasurov',2200,10,'Sergeli')
        ''')

        self.c.execute('''
            INSERT INTO students(name,surname,monthly_payment,course_duration,branch) VALUES
            ('Ali','Karimov',300,6,'Chilonzor'),
            ('Vali','Aliyev',400,5,'Yunusobod'),
            ('Ali','Saidov',350,4,'Chilonzor'),
            ('Hasan','Karimov',500,6,'Sergeli'),
            ('Husan','Aliyev',450,5,'Olmazor'),
            ('Sardor','Saidov',300,3,'Yunusobod'),
            ('Jasur','Karimov',600,6,'Sergeli')
        ''')

        self.db.commit()
    

    def q1(self):
        self.c.execute('''select * from teachers order by salary''')
        natija=self.c.fetchall()
        for i in natija:
            print(i)


    def q2(self):
        self.c.execute('''select * from teachers order by salary , experience desc''')
        natija=self.c.fetchall()
        for i in natija:
            print(i)


    def q3(self):


        self.c.execute("UPDATE teachers SET salary = salary - 200 ORDER BY salary DESC LIMIT 1")
        self.db.commit()
    

    def q4(self):
        self.c.execute("UPDATE teachers SET branch='Chilonzor' ORDER BY experience DESC LIMIT 1")
        self.db.commit()

    def q5(self):
        self.c.execute("SELECT * FROM students ORDER BY surname")
        natija=self.c.fetchall()
        for i in natija:
            print(i)


    def q6(self):
        self.c.execute("SELECT * FROM students ORDER BY monthly_payment DESC")
        natija=self.c.fetchall()
        for i in natija:
            print(i)

    def q7(self):
        self.c.execute("SELECT SUM(monthly_payment * course_duration) FROM students")
        natija=self.c.fetchall()
        for i in natija:
            print(i)

    

    def q8(self):
        self.c.execute("""
            UPDATE students
            SET branch='Dubay'
            ORDER BY (monthly_payment * course_duration) DESC
            LIMIT 1
        """)
        self.db.commit()
    

    def q9(self):
        self.c.execute("""
            SELECT t.name, s.name, t.branch
            FROM teachers t
            INNER JOIN students s
            ON t.branch = s.branch
        """)
        natija=self.c.fetchall()
        for i in natija:
            print(i)
    

    def q10(self):
        self.c.execute("""
            SELECT name, branch FROM students
            WHERE name IN (
                SELECT name FROM students
                GROUP BY name
                HAVING COUNT(*) > 1
            )
        """)
        natija=self.c.fetchall()
        for i in natija:
            print(i)


    def q11(self):
        self.c.execute("""
            SELECT surname, monthly_payment FROM students
            WHERE surname IN (
                SELECT surname FROM students
                GROUP BY surname
                HAVING COUNT(*) > 1
            )
        """)
        natija=self.c.fetchall()
        for i in natija:
            print(i)


mysql=MySQL()
# mysql.insert_data()
# mysql.q1()
# mysql.q2()
# mysql.q3()
# mysql.q4()
# mysql.q5()
# mysql.q6()
# mysql.q7()
# mysql.q8()
# mysql.q9()
# mysql.q10()
# mysql.q11()


