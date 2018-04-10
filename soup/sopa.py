__author__ = 'djoker'
import re
import os
import sys
import urllib
import re
import requests
import cookielib
import os.path
import sys
import time
from bs4 import BeautifulSoup
import urllib
import urllib2
Request = urllib2.Request
urlopen = urllib2.urlopen


mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

HTTP_HEADERS_IPAD = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4'}
cbheaders = {'User-Agent': HTTP_HEADERS_IPAD,
       'Accept': '*/*',
       'Connection': 'keep-alive'}

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}




def getHtml(url, referer='', hdr=None, NoCookie=None, data=None):
    try:
        if not hdr:
            req = Request(url, data, headers)
        else:
            req = Request(url, data, hdr)
        if len(referer) > 1:
            req.add_header('Referer', referer)
        if data:
            req.add_header('Content-Length', len(data))
        response = urlopen(req, timeout=60)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
            f.close()
        else:
            data = response.read()
        response.close()
    except urllib2.HTTPError as e:
        data = e.read()
        raise urllib2.HTTPError()
    return data





def List(url):
    try:
        listhtml = getHtml(url)
        with open("site.html", "w") as text_file:
             text_file.write(listhtml)
        soup = BeautifulSoup(listhtml, 'html.parser') 
        for link in soup.find_all('a'):
            print(link.get('href'))
    except:
        print('Oh oh', 'It looks like this website is down.')
        return None
        
	
        
 




print(" hack by DJOKER");
print("... start");
List('http://tuchkatv.ru/18/');
print("... Operation Completed ;) ");

