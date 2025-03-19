from tkinter import*
#pip install pillow
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3
class categoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Category Page")
        self.root.config(bg="White")
        self.root.focus_force()
        #=================================
        #======Variables======
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        #=====title=====
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="yellow",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)

        lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_title=Entry(self.root,textvariable=self.var_name,font=("goudy old style",20),bg="lightyellow").place(x=50,y=170,width=300)

        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15,"bold"),relief=RAISED,bg="#4caf50",fg="white",activebackground="#4caf50",cursor="hand2").place(x=360,y=170,width=100,height=35)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15,"bold"),relief=RAISED,bg="red",fg="white",activebackground="red",cursor="hand2").place(x=475,y=170,width=100,height=35)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15,"bold"),relief=RAISED,bg="#2196f3",fg="white",activebackground="#2196f3",cursor="hand2").place(x=590,y=170,width=100,height=35)

        #===Category Details===
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=700,y=100,width=380,height=105)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        self.categoryTable.heading("cid",text="C ID")
        self.categoryTable.heading("name",text="Name")
        self.categoryTable["show"]="headings"
        self.categoryTable.column("cid",width=90)
        self.categoryTable.column("name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)

        #====images====
        self.im1=Image.open("images/cat.jpg")
        self.im1=self.im1.resize((500,250),Image.LANCZOS)
        self.im1=ImageTk.PhotoImage(self.im1)

        self.lbl_im1=Label(self.root,image=self.im1,bd=2,relief=RAISED)
        self.lbl_im1.place(x=50,y=220)

        self.im2=Image.open("images/category1.jpg")
        self.im2=self.im2.resize((500,250),Image.LANCZOS)
        self.im2=ImageTk.PhotoImage(self.im2)

        self.lbl_im2=Label(self.root,image=self.im2,bd=2,relief=RAISED)
        self.lbl_im2.place(x=580,y=220)

        self.show()

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Category name should be required",parent=self.root)
            else:
                cur.execute("Select * from category where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already present, try different",parent=self.root)
                else:
                    cur.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from category")
            rows=cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        #print(row)
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),
    
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Please Select Category from the list", parent=self.root)
            else:
                cur.execute("Select * from category where cid=?", (self.var_cat_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Error, please try again", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM category WHERE cid=?", (self.var_cat_id.get(),))
                        con.commit()
                        # Reset auto-increment behavior
                        cur.execute("DELETE FROM sqlite_sequence WHERE name='category'")
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


    
    def clear(self):
        self.var_cat_id.set(""),
        self.var_name.set(""),
        self.show()


if __name__=="__main__":
    root=Tk()
    obj=categoryClass(root)
    root.mainloop()