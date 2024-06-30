from tkinter import *
from tkinter import messagebox
import pymysql
from login import *
from PIL import Image, ImageTk
from room import *
from bookings import *
from customer import *
from update import *
from feedback import *

#connecting data base
conn = pymysql.connect(host="localhost",user="root",password="Admin@123",database="hotel_management")
con= conn.cursor()
def main_func():
    #GUI frame
    a= Tk()
    a.title('Hotel Management')
    a.minsize(width=400,height=400)
    a.geometry('850x750')

    #background size adjustment
    same = True
    n=1

    #background image
    backg = Image.open("mainpic.jfif")
    [imageSizeWidth, imageSizeHeight]= backg.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n)

    backg= backg.resize((newImageSizeWidth,newImageSizeHeight),Image.LANCZOS)
    img= ImageTk.PhotoImage(backg)

    Canvas1 = Canvas(a)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    #textbox and buttons

    frame1= Frame(a,bg='orange',bd=5)
    frame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.26)

    header= Label(frame1,text= "Welcome to \n Heritage Resort Inn\n Varkala, Kerala",bg='black', fg='white', font=('Courier',15))
    header.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(a,text="User Details",bg='black', fg='white',command=customer)
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
        
    btn2 = Button(a,text="Room Availability",bg='black', fg='white',command=room_book)
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
        
    btn3 = Button(a,text="Bookings",bg='black', fg='white',command=bookings)
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        
    btn4 = Button(a,text="Updation /Cancelation",bg='black', fg='white',command=update)
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
        
    btn5 = Button(a,text="Feedback",bg='black', fg='white',command=feedback)
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

    a.mainloop()


