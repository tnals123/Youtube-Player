
from urllib import request
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import sqlite3
import sys
import time
import vlc
import webbrowser
import random
import pafy
import ConnectUi
import videodatabase
import VideoplayerUi
import requests
import SearchVideoUi
from youtube_search import YoutubeSearch
import json
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
        self.searchvideoui=SearchVideoUi.SearchVideoUi()
        self.mainlogic.playlist.youtube.clicked.connect(self.OpenYouTube)
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
        self.videoplayerui.onesongbutton.clicked.connect(self.RepeatPlay)
        self.videoplayerui.orderbutton.clicked.connect(self.OrderedPlay)
        self.videoplayerui.randombutton.clicked.connect(self.ShufflePlay)
        self.mainlogic.playlist.applybutton.clicked.connect(self.ApplyButton)
        self.videoplayerui.positionslider.sliderMoved.connect(self.setPosition)
        self.videoplayerui.timer.timeout.connect(self.updateUI)
        self.videoplayerui.editbutton.clicked.connect(self.ShowDeleteButton)
        
        
        #미니플레이어 함수
        self.mainlogic.miniplayerui.pausebutton.clicked.connect(self.PlayPause)
        self.mainlogic.miniplayerui.playbutton.clicked.connect(self.PlayPause)
        self.mainlogic.miniplayerui.stopbutton.clicked.connect(self.VideoStop)
        self.mainlogic.miniplayerui.volumeslider.valueChanged.connect(self.setVolume)
        self.mainlogic.miniplayerui.nextbutton.clicked.connect(self.NextVideo2)
        self.mainlogic.miniplayerui.backbutton.clicked.connect(self.PreviousVideo2)
        self.mainlogic.miniplayerui.backtovideobutton.clicked.connect(self.BackToVideoPlayer)

        self.StartProgrem()

        #검색창 함수
        self.mainlogic.search.okbutton.clicked.connect(self.AddVideoToPlayList)
        self.mainlogic.search.backtoplaylist.clicked.connect(self.BackToPlaylist)


    def OpenYouTube(self):
        
        webbrowser.open("https://www.youtube.com/")     

   

    def Timeevent(self):
        if self.step >= 100:
            self.mytime.stop()
        self.step+=1
        self.videoplayerui.processbar.setValue(self.step)   

    def doAction(self):
        self.mytime=QtCore.QBasicTimer()
        self.step=0
        if self.step >= 100:
            self.mytime.stop()
        self.step+=1
        self.videoplayerui.processbar.setValue(self.step)   
        if self.mytime.isActive():
            self.mytime.stop()
        
        else:
            self.mytime.start(100, self.videoplayerui.playerui)
           
    ###### 재생목록에 영상 추가 함수

    def PlayListButtonChect(self,event,button):
        self.button=button
        self.button.setDisabled(True)
        

    # self.thumb=self.videodata.urlbuttonlist[i]
    #                 self.thumbnail=pafy.new(self.thumb)
    #                 self.thumbnailimg=self.thumbnail.bigthumb
    #                 self.videotitle=self.thumbnail.title
    #             except KeyError:
    #                 pass
                
    #             image=QtGui.QImage()
    #             #여기!
    #             image.loadFromData(requests.get(self.thumbnailimg).content)
    #             image.scaled(225,140)
    def AddVideoToPlayList(self):
        self.buttonlist=[]
        for i in range(0,len(self.mainlogic.search.videodata.buttonlist)):
            if not self.mainlogic.search.videodata.buttonlist[i].isEnabled():
                self.buttonlist.append(self.mainlogic.search.videodata.buttonlist[i].text())
         
        self.search=self.mainlogic.search.searchlineedit.text()
        
        results = YoutubeSearch(self.search, max_results=3).to_json()
        results_dict = json.loads(results)
        for v in results_dict['videos']:
            self.videothumb=[]
            videotitle=[]
            
            url='https://www.youtube.com' + v['url_suffix']
            self.videothumb.append(url)
            videotitle.append(url)
   
            
            
        for i in range(0,len(self.buttonlist)):
           
            self.videodata.AddVideoToPlayList(self.buttonlist[i],url)
            
    def asdf(self):
        for i in range(0,len(self.videothumb)):

            thumb=self.videothumb[i]
            thumbnail=pafy.new(thumb)
            thumbnailing=thumbnail.bigthumb

            image=QtGui.QImage()
            image.loadFromData(requests.get(thumbnailing).content)
            image.scaled(225,140)

            self.videothumb[i]=QtWidgets.QLabel(self.searchvideoui.paper)
            self.videothumb[i].setGeometry(0,300*i,200,200)
            self.videothumb[i].setPixmap(QtGui.QPixmap(image))

            self.videothumb[i].show()  
           
           

    ###### 영상 재생 함수

    def updateUI(self):
        self.videoplayerui.positionslider.setValue(self.mediaplayer.get_position() * 1000)
        if not self.mediaplayer.is_playing():
            self.videoplayerui.timer.stop()

    def setPosition(self,position):
        self.mediaplayer.set_position(position / 1000.0)

    def RepeatPlay(self):
        self.videothread=VideoThread_Repeat(self.mediaplayer)
        self.videoplayerui.onesongbutton.setDisabled(True)
        self.videoplayerui.orderbutton.setDisabled(False)
        self.videoplayerui.randombutton.setDisabled(False)
        
        
        try:
            self.videothread_ordered.videocount=0
            self.videothread_shuffled.videocount=0
          
        except AttributeError:
            pass
        self.videothread.start()
        
        
    def OrderedPlay(self):
        self.videothread_ordered=VideoThread_Ordered(self.mediaplayer,self.count,self.videodata.titlelist,self.instance)
        self.videoplayerui.onesongbutton.setDisabled(False)
        self.videoplayerui.orderbutton.setDisabled(True)
        self.videoplayerui.randombutton.setDisabled(False)

        
        try:
            self.videothread_shuffled.videocount=0
            self.videothread.videoend=0
            
        except AttributeError:
            pass
        self.videothread_ordered.start()
       
    def ShufflePlay(self):
        self.videothread_shuffled=VideoThread_Shuffled(self.mediaplayer,self.count,self.videodata.titlelist,self.instance)
        self.videoplayerui.onesongbutton.setDisabled(False)
        self.videoplayerui.orderbutton.setDisabled(False)
        self.videoplayerui.randombutton.setDisabled(True)

        
        try:
            self.videothread.videoend=0
            self.videothread_ordered.videocount=0
       
        except AttributeError:
            pass

        self.videothread_shuffled.start()
       
        

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
             self.videoplayerui.timer.start()
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
        self.mainlogic.mainwindow.setWindowTitle("Mini Player")
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



    def DeleteVideo(self,event,video,label,video2,button):
        
        self.video=video
        self.label=label
        self.videodata.DeleteVideo(self.myplaylist,self.video)
        video2.deleteLater()
        self.label.deleteLater()
        button.deleteLater()
        
    def Cancel(self):
        self.videoplayerui.editbutton.show()
        self.videoplayerui.cancelbutton.hide()
        for i in range(0,len(self.videodata.myurl)):
            self.videodata.deletebutton2[i].hide()

    def ShowDeleteButton(self):
        
        self.videoplayerui.editbutton.hide()
        self.videoplayerui.cancelbutton.show()
        self.videoplayerui.cancelbutton.clicked.connect(self.Cancel)
        for i in range(0,len(self.videodata.myurl)):
              
                self.videodata.deletebutton2[i]=QtWidgets.QPushButton(self.videoplayerui.videolistlabelarea)
                self.videodata.deletebutton2[i].setGeometry(265,25+(200*i),30,30)
                self.videodata.deletebutton2[i].setStyleSheet('border-radius:15px;''background:red;')
                self.videodata.deletebutton2[i].setText('X')
                self.videodata.deletebutton2[i].setFont(QtGui.QFont(None,15))
                self.videodata.deletebutton2[i].show()
                self.videodata.deletebutton2[i].mousePressEvent=lambda event,video=self.videodata.myurl[i][0],label=self.videodata.urltitle[i],video2=self.videodata.urlbuttonlist[i],button=self.videodata.deletebutton2[i]:self.DeleteVideo(event,video,label,video2,button)
                

    def PlayVideo(self,event,myplaylist):
        
        self.videoplayerui.mainwindow.setWindowTitle("Video Player")
        self.myplaylist=myplaylist
        
        
        try:
            self.videothread_ordered.videocount=0
            self.videothread_shuffled.videocount=0
            self.videothread.videoend=0
        except AttributeError:
            pass
            
        self.mainlogic.mainwindow.hide()
        self.videoplayerui.mainwindow.show()
        self.videodata=videodatabase.VideoData()
        self.videodata.StoreButtons()
        
        try:
            self.videodata.FindVideoUrl(self.myplaylist)

            for i in range(0,len(self.videodata.myurl)):
                try:
                    self.thumb=self.videodata.urlbuttonlist[i]
                    self.thumbnail=pafy.new(self.thumb)
                    self.thumbnailimg=self.thumbnail.bigthumb
                    self.videotitle=self.thumbnail.title
                except KeyError:
                    pass
                
                image=QtGui.QImage()
                #여기!
                image.loadFromData(requests.get(self.thumbnailimg).content)
                image.scaled(225,140)
                
                
                self.videodata.urlbuttonlist[i]=QtWidgets.QLabel(self.videoplayerui.videolistlabelarea)
                self.videodata.urlbuttonlist[i].setGeometry(0,40+(200*i),280,140)
                self.videodata.urlbuttonlist[i].setStyleSheet('background:white;')
                self.videodata.urlbuttonlist[i].setPixmap(QtGui.QPixmap(image))
                self.videodata.urlbuttonlist[i].mousePressEvent=lambda event,video=self.videotitle,playlist=self.myplaylist:self.SelectVideo(event,video,playlist)
                self.videodata.urlbuttonlist[i].show()
                

                self.videodata.urltitle[i]=QtWidgets.QLabel(self.videoplayerui.videolistlabelarea)
                self.videodata.urltitle[i].setGeometry(0,60+(200*i)+130,270,22)
                self.videodata.urltitle[i].setStyleSheet('color:white;')
                self.videodata.urltitle[i].setText(self.videotitle)
                self.videodata.urltitle[i].show()
                self.videodata.urltitle[i].mousePressEvent=lambda event,video=self.videotitle,playlist=self.myplaylist:self.SelectVideo(event,video,playlist)

                

            if len(self.videodata.myurl)<=3:
                self.videoplayerui.videolistlabelarea.setGeometry(1100,50,310,700)
            else:
                self.videoplayerui.videolistlabelarea.setGeometry(1100,50,310,800+(500*(len(self.videodata.myurl)-3)))
                
        
            url = self.videodata.myurl[self.count][0]                                                                                   
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                    
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play()
            
        except IndexError or TypeError:

            pass

    def SelectVideo(self,event,video,playlist):
        self.list=[]
        self.playlist=playlist
        self.video=video
        self.videodata.FindVideoUrl(self.myplaylist)
        for i in range(0,len(self.videodata.urltitle)):
            try:
                self.videotitle=pafy.new(self.videodata.urltitle[i])
                self.videotitle2=self.videotitle.title
                self.list.append(self.videotitle2)
            except KeyError:
                pass
        self.count=self.list.index(self.video)
      
        url = self.videodata.myurl[self.count][0]                                                                                   
        video = pafy.new(url)                                                                                                                       
        best = video.getbest()                                                                                                                 
        playurl = best.url                                                                                                                          
                                                                                        
        media = self.instance.media_new(playurl)
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()



    def NextVideo2(self):
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
    

    def PreviousVideo2(self):
    
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
            
            
        except IndexError:
            self.count=0 
            url = self.videodata.myurl[self.count][0] 
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                        
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play() 
            
    

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
            
        except IndexError:
            self.count=self.videodata.myurl.index(self.videodata.myurl[-1])
            url = self.videodata.myurl[self.count][0] 
            video = pafy.new(url)                                                                                                                       
            best = video.getbest()                                                                                                                 
            playurl = best.url                                                                                                                          
                                                                                        
            media = self.instance.media_new(playurl)
            self.mediaplayer.set_media(media)
            self.mediaplayer.play() 
            

    def StartProgrem(self):
     
        self.videodata=videodatabase.VideoData()
        self.videodata.StoreButtons()
        
        for i in range(0,len(self.videodata.buttonlist2)):
            
            self.mainlogic.playlist.playlistlocate.buttonlist[i].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[i]:self.PlayVideo(event,myplaylist)
        for i in range(0,len(self.mainlogic.playlist.playlistlocate.buttonlist)):
            self.MyEvent(i)
        self.mainlogic.playlist.searchbutton.clicked.connect(self.SearchPage)
    
    def AfterChange(self):
        for i in range(0,len(self.videodata.buttonlist2)):
            
            self.mainlogic.playlist.playlistlocate.buttonlist[i].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[i]:self.PlayVideo(event,myplaylist)


    #페이지 이동
    def SearchPage(self):
        self.mainlogic.mainwindow.setWindowTitle("Search Page")
        self.mainlogic.mainwindow.resize(self.mainlogic.search.searchui_x,self.mainlogic.search.searchui_y)
        self.mainlogic.mainwindow.move(600,200)
        self.mainlogic.search.ChoicePlaylist()
        for i in range(0,len(self.mainlogic.search.videodata.buttonlist)):
            self.mainlogic.search.videodata.buttonlist[i].mousePressEvent=lambda event,button=self.videodata.strbutton[i]:self.PlayListButtonChect(event,button)
        self.mainlogic.paper.setCurrentIndex(1)

    def BackToVideoList(self):
        
        try:
            for i in range(0,len(self.videodata.myurl)):
                self.videodata.urlbuttonlist[i].deleteLater()
                self.videodata.urltitle[i].deleteLater()
        except IndexError:
            pass
        self.mainlogic.mainwindow.setWindowTitle("Playlist")
        self.mainlogic.mainwindow.move(250,50)
        self.mainlogic.mainwindow.resize(self.mainlogic.playlist.playlistui_x,self.mainlogic.playlist.playlistui_y)
        self.mainlogic.mainwindow.show()
        self.videoplayerui.mainwindow.hide()
        
        self.mediaplayer.stop()
        self.count=0
        try:
            self.videothread.videoend=0
            self.videothread_shuffled.videocount=0
            self.videothread_ordered.videocount=0
        except AttributeError:
            pass
        
        self.mainlogic.paper.setCurrentIndex(0)

    def BackToVideoPlayer(self):
        self.videoplayerui.mainwindow.setWindowTitle("Playlist")
        self.videoplayerui.mainwindow.show()
        self.mainlogic.mainwindow.hide()

    def BackToPlaylist(self):
        
        self.videoplayerui.videolistlabelarea.show()
        self.mainlogic.mainwindow.setWindowTitle("Playlist")
        self.mainlogic.mainwindow.move(250,50)
        self.mainlogic.mainwindow.resize(self.mainlogic.playlist.playlistui_x,self.mainlogic.playlist.playlistui_y)
        self.mainlogic.paper.setCurrentIndex(0)
    
    def Uihide(self):
        self.mainlogic.check.mainwindow.hide()

    #애니메이션 처리
    def EnterAnimation(self,event):
        self.mainlogic.playlist.addpushbutton.setStyleSheet('background-image:url(plus2.png);''border:1px soild black;')
        
    def LeaveAnimation(self,event):
        self.mainlogic.playlist.addpushbutton.setStyleSheet('border:1px solid black;''background-image:url(plus.png);')
    
    def FolderAnimation(self,event,i):
        
        self.mainlogic.playlist.playlistlocate.buttonlist[i].setStyleSheet('background-image:url(folder2.png);''border:1px soild black;')
        
    def FolderLeaveAnimation(self,event,i):
  
        self.mainlogic.playlist.playlistlocate.buttonlist[i].setStyleSheet('background-image:url(folder.png);''border:1px soild black;')

    def FolderAnimation2(self,event,button):
        
        button.setStyleSheet('background-image:url(folder2.png);''border:1px soild black;')
        
    def FolderLeaveAnimation2(self,event,button):
        
        
        button.setStyleSheet('background-image:url(folder.png);''border:1px soild black;')
       

    def MyEvent(self,i):
        
        self.i=i
       
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].enterEvent=lambda event,i=self.i:self.FolderAnimation(event,i)
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].leaveEvent=lambda event,i=self.i:self.FolderLeaveAnimation(event,i)

    #재생목록 편집 함수


    def VideoListEditButton(self):
        
        self.changelist=[]

        print(self.mainlogic.playlist.playlistlocate.buttonlist)
        
        self.mainlogic.playlist.applybutton.show()
        self.mainlogic.playlist.cancelbutton.show()
        self.mainlogic.playlist.addpushbutton.setDisabled(True)

        for i in range(0,len(self.videodata.deletebutton)):
            
            self.videodata.deletebutton[i]=QtWidgets.QPushButton(self.mainlogic.playlist.playlistlist)
            if i<=4 :
                self.videodata.deletebutton[i].setGeometry(20+(300*i)+170,60,30,30)
                self.videodata.deletebutton[i].setStyleSheet('border-radius:15px;''background:red;')
                self.videodata.deletebutton[i].setText('X')
                self.videodata.deletebutton[i].setFont(QtGui.QFont(None,15))
                self.videodata.deletebutton[i].hide()
            if i>=4 and i<8:
                self.videodata.deletebutton[i].setGeometry(20+(300*(i-4))+170,360,30,30)
                self.videodata.deletebutton[i].setStyleSheet('border-radius:15px;''background:red;')
                self.videodata.deletebutton[i].setText('X')
                self.videodata.deletebutton[i].setFont(QtGui.QFont(None,15))
                self.videodata.deletebutton[i].hide()
            if i>=8:
                self.videodata.deletebutton[i].setGeometry(20+(300*(i-8))+170,690,30,30)
                self.videodata.deletebutton[i].setStyleSheet('border-radius:15px;''background:red;')
                self.videodata.deletebutton[i].setText('X')
                self.videodata.deletebutton[i].setFont(QtGui.QFont(None,15))
                self.videodata.deletebutton[i].hide()
            self.videodata.deletebutton[i].show()
       
        for i in range(0,len(self.videodata.deletebutton)):
            
            self.changebuttonname=QtWidgets.QLineEdit(self.mainlogic.playlist.playlistlist)
            self.changelist.append(self.changebuttonname)
            
            
            if i<4:
                self.changelist[i].setGeometry(20+(300*i)+40,240,150,25)
                self.changelist[i].setText(self.videodata.strbutton[i])
                self.changelist[i].setStyleSheet('color:black;''background:white;')
                self.changelist[i].show()  
            if i>=4:
                self.changelist[i].setGeometry(20+(300*(i-4)+40),500,150,25)
                self.changelist[i].setText(self.videodata.strbutton[i])
                self.changelist[i].setStyleSheet('color:black;''background:white;')
                self.changelist[i].show() 




          
            self.mainlogic.playlist.editbutton.hide()

    def ApplyButton(self):
        
        self.mainlogic.playlist.addpushbutton.setDisabled(False)
        self.mainlogic.playlist.applybutton.hide()
        self.mainlogic.playlist.cancelbutton.hide()
        self.mainlogic.playlist.editbutton.show()
        self.videodata.FindCount()
        print(self.videodata.deletebutton)
        for i in range(0,len(self.videodata.deletebutton)):
            
            try:
                self.videodata.ChangeTable(self.videodata.strbutton[i],self.changelist[i].text())
                self.videodata.ChangePlaylist(self.videodata.strbutton[i],self.changelist[i].text())
            except sqlite3.OperationalError:
                pass
           
            self.videodata.strbutton[i]=self.changelist[i].text()
            self.videodata.deletebutton[i].hide()
            self.changelist[i].hide()
            try:
                self.mainlogic.playlist.playlistlocate.mybuttonlabellist[i].setText(self.videodata.strbutton[i])
            except IndexError:
                self.videodata.buttonlabellist[i].setText(self.videodata.strbutton[i])
            self.mainlogic.playlist.playlistlocate.buttonlist[self.videodata.result[0][0]].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[self.videodata.result[0][0]]:self.PlayVideo(event,myplaylist)
        self.videodata.StoreButtons2()
        self.AfterChange()

        

    def CanCelEdit(self):
        self.mainlogic.playlist.addpushbutton.setDisabled(False)
        
        self.mainlogic.playlist.applybutton.hide()
        self.mainlogic.playlist.cancelbutton.hide()
        self.mainlogic.playlist.editbutton.show()
    
        for i in range(0,len(self.videodata.deletebutton)):
            self.videodata.deletebutton[i].hide()
            self.changelist[i].hide()
        

    #재생목록 추가 관련 함수

    def CheckAddPlaylist(self):
        self.videodata=videodatabase.VideoData()
        self.videodata.FindCount()
        self.mainlogic.check.mainwindow.show()
        self.mainlogic.check.lineedit.setText('재생목록'+str(self.videodata.result[0][0]))

    def AddPlaylist(self,event,name2):
        
        self.name2=name2
        self.videodata.CreatePlaylist(self.mainlogic.check.lineedit.text())
        
        self.MakePlaylist()
       
        
        self.videodata.UpdateCount()
        self.videodata.FindCount()
        self.videodata.buttonlist[self.videodata.result[0][0]-1].enterEvent=lambda event,button=self.videodata.buttonlist[self.videodata.result[0][0]-1]:self.FolderAnimation2(event,button)
        self.videodata.buttonlist[self.videodata.result[0][0]-1].leaveEvent=lambda event,button=self.videodata.buttonlist[self.videodata.result[0][0]-1]:self.FolderLeaveAnimation2(event,button)
        if 100+(300*self.videodata.result[0][0]<=700) :
            self.name2.setGeometry(20+(300*self.videodata.result[0][0]),20,200,200)
        if 100+(300*self.videodata.result[0][0])>1000 and 100+(300*self.videodata.result[0][0])<2500:
            self.name2.setGeometry(20+(300*(self.videodata.result[0][0]-4)),300,200,200)
        if (300*self.videodata.result[0][0])>=2400:
             self.name2.setGeometry(20+(300*(self.videodata.result[0][0]-8)),580,200,200)
        self.name2.show()
        self.mainlogic.check.mainwindow.hide()

    

    def MakePlaylist(self):
        self.videodata=videodatabase.VideoData()
        
        self.videodata.FindCount()
        self.videodata.StoreButtons()
       
        self.videodata.buttonlist[self.videodata.result[0][0]]=QtWidgets.QPushButton(self.mainlogic.playlist.playlistlist)
       
        self.videodata.buttonlabellist[self.videodata.result[0][0]]=QtWidgets.QLabel(self.mainlogic.playlist.playlistlist)

        

        if 100+(300*self.videodata.result[0][0]<=1000) :
            self.videodata.buttonlist[self.videodata.result[0][0]].setGeometry(20+(300*self.videodata.result[0][0]),20,200,200)
            self.videodata.buttonlist[self.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
    
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setGeometry(20+(300*self.videodata.result[0][0])+40,240,200,25)
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setStyleSheet('color:white;')

            self.videodata.buttonlist[self.videodata.result[0][0]].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[self.videodata.result[0][0]]:self.PlayVideo(event,myplaylist)
            
            self.videodata.buttonlist[self.videodata.result[0][0]].show()
            self.videodata.buttonlabellist[self.videodata.result[0][0]].show()

        if 100+(300*self.videodata.result[0][0])>1000 and  100+(300*self.videodata.result[0][0])< 2500:
            self.videodata.buttonlist[self.videodata.result[0][0]].setGeometry(20+(300*(self.videodata.result[0][0]-4)),300,200,200)
            self.videodata.buttonlist[self.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
            self.videodata.buttonlist[self.videodata.result[0][0]].show()

            self.videodata.buttonlabellist[self.videodata.result[0][0]].setGeometry(20+(300*(self.videodata.result[0][0]-4))+40,500,200,25)
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setStyleSheet('color:white;')
            self.videodata.buttonlist[self.videodata.result[0][0]].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[self.videodata.result[0][0]]:self.PlayVideo(event,myplaylist)
        
            self.videodata.buttonlist[self.videodata.result[0][0]].show()

        if 100+(300*self.videodata.result[0][0])>=2500:   
            self.videodata.buttonlist[self.videodata.result[0][0]].setGeometry(20+(300*(self.videodata.result[0][0]-8)),580,200,200)
            self.videodata.buttonlist[self.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
            self.videodata.buttonlist[self.videodata.result[0][0]].show()

            self.videodata.buttonlabellist[self.videodata.result[0][0]].setGeometry(20+(300*(self.videodata.result[0][0]-4))+40,760,200,25)
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
            self.videodata.buttonlabellist[self.videodata.result[0][0]].setStyleSheet('color:white;')

            self.videodata.buttonlist[self.videodata.result[0][0]].mousePressEvent=lambda event, myplaylist=self.videodata.strbutton[self.videodata.result[0][0]]:self.PlayVideo(event,myplaylist)

            self.videodata.buttonlist[self.videodata.result[0][0]].show()     
            self.videodata.buttonlabellist[self.videodata.result[0][0]].show()         

class VideoThread_Repeat(threading.Thread):
    def __init__(self,video):
        threading.Thread.__init__(self)
        self.videoend=1
        self.video=video

    def run(self):
        
        while True:
            current_state = str(self.video.get_state())
            time.sleep(1)
           
            if current_state == 'State.Ended':
                self.video.stop()
                self.video.play()
                
            if self.videoend==0:
                break

class VideoThread_Ordered(threading.Thread):

    def __init__(self,mediaplayer,count,urllist,instance):
        threading.Thread.__init__(self)
        self.mediaplayer=mediaplayer
        self.count=count
        self.urllist=urllist
        self.instance=instance
        self.videocount=1
    def run(self):
        while True:
            
            current_state = str(self.mediaplayer.get_state())
            time.sleep(1)
          
                
            if current_state == 'State.Ended':
             
               
                self.count+=1
                try:
                    self.mediaplayer.stop()
                    url=self.urllist[self.count]
                    try:
                        video=pafy.new(url)
                    except KeyError:
                        pass
                    best=video.getbest()
                    playurl=best.url
                    media=self.instance.media_new(playurl)
                    self.mediaplayer.set_media(media)
                    self.mediaplayer.play()
                except IndexError:
                    self.count=0
                    self.mediaplayer.stop()
                    url=self.urllist[self.count]
                    try:
                        video=pafy.new(url)
                    except KeyError:
                        pass
                    best=video.getbest()
                    playurl=best.url
                    media=self.instance.media_new(playurl)
                    self.mediaplayer.set_media(media)
                    self.mediaplayer.play()

            if self.videocount==0:
                break



class VideoThread_Shuffled(threading.Thread):
    def __init__(self,mediaplayer,count,urllist,instance):
        threading.Thread.__init__(self)
        self.mediaplayer=mediaplayer
        self.count=count
        self.urllist=urllist
        self.instance=instance
        self.videocount=1

    def run(self):
        while True:
            current_state = str(self.mediaplayer.get_state())
            time.sleep(1)
          
                
            if current_state == 'State.Ended':
             
               
                self.count=random.randint(0,len(self.urllist))
                try:
                    self.mediaplayer.stop()
                    url=self.urllist[self.count]
                    try:
                        video=pafy.new(url)
                    except KeyError:
                        pass
                    best=video.getbest()
                    playurl=best.url
                    media=self.instance.media_new(playurl)
                    self.mediaplayer.set_media(media)
                    self.mediaplayer.play()
                except IndexError:
                    self.count=0
                    self.mediaplayer.stop()
                    url=self.urllist[self.count]
                    try:
                        video=pafy.new(url)
                    except KeyError:
                        pass
                    best=video.getbest()
                    playurl=best.url
                    media=self.instance.media_new(playurl)
                    self.mediaplayer.set_media(media)
                    self.mediaplayer.play()

            if self.videocount==0:
                break




    

           
            
        


    

            


    
      
        

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=Mainlogic()
    sys.exit(app.exec_())