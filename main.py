import mysql.connector
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '3915',
    port='3306',
    database = 'student_management_db',
)


# ---------GUI------------
window = Tk()
window.title("Student Management System")
window.config(padx=10, pady=10)
window.geometry('450x650')
# ----style----

s = Style()
s.configure('frame1.TFrame', background='blue')
s.configure('frame2.TFrame', background='yellow')
s.configure('btn.TButton', font =('calibri', 12, 'bold'),foreground = 'black')

# ----widget----
img_frame = Frame(width=430, height=220)
#--canvas--
canvas =Canvas(height=215,  width= 425)
img = Image.open('logo.png')
r_img = img.resize((380,230))
logo = ImageTk.PhotoImage(r_img)
canvas.create_image(215,115, image=logo)
canvas.grid(column = 0, row = 0)

img_frame.grid(column=0, row=0,columnspan=6, rowspan=2)
# title------
title_frame = Frame(width=430, height=50)
title = Label(text="Student Management System",font = ("Arial",22,"bold"))
title.grid(column=0, row=2)
title_frame.grid(column=0,row=2, columnspan=6)

#------message---------
def message(msg):
    messagebox.showinfo("Important", f"{msg}")


# -----popup window-------------------------------------------------------------
def popup():
    top = Toplevel(window)
    top.geometry("345x260")
    top.config(padx=10,pady=10)
    top.title("Add Student")
    Label(top, text="Name ", font=('Arial 12 bold')).grid(column=0,row=0,sticky=W)
    name = Entry(top,width=40)
    name.grid(column=1,row=0,ipady=3, pady=10,sticky=E)

    Label(top, text="ID ", font=('Arial 12 bold')).grid(column=0, row=1, sticky=W)
    id = Entry(top, width=40)
    id.grid(column=1, row=1,ipady=3, pady=10, sticky=E)

    Label(top, text="Study ", font=('Arial 12 bold')).grid(column=0, row=2, sticky=W)
    study = Entry(top, width=40)
    study.grid(column=1, row=2,ipady=3, pady=10, sticky=E)

    Label(top, text="Address ", font=('Arial 12 bold')).grid(column=0, row=3, sticky=W)
    address = Entry(top, width=40)
    address.grid(column=1, row=3, ipady=3, pady=10, sticky=E)

    add = Button(top,text="ADD", width=15, style='btn.TButton', command=lambda:[message("Added Suceessfully!"),insert(name,id,study,address)])
    add.grid(column=0, row=4,sticky="EW", pady=10, columnspan=2, ipady=5)


# -----remove student popup------
def remove_popup():
    top = Toplevel(window)
    top.geometry("345x130")
    top.config(padx=10, pady=10)
    top.title("Remove Student")
    Label(top, text="ID ", font=('Arial 12 bold')).grid(column=0, row=0, sticky=W)
    id = Entry(top, width=48)
    id.grid(column=1, row=0, ipady=3, pady=10, sticky=E)

    remove_btn = Button(top, text="REMOVE", width=15, style='btn.TButton',command=lambda:[message("Remove Successfully!"),remove(id)])
    remove_btn.grid(column=0, row=4, sticky="EW", pady=10, columnspan=2, ipady=5)


