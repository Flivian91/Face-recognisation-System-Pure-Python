import cv2
import os
from tkinter import messagebox

name = input("What Your name: ")
print(name)

def face_cropped(img):
   gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
   faces = face_classifier.detectMultiScale(gray, 1.3, 5)

   cropped_faces = []
   for (x,y,w,h) in faces:
      face_cropped = img[y:y+h, x:x+w]
      cropped_faces.append(face_cropped)
   return cropped_faces
face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
img_id = 0
while True:
   ret, frame = cap.read()
   faces = face_cropped(frame)
   for face in faces:
      img_id +=1
      face = cv2.resize(face, (450,450))
      face = cv2.cvtColor(face, cv2.COLOR_RGB2GRAY)
      folder_name = f"C:/Users/FLIVO/Documents/name{name}"
      os.makedirs(folder_name, exist_ok=True)
      file_path = os.path.join(folder_name, f"{name}_{img_id}.jpg")
      cv2.imwrite(file_path, face)
      cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255,0), 2)
      cv2.imshow("capture Face", face)

   if cv2.waitKey(1) & 0xFF == 13 or img_id ==100:
        break
cap.release()
cv2.destroyAllWindows()
messagebox.showinfo(title="Success", message="Dataset generated successfully!!")

