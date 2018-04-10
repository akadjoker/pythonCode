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





def List(url, f):
    try:
        listhtml = getHtml2(url)
        match = re.compile("<div class=\"list-group\">(.+?)</div>", re.DOTALL).findall(listhtml)
        match2 = re.compile("class=\"list-group-item(.+?)\">", re.DOTALL).findall(match[0])
        parts = None
        count = 0
        Data = None
        for item in match2:
            item = item.strip()
            item = item.replace('active" onclick="javascript:checkEngineVersion(', '')
            item = item.replace('onclick="javascript:checkEngineVersion(', '')
            item = item.replace('active"', '')
            item = item.replace('<?//=$active?>"', '')
            item = item.replace("'", '')
            item = item.replace(",", ";")
            item = item.strip()
            parts = item.split(";")
            if len(parts[1]) < 10:
                continue
            url = parts[0].replace('\n', '')
            url = url.replace('\\', '')
            url = url.replace('rn', '')
            url = url.replace('active" n', '')

            link = parts[1].replace('\'', '')
            link = link.replace('\\', '')
            link = link.replace('rn', '')

            print url
            print link
            f.write('#EXTINF:0, ' + url + '\n')
            f.write('acestream://' + link.strip() + '\n')

    except:
      print('Oh oh', 'It looks like this website is down.')
    return None

print os.environ['HOME']+'/Videos'

       
        
file = open(os.environ['HOME']+'/fap.m3u8','w')
file.write('#EXTM3U\n')
List('http://xxx.dvb-p.com/ace_streams/fap-tv-teaching/',file)
List('http://xxx.dvb-p.com/ace_streams/jasmin-tv/',file)
List('http://xxx.dvb-p.com/ace_streams/exotica-tv/',file)
List('http://xxx.dvb-p.com/ace_streams/nuart-tv/',file)
file.close()
print("... Operation Completed ;) ");

