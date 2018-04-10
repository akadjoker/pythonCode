
import urllib2
import os
import sys
import random
import sqlite3
import json
import subprocess
import utils



def ListCamSoda(url):
    count = 0
    max_count = 4

    response = utils.getHtml(url)
    data = json.loads(response)
    for camgirl in data['results']:
        if count >= max_count:
            break

        status=camgirl['status']
        #if (status=='offline'):

         #   continue

        print(status)
        name = camgirl['slug'] #+ " [" + camgirl['status'] + "]"
        videourl = "https://www.camsoda.com/api/v1/video/vtoken/" + camgirl['slug']
        img = "https:" + camgirl['thumb']
        print(name)
        print(videourl)
        print(img);
        PlayvidCamSoda(videourl,name)
        count+=1

def PlayvidCamSoda(url, name):
    url = url + "?username=guest_" + str(random.randrange(100, 55555))
    response = utils.getHtml(url)
    data = json.loads(response)
    if "camhouse" in data['stream_name']:
       videourl = "https://camhouse.camsoda.com/" + data['app'] + "/mp4:" + data['stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']
    else:
       videourl = "https://" + data['edge_servers'][0] + "/" + data['app'] + "/mp4:" + data['stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']

    print(videourl);

def GetvidCamSoda(name):
    url="https://www.camsoda.com/api/v1/video/vtoken/"+name
    url = url + "?username=guest_" + str(random.randrange(100, 55555))
    response = utils.getHtml(url)
    data = json.loads(response)
    if "camhouse" in data['stream_name']:
       videourl = "https://camhouse.camsoda.com/" + data['app'] + "/mp4:" + data['stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']
    else:
       videourl = "https://" + data['edge_servers'][0] + "/" + data['app'] + "/mp4:" + data['stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']

    subprocess.Popen('mpv '+videourl, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(videourl);

#https://www.camsoda.com/api/v1/video/vtoken/loribauer

ListCamSoda('http://www.camsoda.com/api/v1/browse/women')
#ListCamSoda('http://www.camsoda.com/api/v1/browse/online')


#GetvidCamSoda("laratinelli")
