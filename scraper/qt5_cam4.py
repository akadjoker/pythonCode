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



    def getLink(self,url):
        video_link="none"
        listhtml = utils.getHtml(url,'', utils.mobileagent)
        match = re.compile('src="(http[^"]+m3u8)', re.DOTALL | re.IGNORECASE).findall(listhtml)
        return match[0]

        if match:
            videourl = match[0]
            listas = utils.getHtml(videourl,'', utils.mobileagent)
            mylist = listas.split("\n")
            numList = len(mylist)
            print(numList)
            if numList == 5:
                video_link = mylist[3]
            else:
                if numList == 11:
                    video_link = mylist[3]
        #QMessageBox.information(
         #           self, 'Scrap',
          #          'Scraped :D ', QMessageBox.Ok)
          

        return    video_link

    def mouseReleaseEvent(self, QMouseEvent):
        print("parse:"+self.video)
        player=self.getLink(self.video)
        print(player)
        self.cb.clear(mode=self.cb.Clipboard)
        self.cb.setText(player, mode=self.cb.Clipboard)

        print self.name


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)



        container = QWidget()

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFrameStyle(QFrame.NoFrame)
        scrollArea.setFrameShadow(QFrame.Plain)
        scrollArea.setWidget(container)

        self.editBox = QLineEdit()
        self.editBox.setMinimumWidth(250)



        comboBox = QComboBox()
        comboBox.setMinimumWidth(250)
        with open("list", "r") as ins:
            for line in ins:
                comboBox.addItem(line)

        self.editBox.setText(comboBox.itemText(0))



        comboBox.activated[str].connect(self.style_choice)


        okButton = QPushButton("OK",self)
        #okButton.connect(okButton, SIGNAL('clicked()'), self.onClick)
        okButton.clicked.connect(self.onClick)


        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignLeft)




        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignLeft)
        hbox.addWidget(comboBox)
        hbox.addWidget(self.editBox)
        hbox.addWidget(okButton)
      #  hbox.setMargin(2)
        hbox.setSpacing(5)

        vbox.addLayout(hbox)







        self.layout = QGridLayout()
        self.layout.setAlignment(Qt.AlignTop)
        vbox.addLayout(self.layout)
        container.setLayout(vbox)
        layout = QVBoxLayout(self)
        layout.addWidget(scrollArea)
        vbox.setAlignment(Qt.AlignTop)
        hbox.setAlignment(Qt.AlignTop)

    def clearLayout(self, layout):
        for i in range(layout.count()):
            layout.itemAt(i).widget().close()

    def onClick(self):
        self.clearLayout(self.layout)
        url =str(self.editBox.text())
        print (url)
        listhtml = utils.getHtml(url, '')
        match = re.compile(
            'profileDataBox"> <!-- preview --> <a href="([^"]+)".*?src="([^"]+)" title="Chat Now Free with ([^"]+)"',
            re.DOTALL | re.IGNORECASE).findall(listhtml)

        row = 0
        col = 0
        imagesPerRow = 4

        for videourl, img, name in match:
            name = utils.cleantext(name)
            videourl = "http://www.cam4.com" + videourl
            lbl = ImageLabel(100, 100, img, videourl, name)
            self.layout.addWidget(lbl, row, col)
            QApplication.processEvents()
            col += 1
            if col % imagesPerRow == 0:
                row += 1
                col = 0


        print("Openation completed...")





    def style_choice(self, text):
        self.editBox.setText(text)
        print(text)

    def handleButton(self):
        return 0




if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    app.setApplicationName('Cam4 Scrap')
    window = Window()
    window.setGeometry(200, 100, 700, 600)
    window.show()
    sys.exit(app.exec_())
