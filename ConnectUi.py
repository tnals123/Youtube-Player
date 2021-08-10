
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

import VideoplayerUi
import PlaylistUi
import SearchUi
import MiniplayerUi

import CheckAddUi

class Connect(object):
    def __init__(self):
        self.mainwindow=QtWidgets.QMainWindow()

        self.check=CheckAddUi.CheckAddPlaylist()
        self.playlist=PlaylistUi.Playlist()
        self.videoplayerui=VideoplayerUi.Player()
        self.search=SearchUi.SearchUi()
        self.miniplayerui=MiniplayerUi.MiniplayerUi()
       

        self.setupUi()
        self.page()
        


    def show(self):
        self.mainwindow.show()

    def setupUi(self):
        self.mainwindow.resize(1300,900)
        self.paper=QtWidgets.QStackedWidget(self.mainwindow)
        self.paper.setGeometry(0,0,1500,900)

    def page(self):
        self.paper.addWidget(self.playlist.playlistui) #0
        self.paper.addWidget(self.videoplayerui.playerui) #1
        self.paper.addWidget(self.search.searchui) #2
        self.paper.addWidget(self.miniplayerui.miniplayer) #3
   

        self.paper.setCurrentIndex(0)


