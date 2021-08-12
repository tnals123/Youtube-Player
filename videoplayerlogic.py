import VideoplayerUi
import vlc
import pafy
import sys
import videodatabase
from PyQt5 import QtCore, QtGui, QtWidgets
class VideoPlayerLogic:
    def __init__(self):
        self.videoplayerui=VideoplayerUi.VideoPlayer()
        self.instance = vlc.Instance()
        
        self.mediaplayer = self.instance.media_player_new()
        if sys.platform.startswith("linux"):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoplayerui.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.videoplayerui.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.videoplayerui.videoframe.winId())
        

        
    def asdf(self):
        self.videodata=videodatabase.VideoData()
        self.videoplayerui.mainwindow.show()
        url = "https://www.youtube.com/watch?v=h4iGKoTZ4iM"                                                                                         
        video = pafy.new(url)                                                                                                                       
        best = video.getbest()                                                                                                                 
        playurl = best.url                                                                                                                          
                                                                                                
        media = self.instance.media_new(playurl)
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()
        print('asdf')
        

  
# import pafy                                                                                                                                 
# import vlc                                                                                                                                  
# #                                                                                                                                           
# #                                                                                                                                           
# url = "https://www.youtube.com/watch?v=G0OqIkgZqlA"                                                                                         
# video = pafy.new(url)                                                                                                                       
# best = video.getbestaudio()                                                                                                                 
# playurl = best.url                                                                                                                          
# player = vlc.MediaPlayer(playurl)                                                                                                           
# player.play()