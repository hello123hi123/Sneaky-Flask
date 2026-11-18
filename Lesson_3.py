from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <h1>Welcome to my home page</h1>
    <p>Click the link below to navigate</p>
    <img src="/static/images/Flask_logo.svg" width="300">
    <a href=" /about" >Go to about page</a>
    <a href=" /contact" >Go to Contact page</a>
    """
    return html 

    
@app.route("/about")
def about():

    
    html = """
  <h1>Welcome to my about page</h1>
    <p>billie jean is not my lover</p>
    <a href=" /" >Go to Home page</a>
    <a href=" /contact" >Go to Contact page</a>

   
    """

    return html 

@app.route("/contact")
def Contact():

    
    html = """
    <h1>Welcome to my contact page</h1>
    <p>I predict Real madrid will defeat PSG in 2027 ucl final</p>
    <a href=" /about" >Go to about page</a>
    <a href=" /" >Go to Home page</a>

   
    """

    return html 

app.run(debug=True, port=5000)