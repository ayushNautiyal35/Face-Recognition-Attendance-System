from tkinter import *
from PIL import Image
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
from pathlib import Path
import csv
#function for the arrival time
def hd():
    cap = cv2.VideoCapture(0)
    known_face_encoding=[]
    path = 'C:/Users/ayush nautiyal/Documents/fce_recognition/facerecog.py/photos/'
    myList = os.listdir(path)
    for cl in myList:
        image=face_recognition.load_image_file(path+cl)
        image_encoding=face_recognition.face_encodings(image)[0]
        known_face_encoding.append(image_encoding)
    known_faces_names=['ayush','tata']
    students=known_faces_names.copy() 
    face_locations=[]
    face_encodings=[]
    face_names=[]
    s=True
    def markAttendance(name):
        with open('C:/Users/ayush nautiyal\Documents/fce_recognition/Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
              now = datetime.now()
              dtString = now.strftime('%H:%M:%S')
              f.writelines(f'\n{name},{dtString}')
              f.close() 
    while True:
        _,frame= cap.read()
        small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame=small_frame[:,:,::-1]
        if s:
            face_locations=face_recognition.face_locations(rgb_small_frame)
            face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_names=[]
            for face_encoding in face_encodings:
                matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
                name=''
                face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
                best_match_index=np.argmin(face_distance)
                if matches[best_match_index]:
                    name=known_faces_names[best_match_index]
                    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
                    facesCurFrame = face_recognition.face_locations(small_frame)
                    for faceloc in facesCurFrame:
                        y1, x2, y2, x1 = faceloc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                
                    markAttendance(name)
                else:
                    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
                    facesCurFrame = face_recognition.face_locations(small_frame)
                    for faceloc in facesCurFrame:
                        y1, x2, y2, x1 = faceloc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0, 255, 255), cv2.FILLED)
                        cv2.putText(frame, 'Unknown', (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.waitKey(10)
        cv2.imshow("attendance",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 
    


#function for departure time
def cd():
    cap = cv2.VideoCapture(0)
    known_face_encoding=[]
    path = 'C:/Users/ayush nautiyal/Documents/fce_recognition/facerecog.py/photos/'
    myList = os.listdir(path)
    for cl in myList:
        image=face_recognition.load_image_file(path+cl)
        image_encoding=face_recognition.face_encodings(image)[0]
        known_face_encoding.append(image_encoding)
    known_faces_names=['ayush','tata']
    students=known_faces_names.copy() 
    face_locations=[]
    face_encodings=[]
    face_names=[]
    s=True
    def markAttendance(name):
        with open('C:/Users/ayush nautiyal/Documents/fce_recognition/Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name  in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(dtString)
                f.close() 
                cv2.waitKey(10)
                cv2.destroyAllWindows() 
                   
            else:
                messagebox.showinfo("Error",'No entry at arrival time')


    while True:
        _,frame= cap.read()
        small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        rgb_small_frame=small_frame[:,:,::-1]
        if s:
            face_locations=face_recognition.face_locations(rgb_small_frame)
            face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_names=[]
            for face_encoding in face_encodings:
                matches=face_recognition.compare_faces(known_face_encoding,face_encoding)
                name=''
                face_distance=face_recognition.face_distance(known_face_encoding,face_encoding)
                best_match_index=np.argmin(face_distance)
                if matches[best_match_index]:
                    name=known_faces_names[best_match_index]
                    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
                    facesCurFrame = face_recognition.face_locations(small_frame)
                    for faceloc in facesCurFrame:
                        y1, x2, y2, x1 = faceloc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                
                    markAttendance(name)
                else:
                    small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
                    facesCurFrame = face_recognition.face_locations(small_frame)
                    for faceloc in facesCurFrame:
                        y1, x2, y2, x1 = faceloc
                        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                        cv2.rectangle(frame, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                        cv2.putText(frame, 'Unknown', (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                cv2.waitKey(10)
        cv2.imshow("attendance",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 
    
 #function for data entry
def co():
    filename=filedialog.askopenfilename(initialdir="C:/Users/ayush nautiyal/Pictures",title="Select a file",filetypes=(("jpeg flies","*.jpg"),("all files","*.")))
    img = Image.open(filename)
    img.save('C:/Users/ayush nautiyal/Documents/fce_recognition/facerecog.py/photos/'+Path(filename).stem+'.jpg')    

#main function for the code
root=Tk()
root.title('Face Recognition Attendance System- By Ayush Nautiyal')
#root.iconbitmap("favicon.ico")
root.geometry('400x400')

#for the color option wher bg for background,fg for fore ground, active background and foreground when mouse is placed on it
def callfunc(name,index,mode):
    if(clicked.get()=='Arrival Entry'):
        drop.config(bg='black',fg='red',activebackground="white",activeforeground='blue')
    if(clicked.get()=='Departure Entry'):
        drop.config(bg='black',fg='white',activebackground="white",activeforeground='blue')
    if(clicked.get()=='Upload Data'):
        drop.config(bg='black',fg='yellow',activebackground="white",activeforeground='blue')
   

#for function show which get the value in the dropbox we select

def show():
    if(clicked.get()=='Select'):
        messagebox.showinfo("Error",'Please select any value')
    if(clicked.get()=='Arrival Entry'):
        hd()
    if(clicked.get()=='Departure Entry'):
        cd()
    if(clicked.get()=='Upload Data'):
        co()
 

    
        
#options we gonna show in the dropbox         
options={
    "Arrival Entry",
    "Departure Entry",
    "Upload Data"
}

# for adding images
my_img=ImageTk.PhotoImage(Image.open("C:/Users/ayush nautiyal/Documents/fce_recognition/download.jpg"))
img=Label(image=my_img).pack()

#for default value in the dropdown box
clicked=StringVar()
clicked.set("Select")

#for drop down menu
drop=OptionMenu(root,clicked,*options)
drop.pack()

#for changing the color in the dropdown menu
Call=clicked.trace_variable('w',callfunc)
mybutton=Button(root,text="Submit",command=show)
mybutton.configure(bg='grey',fg='black')
mybutton.pack()

#for exit button
button_exit= Button(root,text='Exit',command=root.destroy)
button_exit.configure(bg='red',fg='black')
button_exit.pack()

# for color 
root.configure(bg='white')

#the looop will run until exit not pressed
root.mainloop()