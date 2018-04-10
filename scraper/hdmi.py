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


print(" hack by DJOKER");
print("... start");
f = open(os.environ['HOME']+'/hdmi.m3u8', 'w')
f.write('#EXTM3U\n')

List('http://hdmi-tv.ru/xxx/2651-fap-tv-trans.html','fap tv Trans',f)
List('http://hdmi-tv.ru/xxx/2643-fap-tv-gay.html','fap tv Gay',f)
List('http://hdmi-tv.ru/xxx/2742-fap-tv-shemale.html','fap tv Shemake',f)
List('http://hdmi-tv.ru/xxx/2650-fap-tv-teens.html','fap tv Teens',f)
List('http://hdmi-tv.ru/xxx/2649-fap-tv-teaching.html','fap tv Teaching',f)
List('http://hdmi-tv.ru/xxx/2647-fap-tv-parody.html','fap tv Parody',f)
List('http://hdmi-tv.ru/xxx/2648-fap-tv-pissing.html','fap tv Pissing',f)
List('http://hdmi-tv.ru/xxx/2645-fap-tv-lesbian.html','fap tv Lesbian',f)
List('http://hdmi-tv.ru/xxx/2646-fap-tv-older.html','fap tv Older',f)
List('http://hdmi-tv.ru/xxx/2644-fap-tv-legal-porno.html','fap tv Legal Porno',f)
List('http://hdmi-tv.ru/xxx/6749-fap-tv.html','fap-tv',f)
List('http://hdmi-tv.ru/xxx/2636-fap-tv-2.html','fap tv 2',f)
List('http://hdmi-tv.ru/xxx/2637-fap-tv-3.html','fap tv 3',f)
List('http://hdmi-tv.ru/xxx/2638-fap-tv-4.html','fap tv 4',f)
List('http://hdmi-tv.ru/xxx/2639-fap-tv-amateur.html','fap tv Amateur',f)
List('http://hdmi-tv.ru/xxx/2640-fap-tv-anal.html','fap tv Anal',f)
List('http://hdmi-tv.ru/xxx/2641-fap-tv-bbw.html','fap tv BBW',f)
List('http://hdmi-tv.ru/xxx/2642-fap-tv-compilation.html','fap tv Compilation',f)
List('http://hdmi-tv.ru/xxx/2741-fap-tv-2-hd.html','fap tv 2HD',f)

List('http://hdmi-tv.ru/xxx/6751-passionx.html','passionx',f)
List('http://hdmi-tv.ru/main/6763-tv-xxi.html','tv-xxi',f)

List('http://hdmi-tv.ru/xxx/670-hustler-tv.html','hustler tv',f)
List('http://hdmi-tv.ru/xxx/669-hustler-hd.html','hustler hd',f)
List('http://hdmi-tv.ru/xxx/675-satisfaction-hd.html','satisfaction hd',f)
List('http://hdmi-tv.ru/xxx/674-playboy-tv-.html','playboy',f)
List('http://hdmi-tv.ru/xxx/671-nuart-tv-.html','nuart',f)
List('http://hdmi-tv.ru/xxx/672-o-la-la.html','olala',f)
List('http://hdmi-tv.ru/xxx/2653-jasmin-tv.html','jasmin tv',f)
List('http://hdmi-tv.ru/xxx/3105-passionxxx.html','passionxxx',f)






f.close()
print("... Operation Completed ;) ");

