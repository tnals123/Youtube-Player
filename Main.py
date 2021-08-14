
from urllib import request
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import vlc
import pafy
import ConnectUi
import videodatabase
import videoplayerlogic
import VideoplayerUi
import requests
################################   데이터베이스에 리스트 하나 더 만들어서 매개변수에 넣을 리스트 하나 만들기
class Mainlogic:
    def __init__(self):
        self.count=0
        self.mainlogic=ConnectUi.Connect()
        self.videoplayerui=VideoplayerUi.VideoPlayer()
        
        self.mainlogic.show()
        
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()

        if sys.platform.startswith("linux"):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoplayerui.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.videoplayerui.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.videoplayerui.videoframe.winId())

        self.mainlogic.playlist.addpushbutton.clicked.connect(self.CheckAddPlaylist)
        self.mainlogic.check.cancelbutton.clicked.connect(self.Uihide)
        self.mainlogic.check.addpushbutton.mousePressEvent=lambda event,name2=self.mainlogic.playlist.addpushbutton:self.AddPlaylist(event,name2)
        self.mainlogic.playlist.addpushbutton.enterEvent=lambda event:self.EnterAnimation(event)
        self.mainlogic.playlist.addpushbutton.leaveEvent=lambda event:self.LeaveAnimation(event)
        self.mainlogic.playlist.editbutton.clicked.connect(self.VideoListEditButton)
        self.videoplayerui.previouspagebutton.clicked.connect(self.BackToVideoList)
        self.mainlogic.playlist.cancelbutton.clicked.connect(self.CanCelEdit)
        self.videoplayerui.pausebutton.clicked.connect(self.PlayPause)
        self.videoplayerui.playbutton.clicked.connect(self.PlayPause)
        self.videoplayerui.stopbutton.clicked.connect(self.VideoStop)
        self.videoplayerui.volumeslider.valueChanged.connect(self.setVolume)
        self.videoplayerui.nextbutton.clicked.connect(self.NextVideo)
        self.videoplayerui.backbutton.clicked.connect(self.PreviousVideo)
        self.videoplayerui.miniplayerbutton.clicked.connect(self.MiniPlayer)
        #미니플레이어 함수
        self.mainlogic.miniplayerui.pausebutton.clicked.connect(self.PlayPause)
        self.mainlogic.miniplayerui.playbutton.clicked.connect(self.PlayPause)
        self.mainlogic.miniplayerui.stopbutton.clicked.connect(self.VideoStop)
        self.mainlogic.miniplayerui.volumeslider.valueChanged.connect(self.setVolume)
        self.mainlogic.miniplayerui.nextbutton.clicked.connect(self.NextVideo)
        self.mainlogic.miniplayerui.backbutton.clicked.connect(self.PreviousVideo)
        self.mainlogic.miniplayerui.backtovideobutton.clicked.connect(self.BackToVideoPlayer)

        self.StartProgrem()

    ###### 영상 재생 함수

    def PlayPause(self):
         """Toggle play/pause status
         """
         if self.mediaplayer.is_playing():
             self.mediaplayer.pause()
             self.videoplayerui.pausebutton.hide()
             self.videoplayerui.playbutton.show()
             self.mainlogic.miniplayerui.pausebutton.hide()
             self.mainlogic.miniplayerui.playbutton.show()
         else:
             self.videoplayerui.playbutton.hide()
             self.videoplayerui.pausebutton.show()
             self.mainlogic.miniplayerui.pausebutton.show()
             self.mainlogic.miniplayerui.playbutton.hide()
             self.mediaplayer.play()
             self.isPaused = False

    def VideoStop(self):
        self.mediaplayer.stop()
        self.videoplayerui.pausebutton.hide()
        self.videoplayerui.playbutton.show()

    def setVolume(self, Volume):
        """Set the volume
        """
        self.mediaplayer.audio_set_volume(Volume)


    #### 재생목록별 영상 재생

    def MiniPlayer(self):
        self.titlelist=[]
        self.mainlogic.mainwindow.resize(self.mainlogic.miniplayerui.miniplayer_x,self.mainlogic.miniplayerui.miniplayer_y)
        self.mainlogic.mainwindow.move(800,400)
        self.mainlogic.mainwindow.show()
        self.mainlogic.paper.setCurrentIndex(2)
        self.videoplayerui.mainwindow.hide()
        for i in range(0,len(self.videodata.urltitle_forminiplayer)):
            title=self.videodata.urltitle_forminiplayer[i]
            title1=pafy.new(title)
            title2=title1.title
            self.titlelist.append(title2)
      
        self.mainlogic.miniplayerui.videotitle.setText(self.titlelist[self.count])
        


    def PlayVideo(self,event,myplaylist):
        
        self.myplaylist=myplaylist
  
        self.mainlogic.mainwindow.hide()
        self.videoplayerui.mainwindow.show()
        self.videodata=videodatabase.VideoData()
        self.videodata.StoreButtons()
        
        try:
            self.videodata.FindVideoUrl(self.myplaylist)

            for i in range(0,len(self.videodata.myurl)):
                
                self.thumb=self.videodata.urlbuttonlist[i]
                self.thumbnail=pafy.new(self.thumb)
                self.thumbnailimg=self.thumbnail.bigthumb
                self.videotitle=self.thumbnail.title
                
                image=QtGui.QImage()
              
                image.loadFromData(requests.get(self.thumbnailimg).content)
                image.scaled(225,140)
                
                self.videodata.urlbuttonlist[i]=QtWidgets.QLabel(self.videoplayerui.playerui)
                self.videodata.urlbuttonlist[i].setGeometry(1115,60+(180*i),280,140)
                self.videodata.urlbuttonlist[i].setStyleSheet('background:white;')
                self.videodata.urlbuttonlist[i].setPixmap(QtGui.QPixmap(image))
                self.videodata.urlbuttonlist[i].show()

                self.videodata.urltitle[i]=QtWidgets.QLabel(self.videoplayerui.playerui)
                self.videodata.urltitle[i].setGeometry(1115,60+(180*i)+150,270,22)
                self.videodata.urltitle[i].setStyleSheet('color:white;')
                self.videodata.urltitle[i].setText(self.videotitle)
                self.videodata.urltitle[i].show()
        
            url = self.videodata.myurl[self.count][0]                                                                                   
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                    
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play()
            
        except IndexError or TypeError:
            pass
            

    def NextVideo(self):
        try:
            self.count+=1 
            self.mediaplayer.stop()
            url = self.videodata.myurl[self.count][0]                                                                                   
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                        
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play() 
            
            self.mainlogic.miniplayerui.videotitle.setText(self.titlelist[self.count])
        except IndexError:
            self.count=0 
            url = self.videodata.myurl[self.count][0] 
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                        
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play() 
            self.mainlogic.miniplayerui.videotitle.setText(self.titlelist[self.count])
    

    def PreviousVideo(self):
    
        try:
            self.count-=1 
            self.mediaplayer.stop()
            url = self.videodata.myurl[self.count][0]                                                                                   
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                        
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play() 
            self.mainlogic.miniplayerui.videotitle.setText(self.titlelist[self.count])
        except IndexError:
            self.count=self.videodata.myurl.index(self.videodata.myurl[-1])
            url = self.videodata.myurl[self.count][0] 
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                        
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play() 
            self.mainlogic.miniplayerui.videotitle.setText(self.titlelist[self.count])

    def StartProgrem(self):
        self.videodata=videodatabase.VideoData()
        self.videodata.StoreButtons()

        for i in range(0,len(self.videodata.buttonlist2)):
            
            self.mainlogic.playlist.playlistlocate.buttonlist[i].mousePressEvent=lambda event, myplaylist=self.mainlogic.playlist.playlistlocate.buttonlabellist[i]:self.PlayVideo(event,myplaylist)
        for i in range(0,len(self.mainlogic.playlist.playlistlocate.buttonlist)):
            self.MyEvent(i)
        self.mainlogic.playlist.searchbutton.clicked.connect(self.SearchPage)

    #페이지 이동
    def SearchPage(self):
        self.mainlogic.mainwindow.resize(self.mainlogic.search.searchui_x,self.mainlogic.search.searchui_y)
        self.mainlogic.paper.setCurrentIndex(1)

    def BackToVideoList(self):
        self.mainlogic.mainwindow.resize(self.mainlogic.playlist.playlistui_x,self.mainlogic.playlist.playlistui_y)
        self.mainlogic.mainwindow.show()
        self.videoplayerui.mainwindow.hide()
        self.mediaplayer.stop()
        self.mainlogic.paper.setCurrentIndex(0)

    def BackToVideoPlayer(self):
        self.videoplayerui.mainwindow.show()
        self.mainlogic.mainwindow.hide()
    

   

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
        self.videodata=videodatabase.VideoData()
        self.i=i
        self.videodata.StoreButtons()
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].enterEvent=lambda event,i=self.i:self.FolderAnimation(event,i)
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].leaveEvent=lambda event,i=self.i:self.FolderLeaveAnimation(event,i)

    #재생목록 편집 함수


    def VideoListEditButton(self):
        self.videodata=videodatabase.VideoData()
        self.videodata.StoreButtons()
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
        self.videodata=videodatabase.VideoData()
        self.videodata.FindCount()
        self.mainlogic.check.mainwindow.show()
        self.mainlogic.check.lineedit.setText('재생목록'+str(self.videodata.result[0][0]))


    def Uihide(self):
        self.mainlogic.check.mainwindow.hide()

    def AddPlaylist(self,event,name2):
        self.videodata=videodatabase.VideoData()
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
        self.videodata=videodatabase.VideoData()
        
        self.videodata.FindCount()
        self.videodata.StoreButtons()
        
        self.videodata.buttonlist[self.videodata.result[0][0]]=QtWidgets.QPushButton(self.mainlogic.playlist.playlistui)
       
        self.videodata.buttonlabellist[self.videodata.result[0][0]]=QtWidgets.QLabel(self.mainlogic.playlist.playlistui)
        

        if 100+(300*self.videodata.result[0][0]<=700) :
            self.videodata.buttonlist[self.videodata.result[0][0]].setGeometry(100+(300*self.videodata.result[0][0]),350,200,200)
            self.videodata.buttonlist[self.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
    
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setGeometry(100+(300*self.videodata.result[0][0])+40,450,200,200)
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setStyleSheet('color:white;')

            self.videodata.buttonlist[self.videodata.result[0][0]].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[self.videodata.result[0][0]]:self.PlayVideo(event,myplaylist)

            self.videodata.buttonlist[self.videodata.result[0][0]].show()
            self.videodata.buttonlabellist[self.videodata.result[0][0]].show()

            if 100+(300*self.videodata.result[0][0])>1000:
                self.videodata.buttonlist[self.videodata.result[0][0]].setGeometry(100+(300*(self.videodata.result[0][0]-4)),350*2-100,200,200)
                self.videodata.buttonlist[self.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
                self.videodata.buttonlist[self.videodata.result[0][0]].show()

                self.videodata.buttonlabellist[self.videodata.result[0][0]].setGeometry(100+(300*(self.videodata.result[0][0]-4))+40,350*2,200,200)
                self.videodata.buttonlabellist[self.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
                self.videodata.buttonlabellist[self.videodata.result[0][0]].setStyleSheet('color:white;')

                self.videodata.buttonlist[self.videodata.result[0][0]].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[self.videodata.result[0][0]]:self.PlayVideo(event,myplaylist)

                self.videodata.buttonlist[self.videodata.result[0][0]].show()

    
      
        

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=Mainlogic()
    sys.exit(app.exec_())