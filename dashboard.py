from tkinter import*
#pip install pillow
from PIL import Image,ImageTk 
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
from tkinter import ttk,messagebox
import sqlite3
import os
import time

class IMS:
    def __init__(self,root):
        self.root=root
        #self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.title("Inventory Management System | Developed by Devang & Amardeep")
        self.root.config(bg="White")

        #--title--
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Algerian",40,"bold"),bg="#010c48",fg="White",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #--logout_button--
        self.icon_side_logout=PhotoImage(file="images/inventory system/logout.png")
        btn_logout=Button(self.root,text="Logout",command=self.logout,image=self.icon_side_logout,compound=LEFT,padx=15,font=("Times New Roman",16,"bold"),bg="#333C6C",activebackground="black",fg="white",activeforeground="#666D91",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #--clock--
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("Times New Roman",15),bg="#4d636d",fg="White")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #--Left Menu--
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="White")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("Times New Roman",20),bg="#009688").pack(side=TOP,fill=X)

        self.icon_side_employee=PhotoImage(file="images/inventory system/management.png")
        self.icon_side_supplier=PhotoImage(file="images/inventory system/supply.png")
        self.icon_side_category=PhotoImage(file="images/inventory system/category1.png")
        self.icon_side_product=PhotoImage(file="images/inventory system/product1.png")
        self.icon_side_sales=PhotoImage(file="images/inventory system/sales1.png")
        self.icon_side_exit=PhotoImage(file="images/inventory system/exit.png")

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side_employee,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="White",activebackground="#D3D3D3",activeforeground="red",bd=3,cursor="hand2")
        btn_employee.pack(side=TOP,fill=X)
        btn_employee.bind("<Enter>",lambda event: self.on_enter(event,btn_employee))
        btn_employee.bind("<Leave>",lambda event: self.on_leave(event,btn_employee))
        
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side_supplier,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="White",activebackground="#D3D3D3",activeforeground="red",bd=3,cursor="hand2")
        btn_supplier.pack(side=TOP,fill=X)
        btn_supplier.bind("<Enter>",lambda event: self.on_enter(event,btn_supplier))
        btn_supplier.bind("<Leave>",lambda event: self.on_leave(event,btn_supplier))
        
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side_category,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="White",activebackground="#D3D3D3",activeforeground="red",bd=3,cursor="hand2")
        btn_category.pack(side=TOP,fill=X)
        btn_category.bind("<Enter>",lambda event: self.on_enter(event,btn_category))
        btn_category.bind("<Leave>",lambda event: self.on_leave(event,btn_category))
        
        btn_product=Button(LeftMenu,text="Product",command=self.product,image=self.icon_side_product,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="White",activebackground="#D3D3D3",activeforeground="red",bd=3,cursor="hand2")
        btn_product.pack(side=TOP,fill=X)
        btn_product.bind("<Enter>",lambda event: self.on_enter(event,btn_product))
        btn_product.bind("<Leave>",lambda event: self.on_leave(event,btn_product))

        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side_sales,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="White",activebackground="#D3D3D3",activeforeground="red",bd=3,cursor="hand2")
        btn_sales.pack(side=TOP,fill=X)
        btn_sales.bind("<Enter>",lambda event: self.on_enter(event,btn_sales))
        btn_sales.bind("<Leave>",lambda event: self.on_leave(event,btn_sales))

        btn_exit=Button(LeftMenu,text="Exit",command=self.confirm_exit,image=self.icon_side_exit,compound=LEFT,padx=5,anchor="w",font=("Times New Roman",20,"bold"),bg="White",activebackground="#D3D3D3",activeforeground="red",bd=3,cursor="hand2")
        btn_exit.pack(side=TOP,fill=X)
        btn_exit.bind("<Enter>",lambda event: self.on_enter(event,btn_exit))
        btn_exit.bind("<Leave>",lambda event: self.on_leave(event,btn_exit))

        #--content--
        self.total_employee=PhotoImage(file="images/inventory system/total_emp.png")
        self.lbl_employee=Label(self.root,image=self.total_employee,compound=TOP,pady=3,text="Total Employee\n[ 0 ]",bd=10,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=200,width=300)

        self.total_supplier=PhotoImage(file="images/inventory system/total_sup.png")
        self.lbl_supplier=Label(self.root,image=self.total_supplier,compound=TOP,pady=3,text="Total Supplier\n[ 0 ]",bd=10,relief=RIDGE,bg="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=200,width=300)

        self.total_category=PhotoImage(file="images/inventory system/total_cat.png")
        self.lbl_category=Label(self.root,image=self.total_category,compound=TOP,pady=3,text="Total Category\n[ 0 ]",bd=10,relief=RIDGE,bg="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=200,width=300)

        self.total_product=PhotoImage(file="images/inventory system/total_prod.png")
        self.lbl_product=Label(self.root,image=self.total_product,compound=TOP,pady=3,text="Total Product\n[ 0 ]",bd=10,relief=GROOVE,bg="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=370,height=200,width=300)

        self.total_sales=PhotoImage(file="images/inventory system/total_sales.png")
        self.lbl_sales=Label(self.root,image=self.total_sales,compound=TOP,pady=3,text="Total Sales\n[ 0 ]",bd=10,relief=GROOVE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=370,height=200,width=300)

        self.total_low_stock=PhotoImage(file="images/inventory system/total_stock.png")
        self.lbl_low_stock=Label(self.root,image=self.total_low_stock,compound=TOP,pady=3,text="Low Stock Items\n[ 0 ]",bd=10,relief=GROOVE,bg="#F44336",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_low_stock.place(x=1000,y=370,height=200,width=300)

        #--footer--
        lbl_footer=Label(self.root,text="IMS - Inventory Management System | Developed by Devang & Amardeep \n"
         "Contact Our Team: +91 9876543210 / +91 8976543210 \t " "\t|\t"
         "Email: support@ims.com | Website: www.ims.com \t" "\t|\t"
         "Version: 1.0.0 | © 2025 IMS. All rights reserved.",font=("Times New Roman",10),bg="#4d636d",fg="White").pack(side=BOTTOM,fill=X)

        self.update_content()
#=================================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
    
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            # Updating product count
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[ {str(len(product))} ]')
            
            # Updating supplier count
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[ {str(len(supplier))} ]')
            
            # Updating category count
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')
            
            # Updating employee count
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[ {str(len(employee))} ]')

            # Updating sales count
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[ {str(bill)}]')

            # Reopen the connection before fetching low stock
            con.commit()
            con.close()  # Close old connection
            con = sqlite3.connect(database=r'ims.db')  # Reopen connection
            cur = con.cursor()

            # Updating low stock count (products with quantity < 11)
            cur.execute("SELECT COUNT(*) FROM product WHERE qty < 11")
            low_stock = cur.fetchone()[0]
            self.lbl_low_stock.config(text=f'Low Stock Items\n[ {str(low_stock)} ]')
            
            # Updating Clock
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        except Exception as ex:
            messagebox.showerror('Error',f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    def on_enter(self,event,button):
        button.config(bg='#899499', fg='blue')      # Change background and foreground on hover

    def on_leave(self,event,button):
        button.config(bg='White', fg='black')       # Reset background and foreground on leave

    def confirm_exit(self):
        # Display a message box to confirm exit
        result = messagebox.askyesno("Confirm", "Do you really want to exit?")
        if result:  # If the user clicked 'Yes'
            self.root.destroy()  # Close the application
        else:
            pass  # If 'No', do nothing and return to the app

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()