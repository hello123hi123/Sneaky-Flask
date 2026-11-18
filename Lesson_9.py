import sqlite3

db = sqlite3.connect("DataB/Students_marks.db")


db.row_factory = sqlite3.Row

Students = db.execute("SELECT * From Students").fetchall()



for person in Students:
 print (f"Firstname: {person['firstname']}, Lastname: {person['lastname']}, DOB: {person['dob']}")

 Marks = db.execute("SELECT * From Marks").fetchall()



for mark in Marks:
 print (f"Student_id: {mark['student_id']}, Subject: {mark['subject']}, mark: {mark['mark']}")



       

