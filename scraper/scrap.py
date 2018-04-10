
from PyQt5.QtCore import (QFile, QFileInfo, QPoint, QSettings, QSignalMapper,
        QSize, QTextStream,QUrl, Qt)
from PyQt5.QtGui import QIcon, QKeySequence,QClipboard
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,
        QMdiArea, QMessageBox, QTextEdit, QWidget)
from PyQt5.QtWidgets import QApplication, QWidget ,QMenu,QAction
from PyQt5.QtWebKitWidgets import QWebView, QWebPage
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)

import re
import urllib
import urllib2
import re
import requests

Request = urllib2.Request
urlopen = urllib2.urlopen


mobileagent = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}

HTTP_HEADERS_IPAD = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4'}
cbheaders = {'User-Agent': HTTP_HEADERS_IPAD,
       'Accept': '*/*',
       'Connection': 'keep-alive'}

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

headers = {'User-Agent': USER_AGENT,
           'Accept': '*/*',
           'Connection': 'keep-alive'}





class BrowserCam4(QWebView):
    def __init__(self,MainWindow):
        # QWebView
        self.view = QWebView.__init__(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isUntitled = True



        self.MainWindow=MainWindow


        self.linkClicked.connect(self.handleLinkClicked)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)

    def getHtml(self, url, hdr=None):
        data = None
        try:
            if not hdr:
                req = Request(url, data, headers)
            else:
                req = Request(url, data, hdr)

            response = urlopen(req, timeout=60)
            data = response.read()
            response.close()
        except urllib2.HTTPError as e:
            data = e.read()
            raise urllib2.HTTPError()
        return data

   


    def contextMenuEvent(self, event):
        pos = event.pos()
        element = self.page().mainFrame().hitTestContent(pos)
        link_url = str(element.linkUrl().toString())

        player=self.getLink(link_url)

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(player, mode=cb.Clipboard)

        print(link_url)
        print(player)

    def handleLinkClicked(self, url):
        print("link",url)

    def acceptNavigationRequest(self, frame, request, type):
        print('Navigation Request:', request.url())
        return False

    def Open(self):
        print('Navigation Request:', self.url())

    def load(self, url):
        self.setUrl(QUrl(url))

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def onLinkHovered(self,over,overtile):
        print("over")

    def getLink(self,url):
        video_link="none"
        listhtml = self.getHtml(url, mobileagent)
        match = re.compile('src="(http[^"]+m3u8)', re.DOTALL | re.IGNORECASE).findall(listhtml)
        if match:
            videourl = match[0]
            listas = self.getHtml(videourl, mobileagent)
            mylist = listas.split("\n")
            print(str(mylist))
            numList = len(mylist)
            print(numList)
            if numList == 5:
                video_link = mylist[3]
            else:
                if numList == 11:
                    video_link = mylist[3]
                    
        return match[0]
        return    video_link


    def disableJS(self):
        settings = QWebSettings.globalSettings()

        settings.setAttribute(QWebSettings.JavascriptEnabled, False)



