import pymysql
db=pymysql.connect("localhost","root","root","studentdb")
cursor=db.cursor()
#cursor.execute("create table marks2(name varchar(20), marks)");
#print("table created successfully")
cursor.execute("insert into marks values ('Satyam1',56)");
cursor.execute("select * from marks");
for i in cursor:
    print(i)
cursor.close()

