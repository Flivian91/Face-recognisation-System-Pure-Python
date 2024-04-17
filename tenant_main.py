"""
module Required
1. Tkinter
2. Customtkinter
3. Pillow
4. Time
5. datetime
6. os
"""
from tkinter import*
import tkinter as tk

from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox
from time import strftime
import time as time
import os
from datetime import date
# =========================================Tenant management system Home page=================== #

class Tenant_management_main():
   def __init__(self, root):
      self.root = root
      self.root.geometry("1230x650+20+5")
      self.root.title("Tenant Management System")

      # =================================Variables=================================


      # ======================Header Frame ==========================================
      self.header_frame = ctk.CTkFrame(self.root, fg_color="light green", width=1200, height=100)
      self.header_frame.place(x=4,y=1)

      # ====================Current Time Display===============================
      def time():
        string = strftime("%H:%M:%S %p")
        self.clock.configure(text=string)
        self.clock.after(1000, time)
      self.clock=ctk.CTkLabel(self.header_frame, corner_radius=0, width=200, text_color="red", font=("Bookman Old style", 30)) 
      self.clock.place(x=1000, y=12)
      time()
      
      # Rentals name or title
      self.name=ctk.CTkLabel(self.header_frame, corner_radius=0,text="KIRINYAGA UNIVERSITY RENTALS", text_color="red", font=("Bookman Old style,bold",25)) 
      self.name.place(x=400, y=16)
   
      # main frame for all buttons
      main_frame = tk.Frame(self.root, bg="#c3c3c3")
      main_frame.pack(side=tk.LEFT, padx=3)
      main_frame.pack_propagate(False)
      main_frame.configure(width=200, height=530)

      # tenant name icon
      img = Image.open("C:/Users/FLIVO/Desktop/FACE RECOGNIZATION CLASS ATTENDANCE/Images/icons/username2.png")
      img = img.resize((50, 50))
      self.photoimg = ImageTk.PhotoImage(img)

      f_lbl = tk.Label(self.header_frame, image=self.photoimg, cursor="hand2", background="light green")
      f_lbl.place(x=5, y=5, width=50, height=50)

      # Tenant name label
      tenant_name_lb = tk.Label(self.header_frame, text="Tenant Name", font=("Bookman Old Style", 20), background="light green")
      tenant_name_lb.place(x=50, y=10)

      # ===================================buttons on main frame================================================ 

      # Rental View Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Rental View", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_rental, self.rental_view_fun))
      self.rental_view_btn.place(x=0, y=15)
      
      # rental View indicator with red background

      self.lb_indicator_rental = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_rental.place(x=0, y=15, width=5, height=60)

      # Payment  Button 

      self.payment_btn = ctk.CTkButton(main_frame, text="Payment", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_payment,self.payment_view_fun))
      self.payment_btn.place(x=0, y=90)

      # payment Indicator 
      self.lb_indicator_payment = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_payment.place(x=0, y=90, width=5, height=60)

      # Notifiaction Button 

      self.notification_btn = ctk.CTkButton(main_frame, text="Transaction", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_notification, self.notification_view_fun))
      self.notification_btn.place(x=0, y=180)

      # label to show current messages sent
      message_lb = ctk.CTkLabel(self.notification_btn, text="1",text_color="red",fg_color="white", width=30, font=("Bookman Old Style", 20), corner_radius=15, bg_color="#0beba1")
      message_lb.place(x=160, y=3)
      
      # Notification indicator
      self.lb_indicator_notification = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_notification.place(x=0, y=180, width=5, height=60)

      # Profile Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Profile", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_profile, self.profile_view_fun))
      self.rental_view_btn.place(x=0, y=260)

      # Profile indicator

      self.lb_indicator_profile = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_profile.place(x=0, y=260, width=5, height=60)

      # Contact Us Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Contact Us", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_contact, self.contact_view_fun))
      self.rental_view_btn.place(x=0, y=360)
      
      # contact Us indicator
      self.lb_indicator_contact = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_contact.place(x=0, y=360, width=5, height=60)

      # Logout  Button 

      self.rental_view_btn = ctk.CTkButton(main_frame, text="Loguot", width=200, height=60, font=("Bookman Old Style",20), fg_color="#0beba1", text_color="black", hover_color="#0bfbb1", command=lambda: self.indicator(self.lb_indicator_logout, self.logout_view_fun))
      self.rental_view_btn.place(x=0, y=460)

      # logout Indicator
      self.lb_indicator_logout = tk.Label(main_frame, text="", bg="#0beba1")
      self.lb_indicator_logout.place(x=0, y=460, width=5, height=60)


      # =====================================main Window Frame======================================== 
      self.page_frame = tk.Frame(self.root, highlightthickness=0)
      self.page_frame.pack(side=tk.LEFT)
      self.page_frame.pack_propagate(False)
      self.page_frame.configure(width=1000, height=530)

      # ===================background Image for Rental Houses===========================
      bg_image = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/rental.jpg")
      bg_image = bg_image.resize((990, 530))
      self.bg_photo = ImageTk.PhotoImage(bg_image)

      image_lbl = tk.Label(self.page_frame, image=self.bg_photo)
      image_lbl.place(x=0, y=0, width=1000, height=530)
      
      # footer message
      self.footer_frame = ctk.CTkFrame(self.root, fg_color="light green", width=1200, height=50)
      self.footer_frame.place(x=4,y=595)

      ctk.CTkLabel(self.footer_frame, text="TAGLINE: The Way we see it, real wealth means having the money and the freedom to live life on your own terms", font=("BookMan Old Style", 20)).place(x=10, y=7)

      # ======================================function for indicators==========================================

   def indicator(self, lbl, page):
      self.hide_indicator()
      self.delete_page()
      lbl.config(bg="red")
      page()
      
   # Hide function to hide one button after the other is clicked
   def hide_indicator(self):
      self.lb_indicator_rental.config(bg="#0beba1")
      self.lb_indicator_payment.config(bg="#0beba1")
      self.lb_indicator_notification.config(bg="#0beba1")
      self.lb_indicator_profile.config(bg="#0beba1")
      self.lb_indicator_contact.config(bg="#0beba1")
      self.lb_indicator_logout.config(bg="#0beba1")


   # Rental view page
   def rental_view_fun(self):
      # rental frame contain all the other widget
      rental_main_frame = tk.Frame(self.page_frame, width=1000, height=800)
      rental_main_frame.place(x=10, y=10)

      # search labelframe with location, type, price

      search_frame = tk.LabelFrame(rental_main_frame, text="Search By",bg="light green", font=("Bookman Old Style", 20))
      search_frame.place(x=10, y=5, width=970, height=100)


      # location combobox
      location_cmb = ctk.CTkComboBox(search_frame, values=["a1", "a2", "a3"], state="readonly", width=200, fg_color="light yellow", dropdown_fg_color="#0beba1",font=("Bookman Old Style", 20), dropdown_hover_color="#0bbba1", button_color="#0beba1")
      location_cmb.place(x=4, y=5)
      location_cmb.set(value="Location")

      # Type of house combobox
      location_cmb = ctk.CTkComboBox(search_frame, values=["Single Room", "Bedsitter", "1 Bedroom", "2 Bedroom", "3 Bedroom"], state="readonly", width=250, fg_color="light yellow",font=("Bookman Old Style", 20), dropdown_fg_color="#0beba1", dropdown_hover_color="#0bbba1", button_color="#0beba1")
      location_cmb.place(x=250, y=5)
      location_cmb.set(value="Type")

      # Price of house combobox
      location_cmb = ctk.CTkComboBox(search_frame, values=["2000", "3000", "4000", "5000"], state="readonly", width=200, fg_color="light yellow", dropdown_fg_color="#0beba1",font=("Bookman Old Style", 20), dropdown_hover_color="#0bbba1", button_color="#0beba1")
      location_cmb.place(x=550, y=5)
      location_cmb.set(value="Price")

      # explore all button 
      explore_btn = ctk.CTkButton(search_frame, text="Explore All", width=150, fg_color="blue", height=50, font=("Bookman Old Style", 20))
      explore_btn.place(x=800, y=0)

      # text on screan label
      ctk.CTkLabel(rental_main_frame, text="Our Popular Rentals", font=("Bookman Old Style", 30)).place(x=40, y =105)

      # Create a Canvas widget inside a Frame
      frame = tk.Frame(rental_main_frame)
      self.canvas = tk.Canvas(frame, borderwidth=0, highlightthickness=0, width=1000, height=400)
      scrollbar_y = tk.Scrollbar(frame, orient="vertical", command=self.canvas.yview)
      scrollbar_x = tk.Scrollbar(frame, orient="horizontal", command=self.canvas.xview)

      scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
      scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
      self.canvas.place(x=2, y=2, width=1000, height=400)

      # Configure the canvas to work with the scrollbars
      self.canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
      self.canvas.bind("<Configure>", self.on_configure)

      frame.place(x=2, y=140, width=990, height=500)


      # frame to Hold all the Available houses 
      rental_frame = tk.LabelFrame(self.canvas, text="Availbale Rentals", width=1000, height=1000, bg="#0beba1")
      rental_frame.place(x=0, y=3, width=1000, height=1000)
      self.canvas.create_window((0, 0), window=rental_frame, anchor="nw")



      # ================================1st Available House ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=0)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a2", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================2nd Available House==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=0)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Single", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a2", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 3000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================3rd Available house ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=0)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================4th Available House  ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=180)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="1 Bedroom", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 5000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================5th Available House==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=180)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)
      
      # ================================6th Available House ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=180)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="2 Bedroom", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a1", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 6000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)


      # ================================7th Available House==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=360)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="3 Bedroom", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 7000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================8th Available House ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=360)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="c4", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK B RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)
      
      # ================================9th Available House ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=360)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="2 Bedroom", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="b1", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 6000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

       # ================================10th Available House ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=545)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a2", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================12th Available House==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=545)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Single", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a2", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 3000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================13th Available house ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=545)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================14th Available House  ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=20, y=735)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="1 Bedroom", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 5000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      # ================================15th Available House==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=340, y=735)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="Bedsitter", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a3", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 4000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)
      
      # ================================16th Available House ==================================
      self.house_btn = ctk.CTkButton(rental_frame, text="",width=300, height=150, fg_color="#d0dd1e", hover_color="#d0dd1e", command=self.house_btn_click)
      self.house_btn.configure(cursor="hand2")
      self.house_btn.place(x=665, y=735)

      type_lb = ctk.CTkLabel(self.house_btn, text="Type:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=10)

      type_mode_lb = ctk.CTkLabel(self.house_btn, text="2 Bedroom", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=60, corner_radius=20)
      type_mode_lb.place(x=60, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="Location:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=160, y=10)

      location_mode_lb = ctk.CTkLabel(self.house_btn, text="a1", font=("Bookman Old Style", 15), text_color="black", bg_color="white", width=40, corner_radius=20)
      location_mode_lb.place(x=250, y=10)

      type_lb = ctk.CTkLabel(self.house_btn, text="BLOCK A RENTALS", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=30, y=65)

      type_lb = ctk.CTkLabel(self.house_btn, text="Price:", font=("Bookman Old Style", 20), text_color="black", bg_color="#d0dd1e")
      type_lb.place(x=3, y=110)

      price_mode_lb = ctk.CTkLabel(self.house_btn, text="Ksh 6000", font=("Bookman Old Style", 20), text_color="black", bg_color="white", width=60, corner_radius=20)
      price_mode_lb.place(x=60, y=110)

      self.house_btn_book = ctk.CTkButton(self.house_btn, text="Book Now", width=80, height=20, fg_color="green",hover_color="red", bg_color="#d0dd1e")
      self.house_btn_book.place(x=200, y=120)

      ctk.CTkLabel(rental_frame, text="No more available Rentals....", font=("Bookman Old Style", 20), fg_color="#0beba1", text_color="red").place(x=200, y=930)
      

   # =======================================payment page===========================
   def payment_view_fun(self):
      # Payment Main frame
      payment_main_frame = tk.Frame(self.page_frame, width=1000, height=800)
      payment_main_frame.place(x=0, y=10)


      #==========================Payment variables==========================================
      self.name_var =tk.StringVar()
      self.phone_var =tk.StringVar()
      self.id_var =tk.StringVar()
      self.mpesa_var =tk.StringVar()
      self.paybill_var =tk.StringVar()


      # Image to show Money
      bg_image = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/profile.jpg")
      bg_image = bg_image.resize((950, 100))
      self.bg_photo = ImageTk.PhotoImage(bg_image)

      image_lbl = tk.Label(payment_main_frame, image=self.bg_photo)
      image_lbl.place(x=0, y=0, width=1000, height=100)


      # ==========================label frame to show methods of payment========================================


      payment_mode_frame = tk.LabelFrame(payment_main_frame, text="Select Mode Of payment", font=("Bookman Old Style", 20), bg='#ffd6ff') 
      payment_mode_frame.place(x=1, y=90, width=980, height=150)

      # Mpesa Button

      mpesa_img = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/lipa mpesa.png")
      mpesa_img = mpesa_img.resize((190, 60))
      self.mpesa_photo = ImageTk.PhotoImage(mpesa_img)
      mpesa_btn = tk.Button(payment_mode_frame,text="", image=self.mpesa_photo, width=200, background="green", height=60, cursor="hand2")
      mpesa_btn.place(x=30, y=35)

      mpesa_btn.config(background="red")
      # mpesa label
      ctk.CTkLabel(payment_mode_frame, text="M-pesa", fg_color="green", width=100).place(x=80, y=3)

      """
      mpesa_checked = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/check.png")
      mpesa_checked = mpesa_checked.resize((40, 40))
      self.photo_checked = ImageTk.PhotoImage(mpesa_checked)

      cheked_lb = tk.Label(payment_mode_frame, image=self.photo_checked)
      cheked_lb.place(x=200, y=20)
      """

      # Bank Button
      bank_img = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/kcb bank.png")
      bank_img = bank_img.resize((200, 60))
      self.bank_photo = ImageTk.PhotoImage(bank_img)
      self.bank_btn = tk.Button(payment_mode_frame,text="", image=self.bank_photo,background="green", width=200, height=60, cursor="hand2", command=lambda: self.change(lb=self.bank_btn))
      self.bank_btn.place(x=330, y=35)
      
      # bank label
      ctk.CTkLabel(payment_mode_frame, text="KCB Bank", fg_color="green", width=100).place(x=390, y=3)

      # ATM Button
      atm_img =Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/atm bank.png")
      atm_img = atm_img.resize((190, 60))
      self.atm_photo = ImageTk.PhotoImage(atm_img)
      self.atm_btn = tk.Button(payment_mode_frame,text="", image=self.atm_photo, background="green",width=200, height=60, cursor="hand2", command=lambda: self.change(lb=self.atm_btn))
      self.atm_btn.place(x=630, y=35)

      # ATM label
      ctk.CTkLabel(payment_mode_frame, text="ATM Card", fg_color="green", width=100).place(x=685, y=3)


      # =============================label frame to show details for payment=========================
      pay = tk.LabelFrame(payment_main_frame, text="Complete Payment", font=("Bookman Old Style", 20),bg='#ffd6ff') 
      pay.place(x=1, y=240, width=980, height=280)

      # ==================================================== Full Name ============================
      # names label
      ctk.CTkLabel(pay, text="FULL NAMES", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=146, y=3)

      # Names Entry fields
      names_entry = ctk.CTkEntry(pay, corner_radius=0, textvariable=self.name_var, border_width=2, border_color="pink", width=300,height=40, font=("Bookman Old Style", 20))
      names_entry.place(x=82, y=40)
      names_entry.focus()

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=245, y=0)

      
      # ==================================================== PHONE NUMBER ============================
      # names label
      ctk.CTkLabel(pay, text="Valid Phone Number", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=142, y=90)

      # Names Entry fields
      phone_entry = ctk.CTkEntry(pay, corner_radius=0,textvariable=self.phone_var, border_width=2, border_color="pink", width=300,height=40, font=("Bookman Old Style", 20))
      phone_entry.place(x=82, y=120)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=297, y=90)

            
      # ==================================================== ID Number ============================
      # names label
      ctk.CTkLabel(pay, text="Valid ID Number", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=142, y=160)

      # Names Entry fields
      id_entry = ctk.CTkEntry(pay, corner_radius=0,textvariable=self.id_var, border_width=2, border_color="pink", width=300,height=40, font=("Bookman Old Style", 20))
      id_entry.place(x=82, y=190)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=270, y=162)

      # ==================================================== Mode of Payment ============================
      # mpesa mode label
      ctk.CTkLabel(pay, text="M-PESA MODE", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=610, y=3)

      # Mpesa mode Entry fields
      mpesa_mode_cmb = ctk.CTkComboBox(pay, values=["LIPA NA MPESA", "SEND MONEY"],state="readonly",corner_radius=0, border_width=2, border_color="pink",variable=self.mpesa_var,dropdown_fg_color="#0beba1", width=300,height=40,button_color="#0beba1", button_hover_color="#0beca1" )
      mpesa_mode_cmb.set("LIPA NA MPESA")
      mpesa_mode_cmb.place(x=540, y=40)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=740, y=0)

      
      # ==================================================== Paybill NUMBER ============================

      """Only available when the mode of payment selected is Lipa na Mpesa"""

      # paybill label
      ctk.CTkLabel(pay, text="PAYBILL", text_color="black", font=("Bookman Old Style", 15), width=100).place(x=590, y=90)

      # paybill Entry fields
      """
      Paybill is always disabled and it should be displayed
      """
      paybill_entry = ctk.CTkEntry(pay, corner_radius=0,textvariable=self.paybill_var, placeholder_text="0354734", border_width=2, border_color="pink",state=tk.DISABLED,width=300,height=40, fg_color="#8d99ae", font=("Bookman Old Style", 20))
      paybill_entry.place(x=540, y=120)

      # star sign
      ctk.CTkLabel(pay, text="*", text_color="red", font=("Bookman Old Style", 15)).place(x=680, y=90)

      # back to home button

      back_home = ctk.CTkButton(pay, text="<< Back",text_color="black",command=self.back_home_payment,  height=40, fg_color="green", font=("Bookman Old Style", 20), hover_color="light green")
      back_home.place(x=430, y=190)

      # clear  button

      clear_home = ctk.CTkButton(pay, text="Clear",  height=40, fg_color="green",text_color="black", font=("Bookman Old Style", 20), hover_color="light green", command=self.clear_payment)
      clear_home.place(x=600, y=190)

      # Complete payment  button

      back_home = ctk.CTkButton(pay, text="Complete Payment",  height=40, fg_color="green",text_color="black", font=("Bookman Old Style", 20), hover_color="light green", command=self.complete_payment)
      back_home.place(x=770, y=190)



            

   # =========================Notification ============================================
   def notification_view_fun(self):
      # Main fram for notification bar
      profile = tk.Frame(self.page_frame, width=1000, height=500)
      notification_frame = tk.LabelFrame(profile, text="Transaction", font=("Bookman Old Style", 20), bg="#00f5d4")
      notification_frame.place(x=1, y=1, width=990, height=500)
      profile.place(x=10, y=10)
      
      notification_img = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/transaction.png")
      notification_img = notification_img.resize((200, 100))
      self.bank_photo = ImageTk.PhotoImage(notification_img)
      self.bank_btn = tk.Label(notification_frame,text="", image=self.bank_photo, width=200, height=100)
      self.bank_btn.place(x=10, y=10)

      #tk.Label(notification_frame,image=notification_photo).place(x=0, y=0, width=300)

      transation_frame = tk.Frame(notification_frame)
      transation_frame.place(x=2, y=150, width=960, height=340)


      # Label to show the performance of the Tenant

      # to be replaced in future Since they are not resposible
      payment_state_lb = ctk.CTkLabel(notification_frame, text="",fg_color="light green",width=300, height=130)
      payment_state_lb.place(x=240, y=0)

      ctk.CTkLabel(payment_state_lb, text="Payment Status", font=("Bookman Old Style", 30)).place(x=40, y=5)
      check_box = ctk.CTkCheckBox(payment_state_lb, text="Done", font=("Bookman Old style", 30))
      check_box.place(x=60, y=70)

      payment_state_lb = ctk.CTkLabel(notification_frame, text="",fg_color="lightgreen",width=300, height=130)
      payment_state_lb.place(x=640, y=0)

      ctk.CTkLabel(payment_state_lb, text="Balance Status", font=("Bookman Old Style", 30)).place(x=40, y=5)
      check_box = ctk.CTkCheckBox(payment_state_lb, text="4,000", font=("Bookman Old style", 30))
      check_box.place(x=60, y=70)



      # Showing the tree view with the transation
      self.transtion_details = ttk.Treeview(transation_frame,columns=["month", "name", "id", "payment", "ref_no", "amount", "date","balance"])
      self.transtion_details.place(x=1, y=1, width=960, height=330)

      # scrollbar
      scroll_x = tk.Scrollbar(transation_frame, orient=tk.HORIZONTAL)
      scroll_y = tk.Scrollbar(transation_frame, orient=tk.VERTICAL)

      scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
      scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
      scroll_x.config(command=self.transtion_details.xview)
      scroll_y.config(command=self.transtion_details.yview)

      # showing the Heading of each column
      self.transtion_details.heading("month", text="Month")
      self.transtion_details.heading("name", text="Ful Name")
      self.transtion_details.heading("id", text="ID_No")
      self.transtion_details.heading("payment", text="Payment Mode")
      self.transtion_details.heading("ref_no", text="Ref No.")
      self.transtion_details.heading("amount", text="Amount Paid")
      self.transtion_details.heading("date", text="Date Of Payment")
      self.transtion_details.heading("balance", text="Balance")
      self.transtion_details["show"] = "headings"

      # setting the display width of each of column

      self.transtion_details.column("month", width=100)
      self.transtion_details.column("name", width=150)
      self.transtion_details.column("id", width=80)
      self.transtion_details.column("payment", width=100)
      self.transtion_details.column("ref_no", width=100)
      self.transtion_details.column("amount", width=80)
      self.transtion_details.column("date", width=100)
      self.transtion_details.column("balance", width=80)
   # profile  page

   # =============================================Profile decralation function=============================
   def profile_view_fun(self):

      # ==================================Profile variables ===============================================
      self.f_name_var = tk.StringVar()
      self.l_name_var = tk.StringVar()
      self.email_var = tk.StringVar()
      self.f_phone_var = tk.StringVar()
      self.l_phone_var = tk.StringVar()
      self.dob_var = tk.StringVar()
      self.county_var = tk.StringVar()
      self.gender_var = tk.StringVar()
      self.house_var = tk.StringVar()
      self.id_no_var = tk.StringVar()

      # emergency 
      self.f_name_em_var = tk.StringVar()
      self.l_name_em_var = tk.StringVar()
      self.f_phone_em_var = tk.StringVar()
      self.l_phone_em_var = tk.StringVar()
      self.email_em_var = tk.StringVar()

      # Acceptance
      self.check_accept_var = tk.StringVar()
      self.check_terms_var = tk.StringVar()

      profile_frame = tk.Frame(self.page_frame, bg="green", width=1000, height=560)
      profile_frame.pack()

      # header frame to show the House icon and Description of the Page
      header_frame = tk.Frame(profile_frame)
      header_frame.place(x=4, y=2, width=990, height=100)

      # house Icon on the left side

      house_img = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/house_profile.png")
      house_img = house_img.resize((150, 80))
      self.bank_photo = ImageTk.PhotoImage(house_img)
      self.bank_btn = tk.Label(header_frame, image=self.bank_photo, width=200, height=100)
      self.bank_btn.place(x=1, y=0)

      # House icon on the right side
      house_img1 = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/house_profile.png")
      house_img1 = house_img1.resize((150, 80))
      self.house_photo = ImageTk.PhotoImage(house_img1)
      self.bank_btn = tk.Label(header_frame, image=self.house_photo, width=200, height=100)
      self.bank_btn.place(x=800, y=0)

      # Label to show tenant need to Updte presonal Information

      ctk.CTkLabel(header_frame, text="TENANT PROFILE UPDATE FORM", font=("Bookman Old Style", 30)).place(x=250, y=35)

      #========================================= Personal information frame======================================

      personal_frame = tk.LabelFrame(profile_frame, text="Tenant Personal Details",bg='#ffd6ff', font=("Bookman Old Style", 15))
      personal_frame.place(x=4, y=110, width=500, height=415)

      # names label 
      ctk.CTkLabel(personal_frame, text="First Name", font=("Bookman Old Style", 15)).place(x=40, y=3)
      ctk.CTkLabel(personal_frame, text="Last Name", font=("Bookman Old Style", 15)).place(x=230, y=3)

      # Name Entry Fields
      f_name = ctk.CTkEntry(personal_frame ,textvariable=self.f_name_var, border_color="pink", corner_radius=0, width=160)
      f_name.place(x=10, y=27)

      # Last name field

      l_name = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.l_name_var, corner_radius=0, width=160)
      l_name.place(x=230, y=27)

      # Email Address
      ctk.CTkLabel(personal_frame, text="Email Address", font=("Bookman Old Style", 15)).place(x=80, y=60)

      email_address = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.email_var, corner_radius=0, width=300)
      email_address.place(x=10, y=90)

      # Phone Number label 
      ctk.CTkLabel(personal_frame, text="Phone Number", font=("Bookman Old Style", 15)).place(x=40, y=120)
      ctk.CTkLabel(personal_frame, text="Other Number", font=("Bookman Old Style", 15)).place(x=230, y=120)

      # Phone Number Entry Fields
      f_phone = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.f_phone_var, corner_radius=0, width=160)
      f_phone.place(x=10, y=150)

      # Last Phone number field

      l_phone= ctk.CTkEntry(personal_frame , border_color="pink", corner_radius=0,textvariable=self.l_phone_var, width=160)
      l_phone.place(x=230, y=150)

      # date of birth Address
      ctk.CTkLabel(personal_frame, text="Date of Birth", font=("Bookman Old Style", 15)).place(x=80, y=180)

      dob = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.dob_var, corner_radius=0, width=300)
      dob.place(x=10, y=210)

      # Home county field
      ctk.CTkLabel(personal_frame, text="Home County", font=("Bookman Old Style", 15)).place(x=40, y=240)

      home_county = ctk.CTkComboBox(personal_frame , border_color="pink", corner_radius=0,variable=self.county_var, width=180)
      home_county.configure(values=['Baringo', 'Bomet', 'Bungoma', 'Busia', "Nairobi"])
      home_county.set("Select Home County")
      home_county.place(x=10, y=270)

      # gender field
      ctk.CTkLabel(personal_frame, text="Gender ", font=("Bookman Old Style", 15)).place(x=40, y=300)

      gender = ctk.CTkComboBox(personal_frame , border_color="pink",values=["Male", "Female"],variable=self.gender_var, corner_radius=0, width=180)
      gender.place(x=10, y=330)

      # Type Of House

      ctk.CTkLabel(personal_frame, text="Type Of House ", font=("Bookman Old Style", 15)).place(x=250, y=240)

      house= ctk.CTkComboBox(personal_frame , border_color="pink",values=["a1", "a2", "a3"],variable=self.house_var, corner_radius=0, width=150)

      house.place(x=250, y=270)

      # Id number field
      ctk.CTkLabel(personal_frame, text="ID Number", font=("Bookman Old Style", 15)).place(x=250, y=300)

      id_no = ctk.CTkEntry(personal_frame , border_color="pink",textvariable=self.id_no_var, corner_radius=0, width=200)
      id_no.place(x=250, y=330)

      

      # ===========================emergency information frame========================================

      emergency_frame = tk.LabelFrame(profile_frame, text="Emergency Details",bg='#ffd6ff', font=("Bookman Old Style", 15))
      emergency_frame.place(x=520, y=110, width=475, height=210)

      # names label 
      ctk.CTkLabel(emergency_frame, text="First Name", font=("Bookman Old Style", 15)).place(x=40, y=3)
      ctk.CTkLabel(emergency_frame, text="Last Name", font=("Bookman Old Style", 15)).place(x=230, y=3)

      # Name Entry Fields
      f_name_emergency = ctk.CTkEntry(emergency_frame ,textvariable=self.f_name_em_var, border_color="pink", corner_radius=0, width=160)
      f_name_emergency.place(x=10, y=27)

      # Last name field

      l_name_emergency = ctk.CTkEntry(emergency_frame , border_color="pink", corner_radius=0, width=160,textvariable=self.l_name_em_var)
      l_name_emergency.place(x=230, y=27)

      # Phone Number label 
      ctk.CTkLabel(emergency_frame, text="Phone Number", font=("Bookman Old Style", 15)).place(x=40, y=60)
      ctk.CTkLabel(emergency_frame, text="Other Number", font=("Bookman Old Style", 15)).place(x=230, y=60)

      # Phone Number Entry Fields
      f_phone_emergency = ctk.CTkEntry(emergency_frame , border_color="pink",textvariable=self.f_phone_em_var, corner_radius=0, width=160)
      f_phone_emergency.place(x=10, y=90)

      # Last Phone number field

      l_phone_emergency= ctk.CTkEntry(emergency_frame , border_color="pink", corner_radius=0, width=160,textvariable=self.l_phone_em_var)
      l_phone_emergency.place(x=230, y=90)

      # Email address field
      ctk.CTkLabel(emergency_frame, text="Email Address", font=("Bookman Old Style", 15)).place(x=10, y=120)

      email_emergency = ctk.CTkEntry(emergency_frame , border_color="pink", corner_radius=0, width=300,textvariable=self.email_em_var)
      email_emergency.place(x=10, y=145)




      # ===============================Acceptance  information frame========================================
      acceptance_frame = tk.LabelFrame(profile_frame, text="Acceptance And Signing off",bg='#ffd6ff', font=("Bookman Old Style", 15))
      acceptance_frame.place(x=520, y=323, width=475, height=100)

      # check box for acceptance
      check_accept = ctk.CTkCheckBox(acceptance_frame, text="I Accept to follow All Stipulated Rules of the House", font=("Bookman Old Style", 17), onvalue="yes", offvalue="no",variable=self.check_accept_var)
      check_accept.place(x=5, y=4)

      check_terms = ctk.CTkCheckBox(acceptance_frame, text="I Accept All terms And Conditions", font=("Bookman Old Style", 20), onvalue="yes", offvalue="no",variable=self.check_terms_var)
      check_terms.place(x=5, y=40)

      submit_frame = tk.Frame(profile_frame, bg='#ffd6ff')
      submit_frame.place(x=520, y=425, width=475, height=100)

      # back Changes Button
      clear_profile_btn = ctk.CTkButton(submit_frame,font=("Bookman Old style", 20),text="Clear", height=40, text_color="black", command=self.clear_profile)
      clear_profile_btn.place(x=20, y=30)

      # submit button

      submit_btn = ctk.CTkButton(submit_frame,font=("Bookman Old style", 20),text="Submit", height=40, fg_color="green", hover_color="#0beba1", text_color="black", command=self.submit_profile)
      submit_btn.place(x=260, y=30)

      

   # ====================================contact us page=====================================================
   def contact_view_fun(self):
      # contact Main Frame
      font = ("Bookman Old Style", 12)
      contact_frame = tk.Frame(self.page_frame, bg="green", width=1000, height=560)
      contact_frame.pack()

      # ========================Contact us variables========================================================
      self.tenant_id_var = tk.StringVar()
      self.email_contact = tk.StringVar()
      self.phone_contact = tk.StringVar()
      self.id_no_contact = tk.StringVar()
      self.username_contact = tk.StringVar()
      self.subject_var = tk.StringVar()
      self.message_var = tk.StringVar()




      # conatct Image
      contact_img = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/contact us.jpeg")
      contact_img = contact_img.resize((700, 140))
      self.contact_photo = ImageTk.PhotoImage(contact_img)

      ttk.Label(contact_frame, image=self.contact_photo, text="").place(x=10, y=10)

      text=ctk.CTkLabel(contact_frame, text="",fg_color="#bc6c25",corner_radius=20, width=240, height=150)
      text.place(x=730, y=2)

      # admin Name Inside a text Label
      ttk.Label(text, text="Admin Name:",background="#bc6c25", font=font).place(x=60, y=3)
      ttk.Label(text, text="Flivian",font=font).place(x=80, y=26)

      # admin Email
      ttk.Label(text, text="Admin Email:",background="#bc6c25", font=font).place(x=60, y=50)
      ttk.Label(text, text="flivian@gmail.com",font=font).place(x=50, y=70)

      # Admin Phone number

      ttk.Label(text, text="Admin Cell No:", background="#bc6c25",font=font).place(x=50, y=100)
      ttk.Label(text, text="0718017191",font=font).place(x=60, y=120)

      # label frame for Queries
      ticket_frame = tk.LabelFrame(contact_frame, text="Ticket Information",font=("Bookman Old Style", 20), width=960, height=370, bg="#80ffdb")
      ticket_frame.place(x=5, y=160)
      
      # Tenant Id Field
      ctk.CTkLabel(ticket_frame, text="Tenant Id", font=("Bookman Old Style", 20)).place(x=5, y=3)
      tenant_id = ctk.CTkEntry(ticket_frame, width=270,corner_radius=0, state=tk.DISABLED,textvariable=self.tenant_id_var, fg_color="#8d99ae")
      tenant_id.place(x=5, y=30)

      # Email address Field
      ctk.CTkLabel(ticket_frame, text="Email Address", font=("Bookman Old Style", 20)).place(x=5, y=60)
      email_contact = ctk.CTkEntry(ticket_frame,corner_radius=0,textvariable=self.email_contact, border_color="#c9184a", width=270)
      email_contact.place(x=5, y=90)
      email_contact.focus()

      # Phone Number Field
      ctk.CTkLabel(ticket_frame, text="Phone Number", font=("Bookman Old Style", 20)).place(x=5, y=120)
      phone_contact = ctk.CTkEntry(ticket_frame, width=270,corner_radius=0,textvariable=self.phone_contact, border_color="#c9184a")
      phone_contact.place(x=5, y=150)

      # Id Number Field
      ctk.CTkLabel(ticket_frame, text="Tenant Id", font=("Bookman Old Style", 20)).place(x=5, y=180)
      id_no_contact = ctk.CTkEntry(ticket_frame, width=270, corner_radius=0,textvariable=self.id_no_contact, border_color="#c9184a")
      id_no_contact.place(x=5, y=210)

      # username Field
      ctk.CTkLabel(ticket_frame, text="Username", font=("Bookman Old Style", 20)).place(x=5, y=240)
      username_contact = ctk.CTkEntry(ticket_frame, width=270,textvariable=self.username_contact, corner_radius=0, border_color="#c9184a")
      username_contact.place(x=5, y=270)

      # text box widget for subject
      ctk.CTkLabel(ticket_frame, text="---------------------- Subject Matter -------------------------------", font=("Bookman Old Style", 20)).place(x=290, y=5)
      subject_text = ctk.CTkTextbox(ticket_frame, height=50, width=600, font=("Bookman Old style", 20))
      subject_text.place(x=300, y=30)
      #subject_text.focus()


      # text box widget
      ctk.CTkLabel(ticket_frame, text="---------------------- Message -------------------------------------", font=("Bookman Old Style", 20)).place(x=290, y=80)
      message_text = ctk.CTkTextbox(ticket_frame, height=150,fg_color="#e7ecef", width=600, corner_radius=0, font=("Bookman Old style", 20))
      #message_text.focus()
      message_text.place(x=300, y=140)

      # frame for button to change property in textbox
      icon_frame = ctk.CTkFrame(ticket_frame, width=600, height=40, fg_color="white", corner_radius=0)
      icon_frame.place(x=300, y=105)

      # icons
      # bold icon
      bold_img = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/bold.png")
      bold_img = bold_img.resize((20, 25))
      self.bold_photo = ImageTk.PhotoImage(bold_img)

      bold_btn = tk.Button(icon_frame, image=self.bold_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      bold_btn.place(x=4, y=7)

      # italic icon
      italic_icon = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/italic.png")
      italic_icon = italic_icon.resize((15, 18))
      self.italic_photo = ImageTk.PhotoImage(italic_icon)

      italic_btn = tk.Button(icon_frame, image=self.italic_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      italic_btn.place(x=45, y=10)

      # copy icon
      copy_icon = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/copy.jpg")
      copy_icon = copy_icon.resize((30, 25))
      self.copy_photo = ImageTk.PhotoImage(copy_icon)

      copy_btn = tk.Button(icon_frame, image=self.copy_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      copy_btn.place(x=80, y=5)

      # paste icon
      paste_icon = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/paste.png")
      paste_icon = paste_icon.resize((30, 25))
      self.paste_photo = ImageTk.PhotoImage(paste_icon)

      paste_btn = tk.Button(icon_frame, image=self.paste_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      paste_btn.place(x=120, y=5)

      # font icon
      font_icon = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/font.png")
      font_icon = font_icon.resize((30, 25))
      self.font_photo = ImageTk.PhotoImage(font_icon)

      font_btn = tk.Button(icon_frame, image=self.font_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      font_btn.place(x=170, y=5)

      # center icon
      center_icon = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/center.png")
      center_icon = center_icon.resize((30, 25))
      self.center_photo = ImageTk.PhotoImage(center_icon)

      center_btn = tk.Button(icon_frame, image=self.center_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      center_btn.place(x=210, y=5)

      # copy icon
      justify_icon = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/justify.png")
      justify_icon = justify_icon.resize((30, 25))
      self.justify_photo = ImageTk.PhotoImage(justify_icon)

      justify_btn = tk.Button(icon_frame, image=self.justify_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      justify_btn.place(x=250, y=5)

      # attach icon
      attach_icon = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/attach file.png")
      attach_icon = attach_icon.resize((30, 25))
      self.attach_photo = ImageTk.PhotoImage(attach_icon)

      ctk.CTkLabel(icon_frame, text="Attach File", font=('Bookman Old style', 20)).place(x=490, y=5)
      attach_btn = tk.Button(icon_frame, image=self.attach_photo, text="", bg="white" ,width=30, borderwidth=0, activebackground="white", cursor="hand2")
      attach_btn.place(x=440, y=5)

      # Submit Button
      clear_ticket_btn = ctk.CTkButton(ticket_frame, text="Clear",text_color="black" ,font=('Bookman Old style', 20), height=35, cursor="hand2", command=self.clear_contact)
      clear_ticket_btn.place(x=500, y=295)

      # Submit Button
      submit_ticket_btn = ctk.CTkButton(ticket_frame, text="Submit",hover_color="#55a630", font=('Bookman Old style', 20),fg_color="green", height=35, text_color="black" ,cursor="hand2", command=self.submit_contact)
      submit_ticket_btn.place(x=700, y=295)
           

   # logout page
   def logout_view_fun(self):

      # ===================background Image for Rental Houses when exiting===========================
      bg_image = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/rental.jpg")
      bg_image = bg_image.resize((990, 530))
      self.bg_photo = ImageTk.PhotoImage(bg_image)

      image_lbl = tk.Label(self.page_frame, image=self.bg_photo)
      image_lbl.place(x=0, y=0, width=1000, height=530)
      time.sleep(1)
      respose = messagebox.askquestion(title="Logout Status", message="Are you sure you want to Exit? ", parent=self.root)
      if respose == "yes":
         time.sleep(0)
         self.root.destroy()
      else:
         self.rental_view_fun()

   # to delete the current packed frame and load the next
   def delete_page(self):
      for frame in self.page_frame.winfo_children():
         frame.destroy()

   # ====================================Functtions for House ===================================
   def house_btn_click(self):
      self.house_btn.configure(border_width=2, border_color="red")

   def on_configure(self,event):
      self.canvas.configure(scrollregion=self.canvas.bbox("all"))


   def change(self,lb):
      lb.config(bg="red")


   # ==============================Paymen Function Decration========================================
   def complete_payment(self):
      if self.name_var.get() == "":
         messagebox.showerror(title="Payment status", message="Full names must be Filled!!!")
      elif self.phone_var.get() == "":
         messagebox.showerror(title="Payment status", message="Phone Number must be Filled!!!")
      elif len(self.phone_var.get()) < 10:
         messagebox.showerror(title="Payment status", message="Phone Number must be More Than 9 !!")
      elif len(self.phone_var.get()) > 14:
         messagebox.showerror(title="Payment status", message="phone Number should be Less Than 14!!!")
      elif self.id_var.get() == "":
         messagebox.showerror(title="Payment status", message="Id Number must be Filled!!!")
      elif len(self.id_var.get()) != 8:
         messagebox.showerror(title="Payment status", message="Id Number Must be 8 Characters!!!")
      elif self.mpesa_var.get() =="":
         messagebox.showerror(title="Payment status", message="Mpesa Mode Must be Filled!!!")
      else:
         try:
            #Need to connect With the database to record data there
            pass
         except:
            pass
   #==========================clear records================================
   def clear_payment(self):
      self.name_var.set("")
      self.phone_var.set("")
      self.id_var.set("")
      self.mpesa_var.set("LIPA NA MPESA")

   def back_home_payment(self):
      answer = messagebox.askyesno(title="Payment Status", message="Are You sure You want to Exit payment page")
      if answer == True:
         self.hide_indicator()
         # ===================background Image for Rental Houses when exiting===========================
         bg_image = Image.open("C:/Users/FLIVO/Desktop/RENTAL MANAGEMENT SYSTEM/images/rental.jpg")
         bg_image = bg_image.resize((990, 530))
         self.bg_photo = ImageTk.PhotoImage(bg_image)

         image_lbl = tk.Label(self.page_frame, image=self.bg_photo)
         image_lbl.place(x=0, y=0, width=1000, height=530)
      else:
         pass
   
   # ===========================Profile Function Declaration =============================================
   def submit_profile(self):
      if self.f_name_var.get() == "":
         messagebox.showerror(title="Profile Status", message="First Name Must be Filled!!")
      elif self.l_name_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Last Name Must be Filled!!")
      elif self.email_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Email Address Must be Filled!!")
      elif self.f_phone_var.get() == "" and self.l_phone_var.get() == "":
         messagebox.showerror(title="Profile Status", message="One Phone Number Must be Filled!!")
      elif len(self.f_phone_var.get() and self.l_phone_var.get()) > 14:
         messagebox.showerror(title="Profile Status", message="Phone Number Should Be Less than 14 characters!!")
      elif len(self.f_phone_var.get() and self.l_phone_var.get()) < 10:
         messagebox.showerror(title="Profile Status", message="Phone Number Should Be more than 9 characters!!")
      elif self.dob_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Date of Birth Must be Filled!!")
      elif self.gender_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Gender Must be Selected!!")
      elif self.house_var.get() == "":
         messagebox.showerror(title="Profile Status", message="House Type must be selected!!")
      elif self.id_no_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Id Number Must be Filled!!")
      elif len(self.id_no_var.get()) != 8:
         messagebox.showerror(title="Profile Status", message="Id Number Must be 8 Characters!!")
      # emergency
      elif self.f_name_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Emergency First Name Must be Filled!!")
      elif self.l_name_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Emergency Last Name Must be Filled!!")
      elif self.f_phone_em_var.get() == "" and self.l_phone_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Phone Number Must be Filled On Emergency!!")
      elif len(self.f_phone_em_var.get() and self.l_phone_em_var.get()) > 14:
         messagebox.showerror(title="Profile Status", message="Emergency Phone Number Should Be Less than 14 characters!!")
      elif len(self.f_phone_em_var.get() and self.l_phone_em_var.get()) < 10:
         messagebox.showerror(title="Profile Status", message="Emergency Phone Number Should Be more than 9 characters!!")
      elif self.email_em_var.get() == "":
         messagebox.showerror(title="Profile Status", message="Emergency Email Address Must be Filled!!")
      #Acceptance
      elif self.check_accept_var.get() != "yes":
         messagebox.showerror(title="Profile Status", message="You need To Accept stipulated Rules before proceeding!!")

      elif self.check_terms_var.get() != "yes":
         messagebox.showerror(title="Profile Status", message="You need To Accept Terms and conditions  before proceeding!!")

      else:
         try:
            # connect with the Mysql database
            pass
         except:
            pass

   def clear_profile(self):
      self.f_name_var.set("")
      self.l_name_var.set("")
      self.email_var.set("")
      self.f_phone_var.set("")
      self.l_phone_var.set("")
      self.dob_var.set("")
      self.county_var.set("")
      self.gender_var.set("")
      self.house_var.set("")
      self.id_no_var.set("")
      self.f_name_em_var.set("")
      self.l_name_em_var.set("")
      self.email_em_var.set("")
      self.check_accept_var.set("no")
      self.check_terms_var.set("no")

   #====================== Contact us function declaration============================
   def submit_contact(self):
      """
        if self.tenant_id_var.get() == "":
         messagebox.
      """
      if self.email_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Email Address Must be Filled!!!")
      elif self.phone_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Phone Number Must be Filled!!!")
      elif len(self.phone_contact.get()) < 10:
         messagebox.showerror(title="Contact status", message="Phone Number should be more than 9 characters!!!")
      elif len(self.phone_contact.get()) > 14:
         messagebox.showerror(title="Contact status", message="Phone Number should be less than 14 characters!!!")
      elif self.id_no_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Id Number Must be Filled!!!")
      elif len(self.id_no_contact.get()) != 8:
         messagebox.showerror(title="Contact status", message="Phone Number Must be Filled!!!")
      elif self.username_contact.get() == "":
         messagebox.showerror(title="Contact status", message="Username Must be Filled!!!")
         """
         self.subject_var(self) == "":
         self.message-var(self) == "":
         
         """
      else:
         try:
            # Connect with database to save the records, Send the email to the company Email
            pass
         except:
            pass

   # ========clear contact ===========================
   def clear_contact(self):
      self.email_contact.set("")
      self.phone_contact.set("")
      self.id_no_contact.set("")
      self.username_contact.set("")



if __name__ == "__main__":
   root = tk.Tk()
   Tenant_management_main(root)
   root.mainloop()