from flask import Flask
from flask import request

app = Flask(__name__)
import os

@app.route("/loadavg")
def get_load():
	return str(os.getloadavg())
	return 'HTTP GET loadavg Page'
app.add_url_rule('/loadavg', 'get_load', get_load)

if __name__=="__main__":
	app.run(host='0.0.0.0')
