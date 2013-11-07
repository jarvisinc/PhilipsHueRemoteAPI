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

def constructCustomMsg(apiEndPoint, command):
  #apiEndPoint and command needs to be string
  #command needs to conform to json format
  custom_control_message_structure = 'clipmessage={ bridgeId: "'+bridgeID+'", clipCommand: { url: "/api/0/'+apiEndPoint+'", method: "PUT", body: '+command+' } }'
  return custom_control_message_structure

def philipsControlCustom(msgToSent):
  payload = {'token':token};
  r = requests.post(API_ADDRESS_CONTROL, params=payload,headers=headers,data=msgToSent);
  return r.text

def philipsControl(action):
  payload = {'token':token};
  r = requests.post(API_ADDRESS_CONTROL, params=payload,headers=headers,data=messageToSent(action));
  return r.text

def philipsInfo():
  payload = {'token': token, 'bridgeid': bridgeID};
  r = requests.get(API_STATUS_ADDRESS, params=payload)
  print (json.dumps(json.loads(r.content),indent=4))
  res = json.loads(r.content);
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

def messageToSent(action):
  if (action == "on"):
    return on_message;
  elif (action == "off"):
    return off_message;
  else:
    return "not correct instruction"

def api(request,path):
  print (request.headers)
  print request.headers["Content-Type"]
  print "Request Path: {}".format(path)
  apiEndPoint=path
  # Verify the JSON format
  result = request.get_json(force=True, silent=True, cache=True)
  if result:
    print "JSON: {}".format(result)
    print "JSON String: {}".format(json.dumps(result))
    command = json.dumps(result)
    apiEndPoint = path
    contentToBeRequested=constructCustomMsg(apiEndPoint, command)
    print "constructed custom msg: {}".format(contentToBeRequested)
    print "sending control"
    philipsControlCustom(contentToBeRequested)
    response = make_response('{"status":200}')
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
