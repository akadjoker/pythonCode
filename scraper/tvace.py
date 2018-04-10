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

openloadhdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
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


def unshorten_url(url):
    return requests.head(url, allow_redirects=True).url


def List(url):
    try:
        listhtml = getHtml(url, '')
        #with open("ace.html", "w") as text_file:
             #text_file.write(listhtml)
    except:
        print('Oh oh', 'It looks like this website is down.')
        return None

    try:
		match = re.compile('<option value="([^"]+)".*?</option>',
		                   re.DOTALL | re.IGNORECASE).findall(listhtml)
		s=str(match[0])
		return(s.replace("/player.php?id=","acestream://"))
    except:
        print('Oh oh', 'NO url.')
        return None
        
        
      
#/player.php?id=8fb7fb96bc5369eed7787e98729ece5503552453"

url0 = 'http://tuchkatv.ru/287-satisfaction-hd.html'

print(" hack by DJOKER");
print("... start");
s0=List('http://tuchkatv.ru/287-satisfaction-hd.html');
print 'satisfaction,',s0
s1=List('http://tuchkatv.ru/257-platinum-tv.html')
print 'platium tv,',s1
s2=List('http://tuchkatv.ru/178-hustler-tv.html')
print 'hustler,',s2
s3=List('http://tuchkatv.ru/179-playboy-tv.html')
print 'playboy,',s3
s4=List('http://tuchkatv.ru/182-nochnoy-klub.html')
print 'iskushenie,',s4
s5=List('http://tuchkatv.ru/314-brazzers-tv-europe.html')
print 'brazzers love,',s5
s6=List('http://tuchkatv.ru/415-sct.html')
print 'sct,',s6
s7=List('http://tuchkatv.ru/396-o-la-la.html')
print 'olala,',s7
s8=List('http://tuchkatv.ru/417-centoxcento-tv.html')
print 'centox,',s8
s9=List('http://tuchkatv.ru/9409-fap-tv-lesbian.html')
print 'fap lesbian,',s9
s10=List('http://tuchkatv.ru/262-nuart-tv.html')
print 'nuart,',s10
s11=List('http://tuchkatv.ru/9404-fap-tv-amateur.html')
print 'fap tv amateur,',s11
s12=List('http://tuchkatv.ru/9414-fap-tv-teens.html')
print 'fap tv teen,',s12
s13=List('http://tuchkatv.ru/9410-fap-tv-older.html')
print 'fap older,',s13
s14=List('http://tuchkatv.ru/9405-fap-tv-anal.html')
print 'fap anal,',s14
s15=List('http://tuchkatv.ru/9411-fap-tv-parody.html')
print 'fap parody,',s15

s16=List('http://tuchkatv.ru/9411-fap-tv-parody.html')
print 'fap parody,',s16

file = open('ace.txt','w') 
file.write("satisfaction: ") 
file.write(s0+"\n") 
file.write("platium: ") 
file.write(s1+"\n") 
file.write("hustler: ") 
file.write(s2+"\n")
file.write("playboy: ")  
file.write(s3+"\n")
file.write("iskushenie: ")  
file.write(s4+"\n") 
file.write("brazzers: ") 
file.write(s5+"\n") 
file.write("sct: ")  
file.write(s6+"\n") 
file.write("plala: ") 
file.write(s7+"\n") 
file.write("centox: ") 
file.write(s8+"\n")
file.write("fabp lesbian: ")  
file.write(s9+"\n") 
file.write("nurat: ") 
file.write(s10+"\n") 
file.write("fap amterur: ") 
file.write(s11+"\n") 
file.write("fap teens: ") 
file.write(s12+"\n") 
file.write("fap older: ") 
file.write(s13+"\n") 
file.write("fap anal: ") 
file.write(s14+"\n") 
file.write("fap parody: ") 
file.write(s15+"\n") 
 
file.close() 


#print List('http://tuchkatv.ru/262-nuart-tv.html')

#data = getHtml('http://hdmi-tv.ru/xxx/673-pink-o-tv.html','');
#print data


print("... Operation Completed ;) ");

