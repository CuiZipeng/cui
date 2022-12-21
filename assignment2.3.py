import urllib
import urllib2
import requests
#introduction mod lib


#set a web
URL = 'http:www.geogle.com'
#set code (chinese use code)
res.encoding = 'utf-8'
#play .get method
res = requests.get(URL)
#show result
print(type(res))
print(res.text)
#play put method
res = requests.put(URL)
#show result
print(type(res))
print(res.text)
