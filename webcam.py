from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
from tkinter import messagebox

class Webcam():
   def __init__(self, root):
      self.root = root
      self.root.title("Webcam Application")
      self.root.geometry("800x600+300+100")



      

      # OpenCv Variables
      self.video_capture = cv2.VideoCapture(0)
      self.curremt_image = None

      # create webcam feed display
      self.canvas = Canvas(self.root, width=640, height=480)
      self.canvas.pack()

      self.download_btn = Button(self.root, text="Download", command=self.download_image)
      self.download_btn.pack()
      self.download_btn = Button(self.root, text="open", command=self.face_cropped)
      self.download_btn.pack()

      # start the web
      self.update_webcam()
   
   def update_webcam(self):
      ret, frame = self.video_capture.read()
      if ret:
         self.curremt_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
         self.photo = ImageTk.PhotoImage(image=self.curremt_image)
         self.canvas.create_image(0,0, image=self.photo, anchor=NW)
         self.root.after(15, self.update_webcam)



   def download_image(self):
         if self.curremt_image is not None:
            file_path = os.path.expanduser("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/pic/flivo.png")
            self.curremt_image.save(file_path)
            os.startfile(file_path)



   def face_cropped(img):
         # Convert to grayscale
         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         faces = face_classifier.detectMultiScale(gray, 1.3, 5)
         
         cropped_faces = []
         for (x, y, w, h) in faces:
            face_cropped = img[y:y+h, x:x+w]
            cropped_faces.append(face_cropped)
         
         return cropped_faces

         face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

         cap = cv2.VideoCapture(0)  # Use 0 for default camera, or 1 for external camera
         img_id = 0

         while True:
            ret, my_frame = cap.read()
            faces = face_cropped(my_frame)
            
            for face in faces:
               img_id += 1
               face = cv2.resize(face, (450, 450))
               face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
               file_path = f"data/student.{img_id}.jpg"  # Use f-strings for string formatting
               cv2.imwrite(file_path, face)
               cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
               cv2.imshow("Capture Images", face)

            if cv2.waitKey(1) & 0xFF == 27 or img_id == 100:  # Exit on 'Esc' key or after capturing 100 images
               break

         cap.release()
         cv2.destroyAllWindows()
         messagebox.showinfo("Result", "Generating dataset completed!")





if __name__ == "__main__":
   root = Tk()
   app = Webcam(root)
   root.mainloop()