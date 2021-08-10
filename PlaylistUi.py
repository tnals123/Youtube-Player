from PyQt5 import QtCore, QtGui, QtWidgets
import videodatabase
from PyQt5.QtGui import QIcon, QPixmap

class Playlist:
    def __init__(self):

        self.playlistlocate=videodatabase.VideoData()
        self.playlistlocate.FindCount()
        self.playlistui_x=1300
        self.playlistui_y=900
        self.setupUi()
        
    def setupUi(self):

        

        self.playlistui=QtWidgets.QWidget()
        
        self.background=QtWidgets.QLabel(self.playlistui)
        self.background.setGeometry(0,0,1300,900)
        self.background.setStyleSheet('background: #1C1C1C;')

        self.background2=QtWidgets.QGroupBox(self.playlistui)
        self.background2.setGeometry(50,300,1200,550)
        self.background2.setStyleSheet('background:#000000;''border-color:white;''border-style:dashed;''border-width:3px;')

        self.editbutton=QtWidgets.QPushButton(self.playlistui)
        self.editbutton.setGeometry(1130,260,120,30)
        self.editbutton.setStyleSheet('background: #1C1C1C;''color:white;''border-style:dashed;''border-width:2px;''border-color:red;')
        self.editbutton.setText('재생목록 편집')

        self.searchbutton=QtWidgets.QPushButton(self.playlistui)
        self.searchbutton.setGeometry(100,100,1100,50)
        self.searchbutton.setStyleSheet('text-align:left;''background:white;')
        self.searchbutton.setIcon(QIcon('search.png'))
        self.searchbutton.setIconSize(QtCore.QSize(46,46))
        self.searchbutton.setText('이곳을 눌러 영상을 추가하세요!')

        self.applybutton=QtWidgets.QPushButton(self.playlistui)
        self.applybutton.setGeometry(1000,260,120,30)
        self.applybutton.setStyleSheet('background: #1C1C1C;''color:white;''border-style:dashed;''border-width:2px;''border-color:red;')
        self.applybutton.setText('적용하기')
        self.applybutton.hide()
        
        self.cancelbutton=QtWidgets.QPushButton(self.playlistui)
        self.cancelbutton.setGeometry(870,260,120,30)
        self.cancelbutton.setStyleSheet('background: #1C1C1C;''color:white;''border-style:dashed;''border-width:2px;''border-color:red;')
        self.cancelbutton.setText('취소하기')
        self.cancelbutton.hide()
        

        self.addpushbutton=QtWidgets.QPushButton(self.playlistui)
        if 100+(300*self.playlistlocate.result[0][0]<=700) :
            self.addpushbutton.setGeometry(100+(300*self.playlistlocate.result[0][0]),350,200,200)
            if 100+(300*self.playlistlocate.result[0][0])>1000:
                self.addpushbutton.setGeometry(100+(300*(self.playlistlocate.result[0][0]-4)),350*2-100,200,200)
        self.addpushbutton.setStyleSheet('background: black;''border:1px solid black;''background-image:url(plus.png);')

        self.playlistlocate.StoreButtons()
        for i in range(0,len(self.playlistlocate.buttonlist2)):

           
            self.playlistlocate.buttonlist[i]=QtWidgets.QPushButton(self.playlistui)
            self.myplaylistname=QtWidgets.QLabel(self.playlistui)
            

            if i<=4 :
                self.playlistlocate.buttonlist[i].setGeometry(100+(300*i),350,200,200)
                self.playlistlocate.buttonlist[i].setStyleSheet('background:black;''background-image:url(folder.png);')
                
                self.myplaylistname.setGeometry(100+(300*i)+40,450,200,200)
                self.myplaylistname.setText(self.playlistlocate.buttonlabellist[i])
                self.myplaylistname.setStyleSheet('color:white;')

            if i>=4:
                self.playlistlocate.buttonlist[i].setGeometry(100+(300*(i-4)),350*2-100,200,200)
                self.playlistlocate.buttonlist[i].setStyleSheet('background:black;''background-image:url(folder.png);')
                    
                self.myplaylistname.setGeometry(100+(300*(i-4))+40,350*2,200,200)
                self.myplaylistname.setText(self.playlistlocate.buttonlabellist[i])
                self.myplaylistname.setStyleSheet('color:white;')
        
        for i in range(0,len(self.playlistlocate.buttonlist2)):
             self.playlistlocate.deletebutton[i]=QtWidgets.QPushButton(self.playlistui)
             if i<=4 :
                 self.playlistlocate.deletebutton[i].setGeometry(100+(300*i+170),400,30,30)
                 self.playlistlocate.deletebutton[i].setStyleSheet('border-radius:15px;''background:red;')
                 self.playlistlocate.deletebutton[i].hide()
             if i>=4 :
                 self.playlistlocate.deletebutton[i].setGeometry(100+(300*(i-4)+170),700,30,30)
                 self.playlistlocate.deletebutton[i].setStyleSheet('border-radius:15px;''background:red;')
                 self.playlistlocate.deletebutton[i].hide()
      
       