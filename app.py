from flask import Flask
app = Flask(__name__)
import os

@app.route("/")
def get_load():
	return str(os.getloadavg())
