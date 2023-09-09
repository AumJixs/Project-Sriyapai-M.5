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

cred = credentials.Certificate(r"C:\Users\apichai\Desktop\File code By NongAumJixs\TestKruArm\Files\serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
    "databaseURL" :"https://databasestudentid-default-rtdb.firebaseio.com/",
    "storageBucket":"databasestudentid.appspot.com"
    }
)

bucket = storage.bucket()

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgbg = cv2.imread(r"C:\Users\apichai\Desktop\File code By NongAumJixs\TestKruArm\Files\Resources\background.png")
# cv2.imshow("TEST",imgbg)
folderModePath = "Resources/Modes"

#เจาะเข้าหาpathในfolderModepath
modepath = os.listdir(folderModePath)


imgModeList = []
imgStudent = []
modetype = 0
count = 0
id = -1

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
                    modeType = 1
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
            imgStudent = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555)

            # Update Score on Cloud
            ref = db.reference(f'Students/{id}')
            UpdateScore  =int(studentInfo['Score'])  
            UpdateScore += 1
            print(UpdateScore)
            ref.child('Score').set(UpdateScore)

            if 10<count<20:
                modeType = 2
            
            imgbg[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if count <=10:
                cv2.putText(imgbg, str(id), (1000, 100),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                cv2.putText(imgbg, str(studentInfo['Name']), (1000, 500),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgbg, str(studentInfo["Status"]), (1006, 493),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgbg, str(studentInfo['Score']), (910, 625),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgbg, str(studentInfo['Gender']), (1025, 625),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgbg, str(studentInfo['Class']), (1125, 625),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgbg, str(studentInfo['No']), (1125, 625),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                
                (w, h), _ = cv2.getTextSize(studentInfo['Name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                offset = (414 - w) // 2
                cv2.putText(imgbg, str(studentInfo['Name']), (808 + offset, 445),
                                    cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)
                
                imgbg[175:175 + 216, 909:909 + 216]  = imgStudent

                count+=1

        if count >= 20:
            count = 0
            modeType = 0
            studentInfo = []
            imgStudent = []
            imgbg[44:44 + 633, 808:808 + 414] = imgModeList[modeType]


    #cv2.imshow("Webcam",frame)
    cv2.imshow("Test",imgbg)
    if cv2.waitKey(1) &  0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()


        

