import mysql.connector as mysql

connect=mysql.connect(host="localhost",user="root",password="Biswal@12345",database="sample_fp_10")

cur=connect.cursor()

#excuttion part
cur.execute("create table sample(id int,firstname varchar(100),lastname varchar(100), salary float, location varchar(100))")
cur.execute("show tables")
for table in cur:
    print(table)
cur.close()
connect.close()