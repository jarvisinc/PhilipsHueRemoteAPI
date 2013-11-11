from flask import Flask,request, make_response, jsonify
import requests;
import json;
from credentials import token,bridgeID;

#setup
API_ADDRESS_CONTROL = 'https://www.meethue.com/api/sendmessage'
API_STATUS_ADDRESS = 'https://www.meethue.com/api/getbridge'
ContentType='application/x-www-form-urlencoded'
on_message = 'clipmessage={ bridgeId: "'+bridgeID+'", clipCommand: { url: "/api/0/groups/0/action", method: "PUT", body: {"on":true} } }'
off_message = 'clipmessage={ bridgeId: "'+bridgeID+'", clipCommand: { url: "/api/0/groups/0/action", method: "PUT", body: {"on":false} } }'
headers = {'content-type':ContentType}

#global const
PUT = 'PUT'
GET = 'GET'
DELETE = 'DELETE'
POST = 'POST'


def constructCustomMsg(apiEndPoint, command, method):
  """
  method can be PUT/POST/GET all must be string
  apiEndPoint is 
  command is JSON format same as the official documentation

  :type apiEndPoint: str
  :param apiEndPoint: The same as oficial API /api/<username>/\*\*\* by removing /api/<usename>/ part
  :type command: str
  :param command: JSON string of the command to be sent
  :type method: str
  :param command: PUT/GET/POST/DELETE in string format
  :rtype: str
  :return: the actual API call body sent to the official server

  """
  #apiEndPoint and command needs to be string
  #command needs to conform to json format
  custom_control_message_structure = 'clipmessage={ bridgeId: "'+bridgeID+'", clipCommand: { url: "/api/0/'+apiEndPoint+'", method: "'+method+'", body: '+command+' } }'
  return custom_control_message_structure

def philipsControlCustom(msgToSent):
  """
  actual message sender

  """
  payload = {'token':token};
  r = requests.post(API_ADDRESS_CONTROL, params=payload,headers=headers,data=msgToSent);
  return r.text

def philipsControl(action):
  payload = {'token':token};
  r = requests.post(API_ADDRESS_CONTROL, params=payload,headers=headers,data=messageToSent(action));
  return r.text

def philipsInfo():
  """
  :return: return true if all lights are on, otherwise false

  """ 
  res = getPhilipsHueInfo()
  # print (res['lights']['1']['name']);
  numreachable = 0;
  numon = 0;
  for key in res['lights']:
    reachable = res['lights'][key]['state']['reachable'];
    if (reachable == True):
      numreachable = numreachable+1;
      # print (res['lights'][key]['name']);
      isOn=res['lights'][key]['state']['on'];
      if (isOn):
        numon=numon+1;
  # print numreachable;
  # print numon;
  if (numreachable == numon):
    # print ('all on');
    return 'True';
  else:
    # print ('not all on');
    return 'False';

def getPhilipsHueInfo():
  """
  This method get all info related the the hue bridge

  """
  payload = {'token': token, 'bridgeid': bridgeID};
  r = requests.get(API_STATUS_ADDRESS, params=payload)
  print (json.dumps(json.loads(r.content),indent=4))
  res = json.loads(r.content);
  return res

def messageToSent(action):
  """
  this method construct message to sent in order to turn on or off ALL lights+light strip in the system
  
  :type action: str
  :param action: on/off

  """
  if (action == "on"):
    return on_message;
  elif (action == "off"):
    return off_message;
  else:
    return "not correct instruction"

def api(request,path):
  """
  This class can handle PUT and POST, as a pass-through layer to the official API.
  The response code will always be 200 regardless of the status.
  The GET method will be the same as the official api call to endpoint /api. A full list of all the status of Philips Hue system
  
  :param request: request from flask
  :param path: path info following /api/\*\*\*\*

  """
  print ("The request method is :{}").format(request.method)
  print (request.headers)
  print request.headers["Content-Type"]
  print "Request Path: {}".format(path)
  # apiEndPoint=path
  # Verify the JSON format
  result = request.get_json(force=True, silent=True, cache=True)

  if request.method == 'PUT' or request.method == 'POST':
    if result:
      print "JSON: {}".format(result)
      print "JSON String: {}".format(json.dumps(result))
      command = json.dumps(result)
      apiEndPoint = path
      contentToBeRequested=constructCustomMsg(apiEndPoint, command, request.method)
      print "constructed custom msg: {}".format(contentToBeRequested)
      print "sending control"
      response = make_response(philipsControlCustom(contentToBeRequested))
      # response = make_response('{"status":200}')
      response.mimetype='application/json'
      return response
    else:
      error_msg = "not a valid json request"
      response_json = jsonify(error=error_msg  ,
                     request_received=request.data)
      response = make_response(response_json)
      response.mimetype='application/json'
      print "Not valid JSON"
      return response
  else:
    res=getPhilipsHueInfo()
    response = make_response(json.dumps(res))
    response.mimetype='application/json'
    return response