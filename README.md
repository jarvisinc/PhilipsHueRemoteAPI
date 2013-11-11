#Philips Hue Remote Control API

Sicne the Philips Hue [Portal API](http://developers.meethue.com/5_portalapi.html) is not yet released, this API is developed so that it is possible to control philips hue remotely.

The work is based on [Hacking Lightbulbs: Security Evaluation of the Philips Hue Personal Wireless Lighting System](http://www.dhanjani.com/docs/Hacking%20Lighbulbs%20Hue%20Dhanjani%202013.pdf) by [Nitesh Dhanjani](http://www.dhanjani.com/about.html)

The API server is running on top of [flask](http://flask.pocoo.org/) python web framework.

##REST Endpoint
###/ (depreciated)
Get the status of the light bulbs
###/on (depreciated)
Turn on the light bulb
###/off (depreciated)
Turn off the light bulb
###/api
Transparent API

##Transparent API Layer (/api)
This is a work in progress. It is aimed to support PUT/POST/GET
 * PUT/POST works just like official API
 * The response from PUT/POST is always 200. The call to the API endpoint discovered by the paper only give limited response
 * GET will get all the current status of the Philips Hue bridge

Example:
```
Official API Endpoint : /api/<username>/lights/<id>/state
Official API Method: PUT
Official API Data: {"ct":153, "colormode":"ct"}

Custom API Endpoint : http://localhost:5000/api/lights/<id>/state
Custom API Method: PUT
Custom API Data: EXACT THE SAME AS ABOVE
```
It should in theory support all official PUT API calls to the URL endpoint of ```/api/username/*******```

So any official ```/api/username/**********``` with method PUT
can be achieved using ```http://localhost:5000/api/***********``` with method POST

The response is always 200 unfortunately unless the request body is not JSON format

##Setup
Fill in credentials.py.sample and rename it to credentials.py
In order for it to work you need a token and bridgeID

##Install
Setup virtual environment

```
virtualenv ev
source ev/bin/activate
```

Install required packages

```
pip install -r requirements.txt
```

##Run

```
python hueapiserver.py
```

##Limitations
```On/Off``` is hard coded to work with groups. It's probably shouldn't be included in the API anyway and is part of the legacy code.

With```/api``` you can do PUT/POST to control correctly, GET will get you all the status. Other method is not supported at the moment

##Documentation
http://philips-hue-remote-api.readthedocs.org/

##License
```
The MIT License (MIT)

Copyright (c) 2013 Jarvis Inc (by Jianer Shi hipaulshi@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```