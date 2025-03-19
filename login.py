from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib #pip install smtplib
import time

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System | Developed by Devang & Amardeep")
        #self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.config(bg="#fafafa")

        self.otp=''

        #====images=====
        self.phone_image=ImageTk.PhotoImage(file="images/phone.png")
        self.lbl_Phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        #====Login Frame=====
        self.employee_id=StringVar()
        self.password=StringVar()
        self.show_password=False    #Track Password Visibility

        Login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(Login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        self.Id=PhotoImage(file="images/inventory system/Id.png")
        lbl_user=Label(Login_frame,text="Employee ID",image=self.Id,compound=LEFT,padx=25,font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        self.txt_employee_id=Entry(Login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC")
        self.txt_employee_id.place(x=50,y=140,width=250)
        self.txt_employee_id.bind("<Return>",self.focus_password)   #Bind Enter Key

        self.Password=PhotoImage(file="images/inventory system/Password.png")
        lbl_pass=Label(Login_frame,text="Password",image=self.Password,compound=LEFT,padx=25,font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        self.txt_pass=Entry(Login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC")
        self.txt_pass.place(x=50,y=240,width=250)
        self.txt_pass.bind("<Return>", self.login)  # Bind Enter key to login function
        
        # Eye Button to show/hide password
        self.show_password_icon = Image.open("images/inventory system/open_eye.png")
        self.show_password_icon=self.show_password_icon.resize((20,20),Image.LANCZOS)
        self.show_password_icon=ImageTk.PhotoImage(self.show_password_icon)
        
        self.hide_password_icon=Image.open("images/inventory system/close_eye.png")
        self.hide_password_icon=self.hide_password_icon.resize((20,20),Image.LANCZOS)
        self.hide_password_icon=ImageTk.PhotoImage(self.hide_password_icon)

        self.btn_eye = Button(Login_frame,image=self.show_password_icon,bd=0,relief=RIDGE,bg="#ECECEC",cursor="hand2",activebackground="#ECECEC",command=self.toggle_password)
        self.btn_eye.place(x=275, y=240, width=25, height=25)
       
        btn_login=Button(Login_frame,text="Log In",command=self.login,font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(Login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(Login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        btn_forget=Button(Login_frame,text="Forgot Password ?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=100,y=390)

        #=====Frame2======
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Login To Inventory Management System",font=("Arial Rounded MT Bold",13),bg="white").place(x=0,y=15,relwidth=1)
        #btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",cursor="hand2").place(x=200,y=17)

        '''# Add Help Button
        help_button = Button(Login_frame, text="Help", font=("Arial", 12), bg="#00B0F0", fg="white", command=self.open_help_window)
        help_button.place(x=112, y=420, width=120, height=26)

    def open_help_window(self):
        # Create a new window for Help/Support
        help_win = Toplevel(self.root)
        help_win.title("Help & Support")
        help_win.geometry("700x475+400+150")
        help_win.config(bg="#f0f0f0")

        # Title of Help Window
        title = Label(help_win, text="Help & Support", font=("Arial", 20, "bold"), bg="#3f51b5", fg="white")
        title.pack(fill=X)

        # Help Content (e.g., FAQs, Instructions)
        faq_label = Label(help_win, text="Frequently Asked Questions (FAQs):", font=("Arial", 14), bg="#f0f0f0", anchor="w")
        faq_label.place(x=20, y=60)

        faq_text = Text(help_win, height=8, width=70, font=("Arial", 12), wrap=WORD, bg="#f0f0f0", bd=1, relief=SOLID)
        faq_text.insert(END, "1. How to log in?\n - Enter your Employee ID and Password, then click 'Log In'.\n\n"
                             "2. What to do if I forget my password?\n - Click on 'Forget Password?' to reset your password via email.\n\n"
                             "3. How can I contact support?\n - Use the form below to send us a message.\n")
        faq_text.config(state=DISABLED)  # Make the text area non-editable
        faq_text.place(x=20, y=100)

        # Support Form Section
        contact_label = Label(help_win, text="Contact Support:", font=("Arial", 14), bg="#f0f0f0", anchor="w")
        contact_label.place(x=20, y=250)

        name_label = Label(help_win, text="Name", font=("Arial", 12), bg="#f0f0f0", anchor="w")
        name_label.place(x=20, y=280)
        self.name_entry = Entry(help_win, font=("Arial", 12))
        self.name_entry.place(x=100, y=280, width=450)

        email_label = Label(help_win, text="Email", font=("Arial", 12), bg="#f0f0f0", anchor="w")
        email_label.place(x=20, y=310)
        self.email_entry = Entry(help_win, font=("Arial", 12))
        self.email_entry.place(x=100, y=310, width=450)

        message_label = Label(help_win, text="Message", font=("Arial", 12), bg="#f0f0f0", anchor="w")
        message_label.place(x=20, y=340)
        self.message_text = Text(help_win, height=4, width=60, font=("Arial", 12), wrap=WORD, bg="#f0f0f0", bd=1, relief=SOLID)
        self.message_text.place(x=100, y=340)

        # Submit Button to send the inquiry
        submit_button = Button(help_win, text="Submit", font=("Arial", 12), bg="#00B0F0", fg="white", command=self.submit_support_form)
        submit_button.place(x=560, y=435)

    def submit_support_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        message = self.message_text.get("1.0", END).strip()

        if not name or not email or not message:
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        try:
            # Send support email (This can be done using SMTP or by saving the message in a database)
            self.send_support_email(name, email, message)
            messagebox.showinfo("Success", "Your message has been sent to support. We'll get back to you soon.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error sending message: {str(ex)}", parent=self.root)

    def send_support_email(self, name, email, message):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        
        # Add your email credentials
        email_ = email_pass.email_
        pass_ = email_pass.pass_
        
        s.login(email_, pass_)
        
        subject = "Support Inquiry"
        msg = f"Support Inquiry from {name} ({email} )\n\n{message}"
        msg = f"Subject:{subject}\n\n{msg}"
        
        # Send email to support/admin email address
        s.sendmail(email_, "devangngchekar09@gmail.com", msg)
        
        s.quit()'''

        #====Animation Images=====
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="gray")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()
        
        #======All Functions======
    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)

    def login(self, event=None):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error',"All fields are required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error',"Invalid USERNAME/PASSWORD",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")

        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)

    def forget_window(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror('Error',"Employee ID must be required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror('Error',"Invalid Employee ID,try again",parent=self.root)
                else:
                    #======Forget Window=======
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    #call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error,try again",parent=self.root)
                    else:
                        self.forget_win=Toplevel(self.root)
                        self.forget_win.title('RESET PASSWORD')
                        self.forget_win.geometry('400x350+500+100')
                        self.forget_win.focus_force()

                        title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                        self.btn_reset=Button(self.forget_win,text="SUBMIT",command=self.validate_otp,font=("times new roman",15),bg="lightblue",activebackground="lightblue")
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        lbl_new_pass=Label(self.forget_win,text="NEW PASSWORD",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
    
                        lbl_conf_pass=Label(self.forget_win,text="CONFIRM PASSWORD",font=("times new roman",15)).place(x=20,y=225)
                        txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)
                    
                        self.btn_update=Button(self.forget_win,text="UPDATE",command=self.update_password,state=DISABLED,font=("times new roman",15),bg="lightblue",activebackground="lightblue")
                        self.btn_update.place(x=150,y=300,width=100,height=30)

        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)
    
    #Function to move focus to password entry when Enter is pressed
    def focus_password(self,event=None):
        self.txt_pass.focus_set()


    # Function to trigger login when Enter is pressed in password field
    def trigger_login(self, event=None):
        self.login()

    # Function to toggle password visibility
    def toggle_password(self):
        if self.show_password:
            self.txt_pass.config(show="*")
            self.btn_eye.config(image=self.show_password_icon)
            self.show_password = False
        else:
            self.txt_pass.config(show="")
            self.btn_eye.config(image=self.hide_password_icon)
            self.show_password = True

    def update_password(self):
        if self.var_new_pass.get()=="" or self.var_conf_pass.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.forget_win)
        elif self.var_new_pass.get()!= self.var_conf_pass.get():
            messagebox.showerror("Error","New Password & Confirm Password should be same",parent=self.forget_win)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update employee SET pass=? where eid=?",(self.var_new_pass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Success","Password updated successfully",parent=self.forget_win)
                self.forget_win.destroy()
            except Exception as ex:
                messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)
                

    def validate_otp(self):
        if not self.var_otp.get().isdigit():
            messagebox.showerror("Error", "Invalid OTP format. Please enter numbers only.", parent=self.forget_win)
            return
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP, Try again",parent=self.forget_win)

    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        subj='IMS-Reset Password OTP'
        msg=f'Dear Sir/Madam,\n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards,\nIMS Team'
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'

root=Tk()
obj=Login_System(root)
root.mainloop()