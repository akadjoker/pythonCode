
import os
import sys
import urllib
import urllib2
import cookielib
import clipboard

import re
import requests
import cookielib
import os.path
import sys
import time
import subprocess
import youtube_dl

Request = urllib2.Request
urlopen = urllib2.urlopen

IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
OPERA_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36 OPR/34.0.2036.50'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'




def getUrl(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', FF_USER_AGENT)
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    return link

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    subprocess.check_call(cmd, shell=false)    

def PAGEVIDEOLINKS(url):
    content = getUrl(url)
    match = re.compile('</p><p>([^"]+)</p><p><em>(.*?)</em><br /> <a href="(.*?)" rel="nofollow"  target="_blank" class="external">', re.DOTALL ).findall(content)     
    if (match):
        for misc,names,video in match:
            misc=misc.replace("</p>","")
            misc=misc.replace("<p>","")
            misc=misc.replace("&#","*")
            print names
            print misc
            print video
            clipboard.copy(url +',' +video)
            
           # http://fullxxxmovies.net/pornochic-16-yasmine-and-regina-2008/,https://openload.co/f/bKHbVKngDCc/rtt7888885_7.mp4
            

def VIDEOLINKS(url):
    content = getUrl(url)
    match2 = re.compile('<link rel="next" href="(.*?)" /><meta property="og:locale"', re.DOTALL ).findall(content)     
    match = re.compile('class="entry-title"><a href="(.*?)".*?"bookmark">(.*?)</a>.*?datetime="(.*?)</time>.*?.*?src="(.*?)class="attachment-anninapro_masonry-post', re.DOTALL ).findall(content)     
    if (match):
        count = 0
        for url,title,date,img in match:
            date=date.replace('">',' ')
            #print(title+','+date+','+url+','+img)
            PAGEVIDEOLINKS(url)
            if count>=1:
                break
            count = count +1
	
			
   
    if (match2):
        print(match2[0])
              




#private static final String[] a = new String[]{"https://afdah.org", "https://fmovie.co", "https://genvideos.org", "https://xmovies8.org", "https://putlockerhd.co", "https://watch32hd.co"};
#
    

#content =getUrl('https://openload.co/f/0Wuh0mgeEAo/001_Promo_Video_Games_List.mp4')
#content =getUrl('https://openload.co/embed/kUEfGclsU9o/')
content =getUrl('https://streamango.com/embed/amnsrfbqtfeplnps/Big_Booty_POV_720x404_mp4')
print content
with open("fullmovies.html", "w") as text_file:
   text_file.write(content)




            
    
#VIDEOLINKS('http://fullxxxmovies.net/')    


