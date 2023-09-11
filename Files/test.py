import os
import cv2
import pickle
import face_recognition
import numpy as np
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
    "databaseURL" :"https://databasestudentid-default-rtdb.firebaseio.com/",
    "storageBucket":"gs://databasestudentid.appspot.com/"
    }
)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgbg = cv2.imread(r"C:\Users\apichai\Desktop\File code By NongAumJixs\TestKruArm\Files\Resources\background.png")
# cv2.imshow("TEST",imgbg)
folderModePath = "Resources/Modes"

#เจาะเข้าหาpathในfolderModepath
modepath = os.listdir(folderModePath)

imgModeList = []

for path in modepath:
    imgModeList.append(cv2.imread(os.path.join(folderModePath ,path)))
    

#Load the encoding file

#import student image
folderpath = r"C:\Users\apichai\Desktop\File code By NongAumJixs\TestKruArm\Files\Images"
pathList = os.listdir(folderpath)

imgList= []
studentid = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderpath , path)))
    #print(path)
    #แยกชื่อไฟล์ กับ สกุลไฟล์
    studentid.append(os.path.splitext(path)[0])
    #print(os.path.splitext(path)) 

    fileName = os.path.join(folderpath , path)
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_file(fileName)


def findEncodings(imageList):
    encodeList  = []
    for img in imageList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encoding(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...!")
encodeListKnow = findEncodings(imgList)
encodeListKnowwithids = [encodeListKnow , studentid]
print("Encoding Complete") 

file = open("TestKruArm\Files\EncodeFile.p","wb")
pickle.dump(encodeListKnowwithids,file)
file.close()
print("File Save")

while True:
    ret,frame = cap.read()
       
    imgS = cv2.resize(imgList ,(0,0) ,None , 0.25 , 0.25 )
    imgS = cv2.cvtColor(imgList,cv2.COLOR_BGR2RGB)

    #Detect Faces from Image
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # cv2.imshow("Webcam",imgS)


    imgbg[162:162+480 , 55:55+640] = frame
    imgbg[44:44+633 , 808:808+414] = imgModeList[3]

    if faceCurFrame:
        for encodeFace, faceLoc in zip(encodeCurFrame , faceCurFrame):
            matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
            FaceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
            print("matches", matches)
            print("FaceDis", FaceDis)

            matchindex = np.argmin(FaceDis)
            # print("Match Index", matchindex)

            if matches[matchindex]:
                # print("Know Face Detected")
                # print(studentid[matchindex])
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                imgbg = cvzone.cornerRect(imgbg , bbox,rt =0)


    #cv2.imshow("Webcam",frame)
    cv2.imshow("Test",imgbg)
    if cv2.waitKey(1) &  0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()


        

