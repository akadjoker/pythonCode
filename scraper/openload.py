import sys, re, urllib2
from HTMLParser import HTMLParser

#url = 'https://openload.co/embed/LFWZT-Ig3gk/'
url = 'https://openload.co/f/0Wuh0mgeEAo/001_Promo_Video_Games_List.mp4'
 
_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
 
_regex = re.compile(r'//.+?/(?:embed|f)/([0-9a-zA-Z-_]+)')
 
def get_embed_url(url):
    ids = _regex.findall(url)
    if ids:
        return 'https://openload.co/embed/%s/' % ids[0]
    return url
 
 
def getHtml(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', _USER_AGENT)
    req.add_header('Referer', url)
    response = urllib2.urlopen(req)
    html = response.read()
 
    try:
        content_type = response.headers.get('Content-Type')
        if 'charset=' in content_type:
            encoding = content_type.split('charset=')[-1]
    except:
        pass
 
    m = re.search(r'<meta\s+http-equiv="Content-Type"\s+content="(?:.+?);\s+charset=(.+?)"', html, re.IGNORECASE)
    if m:
        encoding = m.group(1)
 
    try:
        html = unicode(html, encoding)
    except:
        pass
   
    return html
 
 
print url
print '\n'
 
html = getHtml(get_embed_url(url))
 
if any(x in html for x in ['We are sorry', 'File not found']):
    raise Exception('The file was removed')
 
m = re.search(r'<span id="hiddenurl">(.+?)<\/span>', html)
 
if not m:
    raise Exception("Video link encrypted data is not available.")
 
enc_data = m.group(1).strip()
enc_data = HTMLParser().unescape(enc_data)
 
#print enc_data
 
video_url_chars = []
 
for c in enc_data:
    j = ord(c)
    if j >= 33 and j <= 126:
        j = ((j + 14) % 94) + 33
    video_url_chars += chr(j)
 
video_url = 'https://openload.co/stream/%s?mime=true'
video_url = video_url % (''.join(video_url_chars))
 
print video_url
 
raw_input()
