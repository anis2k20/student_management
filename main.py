import mysql.connector
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageTk
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '3915',
    port='3306',
    database = 'student_management_db',
)

mycursor = db.cursor()
mycursor.execute('SELECT * FROM students')
students = mycursor.fetchall()
# ------SQL for insert user------
# sql = "INSERT INTO students(name,id,class,address) VALUES (%s,%s,%s,%s)"
# val = ("Sofikul",107,"JSC","Gazipur")
# mycursor.execute(sql,val)
# db.commit()



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



# -----popup window-------------------------------------------------------------
def popup():
    top = Toplevel(window)
    top.geometry("345x260")
    top.config(padx=10,pady=10)
    top.title("Add Student")
    Label(top, text="Name ", font=('Arial 12 bold')).grid(column=0,row=0,sticky=W)
    input = Entry(top,width=40).grid(column=1,row=0,ipady=3, pady=10,sticky=E)

    Label(top, text="ID ", font=('Arial 12 bold')).grid(column=0, row=1, sticky=W)
    input = Entry(top, width=40).grid(column=1, row=1,ipady=3, pady=10, sticky=E)

    Label(top, text="Study ", font=('Arial 12 bold')).grid(column=0, row=2, sticky=W)
    input = Entry(top, width=40).grid(column=1, row=2,ipady=3, pady=10, sticky=E)

    Label(top, text="Address ", font=('Arial 12 bold')).grid(column=0, row=3, sticky=W)
    input = Entry(top, width=40).grid(column=1, row=3, ipady=3, pady=10, sticky=E)

    add = Button(top,text="ADD", width=15, style='btn.TButton')
    add.grid(column=0, row=4,sticky="EW", pady=10, columnspan=2, ipady=5)




#button------
add_student = Button(text="Add Student", width=15,style='btn.TButton', command=popup)
update_student = Button(text="Update Student",width=15,style='btn.TButton')
remove_student = Button(text="Remove Student",width=15,style='btn.TButton')

add_student.grid(column=0, row=3,sticky="W", columnspan=2, ipady=6)
update_student.grid(column=0, row=3,sticky="E", columnspan=2, ipady=6)
remove_student.grid(column=0, row=3, columnspan=2, ipady=6)

# ------search bar---------
search = Entry(width=45)
search.grid(column = 0, row=4, columnspan=3,pady=10, sticky="W",ipady=8,rowspan=2)

search_btn = Button(text="Search", width=15,style='btn.TButton')
search_btn.grid(column=0, row=4,sticky="E", pady=10, columnspan=2, ipady=6)

# ----------Text box--------
box = Text(height=14,width=50,padx=11,pady=10)








#---fetch data from database---
for i in students:
    box.insert(END,f"Name: {i[0]}\n")
    box.insert(END, f"ID: {i[1]}\n")
    box.insert(END, f"Study: {i[2]}\n")
    box.insert(END, f"Address: {i[3]}\n")
    box.insert(END,"\n\n")
    # box.insert(END,f"Name: {i[0]}\n, ID: {i[1]}\n, Class: {i[2]}\n, Address: {i[3]}\n")
box.grid(column=0, row=6, sticky='W',ipady=5)











window.mainloop()





























