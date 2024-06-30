from tkinter import *
import pymysql
from mainfile import *
from PIL import Image, ImageTk

conn = pymysql.connect(host="localhost",user="root",password="Admin@123",database="hotel_management")
con= conn.cursor()

def register():
    global register_screen
    global e1
    global e2
    register_screen = Toplevel(main_screen)
    register_screen.geometry("300x250")
    register_screen.title("User Registration")
    l0=Label(register_screen,text="User Registration",bg="black",fg="white",height="3",width="100",font="bold")
    l0.pack(pady="3")
    
    l1=Label(register_screen,text="Username",height="1",width="15",bg="black",fg="white")
    l1.pack()
    e1=Entry(register_screen,text="")
    e1.pack(pady="3")
    l2=Label(register_screen,text="Password",height="1",width="15",bg="black",fg="white")
    l2.pack()
    e2=Entry(register_screen,text="",show='*')
    e2.pack(pady="3")
    b1=Button(register_screen,text="Register",height="1",width="15",bg="black",fg="white",command=register_entry)
    b1.pack()
    
def login():
    global login_screen
    global e3
    global e4
    login_screen = Toplevel(main_screen)
    login_screen.geometry("300x250")
    login_screen.title("User login")
    l0=Label(login_screen,text="User login",bg="black",fg="white",height="3",width="100",font="bold")
    l0.pack(pady="3")
    
    l1=Label(login_screen,text="Username",height="2",width="15",bg="black",fg="white")
    l1.pack()
    e3=Entry(login_screen,text="")
    e3.pack(pady="3")
    l2=Label(login_screen,text="Password",height="2",width="15",bg="black",fg="white")
    l2.pack()
    e4=Entry(login_screen,text="",show='*')
    e4.pack(pady="3")
    b1=Button(login_screen,text="Login",height="2",width="15",bg="black",fg="white",command=login_check)
    b1.pack()

def register_entry():
    a=e1.get()
    b=e2.get()
    con.execute("insert into user_reg (name,password) values('"+a+"','"+b+"')")
    conn.commit()
    con.close
    conn.close
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_check():
    user= e3.get()
    pas= e4.get()
    con.execute( "select name,password from user_reg where name =%s and password = %s",(user,pas))
    result=con.fetchone()
    if result==None:
        wrong()
    elif result[0]==user:
        if result[1]==pas:
            login_sucess()
        

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
    
def wrong():
    global wrong_pass_screen
    wrong_pass_screen = Toplevel(login_screen)
    wrong_pass_screen.title("Error")
    wrong_pass_screen.geometry("150x100")
    Label(wrong_pass_screen, text="Invalid Password/\nNo user found ").pack()
    Button(wrong_pass_screen, text="OK", command=delete_wrong_pass).pack()


def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()
    main_func()
    
def delete_wrong_pass():
    wrong_pass_screen.destroy()


    
def main():
    global main_screen
    main_screen =Tk()
    main_screen.geometry("300x250")
    main_screen.title("User Account")
    
    l1=Label(main_screen,text="User Registration / Login",bg="black",fg="white",height="3",width="100",font="bold")
    l1.pack(pady="25")
    b1=Button(main_screen,text="Register",height="2",width="25",bg="black",fg="white",command=register)
    b1.pack()
    b2=Button(main_screen,text="Login",bg="black",fg="white",height="2",width="25",command=login)
    b2.pack(pady="3")
    
    
main()
    
    
