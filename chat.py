from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
from customtkinter import *
from student import Student
import pyttsx3
import os
from tkinter import ttk
import cv2

class practise():
   def __init__(self, root):
      self.root = root
      self.root.title("Hello world")
      self.root.geometry("300x300+100+0")
      self.engine = pyttsx3.init()
      self.voices = self.engine.getProperty("voices")
      self.engine.setProperty("voice", self.voices[1].id)

      lab = CTkLabel(self.root, text="Password")
      lab.pack()

      self.pas_var = StringVar()

      pas = CTkEntry(self.root, placeholder_text="Password", textvariable=self.pas_var)
      pas.pack()

      btn = CTkButton(self.root, text="login", command=self.login)
      btn.pack()

      scrol_x = Scrollbar(self.root, orient="horizontal")
      scrol_x.pack(side=BOTTOM, fill=X)
      scrol_y = Scrollbar(self.root, orient="vertical")
      scrol_y.pack(side=RIGHT, fill=Y)
      self.tree = ttk.Treeview(self.root, columns=("name", "password", "phone"),xscrollcommand=scrol_x, yscrollcommand=scrol_y)
      self.tree.pack()

      self.tree.heading("name", text="Name")
      self.tree.heading("password", text="Password")
      self.tree.heading("phone", text="Phone Number")
      self.tree["show"] = "headings"

      self.tree.column("name", width=100)
      self.tree.column("password", width=100)
      self.tree.column("phone", width=100)

      scrol_x.configure(command=self.tree.xview)
      scrol_y.configure(command=self.tree.yview)


   def login(self):
      
      face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

      def face_croped(img):
               # conver gary sacle
               gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
               faces = face_classifier.detectMultiScale(gray,1.3,5)
               #Scaling factor = 1.3
               # Minimum Neigbour = 5
               for (x,y,w,h) in faces:
                  face_croped=img[y:y+h,x:x+w]
                  return face_croped
               cap=cv2.VideoCapture(1)
               img_id=0
               while True:
                  ret,my_frame=cap.read()
                  if face_croped(my_frame) is not None:
                        
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/student."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                  if cv2.waitKey(0)==13 or int(img_id)==100:
                              break
               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)

      if self.pas_var.get() == "":
         messagebox.showerror(title="Login status", message="Passworld field must be filled")
      else:
         try:
            conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
            cur = conn.cursor()
            cur.execute("select * from registration where password=%s",(self.pas_var.get(),))
            row = cur.fetchone()

            if row == None:
               messagebox.showerror(title="database status", message="Invalid password")
            else:
                open = messagebox.askyesno(title="Database Status", message="Welcome To Mkuu System")
                if open > 0:
                    self.newWindow = Toplevel(self.root)
                    self.app = Student(self.newWindow)
                else:
                    if not open:
                        return
                conn.commit()
            conn.close()

         except Exception as es:
            messagebox.showerror(title="Database status", message=f"Error Due: {str(es)}")




if __name__ == "__main__":
   root = Tk()
   obj = practise(root)
   root.mainloop()
