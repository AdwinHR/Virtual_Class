from tkinter import *
from tkinter import ttk
import pymysql
import os
import cv2


from tkinter import messagebox
from PIL import ImageTk, Image

from tkinter import filedialog



class Register:

    def __init__(self,root):

        self.root = root
        self.root.title("Login")
        self.root.geometry("500x500+0+0")
#        self.root.resizable(0,0)

        
 #       (self.root).iconbitmap("logofinal.jpeg")

        self.username = StringVar()
        self.usn = StringVar()

        

        title = Label(self.root,text="Login",bd = 5,relief=GROOVE,
        font=("Arial",30,"bold"),bg="#FFFCF9",fg="#0A090C")

        title.pack(side=TOP,fill=X)

                

        Main_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame.place(x=10,y=70,width=350,height=290)

        # username

        lbl_username = Label(Main_Frame,text="Username :-",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",10,"bold"))

        lbl_username.grid(row = 1,column=0,pady=45,padx=30,sticky="w")

    

        txt_username = Entry(Main_Frame,textvariable=self.username,width = 12,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)

        txt_username.grid(row = 1,column=1,pady=45,padx=5,sticky="w")

        #usn input

        lbl_usn = Label(Main_Frame,text="Usn :-",bg="#F0EDEE",fg="#0A090C",
        font=("Arial",10,"bold"))

        lbl_usn.grid(row = 2,column=0,pady=45,padx=30,sticky="w")

    

        txt_usn = Entry(Main_Frame,textvariable=self.usn,width = 12,
        font=("Arial",15,"bold"),bd=5,relief=GROOVE)

        txt_usn.grid(row = 2,column=1,pady=45,padx=5,sticky="w")

        

        

        

        btn_frame = Frame(Main_Frame,bg="#F0EDEE")

        btn_frame.place(x=100,y=230,width=170)
        login_btn = Button(btn_frame,text="Login",width=20,relief=GROOVE,bg="#00A1E4", font=("Arial",10,"bold"),
                           command=self.validate_user).grid(row=0,column=0,padx=0,pady=10)

        

    def validate_user(self):

        if self.username.get() == "" or self.usn.get() == "":

            messagebox.showerror("Error","Fields Missing")

        else:

            
            print("called")

            haar_file="haarcascade_frontalface_default_lyst8241.xml"
            datasets="datasets"
            new_data=self.username.get()
            print(new_data)
            sub_data=new_data
            path=os.path.join(datasets,sub_data)
            if not os.path.isdir(path):
                os.mkdir(path)
            (width,height)=(130,100)

            face_cascade=cv2.CascadeClassifier(haar_file)

            webcam=cv2.VideoCapture(0)

            count=1
            while count<31:
                print(count)
                (_,im)=webcam.read()
                gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
                faces=face_cascade.detectMultiScale(gray,1.3,4)
                for (x,y,w,h) in faces:
                    cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                    face=gray[y:y+h,x:x+w]
                    face_resize=cv2.resize(face,(width,height))
                    cv2.imwrite("%s/%s.png"%(path,count),face_resize)
                            
                count=count+1
                cv2.imshow("OpenCV",im)
                key=cv2.waitKey(10)
                if key==27:
                    break;
            webcam.release()
            cv2.destroyAllWindows()

            self.root.destroy()
            st_root=Tk()
            st=Atten_interface(st_root)
                




            
              
























class Atten_interface:

    def __init__(self,root):

        self.root = root
        self.root.title("Signin")
        self.root.geometry("1350x700+0+0")
#        self.root.resizable(0,0)

    
        title = Label(self.root,text="Login",bd = 10,relief=GROOVE,
        font=("Times New Roman",30,"bold"),bg="#FFFCF9",fg="#0A090C")

        title.pack(side=TOP,fill=X)

                

        Main_Frame = Frame(self.root,bd=10,relief=RIDGE,bg="#F0EDEE")
        Main_Frame.place(x=50,y=100,width=200,height=100)

        btn_frame = Frame(Main_Frame,bg="#F0EDEE")

        btn_frame.place(x=100,y=200,width=170)
        login_btn = Button(Main_Frame,text="Take_Attendance",width=20,height=3, relief=GROOVE,bg="#00A1E4",
                           font=("Arial",10,"bold"),command=self.Take_Attendance).grid(row=0,column=0,padx=0,pady=10)



        Main_Frame = Frame(self.root,bd=10,relief=RIDGE,bg="#F0EDEE")
        Main_Frame.place(x=50,y=400,width=200,height=100)

        btn_frame = Frame(Main_Frame,bg="#F0EDEE")

        btn_frame.place(x=100,y=200,width=170)
        login_btn = Button(Main_Frame,text="Add_new_details",width=20,height=3, relief=GROOVE,bg="#00A1E4",
                           font=("Arial",10,"bold"),command=self.Add_new_details).grid(row=0,column=0,padx=0,pady=10)




       



        


        
                            
            
                
            


    def Add_new_details(self):
        
        self.root.destroy()
        st_root=Tk()
        st=Register(st_root)


        



        
            
        
        
            


    def Take_Attendance(self):

        
        import cv2,os,numpy,pandas
        haar_file="haarcascade_frontalface_default_lyst8241.xml"
        datasets="datasets"
        (images,labels,names,id)=([],[],{},0)
        face_cascade=cv2.CascadeClassifier(haar_file)

        from tkinter import messagebox
        from PIL import ImageTk, Image

        from tkinter import filedialog
        for (subdirs,dirs,files) in os.walk(datasets):
            for subdir in dirs:
                names[id]=subdir
                subjectpath=os.path.join(datasets,subdir)
                for filename in os.listdir(subjectpath):
                    path=subjectpath+"/"+filename
                    label=id
                    images.append(cv2.imread(path,0))
                    labels.append(int(label))
                id=id+1
        (width,height)=(130,100)

        (images,labels)=[numpy.array(lis) for lis in [images,labels]]
        #print(images,labels)
        model=cv2.face.LBPHFaceRecognizer_create()

        model.train(images,labels)
        #print("compleated")

        filename = filedialog.askopenfilename(initialdir = "/",
                                                          title = "Select a File",
                                                          filetypes = (("Text files",
                                                                        "*.jpg*"),
                                                                       ("all files",
                                                                        "*.*")))


        a=[]
        count=0
        filename=""+str(filename)+""
        im=cv2.imread(filename)
        #print("'"+str(filename)+"'")
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,4)
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
            face=gray[y:y+h,x:x+w]
            face_resize=cv2.resize(face,(width,height))

            prediction=model.predict(face_resize)
            cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,255),3)
            if prediction[1]<800:
                cv2.putText(im,"%s-%.0f"% (names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
                #print(names[prediction[0]])
                a.append(names[prediction[0]])
                count=0
            else:
                count=count+1
                cv2.putText(im,"unknown",(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
                if count>100:
                    #print("absent")
                    cv2.imwrite("input.jpg",im)
                    count=0
        cv2.imshow("gfgfhgxa",im)
            
        #print(a)

        Main_Frame2 = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame2.place(x=700,y=70,width=450,height=190)
        s1="Present students are \n" +"\n".join(a)
        message =s1

        text_box = Text(
            Main_Frame2,
            height=13,
            width=40,
            wrap='word'
        )
        text_box.pack(expand=True)
        text_box.insert('end', message)


        Main_Frame3 = Frame(self.root,bd=4,relief=RIDGE,bg="#F0EDEE")
        Main_Frame3.place(x=700,y=570,width=450,height=190)

        s2="Present students are \n" +"\n".join(a)
        message2 =s2

        text_box = Text(
            Main_Frame3,
            height=13,
            width=40,
            wrap='word'
        )
        text_box.pack(expand=True)
        text_box.insert('end', message2)

        


            

              

             

