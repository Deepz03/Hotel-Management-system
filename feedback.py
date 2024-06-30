from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

#connecting data base
conn = pymysql.connect(host="localhost",user="root",password="Admin@123",database="hotel_management")
con= conn.cursor()
def feed():
    user=e1.get()
    feedback =e2.get()

    insert= "insert into feedback values('"+user+"','"+feedback+"')"
    try:
        con.execute(insert)
        conn.commit()
        messagebox.showinfo('Success'," Submitted! ")

    except:
        messagebox.showinfo("Cant able to submit ! ")

    a.destroy()
    
def feedback():
    global a,e1,e2
    a= Tk()
    a.title('Feedback')
    a.minsize(width=400,height=400)
    a.geometry('850x750')


    Canvas1 = Canvas(a)    
    Canvas1.config(bg="#97F19E")
    Canvas1.pack(expand=True,fill=BOTH)

    l0=Label(a,text="Feedback",bg="white",fg="black",height="50",width="1000",font="bold")
    l0.place(relx=0.28,rely=0.1, relwidth=0.45, relheight=0.1)

    l1=Label(a,text="User ID",height="1",width="15",bg="white",fg="black",font=(1))
    l1.place(relx=0.2,rely=0.25, relwidth=0.2, relheight=0.06)
    e1=Entry(a,text="",font=(1))
    e1.place(relx=0.4,rely=0.25, relwidth=0.4, relheight=0.06)

    e2=Entry(a,text="",justify="left",font=(1))
    e2.place(relx=0.20,rely=0.35, relwidth=0.6, relheight=0.40)

    SubmitBtn = Button(a,text="submit",bg='white', fg='black',command=feed)
    SubmitBtn.place(relx=0.40,rely=0.80, relwidth=0.18,relheight=0.08)

