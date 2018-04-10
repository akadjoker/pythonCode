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

    
Macintoshagent = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:18.0) Gecko/20100101 Firefox/18.0'}
	
mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}
base_url = "http://www.arenavision.in/"	   



def getHtml3(url):
	headers = {
		"Cookie" : "beget=begetok; has_js=1;"
	}
	source = requests.get(url,headers=headers).text
	with open("ace.html", "w") as text_file:
             text_file.write(str(source.encode('utf-8').strip()))
	if source:
		#match = re.compile('leaf"><a href="(.+?)">(.+?)</a').findall(source)
		match = re.compile('this.loadPlayer([^"]+).*?([^"]+).*?',re.DOTALL | re.MULTILINE).findall(source)
		#match = re.compile('<a href="(.+?)"',re.DOTALL | re.MULTILINE).findall(source)
		
		for link, nome in match:
		    print link
		    print nome

        
 




print(" hack by DJOKER");
print("... start");
#List('http://hideips.com/index.php?q=http://arenavision.esy.es/json.php');
getHtml3('http://arenavision.in/17');
getHtml3('http://arenavision.in/18');
getHtml3('http://arenavision.in/19');
getHtml3('http://arenavision.in/20');
getHtml3('http://arenavision.in/01');
getHtml3('http://arenavision.in/02');

print("... Operation Completed ;) ");

