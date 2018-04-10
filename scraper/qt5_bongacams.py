from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWebKit import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import*
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
        
import sys
import urllib2
import StringIO
import utils
import os
import sys
import json
import subprocess
import threading
import re


class ImageLabel(QLabel):
    def __init__(self,w,h,url_image,video_url,_name):
        QLabel.__init__(self)
        self.video = video_url
        self.name = _name
        data = urllib2.urlopen(url_image).read()
        image = QImage()
        image.loadFromData(data)
        pix = QPixmap(image)
       # pix = pix.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.setPixmap(pix)
        self.cb = QApplication.clipboard()

    #def mousePressEvent(self, QMouseEvent):
     #   return self.name

    def Playvid(self,username, name):
        try:
            postRequest = {'method': 'getRoomData', 'args[]': 'false', 'args[]': str(username)}
            response = utils.postHtml('http://bongacams.com/tools/amf.php', form_data=postRequest,
                                      headers={'X-Requested-With': 'XMLHttpRequest'}, compression=False)
        except:
            print('Oh oh Couldnt find a playable webcam link')
            return None

        amf_json = json.loads(response)

        if amf_json['localData']['videoServerUrl'].startswith("//mobile"):
            videourl = 'https:' + amf_json['localData']['videoServerUrl'] + '/hls/stream_' + username + '.m3u8'
        else:
            videourl = 'https:' + amf_json['localData']['videoServerUrl'] + '/hls/stream_' + username + '/playlist.m3u8'

        return videourl


    def mouseReleaseEvent(self, QMouseEvent):
        print("parse:"+self.video)
        player=self.Playvid(self.video,self.name)
        print(player)
        self.cb.clear(mode=self.cb.Clipboard)
        self.cb.setText(player, mode=self.cb.Clipboard)

        print self.name


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)



        self.select_Text="female";
        self.max_cams=40
        self.cams_count=0


        container = QWidget()

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFrameStyle(QFrame.NoFrame)
        scrollArea.setFrameShadow(QFrame.Plain)
        scrollArea.setWidget(container)





        comboBox = QComboBox()
        comboBox.setMinimumWidth(100)
        comboBox.addItem("female")
        comboBox.addItem("blonde")
        comboBox.addItem("lesbian")
        comboBox.addItem("asian")
        comboBox.addItem("big-butt")
        comboBox.addItem("new")
        comboBox.addItem("ebony")
        comboBox.addItem("babes")
        comboBox.addItem("latina")
        comboBox.addItem("teens-18")
        comboBox.addItem("curvy")
        comboBox.addItem("college-girls")
        comboBox.addItem("shaved-pussy")
        comboBox.addItem("anal-play")
        comboBox.addItem("brunette")
        comboBox.addItem("big-tits")
        comboBox.addItem("medium-tits")
        comboBox.addItem("bbw")
        comboBox.addItem("toys")
        comboBox.addItem("housewives")
        comboBox.addItem("petite-body")
        comboBox.addItem("pornstar")
        comboBox.addItem("squirt")
        comboBox.addItem("white-girls")
        comboBox.addItem("couples")
        comboBox.addItem("transsexual")
        comboBox.addItem("male")
        comboBox.setMaximumWidth(comboBox.width())



        comboBox.activated[str].connect(self.style_choice)

        okButton = QPushButton("OK", self)
        okButton.setMaximumWidth(okButton.width())
        okButton.clicked.connect(self.onClick)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignLeft)




        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignLeft)


        hbox.addWidget(okButton)
        hbox.addWidget(comboBox)
      #  hbox.setMargin(2)
     #   hbox.setSpacing(5)

        vbox.addLayout(hbox)







        self.layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignTop)
        vbox.addLayout(self.layout)
        container.setLayout(vbox)
        layout = QVBoxLayout(self)
        layout.addWidget(scrollArea)
        vbox.setAlignment(Qt.AlignTop)
        hbox.setAlignment(Qt.AlignTop)

    def style_choice(self, text):
        print(text)
    def clearLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().close()

    def loadPerformers(self, url):
        print(url)
        self.cams_count = 0
        self.clearLayout(self.layout)
        data = utils.getHtml(url)
        model_list = json.loads(data)
        row = 0
        col = 0
        imagesPerRow = 4
        for camgirl in model_list:
            img = 'https:' + camgirl['profile_images']['thumbnail_image_big_live']
            username = camgirl['username']
            name = camgirl['display_name']
            lbl = ImageLabel(100, 100, img, username, name)
            self.layout.addWidget(lbl, row, col)
            QApplication.processEvents()
            col += 1

            if col % imagesPerRow == 0:
               row += 1
               col = 0

            if self.cams_count >= self.max_cams:
               break
            self.cams_count += 1
        print("Operation completed...")











    def style_choice(self, text):
        self.select_Text=text
        print(text)

    def onClick(self):
        print(self.select_Text)
        url=str("http://tools.bongacams.com/promo.php?c=226355&type=api&api_type=json&categories[]="+self.select_Text);
        self.loadPerformers(url)
        return




if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    app.setApplicationName('Phonon Player')
    window = Window()
    window.setGeometry(200, 100, 700, 600)
    window.show()
    sys.exit(app.exec_())
