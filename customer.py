from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

#connecting data base
conn = pymysql.connect(host="localhost",user="root",password="Admin@123",database="hotel_management")
con= conn.cursor()

def cus_reg():
    user_id = e5.get()
    user = e1.get()
    mobile=e2.get()
    email=e3.get()
    aadhar=e4.get()

    insert =("insert into customers values('"+user_id+"','"+user+"','"+mobile+"','"+email+"','"+aadhar+"')")
    try:
        con.execute(insert)
        conn.commit()
        messagebox.showinfo('Success'," user details registered ")
    except Exception as e:
        print(e)
        messagebox.showinfo("Error","Can't add data into Database")
        

    print("{} \n{} \n{} \n{} \n{}".format(user_id,user,mobile,email,aadhar))
    
    a.destroy()

def get():
    con.execute("select name,user_id from user_reg where user_id='"+e5.get()+"'")
    res=con.fetchall()
    for i in res:
        e1.insert(0,i[0])
        
def customer():
    global e1,e2,e3,e4,e5,a
    a=Tk()
    a.title('User Registration')
    a.minsize(width=400,height=400)
    a.geometry('850x750')


    Canvas1 = Canvas(a)    
    Canvas1.config(bg="#FBB3BD")
    Canvas1.pack(expand=True,fill=BOTH)
    

    l0=Label(a,text="User Registration",bg="white",fg="black",height="50",width="1000",font="bold")
    l0.place(relx=0.28,rely=0.1, relwidth=0.45, relheight=0.1)
    
    l5=Label(a,text="User ID",height="1",width="15",bg="white",fg="black",font=(1))
    l5.place(relx=0.2,rely=0.25, relwidth=0.2, relheight=0.06)
    e5=Entry(a,text="",font=(1))
    e5.place(relx=0.4,rely=0.25, relwidth=0.45, relheight=0.06)

    l1=Label(a,text="Username",height="1",width="15",bg="white",fg="black",font=(1))
    l1.place(relx=0.2,rely=0.35, relwidth=0.2, relheight=0.06)
    e1=Entry(a,text="",font=(1))
    e1.place(relx=0.4,rely=0.35, relwidth=0.45, relheight=0.06)

    l2=Label(a,text="Mobile No",height="1",width="15",bg="white",fg="black",font=(1))
    l2.place(relx=0.2,rely=0.45, relwidth=0.2, relheight=0.06)
    e2=Entry(a,text="",font=(1))
    e2.place(relx=0.4,rely=0.45, relwidth=0.45, relheight=0.06)

    l3=Label(a,text="Mail Id",height="1",width="15",bg="white",fg="black",font=(1))
    l3.place(relx=0.2,rely=0.55, relwidth=0.2, relheight=0.06)
    e3=Entry(a,text="",font=(1))
    e3.place(relx=0.4,rely=0.55, relwidth=0.45, relheight=0.06)

    l4=Label(a,text="Aadhar Card No",height="1",width="15",bg="white",fg="black",font=(1))
    l4.place(relx=0.2,rely=0.65, relwidth=0.2, relheight=0.06)
    e4=Entry(a,text="",font=(1))
    e4.place(relx=0.4,rely=0.65, relwidth=0.45, relheight=0.06)

    SubmitBtn = Button(a,text="SUBMIT",bg='white', fg='black',command= cus_reg)
    SubmitBtn.place(relx=0.25,rely=0.75, relwidth=0.18,relheight=0.08)

    SubmitBtn = Button(a,text="GET",bg='grey', fg='black',command=get)
    SubmitBtn.place(relx=0.45,rely=0.75, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(a,text="QUIT",bg='#d1ccc0', fg='black', command=a.destroy)
    quitBtn.place(relx=0.65,rely=0.75, relwidth=0.18,relheight=0.08)

    a.mainloop()
