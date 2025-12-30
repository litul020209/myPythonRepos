import mysql.connector as mysql

connect=mysql.connect(host="localhost",user="root",password="Biswal@12345",database="sample_fp_10")

cur=connect.cursor()

#excuttion part
q="insert into sample" \
"values(1,'Litul','B',10000,'BBSR')" 
""
cur.execute(q)
connect.commit()
for row in cur:
    print(row)
cur.close()
connect.close()