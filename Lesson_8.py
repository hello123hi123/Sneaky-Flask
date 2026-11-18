from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def home():
    nameValue = "Bob"
    timeValue = datetime.now().strftime("%Y-%m-%d: %H:%M:%S")
    rowCount = 100

    return render_template('index.html', logged_in=True, name =nameValue, time=timeValue, rows=rowCount)

app.run(debug=True, port=5000)
