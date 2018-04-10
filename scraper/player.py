
#############################################################################




from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

#QMdiSubWindow
class MdiPlayer(QtGui.QFrame):


    def __init__(self,Sound,Mdi):
        super(MdiPlayer, self).__init__()
        self.mdi=Mdi
        self.loading=1 
        self.sound=Sound
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
       # self.setFrameShape(QtGui.QFrame.NoFrame)
       # self.isUntitled = True
        self.media = Phonon.MediaObject(self)
        self.media.stateChanged.connect(self.handleStateChanged)
        self.video = Phonon.VideoWidget(self)
        self.video.setMinimumSize(50, 50)
        self.setBaseSize(80,80)
        self.audio = Phonon.AudioOutput(Phonon.VideoCategory,self)
        Phonon.createPath(self.media, self.video)
        
        if self.sound==True:
           Phonon.createPath(self.media, self.audio)
           self.audio.setVolume(100)
           
    
        layout = QtGui.QVBoxLayout(self)
        layout.setMargin(0)
        layout.addWidget(self.video)


        

    def Close(self):
        self.mdi.removeSubWindow(self)
        self.mdi.closeActiveSubWindow()
        print("close")


    def Player(self, url):
        self.media.setCurrentSource(Phonon.MediaSource(url))
        self.media.play()


    #def mousePressEvent(self, QMouseEvent):
	#	self.Close()
    
    def mouseReleaseEvent(self, QMouseEvent):
        print(str(self.media.state()))

        if (self.media.state() == Phonon.PlayingState):
            self.media.pause()
        elif (self.media.state() == Phonon.PausedState):
            self.media.play()
	
	
			
         
            

    def handleStateChanged(self, newstate, oldstate):
            
        if (oldstate == Phonon.PlayingState and  newstate == Phonon.StoppedState):
			self.Close()
		
          
          
        if newstate == Phonon.PlayingState:
			self.setWindowTitle("Plaing..")
			self.loading=1

        elif newstate == Phonon.BufferingState:
            self.setWindowTitle("Buffering")
            self.loading=1
      
        elif newstate == Phonon.StoppedState:
            self.setWindowTitle("Stop")
            print("Stop")
        elif newstate == Phonon.PausedState:
            self.setWindowTitle("Pause")

        elif newstate == Phonon.LoadingState:
            self.setWindowTitle("Loading")
            self.loading=1

        elif newstate == Phonon.ErrorState:
            self.setWindowTitle("ErrorState")
            self.loading=0

          
      
        	
		#	  if newstate == Phonon.ErrorState:
		#	     source = self.media.currentSource().fileName()
				#	     self.setWindowTitle("error:"+self.media.errorString().toLocal8Bit().data())
				#	     self.Close()
       
      #   elif (newstate != Phonon.LoadingState and  newstate != Phonon.BufferingState):
		#	  if newstate == Phonon.ErrorState:
		#	     source = self.media.currentSource().fileName()
				#	     self.setWindowTitle("error:"+self.media.errorString().toLocal8Bit().data())
				#	     self.Close()
       

    def closeEvent(self, event):
        event.accept()
        if self.media.state() == Phonon.PlayingState:
            self.media.stop()
        print("close event")    

        # event.ignore()




   


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.mdiArea = QtGui.QMdiArea()
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setCentralWidget(self.mdiArea)

        self.mdiArea.subWindowActivated.connect(self.updateMenus)
        self.windowMapper = QtCore.QSignalMapper(self)
        self.windowMapper.mapped[QtGui.QWidget].connect(self.setActiveSubWindow)

        self.createActions()
        self.createMenus()
      
        self.createStatusBar()
        self.updateMenus()

        self.clipboard = QtGui.QApplication.clipboard()

  

        self.setWindowTitle("Qt4 Multi Video Player v0.02 - by Luis Santos AKA DJOKER")
        

    def closeEvent(self, event):
        self.mdiArea.closeAllSubWindows()
        if self.mdiArea.currentSubWindow():
            event.ignore()
        else:
            event.accept()

    def newFile(self):
        child = MdiPlayer(True,self.mdiArea)
        url=self.clipboard.text()
        child.Player(url)
        self.mdiArea.addSubWindow(child)
        child.show()
        self.mdiArea.tileSubWindows()
        
    def newPlayer(self):
        child = MdiPlayer(False,self.mdiArea)
        url=self.clipboard.text()
        child.Player(url)
        self.mdiArea.addSubWindow(child)
        child.show()
        self.mdiArea.tileSubWindows()
    


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
     
        self.newAct = QtGui.QAction("&New Player",
                self, shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new Video Player", triggered=self.newFile)
        
        self.newActPlayer = QtGui.QAction( "&New Player Muted",
                self, shortcut=QtGui.QKeySequence.New,
                statusTip="Create a new Video Player Muted", triggered=self.newPlayer)

        self.exitAct = QtGui.QAction("E&xit", self,
                shortcut=QtGui.QKeySequence.Quit,
                statusTip="Exit the application",
                triggered=QtGui.qApp.closeAllWindows)

       
        self.closeAct = QtGui.QAction("Cl&ose", self,
                statusTip="Close the active window",
                triggered=self.mdiArea.closeActiveSubWindow)

        self.closeAllAct = QtGui.QAction("Close &All", self,
                statusTip="Close all the windows",
                triggered=self.mdiArea.closeAllSubWindows)

        self.tileAct = QtGui.QAction("&Tile", self,
                statusTip="Tile the windows",
                triggered=self.mdiArea.tileSubWindows)

        self.cascadeAct = QtGui.QAction("&Cascade", self,
                statusTip="Cascade the windows",
                triggered=self.mdiArea.cascadeSubWindows)

        self.nextAct = QtGui.QAction("Ne&xt", self,
                shortcut=QtGui.QKeySequence.NextChild,
                statusTip="Move the focus to the next window",
                triggered=self.mdiArea.activateNextSubWindow)

        self.previousAct = QtGui.QAction("Pre&vious", self,
                shortcut=QtGui.QKeySequence.PreviousChild,
                statusTip="Move the focus to the previous window",
                triggered=self.mdiArea.activatePreviousSubWindow)

        self.separatorAct = QtGui.QAction(self)
        self.separatorAct.setSeparator(True)

     

    def createMenus(self):
       
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.newActPlayer)
        self.fileMenu.addSeparator()

       

        self.windowMenu = self.menuBar().addMenu("&Window")
        self.updateWindowMenu()
        self.windowMenu.aboutToShow.connect(self.updateWindowMenu)

    



    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    

    def activeMdiChild(self):
        activeSubWindow = self.mdiArea.activeSubWindow()
        if activeSubWindow:
            return activeSubWindow.widget()
        return None

    def findMdiChild(self, fileName):
        canonicalFilePath = QtCore.QFileInfo(fileName).canonicalFilePath()

        for window in self.mdiArea.subWindowList():
            if window.widget().currentFile() == canonicalFilePath:
                return window
        return None

    

    def setActiveSubWindow(self, window):
        if window:
            self.mdiArea.setActiveSubWindow(window)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

