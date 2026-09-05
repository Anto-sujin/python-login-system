import string
import re
import sqlite3
import text



def contains_number(s):
    return  any(w.isdigit() for w in s)

def contains_sysmbol(s):
    return any(w in string.punctuation for w in s )

def register_db(mail,user_name,password):
    con = sqlite3.connect("user.db")
    ex = con.cursor()
    query =   "INSERT INTO users (email, username, password_hash) VALUES (?, ?, ?)"
    ex.execute(query,(mail,user_name,password))
    con.commit()
    con.close()


num =input("\n1->LOGIN\n2->REGISTER\nenter the number :")

if num =="2":
   
       mail =input("Enter the mail:")
       user_name =input("Enter the username:")
       password =input("Enter the password:")


       pattern = r"^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$"

       if not re.fullmatch(pattern, mail):
             print("Invalid email")    
       elif not text.mail_exist(mail):
           print("MAIL IS ALREADY USED")
           
       elif len(password)<8:
             print("MIN 8 CHARATER REQUIRED")
       elif  not contains_number(password) :
             print("Must contain number's")
       elif  not contains_sysmbol(password):
             print("Must by on special charater")
       else:
             register_db(mail,user_name,password)
    
elif num =="1":
    
    mail =input("enter the mail:")
    password = input("enter the password:")
    
    if not text.mail_exist(mail):
        print("INVALID MAIL ID")
    elif password != text.pass_checker(mail):
        print("INVALID PASSWORD")
    else:
        print("successfully")
        
        
    
