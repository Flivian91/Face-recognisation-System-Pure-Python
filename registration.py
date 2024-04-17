from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import mysql.connector as mysql
from main import Face_recognisation_system
import cv2

class Registration():
   def __init__(self, root):
      self.root = root
      self.root.geometry("1000x600+100+40")
      self.root.resizable(True, False)
      self.root.title("REGISTRATION MANAGEMENT SYSTEM")
      self.root.columnconfigure(0, weight=0)

      # =========================variables=======================================================================

      self.f_name_entry_var = StringVar()
      self.l_name_entry_var = StringVar()
      self.email_entry_var = StringVar()
      self.username_entry_var = StringVar()
      self.f_phone_num_entry_var = StringVar()
      self.l_phone_num_entry_var = StringVar()
      self.dob_var = StringVar()
      self.gender_var = StringVar()
      self.password_var = StringVar()
      self.confirm_password_var = StringVar()
      self.answer_var = StringVar()
      self.recovery_var = StringVar()
      self.accept = StringVar()

      # =========================variables========================================================================

      # tenant name label frame
      label_f = LabelFrame(self.root, text='Admin Name', width=300, height=200, font=("Bookman Old style", 15), background="light pink")
      label_f.place(x=10, y=0,height=100)

      # first name label
      f_name = ctk.CTkLabel(label_f, text="First Name", font=("Times New Roman", 20))
      f_name.grid(row=0, column=1, padx=10)

      # last name label
      l_name = ctk.CTkLabel(label_f, text="Last Name", font=("Times New Roman", 20))
      l_name.grid(row=0, column=2, padx=10)

      # first name entry
    
      f_name_entry = ctk.CTkEntry(label_f, textvariable=self.f_name_entry_var, width=230, border_width=0, height=33)
      f_name_entry.grid(row=1, column=1, padx=10)

      # last name entry
    
      l_name_entry = ctk.CTkEntry(label_f, textvariable=self.l_name_entry_var, width=230, height=33, border_width=0, border_color="light pink")
      l_name_entry.grid(row=1, column=2)

      # Email entry field

      email_l = ctk.CTkLabel(self.root, text="Email",anchor=ctk.W)
      email_l.place(x=30, y=100)

      # star label
      email_l_star = ctk.CTkLabel(self.root, text="*", anchor=ctk.W, text_color="red")
      email_l_star.place(x=67, y=100)

      # email entry field
  
      email_entry = ctk.CTkEntry(self.root, textvariable=self.email_entry_var, width=430, height=40, text_color="blue", border_width=3, border_color="light pink")
      email_entry.place(x=30, y=125)

      # username label

      username_l = ctk.CTkLabel(self.root, text="Username", anchor=ctk.W)
      username_l.place(x=30, y=200)

      # star label
      star = ctk.CTkLabel(self.root, text="*", anchor=ctk.W, text_color="red")
      star.place(x=95, y=200)

      # username field

      username_entry = ctk.CTkEntry(self.root, textvariable=self.username_entry_var, width=430, height=40, text_color="blue", border_width=3, border_color="light pink")
      username_entry.place(x=30, y=225)

      # phone number label frame
      label_f = LabelFrame(self.root, text='Admin Phone Number', width=300, height=200, font=("Times New Roman", 15), bg="light pink")
      label_f.place(x=10, y=295)

      # first name label
      f_phone_num = ctk.CTkLabel(label_f, text="1st Phone Number", font=("Times New Roman", 20))
      f_phone_num.grid(row=0, column=1, padx=10)

      # last name label
      l_phone_num = ctk.CTkLabel(label_f, text="2nd Phone Number", font=("Bookman Old Style", 20))
      l_phone_num.grid(row=0, column=2, padx=10)

      # first phone number entry

      f_phone_num_entry = ctk.CTkEntry(label_f, textvariable=self.f_phone_num_entry_var, width=230, height=33, border_width=0)
      f_phone_num_entry.grid(row=1, column=1, padx=10)

      # last name entry
      
      l_phone_num_entry = ctk.CTkEntry(label_f, textvariable=self.l_phone_num_entry_var, width=230, height=33, border_width=0)
      l_phone_num_entry.grid(row=1, column=2)

      # star mark
      star = ctk.CTkLabel(self.root, text="*", anchor=ctk.W, text_color="red", fg_color='light pink', height=1)
      star.place(x=212, y=326)

      # date of birth label frame
      label_f = LabelFrame(self.root, text='Date of birth', width=300, font=("Times New Roman", 20),background="light pink", height=200, labelanchor=ctk.W)
      label_f.place(x=10, y=435)

      # date of birth entry field
      dob_entry = ctk.CTkEntry(label_f, textvariable=self.dob_var, width=333, height=33, border_width=0)
      dob_entry.grid(row=1, column=1, padx=10, pady=25)

      # Email entry field
      dob_l = ctk.CTkLabel(self.root, text="DD/MM/YYYY",anchor=ctk.W, text_color="red",height=0)
      dob_l.place(x=300, y=442)

      # label frame
      label_f = LabelFrame(self.root, text='Gender', width=400, height=200, font=("Bookman Old Style", 20), background="light pink")
      label_f.place(x=550, y=0)
  
      # female radiobutton
      male_rdb = ctk.CTkRadioButton(label_f, text="Male", value="male", variable=self.gender_var)
      male_rdb.grid(row=1, column=0, padx=10, ipadx=10)

      # female radiobutton
      female_rdb = ctk.CTkRadioButton(label_f, text="Female", value="female", variable=self.gender_var)
      female_rdb.grid(row=1, column=1)

      # not to say option
      not_say_rdb = ctk.CTkRadioButton(label_f, text="Rather Not to Say", value="none", variable=self.gender_var)
      not_say_rdb.grid(row=1, column=3, padx=10, pady=20, ipadx=10)

      # password label frame
      label_f = LabelFrame(self.root, text='Password',width=500, height=200,font=("Bookman Old Style", 15),background="light pink")
      label_f.place(x=550, y=100)

      # new password label
      new_password_label = ctk.CTkLabel(label_f, text="New Password", font=("Bookman Old Style", 20))
      new_password_label.grid(row=0, column=1, pady=0)

      # new password entry

      password_entry = ctk.CTkEntry(label_f, textvariable=self.password_var, width=333, height=33, border_width=0, show="*")
      password_entry.grid(row=1, column=1, padx=15)

      # confirm password label
      confirm_password_label = ctk.CTkLabel(label_f, text="Confirm Password", font=("Bookman Old Style", 20))
      confirm_password_label.grid(row=2, column=1, pady=0)

      # confirm password entry
      
      confirm_password_entry = ctk.CTkEntry(label_f, textvariable=self.confirm_password_var, width=333, height=33, border_width=0, show="*")
      confirm_password_entry.grid(row=3, column=1, padx=25)

      # combobox label
      cb_label = ctk.CTkLabel(label_f, text="Recovery Question", font=("Bookman Old Style", 20))
      cb_label.grid(row=4, column=1, pady=0)

      # combobox place

      cb = ctk.CTkComboBox(label_f, variable=self.recovery_var, state="readonly", dropdown_hover_color="green",dropdown_fg_color="light pink", border_width=0, button_hover_color="blue", dropdown_text_color="black",width=333, height=33, values=["What is the name of your first school?",
                                    "What was the make of your first car?",
                                    "What is your father's middle name",
                                    "What high school did you attend?",
                                    "What is the name of your first school?",
                                    "what is your favorite social media website",
                                    "What is the name of your first grade teacher?",
                                    "What was your favorite place to visit as a child?",
                                    "Which phone number do you remember most from your childhood?",
                                    "What is your favorite movie?"])
      cb.grid(row=5, column=1, padx=25, pady=5)


      # confirm password label
      answer_label = ctk.CTkLabel(label_f, text="Answer", font=("Times New Roman", 20))
      answer_label.grid(row=6, column=1, pady=0)

      # confirm password entry
      
      answer_entry = ctk.CTkEntry(label_f, textvariable=self.answer_var, width=333, height=33, border_width=0)
      answer_entry.grid(row=7, column=1, padx=25, pady=5)

      # add file label
      add_file_label = ctk.CTkLabel(self.root, text="Upload Profile Picture below", fg_color="pink")
      add_file_label.place(x=600, y=400)
      # star on add file
      star = ctk.CTkLabel(self.root, text="*", anchor=ctk.W, text_color="red")
      star.place(x=770, y=395)

      # upload button
 
      my_image = ctk.CTkImage(light_image=Image.open("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/Images/icons/download-icon.png"), size=(20, 20))
      upload_btn = ctk.CTkButton(self.root, image=my_image, cursor='hand2', text="Upload..", compound=ctk.LEFT, command=self.select_file)
      upload_btn.place(x=580, y=450)

      # Save button
      save_btn = ctk.CTkButton(self.root, command=self.save, cursor='hand2', text="Save")
      save_btn.place(x=580, y=530)

      # sign up button

      sign_btn = ctk.CTkButton(self.root, command=self.sign_up, cursor='hand2', text="Sign Up", fg_color="green", hover_color="light green", font=("Times New Roman", 20), text_color="black")
      sign_btn.place(x=780, y=530)

      # label to place the image
      place_label = ctk.CTkLabel(self.root, fg_color="transparent", text="No chosen file",font=("Old bookman style", 20))
      place_label.place(x=730, y=450)


      # accept terms and conditions
      condition = ctk.CTkCheckBox(self.root, variable=self.accept, text="I Agree with terms and conditions of the Application", fg_color="pink", onvalue="yes", offvalue="no", hover_color="Pink")
      condition.place(x=30, y=550)
     


   # ==============================Functions===================================================
   def select_file(self):
         
         filetypes = (
            ('PNG files', '*.png'),
            ('JPG files', '*.jpg'),
            ('All files', '*.*')
         )

         filename = fd.askopenfilename(
               title='Open a file',
               initialdir='c:/user',
               filetypes=filetypes)

         # label to place the image
         place_image_label = ctk.CTkLabel(self.root, fg_color="transparent", text=filename)
         place_image_label.place(x=730, y=450)

         messagebox.showinfo(
               title='Selected File',
               message=filename, parent = self.root)
         
   def save(self):
       
       if self.f_name_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Name!!",parent = self.root)
       elif self.email_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Email!!",parent = self.root)

       elif self.f_phone_num_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Phone Number!!",parent = self.root)

       elif self.username_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Username!!",parent = self.root)

       elif self.gender_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Select Admin Gender!!",parent = self.root)

       elif self.password_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Password!!",parent = self.root)

       elif self.password_var.get() != self.confirm_password_var.get():
           messagebox.showinfo(title="Error Status", message="Please Password & Confirm Pasword Must be same!!",parent = self.root)

       elif self.recovery_var.get() and self.answer_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Recovery Question and Appropriate Answer",parent = self.root)

       else:
           try:
               conn = mysql.connect(host="localhost", username="root", password="flivian254", database="mydb")
               cur = conn.cursor()
               cur.execute("INSERT INTO registration VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (self.f_name_entry_var.get(),
                            self.l_name_entry_var.get(),
                            self.email_entry_var.get(),
                            self.username_entry_var.get(),
                            self.f_phone_num_entry_var.get(),
                            self.l_phone_num_entry_var.get(),
                            self.dob_var.get(),
                            self.gender_var.get(),
                            self.password_var.get(),
                            self.recovery_var.get(),
                            self.answer_var.get()))
               conn.commit()
               conn.close()
               messagebox.showinfo(title="Database Status", message="Record Saved Successfully Proceed And sign Up", parent = self.root)
           except Exception as es:
               messagebox.showerror(title="Database Error", message=f"Error Due {str(es)}", parent = self.root)

   def sign_up(self):
       if self.f_name_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Name!!", parent = self.root)
       elif self.email_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Email!!", parent = self.root)

       elif self.f_phone_num_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Phone Number!!", parent = self.root)

       elif self.username_entry_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Username!!", parent = self.root)

       elif self.gender_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Select Admin Gender!!", parent = self.root)

       elif self.password_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Admin Password!!", parent = self.root)

       elif self.password_var.get() != self.confirm_password_var.get():
           messagebox.showinfo(title="Error Status", message="Please Password & Confirm Pasword Must be same!!", parent = self.root)

       elif self.recovery_var.get() and self.answer_var.get() == "":
           messagebox.showerror(title="Error Status", message="Please Fill Recovery Question and Appropriate Answer", parent = self.root)
       elif self.accept.get() == "yes":
            self.new_window = Toplevel(self.root)
            self.app = Face_recognisation_system(self.new_window)

       else:
           messagebox.showwarning(title="Sign Up Status", message="You need to accept Terms and condtions before Login", parent = self.root)
           
           
           
           

       


if __name__ == "__main__":
   root = Tk()
   obj = Registration(root)
   root.mainloop()