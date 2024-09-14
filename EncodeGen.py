import face_recognition
import cv2
import os
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://attendanceautomation-758b2-default-rtdb.firebaseio.com/",
    'storageBucket': "attendanceautomation-758b2.appspot.com"
})


folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])
    
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        
    return encodeList
print("Encoding started: ")
encodeListKnown = findEncodings(imgList)
encodeListKnownIds = [encodeListKnown,studentIds]

print("Encoding Complete")

file = open("EncodeFile.p",'wb')
pickle.dump(encodeListKnownIds,file)
file.close()
print("File Saved")