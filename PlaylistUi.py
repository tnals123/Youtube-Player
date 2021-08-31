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

        self.scrollarea=QtWidgets.QScrollArea(self.playlistui)
        self.scrollarea.setGeometry(50,300,1200,550)

        self.playlistlist=QtWidgets.QWidget(self.playlistui)
        self.playlistlist.setStyleSheet('background:black;')
        
        
        self.scrollarea.setWidget(self.playlistlist)
        
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

        self.youtube=QtWidgets.QPushButton(self.playlistui)
        self.youtube.setGeometry(100,40,150,60)
        self.youtube.setStyleSheet('background-image:url(youtube.jpg);''border:1px solid #1c1c1c;')
        
        self.addpushbutton=QtWidgets.QPushButton(self.playlistlist)
        if 100+(300*self.playlistlocate.result[0][0]<=700) :
           
            self.addpushbutton.setGeometry(20+(300*self.playlistlocate.result[0][0]),20,200,200)
        if 100+(300*self.playlistlocate.result[0][0])>1000 and 100+(300*self.playlistlocate.result[0][0])<2500:
           
            self.addpushbutton.setGeometry(20+(300*(self.playlistlocate.result[0][0]-4)),200*2-100,200,200)
        if 100+(300*self.playlistlocate.result[0][0])>=2500:    
            print(100+(300*self.playlistlocate.result[0][0]))
            self.addpushbutton.setGeometry(20+(300*(self.playlistlocate.result[0][0]-8)),580,200,200)

        self.addpushbutton.setStyleSheet('background: black;''border:1px solid black;''background-image:url(plus.png);')

        self.playlistlocate.StoreButtons()
        if len(self.playlistlocate.buttonlist2)<=7:
            self.playlistlist.setGeometry(50,300,1170,670)

        elif len(self.playlistlocate.buttonlist2)>=8:
            self.playlistlist.setGeometry(50,300,1170,len(self.playlistlocate.buttonlist2)*100)
            

        for i in range(0,len(self.playlistlocate.buttonlist2)):
            
            self.playlistlocate.buttonlist[i]=QtWidgets.QPushButton(self.playlistlist)
            self.playlistlocate.mybuttonlabellist[i]=QtWidgets.QLabel(self.playlistlist)            

            if i<=4 :
                self.playlistlocate.buttonlist[i].setGeometry(20+(300*i),20,200,200)
                self.playlistlocate.buttonlist[i].setStyleSheet('background:black;''background-image:url(folder.png);')
                
                self.playlistlocate.mybuttonlabellist[i].setGeometry(20+(300*i)+40,240,200,25)
                self.playlistlocate.mybuttonlabellist[i].setText(self.playlistlocate.buttonlabellist[i])
                self.playlistlocate.mybuttonlabellist[i].setStyleSheet('color:white;')
               

            if i>=4 and i<8:
                
                self.playlistlocate.buttonlist[i].setGeometry(20+(300*(i-4)),200*2-100,200,200)
                self.playlistlocate.buttonlist[i].setStyleSheet('background:black;''background-image:url(folder.png);')
                    
                self.playlistlocate.mybuttonlabellist[i].setGeometry(20+(300*(i-4))+40,250*2,200,25)
                self.playlistlocate.mybuttonlabellist[i].setText(self.playlistlocate.buttonlabellist[i])
                self.playlistlocate.mybuttonlabellist[i].setStyleSheet('color:white;')

            if i>=8:
                
                self.playlistlocate.buttonlist[i].setGeometry(20+(300*(i-8)),580,200,200)
                self.playlistlocate.buttonlist[i].setStyleSheet('background:black;''background-image:url(folder.png);')
                    
                self.playlistlocate.mybuttonlabellist[i].setGeometry(20+(300*(i-8))+40,760,200,25)
                self.playlistlocate.mybuttonlabellist[i].setText(self.playlistlocate.buttonlabellist[i])
                self.playlistlocate.mybuttonlabellist[i].setStyleSheet('color:white;')
                
                
            
                
                
                   


  
        
      
       