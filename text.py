import sqlite3

def mail_exist(mail):
   con = sqlite3.connect("user.db")
   ex = con.cursor()
   ex.execute("Select email from users where email==?",(mail,))
   a=ex.fetchone
   ex.close()
   return bool(a)

def pass_checker(mail):
    con = sqlite3.connect("user.db")
    ex = con.cursor()
    
    ex.execute("Select password_hash from users where email==?",(mail,))
    a=ex.fetchone()
    ex.close()
    con.close()
    a=a[0]
    return a