import cv2,os,numpy,pandas
haar_file="haarcascade_frontalface_default_lyst8241.xml"
datasets="datasets"
(images,labels,names,id)=([],[],{},0)
face_cascade=cv2.CascadeClassifier(haar_file)

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
print(images,labels)
model=cv2.face.LBPHFaceRecognizer_create()

model.train(images,labels)
print("compleated")



webcam=cv2.VideoCapture(0)
a=[]
count=0
while 1:
    (_,im)=webcam.read()
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
            print(names[prediction[0]])
            a.append(names[prediction[0]])
            count=0
        else:
            count=count+1
            cv2.putText(im,"unknown",(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0))
            if count>100:
                print("absent")
                cv2.imwrite("input.jpg",im)
                count=0
    cv2.imshow("gfgfhgxa",im)
    key=cv2.waitKey(10)
    if key==27:
        break
print(a)
webcam.release()
cv2.destroyAllWindows()
