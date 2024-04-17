from tkinter import *
from tkinter import ttk
import customtkinter as ctk

from PIL import Image, ImageTk

from tkinter import messagebox
from main import Face_recognisation_system
from registration import Registration
import mysql.connector as mysql
import sys as sy


class login():
   def __init__(self, root):
      self.root = root
      self.root.geometry("600x600+400+40")
      self.root.resizable(False, False)
      self.root.title("Login Form")


      # =========================VAriables====================
      self.name_var = StringVar()
      self.pass_var = StringVar()


      label = ctk.CTkLabel(self.root, text="LOGIN MANAGEMENT SYSTEM",font=("Bookman Old Style", 35),fg_color="light blue", width=600, height=40)
      label.place(x=0, y=3)

      # login profile image

      img2 = Image.open("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/image1.jpeg")
      img2 = img2.resize((600, 250))
      self.photoimg2 = ImageTk.PhotoImage(img2)

      f_lbl = Label(self.root, image=self.photoimg2)
      f_lbl.place(x=0, y=50, width=600, height=250)

      # profile picture

      #img = Image.open("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/Images/student in class.jpg")
      #img = img.resize((1530, 710))
      #self.photoimg = ImageTk.PhotoImage(img)

      #my_label = ctk.CTkLabel(self.root, image=self.photoimg, text="", cursor='hand2')
      #my_label.pack(pady=40)

      # Username
      username_label = ctk.CTkLabel(self.root, text="Username", font=("Time New Roman", 20))
      username_label.place(x=100, y=330)

      username_entry = ctk.CTkEntry(self.root, width=300,textvariable=self.name_var, height=30)
      username_entry.place(x=230, y=330)
      username_entry.focus()

      # password
      password_label = ctk.CTkLabel(self.root, text="Password", font=("Time New Roman", 20))
      password_label.place(x=100, y=400)

      password_entry = ctk.CTkEntry(self.root, width=300, textvariable=self.pass_var, height=30, show="*")
      password_entry.place(x=230, y=400)

      # sign Up Form

      sign_up_btn = ctk.CTkButton(self.root, text="Sign Up", command=self.register, height=35)
      sign_up_btn.place(x=200, y=450)

      # Login Page

      login_btn = ctk.CTkButton(self.root, text="Log in",command=self.login, cursor='hand2', height=35)
      login_btn.place(x=400, y=450)

      # checkbox Remember me
      checkbox_var = ctk.StringVar()
      checkbox = ctk.CTkCheckBox(self.root, variable=checkbox_var, onvalue="yes", offvalue="no", hover_color="red", text="Remember Me")
      checkbox.place(x=100, y=500)

      # forget password form

      forget_pass_btn = ctk.CTkButton(self.root, text="forget password?", text_color="black", hover_color="white", fg_color="transparent")
      forget_pass_btn.place(x=400, y=500)


   # ========================Functions decrations =============================

   # login function

   def login(self):
      if self.name_var.get() == "":
         messagebox.showerror(title="Error", message="Username Field Cannot be Empty!!!", parent=self.root)
      
      elif self.pass_var.get() == "":
         messagebox.showerror(title="Error", message="Password Field Cannot be Empty!!!", parent=self.root)

      elif(self.name_var.get()=="admin" and self.pass_var.get()=="admin"):
         messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
         self.new_window=Toplevel(self.root)
         self.app=Face_recognisation_system(self.new_window)
         self.name_var.set(value="")
         self.pass_var.set(value="")

      else:
         # messagebox.showerror("Error","Please Check Username or Password !")
         conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
         cur = conn.cursor()
         
         cur.execute("select * from registration where Password =%s and Username=%s",
                     (self.pass_var.get(), 
                      self.name_var.get()))
         row=cur.fetchone()
         if row==None:
               messagebox.showerror("Error","Invalid Username and Password!")
         else:
               open_min=messagebox.askyesno("YesNo","Access only Admin")
               if open_min>0:
                  self.new_window=Toplevel(self.root)
                  self.app=Face_recognisation_system(self.new_window)
                  self.name_var.set(value="")
                  self.pass_var.set(value="")
               else:
                  if not open_min:
                     return
         conn.commit()
         conn.close()

   def register(self):
         a =messagebox.askquestion(title="Information", message="Are you Sure You want to create account?", parent = self.root)
         if a == "yes":
            self.new_window = Toplevel(self.root)
            self.app = Registration(self.new_window)
         else:
            pass

if __name__ == "__main__":
   root = Tk()
   obj = login(root)
   root.mainloop()
