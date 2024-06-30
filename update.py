from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
from bookings import *

#connecting data base
conn = pymysql.connect(host="localhost",user="root",password="Admin@123",database="hotel_management")
con= conn.cursor()

def cancel_fun():
    user =e1.get()
    deletesql = "delete from book where user_id = '"+user+"'"
    con.execute(deletesql)
    conn.commit()
    messagebox.showinfo('Success',"Booking Canceled")
    
        
    print(user)
    e1.delete(0,END)
    b.destroy()
    a.destroy()
    
def cancel():
    global b,e1
    b=Tk()
    b.title("cancelation")
    b.geometry('400x400')
    Canvas1 = Canvas(b)    
    Canvas1.config(bg="black")
    Canvas1.pack(expand=True,fill=BOTH)

    l1=Label(b,text="User ID",height="1",width="15",bg="white",fg="black",font=(1))
    l1.place(relx=0.2,rely=0.25, relwidth=0.2, relheight=0.1)
    e1=Entry(b,text="",font=(1))
    e1.place(relx=0.4,rely=0.25, relwidth=0.45, relheight=0.1)

    cancelBtn = Button(b,text="Cancel booking",bg='white',font='1', fg='black',command=cancel_fun)
    cancelBtn.place(relx=0.22,rely=0.45, relwidth=0.5,relheight=0.1)

def updation():
    user=e1.get()
    guest=e2.get()
    check_in=e3.get()
    check_out=e4.get()
    try:

        insert= "update book set guest =%s,checkin=%s,checkout=%s where user_id=%s"
        up=(guest,check_in,check_out,user)
        con.execute(insert,up)
        conn.commit()
        messagebox.showinfo('Success'," Bookings updated ! ")
        print("{}\n{}\n{}\n{}".format(user,guest,check_in,check_out))
        mess()
    except Exception as e:
        messagebox.showinfo('error'," Bookings not updated ! ")
    
def mess():
    a.destroy()
    
def update():
    global a,e1,e2,e3,e4
    a= Tk()
    a.title('Update Bookings')
    a.minsize(width=400,height=400)
    a.geometry('850x750')

    Canvas1 = Canvas(a)    
    Canvas1.config(bg="#B39DDC")
    Canvas1.pack(expand=True,fill=BOTH)

    l0=Label(a,text="Updation",bg="white",fg="black",height="50",width="1000",font="bold")
    l0.place(relx=0.28,rely=0.1, relwidth=0.45, relheight=0.1)

    l1=Label(a,text="User ID",height="1",width="15",bg="white",fg="black",font=(1))
    l1.place(relx=0.2,rely=0.25, relwidth=0.2, relheight=0.06)
    e1=Entry(a,text="",font=(1))
    e1.place(relx=0.4,rely=0.25, relwidth=0.45, relheight=0.06)

    l2=Label(a,text="No of Guests",height="1",width="15",bg="white",fg="black",font=(1))
    l2.place(relx=0.2,rely=0.35, relwidth=0.2, relheight=0.06)
    e2=Entry(a,text="",font=(1))
    e2.place(relx=0.4,rely=0.35, relwidth=0.45, relheight=0.06)

    l3=Label(a,text="Check in",height="1",width="15",bg="white",fg="black",font=(1))
    l3.place(relx=0.2,rely=0.45, relwidth=0.2, relheight=0.06)
    e3=Entry(a,text="",font=(1))
    e3.place(relx=0.4,rely=0.45, relwidth=0.45, relheight=0.06)

    l4=Label(a,text="Check out",height="1",width="15",bg="white",fg="black",font=(1))
    l4.place(relx=0.2,rely=0.55, relwidth=0.2, relheight=0.06)
    e4=Entry(a,text="",font=(1))
    e4.place(relx=0.4,rely=0.55, relwidth=0.45, relheight=0.06)

    SubmitBtn = Button(a,text="Update",bg='white', fg='black',command=updation)
    SubmitBtn.place(relx=0.3,rely=0.65, relwidth=0.18,relheight=0.08)

    cancelBtn = Button(a,text="Cancel booking",bg='white', fg='black',command=cancel)
    cancelBtn.place(relx=0.5,rely=0.65, relwidth=0.18,relheight=0.08)








    
