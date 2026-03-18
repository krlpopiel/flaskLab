from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")  

@app.route("/o-mnie")
def o_mnie():
    return "<p>Oto krótkie informacje o mnie.</p>"  

@app.route("/user/<name>")
def user(name):
    return f"<p>Oto informacje o użytkowniku: {name}</p>"  