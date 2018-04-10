
from PyQt5.QtCore import (QFileInfo, QSignalMapper)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import (QApplication, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import (QMainWindow,
                             QMdiArea)





class VideoPlayer(QWidget):

    def __init__(self,sound, parent=None):
        super(VideoPlayer, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.isUntitled = True
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVolume(100)
        if sound==False:
           self.mediaPlayer.setVolume(0)
           self.mediaPlayer.setMuted(True)
           
        videoWidget = QVideoWidget()
        controlLayout = QVBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.setMinimumSize(60,60)



    def mousePressEvent(self, QMouseEvent):
        return
        

    def mouseReleaseEvent(self, QMouseEvent):
        
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
		    self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            print("Pause")

        


    def Player(self,str):
        self.mediaPlayer.setMedia(QMediaContent(QUrl(str)))
        self.mediaPlayer.play()


    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.setWindowTitle("Playing")
        elif self.mediaPlayer.state() == QMediaPlayer.StoppedState:
            self.setWindowTitle("Stop")
        elif self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.setWindowTitle("Pause")
        else:
            self.setWindowTitle("Unknow")




    def handleError(self):
        print("Error: " + self.mediaPlayer.errorString())








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

        self.clipboard = QApplication.clipboard()

        self.setWindowTitle("Qt5 Multi Video Player v0.02 - by Luis Santos AKA DJOKER")



    def closeEvent(self, event):
        self.mdiArea.closeAllSubWindows()
        if self.mdiArea.currentSubWindow():
            event.ignore()
        else:
            event.accept()

    def newFile(self):
        child = VideoPlayer(True)
        self.mdiArea.addSubWindow(child)
        url = self.clipboard.text()
        child.Player(url)
        child.show()

    def newMute(self):
        child = VideoPlayer(False)
        self.mdiArea.addSubWindow(child)
        url = self.clipboard.text()
        child.Player(url)
        child.show()

        return


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
        self.newAct = QAction( "&New", self,
                shortcut=QKeySequence.New, statusTip="Create a new Video Player",
                triggered=self.newFile)

        self.newActCam4 = QAction("&VideoMute", self,
                              shortcut=QKeySequence.New, statusTip="Create a new Video Player Mute",
                              triggered=self.newMute)

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
