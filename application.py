from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hi kc from Azure Web App!--V1.0</h1>"
