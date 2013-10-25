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
###/status
Same as /

##Setup
Fill in credentials.py.sample and rename it to credentials.py

##Install
Setup virtual environment
```
virtualenv ev
```
Activate virtual environment
```
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
It is hard coded to work with groups but can also be used with individual lights.

##License
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