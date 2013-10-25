from flask import Flask
from callapi import *
app = Flask(__name__)

@app.route("/")
def status():
      return philipsInfo();

@app.route('/on')
def on():
    return philipsControl("on");

@app.route('/off')
def off():
    return philipsControl("off");


if __name__ == "__main__":
      app.run(host='0.0.0.0')

