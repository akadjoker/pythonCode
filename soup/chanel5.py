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
    

        

def Video(url, name):
    try:
        listhtml = getHtml2(url)
        with open("hdmi.html", "w") as text_file:
            text_file.write(listhtml)
    except Exception, e:
        print('Oh oh - Download', str(e))
        return None

    try:

        match = re.compile('<source  src="(.+?)" type="application/x-mpegURL">',re.DOTALL | re.MULTILINE).findall(str(listhtml))
        print str(match[0])
        f.write('#EXTINF:0,'+name+'\n')
        f.write(str(match[0])+'\n')
        print '----------------------------------'
       

    except Exception, e:
      print('Oh oh - Parse', str(e))
      return None


def List(url):
    try:
        listhtml = getHtml2(url)
        file = open('channel5.txt','w') 
        file.write(listhtml)
        file.close() 
        #with open("site.html", "w") as text_file:
         #    text_file.write(listhtml)
        #soup = BeautifulSoup(listhtml, 'html.parser') 
        #for link in soup.find_all('a'):
        #    print(link.get('href'))
    except Exception,e:
        print('Oh oh - Download', str(e))
        return None
        
    try:
		
		#match = re.compile('<div class="short">([^"]+).*?([^"]+).*?([^"]+).*?([^"]+).*?([^"]+).*?([^"]+).*?',          re.DOTALL).findall(listhtml)
		match = re.compile('<div class="short">.+?<a href="(.+?)" title="(.+?)">.+?<img src="(.+?)" .+?',          re.DOTALL).findall(listhtml)

		#file = open('ace.txt','w') 
		#for dummy,aurl,img in match:

		#for dummy,url,tile,caption,dummy2,img in match:
		for url,title,img in match:
			#print(aurl)
			print url
			print title
			print img
			#Video(url,caption,f)

    except Exception,e:
        print('Oh oh - Parse', str(e))
        return None
        
 




print(" hack by DJOKER");
print("... start");

#List('http://hdmi-tv.ru/xxx/',f);
List('https://flixtor.to/');

print("... Operation Completed ;) ");

