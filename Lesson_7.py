from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

@app.route("/")
def home():
    nameValue = "Bob"
    timeValue = datetime.now().strftime("%Y-%m-%d: %H:%M:%S")

    return render_template('index.html', name =nameValue, time=timeValue )


@app.route("/Random")
def Random():
    RandomValue = random.randint(1, 10000)

    return render_template('random.html', randomNumber = RandomValue)

app.run(debug=True, port=5000)

