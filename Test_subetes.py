from flask import Flask, render_template
from datetime import datetime
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    db = sqlite3.connect("DataB/Students_marks.db")
    db.row_factory = sqlite3.Row

    students = db.execute("SELECT * FROM Students").fetchall()

    nameValue = "Bob"
    timeValue = datetime.now().strftime("%Y-%m-%d: %H:%M:%S")
    return render_template("index.html", logged_in=True, name=nameValue, time=timeValue, students=students)

@app.route("/marks")
def marks():
    return render_template("marks.html")

@app.route("/addstudent")
def addstudent():
    return render_template("addstudent.html")

@app.route("/student/<id>")
def student(id):
    db = sqlite3.connect("DataB/Students_marks.db")
    db.row_factory = sqlite3.Row

    studentData = db.execute("SELECT * FROM Students WHERE id = ?", (id,)).fetchone()

    if studentData is None:
        return "Student not found", 404

    markData = db.execute("SELECT * FROM Marks WHERE student_id = ?", (id,)).fetchall()

    return render_template("student.html", student=studentData, marks=markData)

app.run(debug=True, port=5000)