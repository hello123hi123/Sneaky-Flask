from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')   

@app.route("/Marks")
def Marks():
    return render_template('marks.html')   

app.run(debug=True,port=5000)
