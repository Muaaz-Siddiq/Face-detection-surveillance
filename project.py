import cv2
import numpy as np
import os
import face_recognition as fr

# In this file we train the model and then use it.
# locating the folders with image and appending it in list.
# place training pictures in image folder with id as the image name.

path = "images"
images = []
image_name = []
image_list = os.listdir(path)
for img in image_list:
    current_image = cv2.imread(f'{path}/{img}')
    images.append(current_image)
    image_name.append(os.path.splitext(img)[0])

# Training
def findEncoding(images):
    encodelist =[]
    for imag in images:
        imag  = cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(imag)[0]
        encodelist.append(encode)
    return encodelist


encodeList_known = findEncoding(images)
print("encoding complete")

# starting webcam
def Start():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        success, imag = cap.read()
        imagS = cv2.resize(imag,(0,0),None,0.25,0.25)
        imagS = cv2.cvtColor(imagS, cv2.COLOR_BGR2RGB)  # Resizing and changing colors for more accurate results

        facesCurFrame = fr.face_locations(imagS)  # matching webcame and data image by measurements
        encodeCurFrame = fr.face_encodings(imagS,facesCurFrame)

        for encodeFace,faceLoc in zip(encodeCurFrame,facesCurFrame):
            matches = fr.compare_faces(encodeList_known,encodeFace)  # compare face attributes
            faceDist = fr.face_distance(encodeList_known,encodeFace)  # compare face measurements
            #print(faceDist)
            matchIndex = np.argmin(faceDist)

            if matches[matchIndex]:  # check matching conditions
                name = image_name[matchIndex].lower()

                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(imag,(x1,y1),(x2,y2),(0,0,255),2)
                cv2.rectangle(imag,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                #cv2.putText(imag,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            if not matches[matchIndex]:
                name = "No s_id"

                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(imag,(x1,y1),(x2,y2),(0,0,255),2)
                cv2.rectangle(imag,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                cv2.putText(imag,"unidentified person",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

        cv2.imshow("Webcam", imag)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    global s_id
    s_id = name
    #print("s_id = ", s_id)
