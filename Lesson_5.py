from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
   html = """
     <!doctype html>
     <html>
     <head>
        <title>My fellow madridistas</title>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
     </head>
     <body>
        <h1>Welcome to my hehehehaw</h1>
        <p>This is my kingdom rise.</p>
        <p>Nah i'd win</p>
        <img src="/static/images/Flask_logo.svg" alt="Legacy">
    </body>
    </html>




   """
   return html
app.run(debug=True, port=5000)
