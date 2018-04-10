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



def arenavision_streams(name,url):
	source = requests.get(url,headers=headers).text
	print str(source)
	if source:
		match = re.compile('sop://(.+?)"').findall(source)
		if match: sop.sopstreams(name,os.path.join(current_dir,"icon.png"),"sop://" + match[0])
		else:
			match = re.compile('this.loadPlayer\("(.+?)"').findall(source)
			print str(match)

def arenavision_chooser(url):
	source = requests.get(url,headers=headers).text
	if source:
   		 match = re.compile('leaf"><a href="(.+?)">(.+?)</a').findall(source)
		 print str(match)
		 for link,name in match:
		     print link
		     print name
				
def arenavision_menu():
	source = requests.get(base_url,headers=headers).text
	if source:
		match = re.compile('leaf"><a href="(.+?)">(.+?)</a').findall(source)
		for link, nome in match:
		    print link
		    print nome		    
		    
			
    

        





print(" hack by DJOKER");
print("... start");
#List('http://hideips.com/index.php?q=http://arenavision.in/17');
#List('http://arenavision.in/17');
arenavision_streams('AV17','http://arenavision.in/17');
#arenavision_menu()

print("... Operation Completed ;) ");

