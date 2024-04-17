from tkinter import *
from customtkinter import*
import cv2
import os
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox


class Train():
   def __init__(self, root):
      self.root = root
      self.root.title("Face recognisation Systesm")
      self.root.geometry("1366x768+0+0")

      img=Image.open("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/Images/class 2.jpeg")
      img=img.resize((1366,130))
      self.photoimg=ImageTk.PhotoImage(img)
      # This part is image labels setting start 
      # first header image  
      img=Image.open("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/Images/class 2.jpeg")
      img=img.resize((1366,130))
      self.photoimg=ImageTk.PhotoImage(img)

      # set image as lable
      f_lb1 = Label(self.root,image=self.photoimg)
      f_lb1.place(x=0,y=0,width=1366,height=130)



      #title section
      title_lb1 = Label(text="Welcome to Training Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
      title_lb1.place(x=0,y=0,width=1366,height=45)

      # Create buttons below the section 
      # ------------------------------------------------------------------------------------------------------------------- 
      # Training button 1
      std_img_btn=Image.open("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/Images/class 2.jpeg")
      std_img_btn=std_img_btn.resize((180,180))
      self.std_img1=ImageTk.PhotoImage(std_img_btn)

      std_b1 = Button(command=self.train_classifier,image=self.std_img1,cursor="hand2")
      std_b1.place(x=600,y=170,width=180,height=180)

      std_b1_1 = Button(command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
      std_b1_1.place(x=600,y=350,width=180,height=45)



   def train_classifier(self):
      data_dir = "data"
      
      faces = []
      ids = []

      for root, dirs, files in os.walk(data_dir):
         for file in files:
               if file.endswith(".jpg"):  # Assuming the images are in JPEG format
                  image_path = os.path.join(root, file)
                  student_name = os.path.basename(root)  # Use student names as labels
                   
                  img = Image.open(image_path).convert('L')  # Convert to grayscale
                  imageNp = np.array(img, 'uint8')
                  
                  faces.append(imageNp)
                  ids.append(student_name)
                  cv2.imshow("Training",imageNp)
                  cv2.waitKey(1)==13


      # Convert the labels to the correct data type
      ids = np.arange(len(ids), dtype=np.int32)

      # Train the Classifier
      clf = cv2.face_LBPHFaceRecognizer.create()
      clf.train(faces, ids)
      clf.save("classifier.xml")

      # Close the camera window
      #cv2.destroyAllWindows()

      # Show a message that records are saved successfully
      messagebox.showinfo("Result", "Training and records saved successfully!")

   # Call the function to train the classifier and display the message
   #train_classifier(None)  # Replace 'None' with the appropriate parent window if needed






if __name__ == "__main__":
   root = Tk()
   obj = Train(root)
   root.mainloop()