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
import time
import datetime

mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}



USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}





def num_suffix(n):
    '''
    Returns the suffix for any given int
    '''
    suf = ('th','st', 'nd', 'rd')
    n = abs(n) # wise guy
    tens = int(str(n)[-2:])
    units = n % 10
    if tens > 10 and tens < 20:
        return suf[0] # teens with 'th'
    elif units <= 3:
        return suf[units]
    else:
        return suf[0] # 'th'

def day_suffix(t):
    '''
    Returns the suffix of the given struct_time day
    '''
    return num_suffix(t.tm_mday)

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
    

        

def Video(url, name,f):
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


def List(url,f):
    try:
        listhtml = getHtml2(url)
        #with open("site.html", "w") as text_file:
         #    text_file.write(listhtml)
        #soup = BeautifulSoup(listhtml, 'html.parser') 
        #for link in soup.find_all('a'):
        #    print(link.get('href'))
    except Exception,e:
        print('Oh oh - Download', str(e))
        return None
        
    try:
		
		match = re.compile('data-toggle="tooltip" href([^"]+).([^"]+).*?alt([^"]+).*?title([^"]+).*?([^"]+).*?" data-date="([^"]+).*?',          re.DOTALL).findall(listhtml)
		#match = re.compile('data-toggle="tooltip"([^"]+).*?([^"]+).*?([^"]+).*?([^"]+).*?',          re.DOTALL).findall(listhtml)
		#file = open('ace.txt','w') 
		#for dummy,aurl,img in match:
                fulltext=None
		lista = None
		total = 0
		for dummy,ace,dummy2,dummy3,caption,date in match:
		#for dummy,ace,dummy2,caption in match:
			#print(aurl)
			#Video(url,caption,f)
			caption = caption.replace('<br />',';')
			fulltext = caption.strip()
			lista = fulltext.split(';')
			total = len(lista)
			game = lista[0]
			liga = lista[1]
			channel = lista[2]
			language = lista[3]
		        print 'Game:',game
			print 'Liga:',liga
			print 'Channel:',channel
			print 'Language:',language      
			print ace
			print date
			print datetime.datetime.strptime(date, '%Y%m%d').date()
			f.write('#EXTINF:0,'+caption+'\n')
			f.write(ace+'\n')
			
			#print ''    
			#print caption
			
			#print ace
		#	file.write(aurl+'\n')
		#	file.write('\n')
		#file.close()	
    except Exception,e:
        print('Oh oh - Parse', str(e))
        return None
        
 




print(" hack by DJOKER");
print("... start");
f = open(os.environ['HOME']+'/ball.m3u8', 'w')
f.write('#EXTM3U\n')
#List('http://hideips.com/index.php?q=http://acesoplisting.in/',f);
List('http://acesoplisting.in/',f);
f.close()
print("... Operation Completed ;) ");

