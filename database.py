import sqlite3

connect =sqlite3.connect("user.db")
con =connect.cursor()
con.execute("""
select * from users;
""")
for i in con:
    print(i)
connect.commit()
connect.close()
