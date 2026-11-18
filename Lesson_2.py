from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():


    html = f"""
       <!doctype html>
       <html>
       <head>
           <title>Hei</title>
       </head>
       <body>
           <h1>Welcome to my site</h1>
       </body>
       </html>
    """

    return html


app.run(debug=True, port=5000)