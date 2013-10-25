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

def philipsControl(action):
  payload = {'token':token};
  r = requests.post(API_ADDRESS_CONTROL, params=payload,headers=headers,data=messageToSent(action));
  return r.text

def philipsInfo():
  payload = {'token': token, 'bridgeid': bridgeID};
  r = requests.get(API_STATUS_ADDRESS, params=payload)
  # print (r.content.lights);
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

