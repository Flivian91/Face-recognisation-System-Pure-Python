from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import pyttsx3 as pyttsx3
import os



class Face_recognisation_system():
   def __init__(self, root):
      self.root = root
      self.root.title("Face Recognisation System")
      self.root.geometry("1530x790+0+0")

      self.engine = pyttsx3.init()
      self.voices = self.engine.getProperty("voices")
      self.engine.setProperty("voice", self.voices[1].id)

      # first header image

      img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student face.jpg")
      img = img.resize((500, 130))
      self.photoimg = ImageTk.PhotoImage(img)

      f_lbl = Label(self.root, image=self.photoimg)
      f_lbl.place(x=0, y=0, width=500, height=130)

      # second header image

      img1 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student in class.jpg")
      img1 = img1.resize((500, 130))
      self.photoimg1 = ImageTk.PhotoImage(img1)

      f_lbl = Label(self.root, image=self.photoimg1)
      f_lbl.place(x=500, y=0, width=500, height=130)

      # third header image

      img2 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student 2.jpg")
      img2 = img2.resize((500, 130))
      self.photoimg2 = ImageTk.PhotoImage(img2)

      f_lbl = Label(self.root, image=self.photoimg2)
      f_lbl.place(x=900, y=0, width=500, height=130)

      # background image

      img3 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\bg.jpg")
      img3 = img3.resize((1530, 710))
      self.photoimg3 = ImageTk.PhotoImage(img3)

      # bg image

      bg_img = Label(self.root, image=self.photoimg3)
      bg_img.place(x=0, y=130, width=1530, height=710)

      # title label
      title_lbl = Label(bg_img, text="FACE RECOGNITION SYSTEM SOFTWARE",
       font=("Bookman Old Style", 35, "bold"),
       fg='red')
      title_lbl.place(x=0, y=0, width=1400, height=40)

      # button to student

      img4 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student.gif")
      img4 = img4.resize((220, 220))
      self.photoimg4 = ImageTk.PhotoImage(img4)

      b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.student_enter)
      b1.place(x=150, y=60, width=220, height=220)

      b2 = Button(bg_img, text="Student Details", font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue", command=self.student_enter)
      b2.place(x=150, y=250, width=220, height=30)

      # face recognization

      img5 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\face detector 2.jpeg")
      img5 = img5.resize((220, 220))
      self.photoimg5 = ImageTk.PhotoImage(img5)

      b3 = Button(bg_img, image=self.photoimg5, cursor="hand2")
      b3.place(x=430, y=60, width=220, height=220)

      b4= Button(bg_img, text="Face Recognisation", font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue")
      b4.place(x=430, y=250, width=220, height=30)

            # button to student

      img6 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student 2.jpg")
      img6 = img6.resize((220, 220))
      self.photoimg6 = ImageTk.PhotoImage(img6)

      b5 = Button(bg_img, image=self.photoimg6, cursor="hand2")
      b5.place(x=700, y=60, width=220, height=220)

      b6 = Button(bg_img, text="Attendance", font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue")
      b6.place(x=700, y=250, width=220, height=30)

            # button to student

      img7 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student 1.jpg")
      img7 = img7.resize((220, 220))
      self.photoimg7 = ImageTk.PhotoImage(img5)

      b7 = Button(bg_img, image=self.photoimg7, cursor="hand2")
      b7.place(x=950, y=60, width=220, height=220)

      b8= Button(bg_img, text="Train Data", font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue")
      b8.place(x=950, y=250, width=220, height=30)


            # button to student

      img9 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student 3.jpg")
      img9 = img9.resize((220, 220))
      self.photoimg9 = ImageTk.PhotoImage(img9)

      b1 = Button(bg_img, image=self.photoimg9,command=self.photo_image, cursor="hand2")
      b1.place(x=150, y=300, width=220, height=220)

      b2 = Button(bg_img, text="PHOTO",command=self.photo_image, font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue")
      b2.place(x=150, y=490, width=220, height=30)
      
            # button to student

      img10 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\developer.jpg")
      img10 = img10.resize((220, 220))
      self.photoimg10 = ImageTk.PhotoImage(img10)

      b3 = Button(bg_img, image=self.photoimg10, cursor="hand2")
      b3.place(x=430, y=300, width=220, height=220)

      b4= Button(bg_img, text="DEVELOPER", font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue")
      b4.place(x=430, y=490, width=220, height=30)

            # button to student

      img11 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\help.jpg")
      img11 = img11.resize((220, 220))
      self.photoimg11 = ImageTk.PhotoImage(img11)

      b5 = Button(bg_img, image=self.photoimg11, cursor="hand2")
      b5.place(x=700, y=300, width=220, height=220)

      b6 = Button(bg_img, text="HELP", font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue")
      b6.place(x=700, y=490, width=220, height=30)

            # button to student

      img12 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\exit.jpg")
      img12 = img12.resize((220, 220))
      self.photoimg12 = ImageTk.PhotoImage(img12)

      b7 = Button(bg_img, image=self.photoimg12, cursor="hand2")
      b7.place(x=950, y=300, width=220, height=220)

      b8= Button(bg_img, text="EXIT", font=("Bookman Old Style", 15, "bold"), cursor="hand2", fg="white", bg="blue")
      b8.place(x=950, y=490, width=220, height=30)


   def photo_image(self):
      os.startfile("data")


   def student_enter(self):
      self.engine.say(" Welcome To STUDENT management Portal.")
      self.engine.runAndWait()
      self.new_window = Toplevel(self.root)
      self.app = Student(self.new_window)





if __name__ == "__main__":
   root = Tk()
   obj = Face_recognisation_system(root)
   root.mainloop()
