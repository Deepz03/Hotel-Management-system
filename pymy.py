import pymysql


conn= pymysql.connect(host="localhost" ,user="root" ,password="Admin@123" ,database="hotel_management")
con = conn.cursor()
u=1
g=2
ci=2
co=3
r="king"
status="book"
con.execute("insert into book values('"+u+"','"+g+"','"+ci+"','"+co+"','"+r+"','"+s+"')")
conn.commit()
