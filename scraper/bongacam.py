
import urllib2
import os
import sys
import random
import sqlite3
import json
import subprocess
import utils

#             'http://tools.bongacams.com/promo.php?c=226355&type=api&api_type=json&categories[]=female'
#             'http://tools.bongacams.com/promo.php?c=226355&type=api&api_type=json&categories[]=male'
#             'http://tools.bongacams.com/promo.php?c=226355&type=api&api_type=json&categories[]=transsexual
#             'http://tools.bongacams.com/promo.php?c=226355&type=api&api_type=json&categories[]=couples'


def List(url):
    try:
        data = utils.getHtml(url)
    except:

        return None
    model_list = json.loads(data)
    for camgirl in model_list:
        img = 'https:' + camgirl['profile_images']['thumbnail_image_big_live']
        username = camgirl['username']
        name = camgirl['display_name']
        print(img)
        print(name)
        print(username)
        Playvid(username,name)

        break

def Playvid(username, name):
    try:
       postRequest = {'method' : 'getRoomData', 'args[]' : 'false', 'args[]' : str(username)}
       response = utils.postHtml('http://bongacams.com/tools/amf.php', form_data=postRequest,headers={'X-Requested-With' : 'XMLHttpRequest'},compression=False)
    except:
        utils.notify('Oh oh','Couldn\'t find a playable webcam link')
        return None

    amf_json = json.loads(response)

    if amf_json['localData']['videoServerUrl'].startswith("//mobile"):
       videourl = 'https:' + amf_json['localData']['videoServerUrl'] + '/hls/stream_' + username + '.m3u8'
    else:
       videourl = 'https:' + amf_json['localData']['videoServerUrl'] + '/hls/stream_' + username + '/playlist.m3u8'

    print(videourl)
    subprocess.Popen('mpv ' + videourl, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


#List("http://tools.bongacams.com/promo.php?c=226355&type=api&api_type=json&categories[]=female")

Playvid("Meegan","Meegan")