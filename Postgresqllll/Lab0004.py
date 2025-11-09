# import psycopg2
#
# conn = psycopg2.connect(database="postgres", user="postgres", password="abc000",
#                         host="127.0.0.1", port=5432)
#
# print("Opened database successfully")

# import psycopg2
#
# conn = psycopg2.connect(database='postgres', user='postgres', password='abc000',
#                         host='127.0.0.1', port='5432')
# print("Opened databse successfully")
#
# cur=conn.cursor()
cur.execute('''CREATE TABLE COMPANY5
            (ID INT PRIMARY KEY NOT NULL,
            NAME TEXT NOT NULL,
            AGE INT NOT NULL,
            ADDRESS CHAR(50),
            SALARY REAL);''')
#
# print("Create company5 table successfully")
# conn.commit()
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database='postgres', user='postgres', password='abc000',
#                         host='127.0.0.1', port='5432')
# print("Opened database sucessfully")
#
# cur=conn.cursor()
# cur.execute("INSERT INTO COMPANY5(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(1,'PAUL',12,'NORWAY', 5000)"),
# cur.execute("INSERT INTO COMPANY5(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(2,'ANDY', 14, 'CALIFORNIA', 6000)"),
# cur.execute("INSERT INTO COMPANY5(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(3, 'TOM', 16, 'BUDAPEST', 18000)"),
# cur.execute("INSERT INTO COMPANY5(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(4, 'ROBIN', 29, 'GOA', 22000)");
# conn.commit()
# print("Inserted records successfully")
# conn.close()

# import psycopg2
#
# conn = psycopg2.connect(database='postgres', user='postgres', password='abc000',
#                         host='127.0.0.1', port='5432')
# print("Opened database successfully")
#
# cur = conn.cursor()
# cur.execute("SELECT id, name, age, address, salary from COMPANY5")
# rows=cur.fetchall()
# for row in rows:
#     print("\nID = ", row[0])
#     print("NAME = ", row[1])
#     print("AGE = ", row[2])
#     print("ADDRESS = ", row[3])
#     print("SALARY = ", row[4], "\n")
#
# print("Operation done successfully")
# conn.close()

# import psycopg2
#
# conn=psycopg2.connect(database='postgres', user='postgres', password='abc000',
#                       host='127.0.0.1', port='5432')
# print("Opened databse sucessfully")
#
# cur=conn.cursor()
# cur.execute("DELETE from COMPANY5 where ID=2")
# conn.commit()
# print("Total number of rows deleted:", cur.rowcount)
#
# cur.execute("SELECT id,name,age,address,salary from COMPANY5")
# rows=cur.fetchall()
# for row in rows:
#     print("\nID=",row[0])
#     print("NAME=",row[1])
#     print("AGE=",row[2])
#     print("ADDRESS=",row[3])
#     print("SALARY=",row[4])
#
# print("Operation done successfully")
# conn.close()

