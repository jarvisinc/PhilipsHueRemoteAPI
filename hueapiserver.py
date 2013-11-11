from flask import Flask,request
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

@app.route('/api', methods=['GET'])
def apiHandlerDefault():
	return api(request,'');

@app.route('/api/', methods=['GET'])
def apiHandlerDefault2():
	return api(request,'');


@app.route('/api/<path:path>',methods=['POST','PUT'])
def apiHandler(path):
	return api(request,path);

if __name__ == "__main__":
      app.run(host='0.0.0.0', debug=True)


