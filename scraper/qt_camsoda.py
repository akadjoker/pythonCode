from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib2
import StringIO
import utils
import os
import sys
import random
import json
import subprocess
import threading
import re


class ImageLabel(QtGui.QLabel):
    def __init__(self,w,h,url_image,video_url,_name):
        QtGui.QLabel.__init__(self)
        self.video = video_url
        self.name = _name
        data = urllib2.urlopen(url_image).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        pix = QtGui.QPixmap(image)
       # pix = pix.scaled(w, h, QtCore.Qt.KeepAspectRatio)
        self.setPixmap(pix)
        self.cb = QApplication.clipboard()

    #def mousePressEvent(self, QMouseEvent):
     #   return self.name

    def Playvid(self,url, name):
        url = url + "?username=guest_" + str(random.randrange(100, 55555))
        response = utils.getHtml(url)
        data = json.loads(response)
        if "camhouse" in data['stream_name']:
            videourl = "https://camhouse.camsoda.com/" + data['app'] + "/mp4:" + data[
                'stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']
        else:
            videourl = "https://" + data['edge_servers'][0] + "/" + data['app'] + "/mp4:" + data[
                'stream_name'] + "_mjpeg/playlist.m3u8?token=" + data['token']

        return videourl


    def mouseReleaseEvent(self, QMouseEvent):
        print("parse:"+self.video)
        player=self.Playvid(self.video,self.name)
        print(player)
        self.cb.clear(mode=self.cb.Clipboard)
        self.cb.setText(player, mode=self.cb.Clipboard)

        print self.name


class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)



        self.select_Text="female";
        self.max_cams=40
        self.cams_count=0


        container = QtGui.QWidget()

        scrollArea = QtGui.QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFrameStyle(QtGui.QFrame.NoFrame)
        scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        scrollArea.setWidget(container)





        comboBox = QtGui.QComboBox()
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

        okButton = QtGui.QPushButton("OK", self)
        okButton.setMaximumWidth(okButton.width())
        okButton.clicked.connect(self.onClick)

        vbox = QtGui.QVBoxLayout()
        vbox.setAlignment(QtCore.Qt.AlignLeft)




        hbox = QtGui.QHBoxLayout()
        hbox.setAlignment(QtCore.Qt.AlignLeft)


        hbox.addWidget(okButton)
        hbox.addWidget(comboBox)
        hbox.setMargin(2)
        hbox.setSpacing(5)

        vbox.addLayout(hbox)







        self.layout = QtGui.QGridLayout()
        self.layout.setAlignment(Qt.AlignTop)
        vbox.addLayout(self.layout)
        container.setLayout(vbox)
        layout = QtGui.QVBoxLayout(self)
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
        row = 0
        col = 0
        imagesPerRow = 4
        response = utils.getHtml(url)
        data = json.loads(response)
        for camgirl in data['results']:
            status = camgirl['status']
            # if (status=='offline'):
            #   continue

            name = camgirl['slug']  # + " [" + camgirl['status'] + "]"
            videourl = "https://www.camsoda.com/api/v1/video/vtoken/" + camgirl['slug']
            img = "https:" + camgirl['thumb']
            lbl = ImageLabel(100, 100, img, videourl, name)
            self.layout.addWidget(lbl, row, col)
            QtGui.QApplication.processEvents()
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
        url=str("http://www.camsoda.com/api/v1/browse/"+self.select_Text);
        self.loadPerformers(url)
        return




if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Phonon Player')
    window = Window()
    window.setGeometry(200, 100, 700, 600)
    window.show()
    sys.exit(app.exec_())
