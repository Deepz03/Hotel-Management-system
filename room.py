from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
from bookings import *

#connecting data base
conn = pymysql.connect(host="localhost",user="root",password="Admin@123",database="hotel_management")
con= conn.cursor()

def king_room():
    global k,king
    k = Toplevel(a)
    k.title("King room availability")
    k.geometry("300x150")
    king = 2
    ki="king"
    con.execute("select room from book where room = %s",(ki))
    conn.commit()
    for i in con:
        if i[0] == "king":
            king=king-1
            
    Label(k, text="Availability is {} rooms".format(king),font=1,pady="20").pack()
    Button(k, text="OK", command=delete_k).pack()
    
def delete_k():
    k.destroy()

def queen_room():
    global q,queen
    q = Toplevel(a)
    q.title("queen room availability")
    q.geometry("300x150")
    queen = 2
    qi="queen"
    con.execute("select room from book where room = %s",(qi))
    conn.commit()
    for i in con:
        if i[0]=="queen":
            queen =queen-1
        
    Label(q, text="Availability is {} rooms".format(queen),font=1,pady="20").pack()
    Button(q, text="OK", pady="5",command=delete_q).pack()
def delete_q():
    q.destroy()

def budget_room():
    global bu,budget
    bu = Toplevel(a)
    bu.title("Budget room availability")
    bu.geometry("300x150")
    budget = 3
    bi="budget"
    con.execute("select room from book where room = %s",(bi))
    conn.commit()
    for i in con:
        if i[0]=="budget":
            budget =budget-1
       
    Label(bu, text="Availability is {} rooms".format(budget),font=1,pady="20").pack()

    Button(bu, text="OK", command=delete_bu).pack()
def delete_bu():
    bu.destroy()
    
def book_reg():
    global rooms,check_in,check_out,user,guest
    user=e1.get()
    guest=e2.get()
    check_in=e3.get()
    check_out=e4.get()
    rooms=e5.get()
    status= "booked"
    try:
        insert= "insert into book (user_id,guest,checkin,checkout,room,status) values('"+user+"','"+guest+"','"+check_in+"','"+check_out+"','"+rooms+"','"+status+"')"
        con.execute(insert)
        conn.commit()
        messagebox.showinfo('Success'," Bookings confirmed ! ")
        print("{}\n{}\n{}\n{}\n{}".format(user,guest,check_in,check_out,rooms))
        mess()

    except Exception as e:
        print(e)
        messagebox.showinfo('error'," Error/rooms are not booked ! ")
        mess()



def mess():
    b.destroy()
    a.destroy()
    
def register():
    global b,e1,e2,e3,e4,e5
    b=Tk()
    b.title('Bookings')
    b.minsize(width=400,height=400)
    b.geometry('850x750')

    Canvas1 = Canvas(b)    
    Canvas1.config(bg="#FFEE93")
    Canvas1.pack(expand=True,fill=BOTH)
    
    l1=Label(b,text=" Bookings: ",bg="white",fg="black",height="50",width="1000",font="bold")
    l1.place(relx=0.26,rely=0.1, relwidth=0.45, relheight=0.1)

    l1=Label(b,text="User ID",height="1",width="15",bg="white",fg="black",font=(1))
    l1.place(relx=0.2,rely=0.25, relwidth=0.2, relheight=0.06)
    e1=Entry(b,text="",font=(1))
    e1.place(relx=0.4,rely=0.25, relwidth=0.45, relheight=0.06)

    l2=Label(b,text="No of Guests",height="1",width="15",bg="white",fg="black",font=(1))
    l2.place(relx=0.2,rely=0.35, relwidth=0.2, relheight=0.06)
    e2=Entry(b,text="",font=(1))
    e2.place(relx=0.4,rely=0.35, relwidth=0.45, relheight=0.06)

    l3=Label(b,text="Check in",height="1",width="15",bg="white",fg="black",font=(1))
    l3.place(relx=0.2,rely=0.45, relwidth=0.2, relheight=0.06)
    e3=Entry(b,text="",font=(1))
    e3.place(relx=0.4,rely=0.45, relwidth=0.45, relheight=0.06)
    
    l4=Label(b,text="Check out",height="1",width="15",bg="white",fg="black",font=(1))
    l4.place(relx=0.2,rely=0.55, relwidth=0.2, relheight=0.06)
    e4=Entry(b,text="",font=(1))
    e4.place(relx=0.4,rely=0.55, relwidth=0.45, relheight=0.06)

    l5=Label(b,text="Room Type\nking=1 \nqueen=2 \nbudget =3",height="10",width="15",bg="white",fg="black",font=(1))
    l5.place(relx=0.2,rely=0.65, relwidth=0.2, relheight=0.15)
    e5=Entry(b,text="",font=(1))
    e5.place(relx=0.4,rely=0.65, relwidth=0.45, relheight=0.06)

    SubmitBtn = Button(b,text="SUBMIT",bg='white', fg='black',command=book_reg)
    SubmitBtn.place(relx=0.3,rely=0.85, relwidth=0.18,relheight=0.08)

    quitBtn = Button(b,text="Quit",bg='#d1ccc0', fg='black', command=des)
    quitBtn.place(relx=0.5,rely=0.85, relwidth=0.18,relheight=0.08)

def des():
    b.destroy()
    a.destroy()

def room_book():
    global a
    a= Tk()
    a.title('Room Availability')
    a.minsize(width=400,height=400)
    a.geometry('850x750')


    Canvas1 = Canvas(a)    
    Canvas1.config(bg="#808080")
    Canvas1.pack(expand=True,fill=BOTH)

    l0=Label(a,text="Room Availability",bg="white",fg="black",height="50",width="1000",font="bold")
    l0.place(relx=0.26,rely=0.1, relwidth=0.45, relheight=0.1)

    king= Button(a,text="KING ROOM \nBed: 1 Large double bed\n 200m2, Air conditioning, \nPrivate bathroom, heating, \nbalcony, Garden view, Free Wifi",font=1,bg="white",fg="black",command=king_room)
    king.place(relx=0.06,rely=0.25, relwidth=0.40, relheight=0.25)

    queen= Button(a,text="QUEEN ROOM \nBed: 1 Large double bed\n 100m2, Air conditioning, \nPrivate bathroom, heating, \nHall, Free Wifi",font=1,bg="white",fg="black",command=queen_room)
    queen.place(relx=0.5,rely=0.25, relwidth=0.40, relheight=0.25)

    budget= Button(a,text="BUDGET DOUBLE ROOM \nBed: 1 double bed \nPrivate bathroom\nFree Wifi",font=1,bg="white",fg="black",command=budget_room)
    budget.place(relx=0.26,rely=0.55, relwidth=0.40, relheight=0.25)

    book= Button(a,text="BOOK",font=1,bg="white",fg="black",command=register)
    book.place(relx=0.37,rely=0.85, relwidth=0.20, relheight=0.1)