class BrowserChaturbate(QWebView):
    def __init__(self,MainWindow):
        # QWebView
        self.view = QWebView.__init__(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isUntitled = True



        self.MainWindow=MainWindow


        self.linkClicked.connect(self.handleLinkClicked)
        self.setWindowTitle('Loading...')
        self.titleChanged.connect(self.adjustTitle)




    def getLink(self, url):
        result = requests.get(url)
        match = re.compile('<head>(.+?)</html>', re.DOTALL).findall(result.content)
        string = str(match).replace('\\', '').replace('(', '').replace(')', '')
        return  re.compile("playsinline autoplay><source src='(.+?)'").findall(string)[0]
       


    def contextMenuEvent(self, event):
        pos = event.pos()
        element = self.page().mainFrame().hitTestContent(pos)
        link_url = str(element.linkUrl().toString())

        player=self.getLink(link_url)

        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(player, mode=cb.Clipboard)

        print(link_url)
        print(player)

    def handleLinkClicked(self, url):
        print("link",url)

    def acceptNavigationRequest(self, frame, request, type):
        print('Navigation Request:', request.url())
        return False

    def Open(self):
        print('Navigation Request:', self.url())

    def load(self, url):
        self.setUrl(QUrl(url))

    def adjustTitle(self):
        self.setWindowTitle(self.title())

    def onLinkHovered(self,over,overtile):
        print("over")


    def disableJS(self):
        settings = QWebSettings.globalSettings()

        settings.setAttribute(QWebSettings.JavascriptEnabled, False)
class MdiChild(QTextEdit):
    sequenceNumber = 1

    def __init__(self):
        super(MdiChild, self).__init__()

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isUntitled = True



    def closeEvent(self, event):
         event.accept()





class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.mdiArea = QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)

        self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.windowMapper = QSignalMapper(self)
        self.windowMapper.mapped[QWidget].connect(self.setActiveSubWindow)

        self.createActions()
        self.createMenus()

        self.createStatusBar()
        self.updateMenus()



        self.setWindowTitle("MDI")



    def closeEvent(self, event):
        self.mdiArea.closeAllSubWindows()
        if self.mdiArea.currentSubWindow():
            event.ignore()
        else:
            event.accept()

    def newFile(self):
        child = BrowserChaturbate(self.mdiArea)
        self.mdiArea.addSubWindow(child)
        child.load("https://www.chaturbate.com/")
        child.resize(320, 240)
        child.show()



    def newCam4(self):
        child = BrowserCam4(self.mdiArea)
        self.mdiArea.addSubWindow(child)
        child.load("https://www.cam4.com")
        child.resize(320, 240)
        child.show()


    def updateMenus(self):
        hasMdiChild = (self.activeMdiChild() is not None)

        self.closeAct.setEnabled(hasMdiChild)
        self.closeAllAct.setEnabled(hasMdiChild)
        self.tileAct.setEnabled(hasMdiChild)
        self.cascadeAct.setEnabled(hasMdiChild)
        self.nextAct.setEnabled(hasMdiChild)
        self.previousAct.setEnabled(hasMdiChild)
        self.separatorAct.setVisible(hasMdiChild)



    def updateWindowMenu(self):
        self.windowMenu.clear()
        self.windowMenu.addAction(self.closeAct)
        self.windowMenu.addAction(self.closeAllAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.tileAct)
        self.windowMenu.addAction(self.cascadeAct)
        self.windowMenu.addSeparator()
        self.windowMenu.addAction(self.nextAct)
        self.windowMenu.addAction(self.previousAct)
        self.windowMenu.addAction(self.separatorAct)

        windows = self.mdiArea.subWindowList()
        self.separatorAct.setVisible(len(windows) != 0)



    def createMdiChild(self):
        child = MdiChild()
        self.mdiArea.addSubWindow(child)



        return child

    def createActions(self):
        self.newAct = QAction( "&Chartubate", self,
                shortcut=QKeySequence.New, statusTip="Browse Chartubate",
                triggered=self.newFile)

        self.newActCam4 = QAction("&Cam4", self,
                              shortcut=QKeySequence.New, statusTip="Browse Cam4",
                              triggered=self.newCam4)

        self.closeAct = QAction("Cl&ose", self,
                statusTip="Close the active window",
                triggered=self.mdiArea.closeActiveSubWindow)

        self.closeAllAct = QAction("Close &All", self,
                statusTip="Close all the windows",
                triggered=self.mdiArea.closeAllSubWindows)

        self.tileAct = QAction("&Tile", self, statusTip="Tile the windows",
                triggered=self.mdiArea.tileSubWindows)

        self.cascadeAct = QAction("&Cascade", self,
                statusTip="Cascade the windows",
                triggered=self.mdiArea.cascadeSubWindows)

        self.nextAct = QAction("Ne&xt", self, shortcut=QKeySequence.NextChild,
                statusTip="Move the focus to the next window",
                triggered=self.mdiArea.activateNextSubWindow)

        self.previousAct = QAction("Pre&vious", self,
                shortcut=QKeySequence.PreviousChild,
                statusTip="Move the focus to the previous window",
                triggered=self.mdiArea.activatePreviousSubWindow)

        self.separatorAct = QAction(self)
        self.separatorAct.setSeparator(True)



    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.newActCam4)

        self.exitAct = QAction("E&xit", self, shortcut=QKeySequence.Quit,
                               statusTip="Exit the application",
                               triggered=QApplication.instance().closeAllWindows)

        self.fileMenu.addSeparator()
        action = self.fileMenu.addAction("Switch layout direction")
        action.triggered.connect(self.switchLayoutDirection)
        self.fileMenu.addAction(self.exitAct)



        self.windowMenu = self.menuBar().addMenu("&Window")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

        self.menuBar().addSeparator()






    def createStatusBar(self):
        self.statusBar().showMessage("Ready")



    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def findMdiChild(self, fileName):
        canonicalFilePath = QFileInfo(fileName).canonicalFilePath()

        for window in self.mdiArea.subWindowList():
            if window.widget().currentFile() == canonicalFilePath:
                return window
        return None

    def switchLayoutDirection(self):
        if self.layoutDirection() == Qt.LeftToRight:
            QApplication.setLayoutDirection(Qt.RightToLeft)
        else:
            QApplication.setLayoutDirection(Qt.LeftToRight)

    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
