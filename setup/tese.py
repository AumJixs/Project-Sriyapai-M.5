import os
import cv2
import pickle
import face_recognition
import numpy as np
import cvzone

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
    print(path)

#Load the encoding file
print("Loading Encode File ....") 
file = open('EncodeFile.p','rb')
encodelistwithids = pickle.load(file)
file.close()
encodeListKnow  = encodelistwithids
studentid = encodelistwithids

print("Encode File Loaded")


def findEncodings(imageList):
    encodeList  = []
    for img in imageList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encoding(img)[0]
        encodeList.append(encode)

    return encodeList

while True:
    ret,frame = cap.read()
       
    imgS = cv2.resize(frame ,(0,0) ,None , 0.25 , 0.25 )
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    #Detect Faces from Image
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    # cv2.imshow("Webcam",imgS)


    imgbg[162:162+480 , 55:55+640] = frame
    imgbg[44:44+633 , 808:808+414] = imgModeList[3]

    for encodeFace, faceLoc in zip(encodeCurFrame , faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnow,encodeFace)
        FaceDis = face_recognition.face_distance(encodeListKnow,encodeFace)
        print("matches", matches)
        print("FaceDis", FaceDis)

        # matchindex = np.argmin(FaceDis)
        # print("Match Index", matchindex)

        # if matches[matchindex]:
        #         # print("Know Face Detected")
        #         # print(studentid[matchindex])
        #     y1, x2, y2, x1 = faceLoc
        #     y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        #     bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
        #     imgbg = cvzone.cornerRect(imgbg , bbox,rt =0)

    #cv2.imshow("Webcam",frame)
    cv2.imshow("Test",imgbg)
    if cv2.waitKey(1) &  0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()


        

