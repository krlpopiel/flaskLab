from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"   

@app.route("/o-mnie")
def o_mnie():
    return "<p>Oto krótkie informacje o mnie.</p>"  

@app.route("/user/<name>")
def user(name):
    return f"<p>Oto informacje o użytkowniku: {name}</p>"  