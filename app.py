from flask import Flask
app = Flask(__name__)
import os

#def get_loadavg():
#    if hasattr(os, 'getloadavg'):
#        return os.getloadavg()
#    return None

@app.route("/")
def get_load():
	return ("Load avg","200",os.getloadavg())

get_load()

