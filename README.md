#Philips Hue Remote Control API

Sicne the Philips Hue [Portal API](http://developers.meethue.com/5_portalapi.html) is not released yet, this API is developed to server the very basic tasks of controlling Philips Hue light remotely.

The work is based on this paper: [Hacking Lightbulbs: Security Evaluation of the Philips Hue Personal Wireless Lighting System](http://www.dhanjani.com/docs/Hacking%20Lighbulbs%20Hue%20Dhanjani%202013.pdf) by [Nitesh Dhanjani](http://www.dhanjani.com/about.html)

The API server is running on top of [flask](http://flask.pocoo.org/)

##REST Endpoint
###/
Get the status of the light bulbs
###/on
Turn on the light bulb
###/off
Turn off the light bulb
###/api
Transparent API POST (=official PUT API)

Example:
```
Official API Endpoint : /api/<username>/lights/<id>/state
Official API Method: PUT
Official API Data: {"ct":153, "colormode":"ct"}

Custom API Endpoint : http://localhost:5000/api/lights/<id>/state
Custom API Method: POST
Custom API Data: EXACT THE SAME AS ABOVE
```
It should in theory support all official PUT API calls to the URL endpoint of ```/api/username/*******```

So any official ```/api/username/**********``` with method PUT
can be achieved using ```http://localhost:5000/api/***********``` with method POST

The response is always 200 unfortunately unless the request body is not JSON format

##Setup
Fill in credentials.py.sample and rename it to credentials.py

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
```On/Off``` is hard coded to work with groups but can also be used with individual lights.
with ```/api``` you can do any method you like but currently only support POST (=PUT on official API)

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