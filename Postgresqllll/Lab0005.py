import psycopg2

conn = psycopg2.connect(database='postgres', user='postgres', password='abc000',
                        host='127.0.0.1', port='5432')
print("Opened database sucessfully")

cur=conn.cursor()
# cur.execute('''CREATE TABLE COMPANY9
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL,
#             ADDRESS CHAR(50),
#             SALARY REAL);''')
#
# print("Created table sucessfully")
# conn.commit()
#
# cur.execute("INSERT INTO COMPANY9(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(1,'Amrith', 32, 'California', 8000)");
# cur.execute("INSERT INTO COMPANY9(ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES(2, 'Bala', 33, 'Norway', 10000)");
# cur.execute("INSERT INTO COMPANY9(id,name,age,address,salary)\
#             VALUES(3, 'Christopher', 34, 'England', 12000)");
# cur.execute("INSERT INTO COMPANY9(id,name,age,address,salary)\
#             VALUES(4, 'Daniel', 35, 'Los_Angels', 14000)");
#
# conn.commit()
# print("Inserted into table successfully")

cur.execute("UPDATE COMPANY9 set SALARY = 25000 where ID=1")
conn.commit()
print("Total number of rows updated:", cur.rowcount)

cur.execute("SELECT id,name,age,address,salary from COMPANY9")
rows=cur.fetchall()
for row in rows:
    print("\nID=",row[0])
    print("NAME=",row[1])
    print("AGE=",row[2])
    print("ADDRESS=",row[3])
    print("SALARY=",row[4], '\n')

print("Operations done successfully")


cur.execute("DELETE from COMPANY9 where ID=2")
conn.commit()
print("Total number of rows updated:", cur.rowcount)
cur.execute("SELECT id,name,age,address,salary from COMPANY9")
rows=cur.fetchall()
for row in rows:
    print("\nID=", row[0])
    print("NAME=", row[1])
    print("AGE=", row[2])
    print("ADDRESS=",row[3])
    print("SALARY=", row[4], '\n')

print("Operations done successfully")
conn.close()