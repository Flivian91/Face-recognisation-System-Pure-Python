import customtkinter as ctk
from tkinter import *


class Forgot():
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x350+700+70")
        # label to show reset password
        reset_label = ctk.CTkLabel(self.root, text="Reset Password",font=("Bookman Old style", 20))
        reset_label.place(x=120, y=10)

        # label to show what to feed
        put_label = ctk.CTkLabel(self.root, text="Input your Registered Email to reset password",font=("Bookman Old style", 20))
        put_label.place(x=20, y=50)

        # username label
        username_l = ctk.CTkLabel(self.root, text="Email",font=("Bookman Old style", 20),anchor=ctk.W)
        username_l.place(x=30, y=80)
        star = ctk.CTkLabel(self.root, text="*",anchor=ctk.W,text_color="red")
        star.place(x=83, y=75)

        # email entry field
        email_entry_var = ctk.StringVar()
        email_entry = ctk.CTkEntry(self.root, textvariable=email_entry_var,width=430,height=40,text_color="blue",border_width=3,border_color="light pink")
        email_entry.place(x=30, y=110)

        # submit button
        def submit():
            pass
        submit_btn = ctk.CTkButton(self.root,width=430,height=40,border_width=1,fg_color="green",text="Submit",text_color="black",font=("bookman old style", 20),command=submit)
        submit_btn.place(x=30, y=170)
        # Label for details
        detail_l = ctk.CTkLabel(self.root, text="If your email corresponds to a valid user, we will send a link to\n""reset your password.",font=("Bookman Old style", 16),anchor=ctk.W)
        detail_l.place(x=3, y=230)

        # Label for details
        done_l = ctk.CTkLabel(self.root, text="Done Here?",font=("Bookman Old style", 16),anchor=ctk.W)
        done_l.place(x=10, y=290)

        # login
        done_l = ctk.CTkButton(self.root, text="Login?",font=("Bookman Old style", 16),anchor=ctk.W,width=20,cursor='hand2',text_color="blue",fg_color="transparent",hover_color="white")
        done_l.place(x=100, y=290)


if __name__ == "__main__":
    root = Tk()
    obj = Forgot(root)
    root.mainloop()
