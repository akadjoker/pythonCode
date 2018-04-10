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
HTTP_HEADERS_IPAD = {
    'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4'}
cbheaders = {'User-Agent': HTTP_HEADERS_IPAD,
             'Accept': '*/*',
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


def Playvid(url, name, chatslow=1):
    listhtml = getHtml(url, USER_AGENT)
    with open("chartubate.html", "w") as tf:
         tf.write(listhtml)
    m3u8url = re.compile(r"jsplayer, '([^']+)", re.DOTALL | re.IGNORECASE).findall(listhtml)
    print(m3u8url[0])
    if m3u8url:
        m3u8stream = m3u8url[0]
        m3u8stream = m3u8stream.replace('_fast', '')
    else:
        m3u8stream = False
        

    if m3u8stream:
        videourl = m3u8stream
        text_file.write('#EXTINF:-1, ' + name + '\n')
        text_file.write(videourl + '\n')
    else:
        print('Oh oh', 'Couldn\'t find a playable webcam link')
        return


def List(url):
    try:
        listhtml = getHtml(url, url)

    except:
        print('Oh oh', 'It looks like this website is down.')
        return None
    match = re.compile(
        r'<li>\s+<a href="([^"]+)".*?src="([^"]+)".*?<div[^>]+>([^<]+)</div>.*?href[^>]+>([^<]+)<.*?age[^>]+>([^<]+)<',
        re.DOTALL | re.IGNORECASE).findall(listhtml)

    for videopage, img, status, name, age in match:
        name = cleantext(name.strip())
        status = status.replace("\n", "").strip()
        name = 'Name:' + name + ', Age: ' + age
        print status
        videopage = "https://chaturbate.com" + videopage
        Playvid(videopage, name, 0)
        break


url0 = 'https://chaturbate.com/new-cams/female/?page=1'
url1 = 'https://chaturbate.com/teen-cams/female/?page=1'
url2 = 'https://chaturbate.com/female-cams/?page=1'
url3 = 'https://chaturbate.com/18to21-cams/female/?page=1'
url4 = 'https://chaturbate.com/north-american-cams/?page=1'
url5 = 'https://chaturbate.com/other-region-cams/female/?page=1'
url6 = 'https://chaturbate.com/euro-russian-cams/male/?page=1'
url7 = 'https://chaturbate.com/philippines-cams/female/?page=1'
url8 = 'https://chaturbate.com/asian-cams/female/?page=1'
url9 = 'https://chaturbate.com/south-american-cams/female/?page=1'

text_file = open("ctb.m3u8", "w")
text_file.write('#EXTM3U\n')
print("Chartubate hack by DJOKER");
print("... start");
List(url0)
text_file.close()

print("... Operation Completed ;) ");

