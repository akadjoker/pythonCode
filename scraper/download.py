__author__ = 'djoker'
import re
import os
import sys
import urllib
import urllib2

import re
import requests
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
    response = urlopen(req, timeout=80)
    data = response.read()
    response.close()
    return data



def List(url, name,f):
    try:
        listhtml = getHtml2(url)
        with open("fap-shame.html", "w") as text_file:
            text_file.write(listhtml)
    except Exception, e:
        print('Oh oh - Download', str(e))
        return None




print(" hack by DJOKER");
print("... start");



List('http://hdmi-tv.ru/xxx/','fap tv shemake',None)





print("... Operation Completed ;) ");

