from flask import Flask
app = Flask(__name__)
import os

#def get_loadavg():
#    if hasattr(os, 'getloadavg'):
#        return os.getloadavg()
#    return None

@app.route("/")
def getload(self,):
	return 	getloadavg()[0] 
