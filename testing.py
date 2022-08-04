'''import cv2
import numpy as np
import os
import face_recognition as fr
import pymongo

# This file is just for testing purpose of project please ignore.


# Creating connection with database
database_connection = pymongo.MongoClient('mongodb://localhost:27017/')
mydb =database_connection['project_database']
get_data = mydb['project _data']

# locating the folders with image and appending it in list
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

                #print(name)
                y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(imag,(x1,y1),(x2,y2),(0,0,255),2)
                cv2.rectangle(imag,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
                cv2.putText(imag,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            if not matches[matchIndex]:
                name = "No s_id"
                names = name

                #print("match not found")
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
    print("s_id = ", s_id)
    # Searching in database by Secret id'''

'''def Get():
    s_id = 'a1'
    if s_id == "No s_id":
        print("Un-Identified person -->> no s_id for tracing")
    else:
        records = get_data.find({'s_id': s_id})
        nrec = []
        for i in records:
            #print(i['name'])
            nrec.append(i['name'])
            nrec.append(i['age'])
            name_lab1 = gui_overview.Label(gui_overview.root,text=nrec, bg='#4b3c4f', fg='white')
            name_lab1['font'] = gui_overview.myFont
            name_lab1.place(x=300, y=150)
            print(nrec)
    #print(f'Record Data:- {records}')'''

'''s_id = 'a1'
if s_id == "No s_id":
    print("Un-Identified person -->> no s_id for tracing")
else:
    records = get_data.find({'s_id': s_id})
    for i in records:
        #print(i['name'])
        nrec.append(i['name'])
        nrec.append(i['age'])
    #print(f'Record Data:- {records}')
print(nrec[0])'''

'''i = input("sid : ")
path = 'F:/py programs/Surveillance project/images/' + i + '.JPEG'
print(path)'''

# x = "bob"
# def foo():
#     x = "alice"
#     def bar(x):
#         x = "willis"
#         y = "morgan"
#         print(x)
#     bar(x)
# foo()


# True = False
# while True:
#     print(True)
#     break