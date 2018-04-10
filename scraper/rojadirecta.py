__author__ = 'djoker'
import re
import os
import sys
import sqlite3
import urllib
import urllib2
import re
import requests
import cookielib
import os.path
import sys
import time
import tempfile
import urlparse
import base64
from StringIO import StringIO
import gzip
import httplib
import urlparse

import re


mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}


urlopen = urllib2.urlopen
Request = urllib2.Request


def getHtml2(url):
    req = Request(url, None, mobileagent)
    response = urlopen(req, timeout=60)
    data = response.read()
    response.close()
    return data


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
        listhtml = getHtml(url,'')
        with open("rojadirecta.html", "w") as text_file:
             text_file.write(listhtml)
    except Exception,e:
        print('Oh oh - Download', str(e))
        return None

    try:
		match = re.compile('<option value="([^"]+)".*?</option>',
		                   re.DOTALL | re.IGNORECASE).findall(listhtml)
		s=str(match[0])
		return(s.replace("/player.php?id=","acestream://"))
    except Exception,e:
        print('Oh oh - Parse', str(e))
        return None
        
        
      




print(" hack by DJOKER");
print("... start");
texto=List('http://hideips.com/?q=http%3A%2F%2Fwww.rojadirecta.me%2F&hl=3e5')
print texto
'''
file = open('ace.txt','w') 
file.write("satisfaction: ") 
file.write(s15+"\n") 
 
file.close() 
'''



print("... Operation Completed ;) ");

