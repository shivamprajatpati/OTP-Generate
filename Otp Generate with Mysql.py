from tkinter import*
import pymysql
import random
frame=Tk()
frame.geometry('600x600')
frame.configure(background= "darkcyan")
frame.title("Otp Generate")

def ot():
    na=en1.get()
    conn=pymysql.Connection(user="root",password="",host="localhost",port=3306,database="avi")
    cursor=conn.cursor()
    cursor.execute("insert into ot(otp) values(%s)",(na))
    conn.commit()
    sb.set("Submit")
    

def generate():
    st="abcdef12345"
    otp=""
    for i in range(5):
        otp+=random.choice(st)
    nn.set(otp)
    
    
    
nn=StringVar()
sb=StringVar()

name=Label(text="OTP")
name.place(x=30,y=50)

en1=Entry(textvariable=nn)
en1.place(x=90,y=50)

submit=Label(textvariable=sb)
submit.place(x=50,y=250)

name2=Button(text="Generate OTP",command=generate)
name2.place(x=80,y=100)


name3=Button(text="Save",command=ot)
name3.place(x=80,y=150)



