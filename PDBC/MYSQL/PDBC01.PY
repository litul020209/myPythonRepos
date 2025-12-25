import mysql.connector as mysql

connect=mysql.connect(host="localhost",user="root",password="Biswal@12345")

cur=connect.cursor()

#excuttion part
cur.execute("create database sample_fp_10")
cur.excute("show databases")
for db in cur:
    print(db)
cur.close()
connect.close()