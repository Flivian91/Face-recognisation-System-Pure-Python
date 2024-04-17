from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from pathlib import Path
import os
import threading





class Student():
   def __init__(self, root):
      self.root = root
      self.root.title("Student Management System")
      self.root.geometry("1530x790+0+0")
   

      # ==================================== variables ==================================
      self.dep_var = StringVar()
      self.year_var = StringVar()
      self.course_var = StringVar()
      self.sem_var = StringVar()
      self.student_id_var = StringVar()
      self.class_div_var = StringVar()
      self.gender_var = StringVar()
      self.email_var = StringVar()
      self.address_var = StringVar()
      self.name_var = StringVar()
      self.roll_no_var = StringVar()
      self.dob_var = StringVar()
      self.phone_no_var = StringVar()
      self.teacher_var = StringVar()

      
      # first header image

      img = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\class 1.png")
      img = img.resize((500, 100))
      self.photoimg = ImageTk.PhotoImage(img)

      f_lbl = Label(self.root, image=self.photoimg)
      f_lbl.place(x=0, y=0, width=500, height=100)

      # second header image

      img1 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student in class.jpg")
      img1 = img1.resize((500, 100))
      self.photoimg1 = ImageTk.PhotoImage(img1)

      f_lbl = Label(self.root, image=self.photoimg1)
      f_lbl.place(x=500, y=0, width=500, height=100)

      # third header image

      img2 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\class 2.jpeg")
      img2 = img2.resize((500, 100))
      self.photoimg2 = ImageTk.PhotoImage(img2)

      f_lbl = Label(self.root, image=self.photoimg2)
      f_lbl.place(x=900, y=0, width=500, height=100)

      # background image

      img3 = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\bg.jpg")
      img3 = img3.resize((1530, 710))
      self.photoimg3 = ImageTk.PhotoImage(img3)

      # bg image

      bg_img = Label(self.root, image=self.photoimg3)
      bg_img.place(x=0, y=100, width=1530, height=710)

      # title label
      title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
       font=("Bookman Old Style", 25, "bold"),
       fg='white', bg="red")
      title_lbl.place(x=0, y=0, width=1400, height=30)

      # main frame
      main_frame = Frame(bg_img, bd=2)
      main_frame.place(x=5, y=28, width=1260, height=550)

      # left label frame
      left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Information", font=("Bookman Old Style", 15, "bold"), bg="white")
      left_frame.place(x=5, y=2, width=630, height=530)

      # left label frame
      right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,text="Student Details", font=("Bookman Old Style", 15, "bold"), bg="white")
      right_frame.place(x=640, y=2, width=620, height=550)

      
      img_left = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student.gif")
      img_left = img_left.resize((620, 100))
      self.photoimgleft = ImageTk.PhotoImage(img_left)

      f_lbl = Label(left_frame, image=self.photoimgleft)
      f_lbl.place(x=5, y=0, width=620, height=100)

      # course label frame
      course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE,text="Student Details", font=("Bookman Old Style", 15, "bold"), bg="white")
      course_frame.place(x=6, y=100, width=620, height=100)

      # Department
      dep_label = Label(course_frame, text="Department", font=("Bookman Old Style", 10, "bold"), bg="white")
      dep_label.grid(row=0, column=0, padx=3)

      dep_combo = ttk.Combobox(course_frame,textvariable=self.dep_var, font=("Bookman Old Style", 10, "bold"), state="readonly")
      dep_combo["values"] = ("Select Department", "Pure and Applied Science", "Engineering", "Medicine")
      dep_combo.current(0)
      dep_combo.grid(row=0, column=1)

      #year

      year_label = Label(course_frame, text="Year", font=("Bookman Old Style", 10, "bold"), bg="white")
      year_label.grid(row=1, column=0, pady=5)

      year_combo = ttk.Combobox(course_frame,textvariable=self.year_var, font=("Bookman Old Style", 10, "bold"), state="readonly")
      year_combo["values"] = ("2023","2022", "2021", "2020", "2019")
      year_combo.current(0)
      year_combo.grid(row=1, column=1, pady=5)

      # course


      course_label = Label(course_frame, text="Department", font=("Bookman Old Style", 10, "bold"), bg="white")
      course_label.grid(row=0, column=2, padx=0)

      course_combo = ttk.Combobox(course_frame, textvariable=self.course_var, font=("Bookman Old Style", 10, "bold"), state="readonly")
      course_combo["values"] = ("Select Course", "IT", "CS", "SE", "CSE")
      course_combo.current(0)
      course_combo.grid(row=0, column=3)

      # semister

      sem_label = Label(course_frame, text="Semister", font=("Bookman Old Style", 10, "bold"), bg="white")
      sem_label.grid(row=1, column=2, pady=5)

      sem_combo = ttk.Combobox(course_frame,textvariable=self.sem_var, font=("Bookman Old Style", 10, "bold"), state="readonly")
      sem_combo["values"] = (1, 2)
      sem_combo.current(0)
      sem_combo.grid(row=1, column=3, pady=10)

      # student information label frame

      student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE,text="Student Class Information", font=("Bookman Old Style", 15, "bold"), bg="white")
      student_frame.place(x=6, y=200, width=620, height=400)

      # student Id number
      student_Id = Label(student_frame, text="Student ID: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      student_Id.grid(row=0, column=0, sticky=W)

      student_entry = ttk.Entry(student_frame,textvariable=self.student_id_var, font=("Bookman Old Style", 10, "bold"))
      student_entry.grid(row=0, column=1, sticky=W)

      # class division
      class_label = Label(student_frame, text="Class Division", font=("Bookman Old Style", 10, "bold"), bg="white")
      class_label.grid(row=1, column=0, pady=5, sticky=W)

      class_combo = ttk.Combobox(student_frame, textvariable=self.class_div_var, font=("Bookman Old Style", 10, "bold"), state="readonly")
      class_combo["values"] = (1, 2)
      class_combo.current(0)
      class_combo.grid(row=1, column=1, pady=10, sticky=W)

      # gender

      gender_label = Label(student_frame, text="gender", font=("Bookman Old Style", 10, "bold"), bg="white")
      gender_label.grid(row=2, column=0, pady=5, sticky=W)

      gender_combo = ttk.Combobox(student_frame, textvariable=self.gender_var, font=("Bookman Old Style", 10, "bold"), state="readonly")
      gender_combo["values"] = ("Male", "Female")
      gender_combo.current(0)
      gender_combo.grid(row=2, column=1, pady=10, sticky=W)


      # Email
      email = Label(student_frame, text="Email: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      email.grid(row=3, column=0, sticky=W)

      email_entry = ttk.Entry(student_frame, textvariable=self.email_var, font=("Bookman Old Style", 10, "bold"))
      email_entry.grid(row=3, column=1, sticky=W)

      # Address
      address_Id = Label(student_frame, text="Address: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      address_Id.grid(row=4, column=0, sticky=W)

      address_entry = ttk.Entry(student_frame, textvariable=self.address_var, font=("Bookman Old Style", 10, "bold"))
      address_entry.grid(row=4, column=1, pady=5, sticky=W)

      # Name
      name = Label(student_frame, text="Name: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      name.grid(row=0, column=2, sticky=W)

      name = ttk.Entry(student_frame, textvariable=self.name_var, font=("Bookman Old Style", 10, "bold"))
      name.grid(row=0, column=3, pady=5, sticky=W)

      # roll no
      roll_no = Label(student_frame, text="Roll No: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      roll_no.grid(row=1, column=2, sticky=W)

      roll_no = ttk.Entry(student_frame, textvariable=self.roll_no_var, font=("Bookman Old Style", 10, "bold"))
      roll_no.grid(row=1, column=3, pady=5, sticky=W)

      # date of birth
      dob = Label(student_frame, text="D.O.B: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      dob.grid(row=2, column=2, sticky=W)

      dob = ttk.Entry(student_frame, textvariable=self.dob_var, font=("Bookman Old Style", 10, "bold"))
      dob.grid(row=2, column=3, pady=5, sticky=W)

      # phone number
      phone_number = Label(student_frame, text="Phone No: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      phone_number.grid(row=3, column=2, sticky=W)

      phone_number = ttk.Entry(student_frame, textvariable=self.phone_no_var, font=("Bookman Old Style", 10, "bold"))
      phone_number.grid(row=3, column=3, pady=5, sticky=W)

      # teacher name
      teacher_name = Label(student_frame, text="Teacher No: ", bg="white", font=("Bookman Old Style", 10, "bold"))
      teacher_name.grid(row=4, column=2, sticky=W)

      teacher_name = ttk.Entry(student_frame, textvariable=self.teacher_var, font=("Bookman Old Style", 10, "bold"))
      teacher_name.grid(row=4, column=3, pady=5, sticky=W)

      # radio buttons
      self.radio1_var = StringVar()

      radiobtn1 = ttk.Radiobutton(student_frame, variable=self.radio1_var, text="Take Photo Sample", value="yes")
      radiobtn1.grid(row=5, column=0, padx=0)

      radiobtn2= ttk.Radiobutton(student_frame, variable=self.radio1_var, text="No Photo Sample ", value="no")
      radiobtn2.grid(row=5, column=1)

      # buttons frame
      button_frame = Frame(left_frame,  relief=RIDGE, bg="white")
      button_frame.place(x=5, y=435, width=700, height=120)

      # save button
      savebtn = Button(button_frame, text="Save",command=self.save, font=("Bookman Old Style", 10, "bold"), bg="blue")
      savebtn.place(x=20, y=5)

      # update button
      updatebtn = Button(button_frame, text="Update",command=self.update,  font=("Bookman Old Style", 10, "bold"), bg="blue")
      updatebtn.place(x=155, y=5)

      # delete

      deletebtn = Button(button_frame, text="Delete",command=self.delete_data,  font=("Bookman Old Style", 10, "bold"), bg="blue")
      deletebtn.place(x=305, y=5)
      

      # reset
      resetbtn = Button(button_frame, command=self.reset, text="Reset",  font=("Bookman Old Style", 10, "bold"), bg="blue")
      resetbtn.place(x=455, y=5)

      # add photo
      ass_photobtn = Button(button_frame, text="Add photo Sample",command=self.generate_dataset,  font=("Bookman Old Style", 10, "bold"), bg="blue")
      ass_photobtn.place(x=5, y=35)

      # update photo sample
      update_photobtn = Button(button_frame, text="Update photo Sample", command=self.update_photo, font=("Bookman Old Style", 10, "bold"), bg="blue")
      update_photobtn.place(x=185, y=35)

      # right frame

      img_right = Image.open(r"C:\Users\Flivian\Desktop\PROJECTS\FACE RECOGNIZATION CLASS ATTENDANCE\Images\student 4.jpg")
      img_right = img_right.resize((620, 100))
      self.photoimgright = ImageTk.PhotoImage(img_right)

      f_lbl = Label(right_frame, image=self.photoimgright)
      f_lbl.place(x=5, y=0, width=620, height=100)

      # ===========================Search system============================

      search_frame = LabelFrame(right_frame, text="Search system",  relief=RIDGE, bg="white",  font=("Bookman Old Style", 10, "bold"))
      search_frame.place(x=10, y=100, width=700, height=60)

      # search label

      search_lbl = Label(search_frame, text="Search By", font=("Bookman Old Style", 13, "bold"), bg="red")
      search_lbl.grid(row=0, column=0)

      # combobox
      self.search_var = StringVar()
      search_combo = ttk.Combobox(search_frame, textvariable=self.search_var, font=("Bookman Old Style", 10, "bold"), state="readonly", width=15)
      search_combo["values"] = ("Select", "Roll No", "Phone No")
      search_combo.current(0)
      search_combo.grid(row=0, column=1)

      # search entry
      self.search_entry_var = StringVar()
      search_entry = ttk.Entry(search_frame, textvariable=self.search_entry_var, font=("Bookman Old Style", 15, "bold"), width=15)
      search_entry.grid(row=0, column=2, padx=2)

      # search button
      searchbtn = Button(search_frame, text="Search",command=self.search_data,  font=("Bookman Old Style", 10, "bold"), bg="blue")
      searchbtn.grid(row=0, column=3, padx=5)

      # showall button
      showallbtn = Button(search_frame, text="Show All",  font=("Bookman Old Style", 10, "bold"), bg="blue")
      showallbtn.grid(row=0, column=4, padx=5)


      # table
      table_frame = Frame(right_frame, relief=RIDGE, bg="white")
      table_frame.place(x=10, y=167, width=610, height=354)

      # scrollbar
      scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
      scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

      self.student_table = ttk.Treeview(table_frame, columns=("dep","year","course", "sem","id", "div", "gender", "email", "address", "name", "roll", "dob", "phone", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_x.config(command=self.student_table.xview)
      scroll_y.config(command=self.student_table.yview)

      self.student_table.heading("dep", text="Department")
      self.student_table.heading("year", text="Year")
      self.student_table.heading("course", text="courses")
      self.student_table.heading("sem", text="Semister")
      self.student_table.heading("id", text="Student Id")
      self.student_table.heading("div", text="Class Division")
      self.student_table.heading("gender", text="Gender")
      self.student_table.heading("email", text="Email")
      self.student_table.heading("address", text="Address")
      self.student_table.heading("name", text="Name")
      self.student_table.heading("roll", text="Roll No")
      self.student_table.heading("dob", text="D.O.B")
      self.student_table.heading("phone", text="Phone No")
      self.student_table.heading("teacher", text="Teacher Name")
      self.student_table.heading("photo", text="Photo added")
      self.student_table["show"] = "headings"


      self.student_table.pack(fill=BOTH, expand=1)

      self.student_table.column("dep", width=200)
      self.student_table.column("year", width=100)
      self.student_table.column("course", width=100)
      self.student_table.column("sem", width=100)
      self.student_table.column("id", width=100)
      self.student_table.column("div", width=100)
      self.student_table.column("gender", width=100)
      self.student_table.column("email", width=100)
      self.student_table.column("address", width=100)
      self.student_table.column("name", width=100)
      self.student_table.column("roll", width=100)
      self.student_table.column("dob", width=100)
      self.student_table.column("phone", width=100)
      self.student_table.column("teacher", width=100)
      self.student_table.column("photo", width=100)
      self.student_table.bind("<ButtonRelease>", self.get_cursor)

      self.fetch_data()



   # =================================Functio decration =====================================
   def save(self):
      if self.dep_var.get() == "Select Department" or self.student_id_var.get() == "" or self.name_var.get() == "":
         messagebox.showerror(title="Error", message="All Fields Must Be filled", parent=self.root)
      else:
         try:
            conn = mysql.connector.connect(host="localhost", username="root", password="flivian254", database="mydb")
            c =conn.cursor()
            c.execute("INSERT INTO student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
               self.dep_var.get(),
               self.year_var.get(),
               self.course_var.get(),
               self.sem_var.get(),
               self.student_id_var.get(),
               self.class_div_var.get(),
               self.gender_var.get(),
               self.email_var.get(),
               self.address_var.get(),
               self.name_var.get(),
               self.roll_no_var.get(),
               self.dob_var.get(),
               self.phone_no_var.get(),
               self.teacher_var.get(),
               self.radio1_var.get()

            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo(title="Successfully", message="Record Updated successfully on database", parent=self.root)
         except Exception as es:
            messagebox.showerror(title="Error", message=f"Error Due {str(es)}", parent=self.root)

   # ================================== fetch data and show on  treeview ======================

   def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="flivian254", database="mydb")
            c =conn.cursor()
            c.execute("SELECT * FROM student")
            data = c.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
   # ======================= cursor =======================
   def get_cursor(self, event=" "):
       cursor_focus = self.student_table.focus()
       content = self.student_table.item(cursor_focus)
       data = content["values"]

       self.dep_var.set(data[0]),
       self.year_var.set(data[1]),
       self.course_var.set(data[2]),
       self.sem_var.set(data[3]),
       self.student_id_var.set(data[4]),
       self.class_div_var.set(data[5]),
       self.gender_var.set(data[7]),
       self.email_var.set(data[6]),
       self.address_var.set(data[8]),
       self.name_var.set(data[9]),
       self.roll_no_var.set(data[10]),
       self.dob_var.set(data[11]),
       self.phone_no_var.set(data[12]),
       self.teacher_var.set(data[13]),
       self.radio1_var.set(data[14])
   
   # =================================UPDATE===========================================


   def update(self):
         if self.dep_var.get() == "Select Department" or self.student_id_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror(title="Error", message="All Fields Must Be filled", parent=self.root)
         else:
             try:

               update_data = messagebox.askyesno(title="Inquiring", message="Are you sure you want to update this information", parent=self.root)
               
               if update_data > 0:
                
                  conn = mysql.connector.connect(host="localhost", username="root", password="flivian254", database="mydb")
                  c =conn.cursor()
                  c.execute("update student set dep=%s, year=%s, course=%s, sem=%s, class=%s, gender=%s, email=%s, address=%s, name=%s, roll =%s, dob = %s, phone = %s, teacher=%s, photo=%s where std_no =%s ", (
                                    self.dep_var.get(),
                                    self.year_var.get(),
                                    self.course_var.get(),
                                    self.sem_var.get(),
                                    
                                    self.class_div_var.get(),
                                    self.gender_var.get(),
                                    self.email_var.get(),
                                    self.address_var.get(),
                                    self.name_var.get(),
                                    self.roll_no_var.get(),
                                    self.dob_var.get(),
                                    self.phone_no_var.get(),
                                    self.teacher_var.get(),
                                    self.radio1_var.get(),
                                    self.student_id_var.get()
                                    
                                    
                  ))
               else:
                   if not update_data:
                       return
               messagebox.showinfo(title="Success", message="Record Updated Successfully", parent = self.root)
               conn.commit()
               self.fetch_data()
               conn.close()
            
             except Exception as es:
                     messagebox.showerror(title="Error", message=f"Error Due {str(es)}", parent=self.root)  

   # ========================================== DELETE FUNCTION ====================================


   def delete_data(self):
            if self.student_id_var.get()=="":
               messagebox.showerror(title="Error", message="Student Id Must be Required!",parent=self.root)

            else:
               try:
                  delete_data=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                  
                  if delete_data > 0:
   
                        conn = mysql.connector.connect(host="localhost", username="root", password="flivian254", database="mydb")
                        c =conn.cursor()
                        c.execute("DELETE FROM student WHERE std_no = %s", (self.student_id_var.get(),))
                  else:
                        if not delete_data:
                           return
                             
                  conn.commit()
                  self.fetch_data()
                  conn.close()
                  messagebox.showinfo(title="Delete", message="REcord deleted successfully", parent=self.root)
               except Exception as es:
                  messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
       
      # ===============================RESET DATA FUNCTION ======================================


   def reset(self):
       self.dep_var.set("Select Department"),
       self.year_var.set("2023"),
       self.course_var.set("Select course"),
       self.sem_var.set(1),
       self.student_id_var.set(""),
       self.class_div_var.set(1),
       self.gender_var.set("male"),
       self.email_var.set(""),
       self.address_var.set(""),
       self.name_var.set(""),
       self.roll_no_var.set(""),
       self.dob_var.set(""),
       self.phone_no_var.set(""),
       self.teacher_var.set(""),
       self.radio1_var.set("")


       # ==========================SEARCH FOR DATA ==========================================
   def search_data(self):
         if self.search_entry_var.get()=="" or self.search_var.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
         else:
            try:
                conn = mysql.connector.connect(username='root', password='flivian254',host='localhost',database='mydb')
                c = conn.cursor()
                sql = "SELECT dep,year,course,sem,std_no,class,gender,email,address,name,roll,dob,phone,teacher,photo FROM student where roll='" +str(self.search_entry_var.get()) + "'" 
                c.execute(sql)
                # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                rows=c.fetchall()        
                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Data Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
       
   
   # =============================Generate dataset ========================================

   def generate_dataset(self):
      if self.dep_var.get() == "Select Department" or self.student_id_var.get() == "" or self.name_var.get() == "":
         messagebox.showerror(title="Error", message="All Fields Must Be filled", parent=self.root)
      else:
         try:
            conn = mysql.connector.connect(host="localhost", username="root", password="flivian254", database="mydb")
            c =conn.cursor()
            c.execute("SELECT * FROM student")
            my_result = c.fetchall()
            conn.commit()
            id = 0

            for x in my_result:
                id+=1
            
            c.execute("update student set dep=%s, year=%s, course=%s, sem=%s, class=%s, gender=%s, email=%s, address=%s, name=%s, roll =%s, dob = %s, phone = %s, teacher=%s, photo=%s where std_no =%s ", (
                                    self.dep_var.get(),
                                    self.year_var.get(),
                                    self.course_var.get(),
                                    self.sem_var.get(),
                                    self.class_div_var.get(),
                                    self.gender_var.get(),
                                    self.email_var.get(),
                                    self.address_var.get(),
                                    self.name_var.get(),
                                    self.roll_no_var.get(),
                                    self.dob_var.get(),
                                    self.phone_no_var.get(),
                                    self.teacher_var.get(),
                                    self.radio1_var.get(),
                                    self.student_id_var.get()==id+1                 
                  ))
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            # ================= load predefined data on face for OpenCv =========================

            import cv2
            import os
            from tkinter import messagebox
            import threading

            def face_cropped(img):
               gray_frame = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
               faces = face_classifier.detectMultiScale(gray_frame, 1.3, 5)
               
               cropped_faces = [cv2.resize(img[y:y+h, x:x+w], (450, 450)) for (x, y, w, h) in faces]
               return cropped_faces

            def capture_images(cap, student_name):
               img_id = 0
               for _ in range(skip_frames):
                  cap.read()  # Skip frames

               while img_id < 100:
                  ret, my_frame = cap.read()
                  faces = face_cropped(my_frame)

                  for face in faces:
                        img_id += 1
                        folder_name = f"data/{student_name}"
                        os.makedirs(folder_name, exist_ok=True)
                        file_path = os.path.join(folder_name, f"{student_name}_{img_id}.jpg")

                        threading.Thread(target=cv2.imwrite, args=(file_path, face)).start()

                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)

                  if cv2.waitKey(1) & 0xFF == 13:
                        break

               cap.release()
               cv2.destroyAllWindows()
               messagebox.showinfo("Result", "Generating dataset completed!", parent=self.root)

            try:
               face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
               cap = cv2.VideoCapture(0)
               student_name = "flivian"  # Replace with the actual student name
               skip_frames = 5  # Adjust as needed

               capture_thread = threading.Thread(target=capture_images, args=(cap, student_name))
               capture_thread.start()

            except Exception as es:
               messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
         except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

   def update_photo(self):
      messagebox.showinfo(title="success", message="Photo sample Updated Successfully!!", parent=self.root)
      self.root.destroy()
# main class object                


if __name__ == "__main__":
   root = Tk()
   obj = Student(root)
   root.mainloop()