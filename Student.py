from tkinter import *
from tkinter import ttk
import pymysql
from Student import *
from tkinter import messagebox
from Atten_interface import *
class Student:

    def __init__(self,root):

        self.root = root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
#        self.root.resizable(0,0)

        
 #       (self.root).iconbitmap("logofinal.jpeg")

        
        self.username = StringVar()
        self.password = StringVar()

        

        title = Label(self.root,text="Login",bd = 5,relief=GROOVE,
        font=("Arial",30,"bold"),bg="#FFFCF9",fg="#0A090C")

        title.pack(side=TOP,fill=X)

        #main frame

        Main_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame.place(x=70,y=100,width=350,height=290)

        

        lbl_username = Label(Main_Frame,text="Attendance",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold"))

        lbl_username.grid(row = 1,column=0,pady=45,padx=30,sticky="w")

    

        

        

        btn_frame = Frame(Main_Frame,bg="#F0EDEE")

        btn_frame.place(x=100,y=200,width=170)

        

        login_btn = Button(btn_frame,text="Attendance",width=20,relief=GROOVE,bg="#00A1E4",
        font=("Arial",10,"bold"),command=self.Attendance).grid(row=0,column=0,padx=0,pady=10)


 #       mainframe1
        Main_Frame1 = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame1.place(x=550,y=100,width=350,height=290)

        

        lbl_username = Label(Main_Frame1,text="virtual board",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold"))

        lbl_username.grid(row = 1,column=0,pady=45,padx=30,sticky="w")


        btn_frame = Frame(Main_Frame1,bg="#F0EDEE")

        btn_frame.place(x=100,y=200,width=170)

        

        login_btn = Button(btn_frame,text="Login",width=20,relief=GROOVE,bg="#00A1E4",
        font=("Arial",10,"bold"),command=self.virtual).grid(row=0,column=0,padx=0,pady=10)

 #       mainframe2
        Main_Frame2 = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame2.place(x=900,y=100,width=350,height=290)

        

        lbl_username = Label(Main_Frame2,text="computr",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",30,"bold"))

        lbl_username.grid(row = 1,column=0,pady=45,padx=30,sticky="w")

    
        btn_frame = Frame(Main_Frame2,bg="#F0EDEE")

        btn_frame.place(x=100,y=200,width=170)

        

        login_btn = Button(btn_frame,text="Login",width=20,relief=GROOVE,bg="#00A1E4",
        font=("Arial",10,"bold"),command=self.manage).grid(row=0,column=0,padx=0,pady=10)

    def Attendance(self):
        self.root.destroy()
        st_root=Tk()
        st=Atten_interface(st_root)


    

    def virtual(self):

        pass

    def manage(self):

        pass














