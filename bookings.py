from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

#connecting data base
conn = pymysql.connect(host="localhost",user="root",password="Admin@123",database="hotel_management")
con= conn.cursor()
def bookings():
    a= Tk()
    a.title('Bookings')
    a.minsize(width=400,height=400)
    a.geometry('850x750')

    Canvas1 = Canvas(a)    
    Canvas1.config(bg="#FFEFD9")
    Canvas1.pack(expand=True,fill=BOTH)

    l0=Label(a,text="Bookings",bg="white",fg="black",height="50",width="1000",font="bold")
    l0.place(relx=0.26,rely=0.1, relwidth=0.45, relheight=0.1)

    labelFrame = Frame(a,bg='white')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-13s%-15s%-17s%-13s"%('User','Type','Check in','Check out','Status'),bg='white',fg='black',font=1).place(relx=0.07,rely=0.1)
    Label(labelFrame, text="-----------------------------------------------------------------------------------------------------------------------------",bg='white',fg='black').place(relx=0.05,rely=0.2)

    table ="select user_id,room,checkin,checkout,status from book  "
    try:
        con.execute(table)
        conn.commit()
        
        for i in con:
            Label(labelFrame, text="%-10s%-18s%-19s%-18s%-13s"%(i[0],i[1],i[2],i[3],i[4]),bg='white',fg='black',font=1).place(relx=0.07,rely=y)
            y += 0.1
    except Exception as e:
        messagebox.showinfo("Failed to fetch files from database")
        print(e)


    quitBtn = Button(a,text="Quit",bg='#f7f1e3', fg='black', command=a.destroy)
    quitBtn.place(relx=0.4,rely=0.85, relwidth=0.18,relheight=0.08)
    

 

    

    

    
