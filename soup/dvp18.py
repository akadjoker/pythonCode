__author__ = 'djoker'
import re
import os
import sys
import urllib
import urllib2

import re
import requests
import cookielib
import os.path
import sys
import time

import re
Request = urllib2.Request
urlopen = urllib2.urlopen


mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}



USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}





def getHtml2(url):
    req = Request(url, None, mobileagent)
    response = urlopen(req, timeout=5)
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
    


def Video2(url):
    try:
        listhtml = getHtml(url,'',mobileagent)
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
        

def Video(url):
    try:
        listhtml = getHtml(url,'',mobileagent)
        #with open("site.html", "w") as text_file:
         #    text_file.write(listhtml)
    except Exception,e:
        print('Oh oh - Download', str(e))
        return None

    try:
		match = re.compile('javascript:checkEngineVersion([^"]+).*?''',
		                   re.DOTALL | re.IGNORECASE).findall(listhtml)
		s=str(match[0])
		print(s)
		return match[0];
    except Exception,e:
        print('Oh oh - Parse', str(e))
        return None

def List(url):
    try:
        listhtml = getHtml(url,'')
        #with open("site.html", "w") as text_file:
         #    text_file.write(listhtml)
        #soup = BeautifulSoup(listhtml, 'html.parser') 
        #for link in soup.find_all('a'):
        #    print(link.get('href'))
    except Exception,e:
        print('Oh oh - Download', str(e))
        return None
        
    try:
		#<div class="maincont">([^"]+).*?([^"]+).*?<div class="clr"></div>',
		#<div class="maincont">([^"]+).*?([^"]+).*?<p style="text-align:center;"><img src="([^"]+).*?alt="([^"]+).*?<div class="clr"></div>
		
		match = re.compile('<div class="maincont">([^"]+).*?([^"]+).*?<p style="text-align:center;"><img src="([^"]+).*?<div class="clr"></div>',
		                   re.DOTALL | re.MULTILINE).findall(listhtml)
		file = open('ace.txt','w') 
		for dummy,aurl,img in match:
			print(aurl)
			print(img)
			ace=Video2(aurl)
			print ace
			file.write(aurl+'\n')
			file.write(ace+'\n')
			file.write('\n')
		file.close()	
    except Exception,e:
        print('Oh oh - Parse', str(e))
        return None
        
 




print(" hack by DJOKER");
print("... start");
#List('http://xxx.dvb-p.com/channels/');
List('http://hideips.com/?q=http://tuchkatv.ru/18/');
#List('http://tuchkatv.ru/18/');
#Video('http://hideips.com/?q=http://xxx.dvb-p.com/ace_streams/nuart-tv/')
#Video('http://hideips.com/?q=http://xxx.dvb-p.com/ace_streams/nuart-tv/')

'''
Video('http://xxx.dvb-p.com/ace_streams/blue-hustler/')
Video('http://xxx.dvb-p.com/ace_streams/jasmin-tv/')
Video('http://xxx.dvb-p.com/ace_streams/nuart-tv/')
Video('http://xxx.dvb-p.com/ace_streams/o-la-la/')
Video('http://xxx.dvb-p.com/ace_streams/playboy-tv/')
Video('http://xxx.dvb-p.com/ace_streams/%d0%b8%d1%81%d0%ba%d1%83%d1%88%d0%b5%d0%bd%d0%b8%d0%b5/')
'''
#Video('http://xxx.dvb-p.com/ace_streams/fap-tv-pissing/')
print("... Operation Completed ;) ");

