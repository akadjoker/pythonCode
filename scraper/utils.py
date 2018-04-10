import urllib
import urllib2
import re
import requests
import os.path
import sys
import time
import json
import urlparse
from StringIO import StringIO
import gzip
import base64
import threading



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


def download(link, filelocation):
    r = requests.get(link, stream=True)
    with open(filelocation, 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)

def createNewDownloadThread(link, filelocation):
    download_thread = threading.Thread(target=download, args=(link,filelocation))
    download_thread.start()

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
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
            f.close()
        else:
            data = response.read()
        response.close()
    except urllib2.HTTPError as e:
        data = e.read()
    except Exception as e:
        if 'SSL23_GET_SERVER_HELLO' in str(e):
            print('Oh oh','Python version to old - update to Krypton or FTMC')
            raise urllib2.HTTPError()
        else:
            print('Oh oh','It looks like this website is down.')
            raise urllib2.HTTPError()
        return None
    return data

def postHtml(url, form_data={}, headers={}, compression=True, NoCookie=None):
    try:
        _user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 ' + \
                      '(KHTML, like Gecko) Chrome/13.0.782.99 Safari/535.1'
        req = urllib2.Request(url)
        if form_data:
            form_data = urllib.urlencode(form_data)
            req = urllib2.Request(url, form_data)
        req.add_header('User-Agent', _user_agent)
        for k, v in headers.items():
            req.add_header(k, v)
        if compression:
            req.add_header('Accept-Encoding', 'gzip')
        response = urllib2.urlopen(req)
        data = response.read()
        response.close()
    except Exception as e:
        if 'SSL23_GET_SERVER_HELLO' in str(e):
            print('Oh oh','Python version to old - update to Krypton or FTMC')
            raise urllib2.HTTPError()
        else:
            print('Oh oh','It looks like this website is down.')
            raise urllib2.HTTPError()
        return None
    return data

def getVideoLink(url, referer, hdr=None, data=None):
    if not hdr:
        req2 = Request(url, data, headers)
    else:
        req2 = Request(url, data, hdr)
    if len(referer) > 1:
        req2.add_header('Referer', referer)
    url2 = urlopen(req2).geturl()
    return url2

def unshorten_url(url):
    return requests.head(url, allow_redirects=True).url


def ListCamSoda(url):
    response = utils.getHtml(url)
    data = json.loads(response)
    for camgirl in data['results']:
        name = camgirl['slug'] + " [" + camgirl['status'] + "]"
        videourl = "https://www.camsoda.com/api/v1/video/vtoken/" + camgirl['slug']
        img = "https:" + camgirl['thumb']
        print(name)
        print(videourl)
        print(img);
        #Playvid(videourl,name)

def PlayvidCamSoda(url, name):
    url = url + "?username=guest_" + str(random.randrange(100, 55555))
    response = utils.getHtml(url)
    data = json.loads(response)
    if "camhouse" in data['stream_name']:
       videourl = "https://camhouse.camsoda.com/" + data['app'] + "/mp4:" + data['stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']
    else:
       videourl = "https://" + data['edge_servers'][0] + "/" + data['app'] + "/mp4:" + data['stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']
