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
import time
import Net
from time import sleep



std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
} 

IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
OPERA_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'


def getUrl(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

        
		

def cleanse_html(html):
    for match in re.finditer('<!--(.*?)-->', html, re.DOTALL):
        if match.group(1)[-2:] != '//': html = html.replace(match.group(0), '')
    
    html = re.sub('''<(div|span)[^>]+style=["'](visibility:\s*hidden|display:\s*none);?["']>.*?</\\1>''', '', html, re.I | re.DOTALL)
    return html
    
def get_hidden(html, form_id=None, index=None, include_submit=True):
    hidden = {}
    if form_id:
        pattern = '''<form [^>]*(?:id|name)\s*=\s*['"]?%s['"]?[^>]*>(.*?)</form>''' % (form_id)
    else:
        pattern = '''<form[^>]*>(.*?)</form>'''
    
    html = cleanse_html(html)
        
    for i, form in enumerate(re.finditer(pattern, html, re.DOTALL | re.I)):
        if index is None or i == index:
            for field in re.finditer('''<input [^>]*type=['"]?hidden['"]?[^>]*>''', form.group(1)):
                match = re.search('''name\s*=\s*['"]([^'"]+)''', field.group(0))
                match1 = re.search('''value\s*=\s*['"]([^'"]*)''', field.group(0))
                if match and match1:
                    hidden[match.group(1)] = match1.group(1)
            
            if include_submit:
                match = re.search('''<input [^>]*type=['"]?submit['"]?[^>]*>''', form.group(1))
                if match:
                    name = re.search('''name\s*=\s*['"]([^'"]+)''', match.group(0))
                    value = re.search('''value\s*=\s*['"]([^'"]*)''', match.group(0))
                    if name and value:
                        hidden[name.group(1)] = value.group(1)
            
   # print('Hidden fields are: %s' % (hidden))
    return hidden
    
                
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '*'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
  #  if iteration == total: 
   #     print()
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '*' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('\r[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()     

      
                        
def get_media_url(web_url):
        headers = {'User-Agent': FF_USER_AGENT}
        net = Net.Net()
        response = net.http_GET(web_url, headers=headers)
        html = response.content
        if re.search('>(File Not Found)<', html):
            print('File Not Found or removed')

        cnt = 10
        match = re.search('count\s*=\s*(\d+);', html)
        if match:
            cnt = int(match.group(1))
        cnt += 1
        data = get_hidden(html)
        #print ('data:',data)
        headers.update({'Referer': web_url})
        total=cnt
        i = 0
        #printProgressBar(0, total, 'Progress:', 'Complete',  5)
        while i < total:
             progress(i, total, status='Progress:')
             #printProgressBar(i + 1, total, 'Progress:',  'Complete', 5)
             time.sleep(0.9)  
             i += 1
    
        
        html = net.http_POST(response.get_url(), form_data=data, headers=headers).content
        match = re.compile('''file\s*:\s*["'](?P<url>[^"']+)''', re.DOTALL | re.IGNORECASE).findall(html)
        return match[0]

        '''

                
        https://pornfree.tv/  
        http://pornflixhd.com/  
        http://fullxxxmovies.net/
        https://mangoporn.net/

		'''
		
                    
def getVideo(web_url):
    headers = {'User-Agent': FF_USER_AGENT}
    net = Net.Net()
    response = net.http_GET(web_url, headers=headers)
    html = response.content
    try:
       match = re.compile('host=StreamCloud&video=(.*?)"',re.DOTALL).findall(html)
    except:
      print('Oh oh', 'NO Match.')
      return None
    surl = match[0]
    surl = surl.replace("%3A", ":")
    surl = surl.replace("%2F", "/")
    video=get_media_url(surl)
    print video

def getVideos(urlmain):
	content = getUrl(urlmain)
	n1 = content.find("<!-- main content -->", 0)
	content = content[n1:]
	regexvideo = 'align="left"><a href="(.*?)"><img src="(.*?)".*?class="movie">(.*?)<'
	match = re.compile(regexvideo,re.DOTALL).findall(content)
	for url, pic, name in match:
	    print (url,pic,name)
	            
def showContent():
    Host = "http://www.wildfireporn.com/cat/1.html"
    content = getUrl(Host)
    match = re.compile('class="subCategoryList".*?href="(.*?)">(.*?)<',re.DOTALL).findall(content)
    for url, name in match:
        print url
        print name
                
       
     
#http://www.wildfireporn.com/cat/37.html english
#http://www.wildfireporn.com/cat/19.html jaba unce        
print("... start");
Host = "http://www.wildfireporn.com/video/8091-Silicone_Queens_2014_SC.html"
#Host = "http://www.wildfireporn.com/video/12709-Modern_Romance_2014_SC.html
#getVideo(Host)
        
   
#showContent()
#showContent()
getVideos ('http://www.wildfireporn.com/cat/37.html')
print("... Operation Completed ;) ");

'''
09:33:09.183 T:140018936960768  NOTICE: Creating audio stream (codec id: 86018, channels: 1, sample rate: 44100, no pass-through)
09:33:09.193 T:140019980319616   ERROR: GetDirectory - Error getting plugin://plugin.video.wildfire/?mode=4&name=Silicone%20Queens%20(2014)%20SC&url=http%3a%2f%2fwww.wildfireporn.com%2fvideo%2f8091-Silicone_Queens_2014_SC.html
09:33:09.196 T:140019980319616   ERROR: CGUIMediaWindow::GetDirectory(plugin://plugin.video.wildfire/?mode=4&name=Silicone%20Queens%20(2014)%20SC&url=http%3a%2f%2fwww.wildfireporn.com%2fvideo%2f8091-Silicone_Queens_2014_SC.html) failed
09:33:09.199 T:140019146680064  NOTICE: PulseAudio: Opened device Default in pcm mode with Buffersize 150 ms
'''

