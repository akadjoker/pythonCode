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


def clean_filename(s):
    if not s:
        return ''
    badchars = '\\/:*?\"<>|\''
    for c in badchars:
        s = s.replace(c, '')
    return s


def getHtml2(url):
    req = Request(url, None, mobileagent)
    response = urlopen(req, timeout=60)
    data = response.read()
    response.close()
    return data


def cleantext(text):
    text = text.replace('&amp;', '&')
    text = text.replace('&#8211;', '-')
    text = text.replace('&ndash;', '-')
    text = text.replace('&#038;', '&')
    text = text.replace('&#8217;', '\'')
    text = text.replace('&#8216;', '\'')
    text = text.replace('&#8230;', '...')
    text = text.replace('&quot;', '"')
    text = text.replace('&#039;', '`')
    text = text.replace('&rsquo;', '\'')
    return text


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

	
def makeRequest(url, headers=None):
	try:
		if not headers:
			headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0'}
		req = urllib2.Request(url,None,headers)
		response = urllib2.urlopen(req)
		data = response.read()
		response.close()
		return data
	except:
		sys.exit(0)
		
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


def Playvid(url, name):
    listhtml = getHtml(url, '', mobileagent)
    match = re.compile('src="(http[^"]+m3u8)', re.DOTALL | re.IGNORECASE).findall(listhtml)
    
    
   # with open("cam4.txt", "w") as text_file:
   #      text_file.write(str(match))
    
    if match:
        videourl = match[0]
        print videourl
        listas = getHtml(videourl, '', mobileagent)
        mylist = listas.split("\n")
        numList=len(mylist)
        print(mylist);
        print(numList)
        '''
        if numList==5:
           print(mylist[0])
           print(mylist[1])
           print(mylist[2])
           print(mylist[3])
           print(mylist[4])
        else:
           if numList==11:
             print(mylist[3])
             print(mylist[5])
             print(mylist[7])
             print(mylist[9])
    else:
		print('No Match')  
		'''       




       # print(mylist)
        #m3u8_obj = m3u8.loads(listas)
        #playlist = m3u8_obj.playlists[0]
        #text_file.write('#EXTINF:-1,'+name+' *resolution:'+str(playlist.stream_info.resolution)+'\n')
        #if playlist.uri!= None:
        #text_file.write('#EXTINF:-1, '+name+'\n')
        #text_file.write(playlist.uri+'\n')
        #print(playlist.uri)


def List(url):
    try:
        listhtml = makeRequest(url)
        with open("cam4.html", "w") as text_file:
             text_file.write(listhtml)
    except:
        print('Oh oh', 'It looks like this website is down.')
        return None
    #match = re.compile('profileDataBox"> <!-- preview --> <a href="([^"]+)".*?src="([^"]+)" title="Chat Now Free with ([^"]+)"',  re.DOTALL | re.IGNORECASE).findall(listhtml)
    match = re.compile('profileDataBox"> <!-- preview --> <a href="([^"]+)".*?data-hls-preview-url="(.*?)">.*?src="([^"]+)" title="Chat Now Free with ([^"]+)"',  re.DOTALL | re.IGNORECASE).findall(listhtml)
    count = 0
    for videourl,link, img, name in match:
        name = cleantext(name)
        videourl = "http://www.cam4.com" + videourl
        print(name)
        print link
        print img
        print videourl
        #Playvid(videourl, name)
        count += 1
        if count >= 20:
            break


url0 = 'http://www.cam4.com/featured/1'
url1 = 'http://www.cam4.com/female/1'
url2 = 'http://www.cam4.com/couple/1'
url3 = 'http://www.cam4.com/male/1'
url4 = 'http://www.cam4.com/shemale/1'
url5 = 'http://pt.cam4.com/cams/portugal/1'

print("Cam4 hack by DJOKER");
print("... start");
List(url0)
#Playvid("https://www.cam4.com/arianasil000","arianasil000")
print("... Operation Completed ;) ");


'''text_file = open("cam4.m3u8", "w")
'text_file.write('#EXTM3U\n')
print("Cam4 hack by DJOKER");
print("... start");
List(url0)
text_file.close()
print("... Operation Completed ;) ");

'''
