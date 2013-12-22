"""

Getting Access Token via scrapping
Very unreliable, just for testing, may break easily with any format change on the official website.
No other part of the API relies on the ACCESSTOKEN you acquired here.
You probably will get a new token everytime, your old token will no longer work.
please set up your meethue_email and meethue_password inside credentials.py for this to work

"""

import requests
from bs4 import BeautifulSoup
from credentials import meethue_email,meethue_password, BRIDGEID

lookupBridgeIDURL = "https://www.meethue.com/en-US/api/gettoken?devicename=iPhone+5&appid=hueapp&deviceid="+BRIDGEID
submitPostURL = "https://www.meethue.com//en-US/api/getaccesstokengivepermission"
getTokenURL = "https://www.meethue.com/en-US/api/getaccesstokenpost"

session = requests.Session()

r = session.get(lookupBridgeIDURL)

payload = {
    'email': meethue_email,
    'password': meethue_password  # remember me
}

#actual permission page
print "asking for permission to authorize the app"
r = session.post(submitPostURL, data=payload)
# print r.cookies
print r

print "getting the access token"
result = session.get(getTokenURL)
# print result.cookies
print result

c = result.content
soup = BeautifulSoup(c)
tokenline = soup.find('a')['href']
# print tokenline
tokenArray = tokenline.split('phhueapp://sdk/login/')
print "ACCESSTOKEN is ",tokenArray[1]