# ---------update student popup---------
def update_popup():
    top = Toplevel(window)
    top.geometry("400x260")
    top.config(padx=10, pady=10)
    top.title("Update Student Data")

    Label(top, text="ID ", font=('Arial 12 bold')).grid(column=0, row=0, sticky=W)
    id = Entry(top, width=35)
    id.grid(column=1, row=0, ipady=3, pady=10, sticky=W)

    def update(id,name,study,address):
        id = id
        name = name.get()
        study = study.get()
        address = address.get()

        try:
            with db.cursor() as cursor:
                sql = f"UPDATE students SET name='{name}',class='{study}',address='{address}' WHERE id={id}"
                cursor.execute(sql)
            db.commit()
        finally:
            pass




    def search_result(id):
        id = id.get()
        s_id = int(id)
        try:
            with db.cursor() as cursor:
                sql = f"SELECT * FROM students WHERE id={s_id}"
                cursor.execute(sql)
                row = cursor.fetchall()

                # empty field--------
                Label(top, text="Name ", font=('Arial 12 bold')).grid(column=0, row=1, sticky=W)
                name = Entry(top, width=35)
                name.insert(0,f"{row[0][0]}")
                name.grid(column=1, row=1, ipady=3, pady=10, sticky=W, columnspan=2)

                Label(top, text="Study ", font=('Arial 12 bold')).grid(column=0, row=2, sticky=W)
                study = Entry(top, width=35)
                study.insert(0,f"{row[0][2]}")
                study.grid(column=1, row=2, ipady=3, pady=10, sticky=W, columnspan=2)

                Label(top, text="Address ", font=('Arial 12 bold')).grid(column=0, row=3, sticky=W)
                address = Entry(top, width=35)
                address.insert(0, f"{row[0][3]}")
                address.grid(column=1, row=3, ipady=3, pady=10, sticky=W, columnspan=2)

                update_btn = Button(top, text="UPDATE", width=15, style='btn.TButton', command=lambda:[update(s_id,name,study,address), message("Data Update Successfully!")])
                update_btn.grid(column=0, row=4, sticky="EW", pady=10, columnspan=3, ipady=3)

        finally:
            # db.close()
            pass


    search_btn = Button(top, text="Search", width=10, style='btn.TButton',command=lambda: [search_result(id)])
    search_btn.grid(column=2,row=0, sticky=E,pady=10, ipady=2)



# -------------src result------
def src_result(id):

    id = id.get()
    def info_message(rows):
        messagebox.showinfo("Student Information",f"ID: {id}\nName: {rows[0][0]}\nStudy: {rows[0][2]}\nAddress: {rows[0][3]}")

    try:
        with db.cursor() as cursor:
            sql = f"SELECT * FROM students WHERE id={id}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            info_message(rows)
    finally:
        pass



# ------Remove data from popup form------
def remove(id):
    s_id = id.get()

    try:
        with db.cursor() as cursor:
            sql = "DELETE FROM students WHERE id=%s"
            val = [(s_id,)]
            cursor.executemany(sql,val)
        db.commit()
    finally:
        pass


# -------insert Data from popup form----
def insert(name,id,study,address):
    s_name = name.get()
    s_id = id.get()
    s_study = study.get()
    s_address = address.get()
    try:
        with db.cursor() as cursor:
            sql = "INSERT INTO students(name,id,class,address) VALUES (%s,%s,%s,%s)"
            val = [(s_name,s_id,s_study,s_address)]
            cursor.executemany(sql,val)
        db.commit()
    finally:
        pass
        # db.close()

#button------
add_student = Button(text="Add Student", width=15,style='btn.TButton', command=popup)
update_student = Button(text="Update Student",width=15,style='btn.TButton',command=update_popup)
remove_student = Button(text="Remove Student",width=15,style='btn.TButton',command=remove_popup)

add_student.grid(column=0, row=3,sticky="W", columnspan=2, ipady=6)
update_student.grid(column=0, row=3,sticky="E", columnspan=2, ipady=6)
remove_student.grid(column=0, row=3, columnspan=2, ipady=6)

# ------search bar---------
search = Entry(width=45)
search.grid(column = 0, row=4, columnspan=3,pady=10, sticky="W",ipady=8,rowspan=2)

search_btn = Button(text="Search", width=15,style='btn.TButton',command=lambda:[src_result(search)])
search_btn.grid(column=0, row=4,sticky="E", pady=10, columnspan=2, ipady=6)

# ----------Text box--------
box = Text(height=14,width=50,padx=11,pady=10)


#---fetch data from database---
try:
    with db.cursor() as cursor:
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        students = cursor.fetchall()
        for i in students:
            box.insert(END,f"Name: {i[0]}\n")
            box.insert(END, f"ID: {i[1]}\n")

            box.insert(END, f"Study: {i[2]}\n")
            box.insert(END, f"Address: {i[3]}\n")
            box.insert(END,"\n")

finally:
    # db.close()
    pass

    # box.insert(END,f"Name: {i[0]}\n, ID: {i[1]}\n, Class: {i[2]}\n, Address: {i[3]}\n")
box.grid(column=0, row=6, sticky='W',ipady=5)











window.mainloop()





























