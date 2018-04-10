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
    req = Request(url, None, headers)
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


def unshorten_url(url):
    return requests.head(url, allow_redirects=True).url


def List(url,f):
    try:
        listhtml = getHtml(url, '')
        match = re.compile('<div class="list-group">(.+?)</div>',re.DOTALL).findall(listhtml)
        match2 = re.compile('class="list-group-item(.+?)">',re.DOTALL).findall(str(match))  
        fulltext=''
        count =0
        for item in match2:
			print count
			#item = item.replace('class="list-group-item active"' ,'')
			#item = item.replace('class="list-group-item <?//=$active?>"' ,'')
			#item = item.replace('onclick="javascript:checkEngineVersion("' ,'')
			item = item.replace('<?//=$active?>" onclick="javascript:checkEngineVersion(' ,'')
			item = item.replace('active" onclick="javascript:checkEngineVersion(' ,'')
			item = item.replace('active" onclick="javascript:checkEngineVersion(\r\n','')
			item = item.replace('\');return false;','')
			print item
			fulltext+=item.strip()
			count+=1
        list=fulltext.split('\',');
        total=len(list)
        f.write('-------------------------------------------------\n')
        mode=0
        for i in range(0,total):
                url  = list[i]
                url=url.strip()
                url=url.replace('\'','')
                url=url.replace('\\','')
                url=url.replace('rn','')
                url=url.strip()
                print url
                if mode % 2 == 0:
                   f.write('#EXTINF:0, '+url+'\n')
                else:
                   f.write('acestream://'+url+'\n')
                   
                mode+=1
        
        
       
    except:
        print('Oh oh', 'It looks like this website is down.')
        return None

print os.environ['HOME']+'/Videos'

       
        
file = open(os.environ['HOME']+'/fap.m3u8','w')
file.write('#EXTM3U\n')
#List('http://xxx.dvb-p.com/ace_streams/fap-tv-teaching/',file)
#List('http://xxx.dvb-p.com/ace_streams/jasmin-tv/',file)
#List('http://xxx.dvb-p.com/ace_streams/exotica-tv/',file)
List('http://xxx.dvb-p.com/ace_streams/nuart-tv/',file)
file.close()
print("... Operation Completed ;) ");

