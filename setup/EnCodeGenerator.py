import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred , {
    "databaseURL" :"https://databasestudentid-default-rtdb.firebaseio.com/",
    "storageBucket":"databasestudentid.appspot.com"
    }
)

#import student image
folderpath = "stdphoto"
pathList = os.listdir(folderpath)
print(pathList)
foldername = "stdphoto"

imgList= []
studentid = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderpath , path)))
    #print(path)

    #แยกชื่อไฟล์ กับ สกุลไฟล์
    studentid.append(os.path.splitext(path)[0])
    #print(os.path.splitext(path)) 

    #อัพรูปขึ้น firebase
    fileName = f'{folderpath}/{path} '
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


print(studentid)

def findEncodings(imageList):
    encodeList  = []
    for img in imageList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...!")
encodeListKnow = findEncodings(imgList)
encodeListKnowwithids = [encodeListKnow , studentid]
print("Encoding Complete") 

file = open("EncodeFile.p","wb")
pickle.dump(encodeListKnowwithids,file)
file.close()
print("File Save")