# Philips Hue Remote Control API

This is the unofficial implementation of Philips Hue [Portal API](http://developers.meethue.com/5_portalapi.html). It allows remote control to Philips Hue from outside the local network.

The work is based on [Hacking Lightbulbs: Security Evaluation of the Philips Hue Personal Wireless Lighting System](http://www.dhanjani.com/docs/Hacking%20Lighbulbs%20Hue%20Dhanjani%202013.pdf) by [Nitesh Dhanjani](http://www.dhanjani.com/about.html)

The API server is running on top of [flask](http://flask.pocoo.org/) python web framework. The API server is supposed to run in the cloud, so you can access it from anywhere.

## How Does This Remote API Work?
I wrote a overview explanation of the remote API hack of the Philips Hue in a blog post here: [http://paulshi.github.io/technical/2013/11/27/Philips-Hue-Remote-API-Explained.html](http://paulshi.github.io/technical/2013/11/27/Philips-Hue-Remote-API-Explained.html)

## RESTful API Endpoint

#### /api
(Transparent API)

Features:

 * PUT/POST works just like official API
 * GET will get info for all devices

Limitations:

 * PUT/POST Response is always 200
 * GET only works to root api endpoint (`/api`)
 
The first limitation is due to the private endpoint on Philips Hue website side. It only gives response when it receives or rejects your command, but doesn't tell you whether it succeeded in executing it or not. 
 
Example:

`PUT`/`POST`

	Official API Endpoint : /api/<username>/lights/<id>/state
	Official API Method: PUT
	Official API Data: {"ct":153, "colormode":"ct"}

	Custom API Endpoint : http://localhost:5000/api/lights/<id>/state
	Custom API Method: PUT
	Custom API Data: EXACT THE SAME AS ABOVE

`GET`

	Custom API Endpoint: http://localhost:5000/api
	Custom API Method: GET
		
It should in theory support all official PUT/POST API calls to the URL endpoint of `/api/username/*******`

So any official `/api/username/**********` with method PUT/POST
can be achieved using `http://localhost:5000/api/***********` with method PUT/POST

## Setup
Fill in `credentials.py.sample` and rename it to ```credentials.py```, there are 2 parameters you need to fill:
	
* `ACCESSTOKEN`
* `BRIDGEID`

Steps:

1. Find your `BRIDGEID` from [https://www.meethue.com/api/nupnp](https://www.meethue.com/api/nupnp). (or in [My bridge](https://www.meethue.com/en-US/user/preferencessmartbridge) page on the meethue website and by clicking on "Show me more")

2. Get `ACCESSTOKEN`

		www.meethue.com/en-US/api/gettoken?devicename=iPhone+5&appid=hueapp&deviceid=**BRIDGEID**

3. **Right** click on "BACK TO THE APP" and write down `ACCESSTOKEN` inside the link it redirect to

		phhueapp://sdk/login/**ACCESSTOKEN**


as explained in my [post](http://paulshi.github.io/technical/2013/11/27/Philips-Hue-Remote-API-Explained.html) mentioned earlier.

## Install
Setup virtual environment

```
virtualenv ev
source ev/bin/activate
```

Install required packages

```
pip install -r requirements.txt
```

## Run

```
python hueapiserver.py
```

## Documentation
http://philips-hue-remote-api.readthedocs.org/

## License

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

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/jarvisinc/philipshueremoteapi/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

