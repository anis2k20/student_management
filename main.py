import mysql.connector

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

for i in students:
    print(f"Name: {i[0]}, ID: {i[1]}, Class: {i[2]}, Address: {i[3]}",end="\n")