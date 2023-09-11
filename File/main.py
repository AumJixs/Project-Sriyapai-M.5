import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
# from gpiozero import AngularServo
from time import sleep
import subprocess 
import torch
from ultralytics import YOLO
import math


cred = credentials.Certificate(r"C:\Users\apichai\Desktop\File code By NongAumJixs\TestKruArm\Files\serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
    "databaseURL" :"https://databasestudentid-default-rtdb.firebaseio.com/",
    "storageBucket":"databasestudentid.appspot.com"
    }
)

bucket = storage.bucket()

model = YOLO(r"C:\Users\apichai\Desktop\File code By NongAumJixs\TestKruArm\yolov8\runs\detect\train\weights\best.pt")

names = ["black_plastic_bag" , "bottle","foam","plastic_bag"]

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgbg = cv2.imread(r"C:\Users\apichai\Desktop\File code By NongAumJixs\TestKruArm\Files\Resources\background.png")
# cv2.imshow("TEST",imgbg)
folderModePath = "Resources/Modes"

#เจาะเข้าหาpathในfolderModepath
modepath = os.listdir(folderModePath)

# servo_1 =AngularServo(18, min_angle=0, max_angle=270, min_pulse_width=0.0005, max_pulse_width=0.0025)


imgModeList = []
imgstudent = []
modetype = 0
count = 0
countbin = 0
id = -1
part = 0


for path in modepath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath ,path)))
    print(path)

#Load the encoding file
print("Loading Encode File ....") 
file = open('EncodeFile.p','rb')
encodelistwithids = pickle.load(file)
file.close()
encodeListKnow ,studentid  = encodelistwithids
 
print("Encode File Loaded")


while True:
    ret,frame = cap.read()
    
    frame = cv2.flip(frame,1)

    imgS = cv2.resize(frame ,(0,0) ,None , 0.25 , 0.25 )
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    #Detect Faces from Image
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # cv2.imshow("Webcam",imgS)

    imgbg[162:162+480 , 55:55+640] = frame
    imgbg[44:44+633 , 808:808+414] = imgModeList[modetype]

    
    for encodeFace, faceLoc in zip(encodeCurFrame , faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
        FaceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
        print("matches", matches)
        print("FaceDis", FaceDis)

        matchindex = np.argmin(FaceDis)
        # print("Match Index", matchindex)

        if matches[matchindex]:
        #     # print("Know Face Detected")
        #     # print(studentid[matchindex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgbg = cvzone.cornerRect(imgbg , bbox,rt =0)
            id = studentid[matchindex]
            if count ==0 :
                    # cvzone.putTextRect(imgbg, "Loading", (275, 400))
                    # cv2.imshow("Face Attendance", imgbg)
                    # cv2.waitKey(1)
                    count = 1
                    modetype = 1
    if count != 0:

        if count ==1:
            array = []
            # Get the Data
            studentInfo = db.reference(f'Students/{id}').get()
            print(studentInfo)
            # Get the Image from the storage
            Blob = bucket.get_blob(f"Images/{id}.jpg")
            print(Blob)
            arr = np.frombuffer(Blob.download_as_string(),np.uint8)
            imgstudent = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)


            #Update imgbginfo to imgbgmarked
            if modetype != 3:

                if 10 < count < 20:
                    modetype = 2
            
            imgbg[44:44 + 633, 808:808 + 414] = imgModeList[modetype]

            if count <= 10 :
                print("starts")
                cv2.putText(imgbg, str(id), (860 , 95),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(imgbg, str(studentInfo['Name']), (955, 405),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgbg, str(studentInfo["Status"]), (990, 452),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                cv2.putText(imgbg, str(studentInfo['Score']), (1015, 505),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
                cv2.putText(imgbg, str(studentInfo['Gender']), (1100, 595),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 196, 54), 1)
                cv2.putText(imgbg, str(studentInfo['Class']), (930, 595),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 196, 54), 1)

                
                imgbg[140:140 + 225, 930:930 + 169]  = imgstudent
                print("finish")

                if part == 0 :
                    results = model(imgbg, stream=True)
                    for r in results:
                        boxes = r.boxes
                        for box in boxes:
                            # Bounding Box
                            x1, y1, x2, y2 = box.xyxy[0]
                            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
                            w, h = x2 - x1, y2 - y1
                            # cvzone.cornerRect(img, (x1, y1, w, h))
                            
                            # Confidence
                            conf = math.ceil((box.conf[0] * 100)) / 100
                            # Class Name
                            cls = int(box.cls[0])
                            currentClass = names[cls]
                            print(currentClass)
                            if conf>0.65:
                                #----Example----#
                                # if currentClass =='NO-Hardhat' or currentClass =='NO-Safety Vest' or currentClass == "NO-Mask":
                                #     myColor = (0, 0,255)
                                # elif currentClass =='Hardhat' or currentClass =='Safety Vest' or currentClass == "Mask":
                                #     myColor =(0,255,0)
                                # else:
                                #     myColor = (255, 0, 0)
                                if currentClass == "black_plastic_bag" :
                                    print("black_plastic_bag")
                                    myColor = (0, 0,0)
                                if currentClass == "bottle" :
                                    print("bottle")
                                    myColor = (13, 18, 130)
                                if currentClass == "foam" :
                                    print("foam")
                                    myColor = (238, 237, 237)
                                if currentClass == "plastic_bag" :
                                    print("plastic_bag")
                                    myColor = (240, 222, 54)
                                cvzone.putTextRect(imgbg, f'{names[cls]} {conf}',
                                                (max(0, x1), max(35, y1)), scale=1, thickness=1,colorB=myColor,
                                                colorT=(255,255,255),colorR=myColor, offset=5)
                                cv2.rectangle(imgbg, (x1, y1), (x2, y2), myColor, 3)
                # count+=1
                    # # Update Score on Cloud
                    # ref = db.reference(f'Students/{id}')
                    # UpdateScore  =int(studentInfo['Score'])  
                    # UpdateScore += 1
                    # print(UpdateScore)
                    # ref.child('Score').set(UpdateScore)
        
                count += 1

        if count >= 20:
            count = 0
            modetype = 0
            studentInfo = []
            imgstudent = []
            imgbg[44:44 + 633, 808:808 + 414] = imgModeList[modetype]

        else :
            modetype = 0
            count = 0

    #cv2.imshow("Webcam",frame)
    cv2.imshow("Test",imgbg)
    if cv2.waitKey(1) &  0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()


        

