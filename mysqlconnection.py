import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='gameover007',database='queen')
mycursor=mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
    print(i)