import cv2
import numpy as np
import firebase
import time

config = {
    'apiKey': "AIzaSyDYr4tMw5XPCh_NBltDqQ4DyuvsQEA6flI",
    'authDomain': "eons-2c748.firebaseapp.com",
    'databaseURL': "https://eons-2c748.firebaseio.com",
    'projectId': "eons-2c748",
    'storageBucket': "eons-2c748.appspot.com",
    
}



recog = cv2.face.LBPHFaceRecognizer_create()
recog.read('recognizer/trainningData.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceDetect = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
id=0

####font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX

first='absent'
second='absent'
allcount=0
count1=0
count2=0
timer=time.time()
while True:
    ret, img =cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imwrite('abc.jpg',gray[y:y+h,x:x+w])
        id, conf = recog.predict(gray[y:y+h,x:x+w])
        if id==1:
            id="Amir khan"
            first='present'
            count1=0
            
       
        elif id==2:
            id ='Ayushi  '
            second='present'
            count2=0
            
        count1 +=1
        count2 +=1
        if count1>30 and count2>30:
            first='absent'
            second='absent'
        if count1<30 and count2<30:
            first='present'
            second='present'
        if count1>30 and count2<30:
            first='absent'
            second='present'
        if count1<30 and count2>30:
            first='present'
            second='absent'
        if timer +10<time.time():    
            db.child('Attendance/M1').set(first)
            db.child('Attendance/M2').set(second)
            timer=time.time()
        allcount=0
##        cv2.putText(img, str(id),(x,y+h),font,255,1)
        cv2.putText(img,str(id),(x,y+h),font,0.55,(0,255,0),1)
    else:
        if allcount>50:
            allcount=60
        else:    
            allcount +=1
            
        if allcount==50:
            first='absent'
            second='absent'
            db.child('Attendance/M1').set(first)
            db.child('Attendance/M2').set(second)
        time.sleep(.01)
        
    cv2.imshow('Face',img) 
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



                         
