
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ConnectUi
import videodatabase
import videoplayerlogic
import VideoplayerUi
class Mainlogic:
    def __init__(self):
        
        self.mainlogic=ConnectUi.Connect()
        self.videoplayerui=VideoplayerUi.VideoPlayer()
        self.videoplayerlogic=videoplayerlogic.VideoPlayerLogic()
        self.mainlogic.show()
        self.videodata=videodatabase.VideoData()


        self.mainlogic.playlist.addpushbutton.clicked.connect(self.CheckAddPlaylist)
        self.mainlogic.check.cancelbutton.clicked.connect(self.Uihide)
        self.mainlogic.check.addpushbutton.mousePressEvent=lambda event,name2=self.mainlogic.playlist.addpushbutton:self.AddPlaylist(event,name2)
        self.mainlogic.playlist.addpushbutton.enterEvent=lambda event:self.EnterAnimation(event)
        self.mainlogic.playlist.addpushbutton.leaveEvent=lambda event:self.LeaveAnimation(event)
        self.mainlogic.playlist.editbutton.clicked.connect(self.VideoListEditButton)
        self.videoplayerui.previouspagebutton.clicked.connect(self.BackToVideoList)
        self.mainlogic.playlist.cancelbutton.clicked.connect(self.CanCelEdit)
        self.videodata.StoreButtons()

        for i in range(0,len(self.videodata.buttonlist2)):
            self.mainlogic.playlist.playlistlocate.buttonlist[i].clicked.connect(self.GoToVideoPlayerPage)
            self.mainlogic.playlist.playlistlocate.buttonlist[i].clicked.connect(self.videoplayerlogic.asdf)
        for i in range(0,len(self.mainlogic.playlist.playlistlocate.buttonlist)):
            self.MyEvent(i)
        self.mainlogic.playlist.searchbutton.clicked.connect(self.SearchPage)
    
    #페이지 이동
    def SearchPage(self):
        self.mainlogic.mainwindow.resize(self.mainlogic.search.searchui_x,self.mainlogic.search.searchui_y)
        self.mainlogic.paper.setCurrentIndex(1)

    def BackToVideoList(self):
        self.mainlogic.mainwindow.resize(self.mainlogic.playlist.playlistui_x,self.mainlogic.playlist.playlistui_y)
        self.mainlogic.paper.setCurrentIndex(0)

    def GoToVideoPlayerPage(self):
        self.mainlogic.mainwindow.hide()
        
        self.videoplayerlogic.asdf()

    #애니메이션 처리
    def EnterAnimation(self,event):
        self.mainlogic.playlist.addpushbutton.setStyleSheet('background-image:url(plus2.png);''border:1px soild black;')
        
    def LeaveAnimation(self,event):
        self.mainlogic.playlist.addpushbutton.setStyleSheet('border:1px solid black;''background-image:url(plus.png);')
    
    def FolderAnimation(self,event,i):
        
        self.mainlogic.playlist.playlistlocate.buttonlist[i].setStyleSheet('background-image:url(folder2.png);''border:1px soild black;')
        
    def FolderLeaveAnimation(self,event,i):
  
        self.mainlogic.playlist.playlistlocate.buttonlist[i].setStyleSheet('background-image:url(folder.png);''border:1px soild black;')
       

    def MyEvent(self,i):
        self.i=i
        self.videodata.StoreButtons()
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].enterEvent=lambda event,i=self.i:self.FolderAnimation(event,i)
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].leaveEvent=lambda event,i=self.i:self.FolderLeaveAnimation(event,i)

    #재생목록 편집 함수


    def VideoListEditButton(self):
        self.mainlogic.playlist.applybutton.show()
        self.mainlogic.playlist.cancelbutton.show()
        try:
            for i in range(0,len(self.videodata.deletebutton)):
                self.videodata.deletebutton[i]=QtWidgets.QPushButton(self.mainlogic.playlist.playlistui)
                
                if 100+(300*i)<=1000 :
                    self.videodata.deletebutton[i].setGeometry(100+(300*i+170),400,30,30)
                    self.videodata.deletebutton[i].setStyleSheet('background:red;''border-radius:15px;')
                    self.videodata.deletebutton[i].setText('X')
                    self.videodata.deletebutton[i].setFont(QtGui.QFont(None,15))
                    self.videodata.deletebutton[i].show()
                
                elif 100+(300*i)>=1300:
                    self.videodata.deletebutton[i].setGeometry(100+(300*(i-4)+170),660,30,30)
                    self.videodata.deletebutton[i].setStyleSheet('background:red;''border-radius:15px;')
                    self.videodata.deletebutton[i].setText('X')
                    self.videodata.deletebutton[i].setFont(QtGui.QFont(None,15))
                    self.videodata.deletebutton[i].show()
                    self.videodata.deletebutton[i].show()
        except AttributeError:
            pass
            
        for i in range(0,len(self.mainlogic.playlist.playlistlocate.deletebutton)):
            
            if i<=4 :
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setGeometry(100+(300*i+170),400,30,30)
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setStyleSheet('border-radius:15px;''background:red;')
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setText('X')
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setFont(QtGui.QFont(None,15))
            if i>=4 :
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setGeometry(100+(300*(i-4)+170),660,30,30)
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setStyleSheet('border-radius:15px;''background:red;')
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setText('X')
                self.mainlogic.playlist.playlistlocate.deletebutton[i].setFont(QtGui.QFont(None,15))
            self.mainlogic.playlist.playlistlocate.deletebutton[i].show()

            self.mainlogic.playlist.editbutton.hide()
            

    def CanCelEdit(self):
        self.mainlogic.playlist.applybutton.hide()
        self.mainlogic.playlist.cancelbutton.hide()
        self.mainlogic.playlist.editbutton.show()
    
        for i in range(0,len(self.mainlogic.playlist.playlistlocate.deletebutton)):
            self.mainlogic.playlist.playlistlocate.deletebutton[i].hide()
        for i in range(0,len(self.videodata.deletebutton)):
            self.videodata.deletebutton[i].hide()

    #재생목록 추가 관련 함수

    def CheckAddPlaylist(self):
        self.videodata.FindCount()
        self.mainlogic.check.mainwindow.show()
        self.mainlogic.check.lineedit.setText('재생목록'+str(self.videodata.result[0][0]))


    def Uihide(self):
        self.mainlogic.check.mainwindow.hide()

    def AddPlaylist(self,event,name2):
        self.name2=name2
        self.videodata.CreatePlaylist(self.mainlogic.check.lineedit.text())
        self.videodata.StoreButtons()
        self.MakePlaylist()
        
        self.videodata.UpdateCount()
        self.videodata.FindCount()
        if 100+(300*self.videodata.result[0][0]<=700) :
            self.name2.setGeometry(100+(300*self.videodata.result[0][0]),350,200,200)
            if 100+(300*self.videodata.result[0][0])>1000:
                self.name2.setGeometry(100+(300*(self.videodata.result[0][0]-4)),350*2-100,200,200)
        self.mainlogic.check.mainwindow.hide()

    

    def MakePlaylist(self):
        self.videodata.FindCount()
        
        self.videodata.buttonlist[self.videodata.result[0][0]]=QtWidgets.QPushButton(self.mainlogic.playlist.playlistui)
       
        self.videodata.buttonlabellist[self.videodata.result[0][0]]=QtWidgets.QLabel(self.mainlogic.playlist.playlistui)
        

        if 100+(300*self.videodata.result[0][0]<=700) :
            self.videodata.buttonlist[self.videodata.result[0][0]].setGeometry(100+(300*self.videodata.result[0][0]),350,200,200)
            self.videodata.buttonlist[self.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
    
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setGeometry(100+(300*self.videodata.result[0][0])+40,450,200,200)
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setStyleSheet('color:white;')

            self.videodata.buttonlist[self.videodata.result[0][0]].clicked.connect(self.GoToVideoPlayerPage)

            self.videodata.buttonlist[self.videodata.result[0][0]].show()
            self.videodata.buttonlabellist[self.videodata.result[0][0]].show()

            if 100+(300*self.videodata.result[0][0])>1000:
                self.videodata.buttonlist[self.videodata.result[0][0]].setGeometry(100+(300*(self.videodata.result[0][0]-4)),350*2-100,200,200)
                self.videodata.buttonlist[self.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
                self.videodata.buttonlist[self.videodata.result[0][0]].show()

                self.videodata.buttonlabellist[self.videodata.result[0][0]].setGeometry(100+(300*(self.videodata.result[0][0]-4))+40,350*2,200,200)
                self.videodata.buttonlabellist[self.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
                self.videodata.buttonlabellist[self.videodata.result[0][0]].setStyleSheet('color:white;')

                self.videodata.buttonlist[self.videodata.result[0][0]].clicked.connect(self.GoToVideoPlayerPage)

                self.videodata.buttonlist[self.videodata.result[0][0]].show()
        
        
    
        

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=Mainlogic()
    sys.exit(app.exec_())