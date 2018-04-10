
import urllib2
import os
import sys
import re
import requests
import random
import sqlite3
import json
import subprocess
import utils
import websocket
import random
import json

def List(url):
    try:
        listhtml = utils.getHtml2(url)
        print(listhtml)
    except:

        return None
    match = re.compile("model_detail=(.*?)&.*?img src=(.*?)jpg.*?</div>", re.DOTALL | re.IGNORECASE).findall(listhtml)
    for name, img in match:
        url = name
        name = utils.cleantext(name)
        img = img + 'jpg'
        #img = img.replace('90x90', '300x300')
        print(url)
        print(name)
        print(img)
        u=myfreecam_start(url)
        print(u)
        #Url = "http://video" + str(CAMGIRLSERVER) + ".myfreecams.com:1935/NxServer/ngrp:mfc_" + \
         #     str(CAMGIRLCHANID) + ".f4v_mobile/playlist.m3u8"  # better resolution


# from iptvplayer

vs_str = {}
vs_str[0] = "PUBLIC"
vs_str[2] = "AWAY"
vs_str[12] = "PVT"
vs_str[13] = "GROUP"
vs_str[90] = "CAM OFF"
vs_str[127] = "OFFLINE"
vs_str[128] = "TRUEPVT"


def fc_decode_json(m):
    try:
        m = m.replace('\r', '\\r').replace('\n', '\\n')
        return json.loads(m[m.find("{"):].decode("utf-8", "ignore"))
    except:
        return json.loads("{\"lv\":0}")


def read_model_data(m):
    global CAMGIRLSERVER
    global CAMGIRLCHANID
    global CAMGIRLUID
    usr = ''
    msg = fc_decode_json(m)
    try:
        sid = msg['sid']
        level = msg['lv']
    except:
        return

    vs = msg['vs']

    if vs == 127:
        return

    usr = msg['nm']
    CAMGIRLUID = msg['uid']
    CAMGIRLCHANID = msg['uid'] + 100000000
    camgirlinfo = msg['m']
    flags = camgirlinfo['flags']
    u_info = msg['u']

    try:
        CAMGIRLSERVER = u_info['camserv']
        if CAMGIRLSERVER >= 500:
            CAMGIRLSERVER = CAMGIRLSERVER - 500
        if vs != 0:
            CAMGIRLSERVER = 0
    except KeyError:
        CAMGIRLSERVER = 0

    truepvt = ((flags & 8) == 8)

    buf = usr + " =>"
    try:
        if truepvt == 1:
            buf += " (TRUEPVT)"
        else:
            buf += " (" + vs_str[vs] + ")"
    except KeyError:
        pass


def myfreecam_start(url):
    global CAMGIRL
    global CAMGIRLSERVER
    global CAMGIRLUID
    global CAMGIRLCHANID
    CAMGIRL = url
    CAMGIRLSERVER = 0

    try:
        xchat = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
                 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
                 33, 34, 35, 36, 39, 40, 41, 42, 43, 44, 45, 46,
                 47, 48, 49, 56, 57, 58, 59, 60, 61
                 ]
        #host = "ws://xchat" + str(random.choice(xchat)) + ".myfreecams.com:8080/fcsl"
        host = "ws://xchat60.myfreecams.com:8080/fcsl"
        ws = websocket.WebSocket()
        ws = websocket.create_connection(host)
        ws.send("hello fcserver\n\0")
        ws.send("1 0 0 20071025 0 guest:guest\n\0")
    except:
        print('fucked')
        return ''
    rembuf = ""
    quitting = 0
    while quitting == 0:
        sock_buf = ws.recv()
        sock_buf = rembuf + sock_buf
        rembuf = ""
        while True:
            hdr = re.search(r"(\w+) (\w+) (\w+) (\w+) (\w+)", sock_buf)
            if bool(hdr) == 0:
                break

            fc = hdr.group(1)

            mlen = int(fc[0:4])
            fc_type = int(fc[4:])

            msg = sock_buf[4:4 + mlen]

            if len(msg) < mlen:
                rembuf = ''.join(sock_buf)
                break

            msg = urllib.unquote(msg)

            if fc_type == 1:
                ws.send("10 0 0 20 0 %s\n\0" % CAMGIRL)
            elif fc_type == 10:
                read_model_data(msg)
                quitting = 1

            sock_buf = sock_buf[4 + mlen:]

            if len(sock_buf) == 0:
                break
    ws.close()
    if CAMGIRLSERVER != 0:
        Url = "http://video" + str(CAMGIRLSERVER) + ".myfreecams.com:1935/NxServer/ngrp:mfc_" + \
              str(CAMGIRLCHANID) + ".f4v_mobile/playlist.m3u8"  # better resolution
        return Url
    else:
        pass


List('https://www.myfreecams.com/mfc2/php/online_models_splash.php')