import pymysql
db=pymysql.connect("localhost","root","root","studentdb")
cursor=db.cursor()
#print("table created successfully")
cursor.execute("insert into marks values ('Satyam1',56)");
cursor.execute("select name,mark from marks");
for i in cursor:
    print(i)
print("-------------------------")
db.commit()

cursor.execute("UPDATE marks set name ='Aaush' where mark=69")
cursor.execute("select * from marks")
for i in cursor:
    print(i)
print("-------------------------")
cursor.execute("DELETE from marks where name='Aaush'")
cursor.execute("select * from marks")
for i in cursor:
    print(i)
db.rollback()
cursor.close()

