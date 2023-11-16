import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password= '3915',
#     port='3306',
#     database = 'student_management_db',
#
# )
#
# mycursor = db.cursor()
# mycursor.execute('SELECT * FROM students')
# students = mycursor.fetchall()
#
# for i in students:
#     print(f"Name: {i[0]}, ID: {i[1]}, Class: {i[2]}, Address: {i[3]}",end="\n")

# ---------GUI------------
window = Tk()
window.title("Student Management System")
window.config(padx=10, pady=10)
# --canvas--
canvas =Canvas(height=620,  width= 450)
img = Image.open('logo.png')
r_img = img.resize((380,230))
logo = ImageTk.PhotoImage(r_img)
canvas.create_image(220,110, image=logo)
canvas.grid(column = 0, row = 0, columnspan=6,rowspan=6)

# title label--------
title = Label(text="Student Management System",
                # fg="yellow",
                # bg="black",
                font = ("Arial",22,"bold"))
# title.place(relx = 0.05, rely = 0.40, anchor = 'sw')

title.grid(column =0, row = 1, columnspan=6, rowspan=3)

# --search bar--
search = Entry(width=49)

search.grid(column = 1, row=2, columnspan=3, ipady=10,rowspan=2)




# ---button---
search_student = Button(
    text="Search",
    width=15,
    height=2,
    bg="#00C8D3",
    fg="black",
    font=("Arial",11,"bold")
)

add_student = Button(
    text="Add Student",
    width=15,
    height=2,
    bg="#4C9930",
    fg="white",
    font=("Arial",11,"bold")
)
update_student = Button(
    text="Update Student",
    width=15,
    height=2,
    bg="#3F466E",
    fg="white",
    font=("Arial",11,"bold")
)
remove_student = Button(
    text="Remove Student",
    width=15,
    height=2,
    bg="#CF263B",
    fg="white",
    font=("Arial",11,"bold")
)


search_student.grid(column=4,row=2, columnspan=2,rowspan=2)

add_student.grid(column=0,row=3, columnspan=2,rowspan=1)
update_student.grid(column=2,row=3, columnspan=2,rowspan=1)
remove_student.grid(column=4,row=3, columnspan=2,rowspan=1)

# ---data---
# box = Frame(width=100,height=150)
# box.grid(column=0,row=4,columnspan=6)




window.mainloop()





























