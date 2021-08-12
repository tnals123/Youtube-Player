from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class VideoPlayer(object):
    def __init__(self):
        self.mainwindow=QtWidgets.QMainWindow()
        self.playerui_x=1400
        self.playerui_y=900
       
        self.setupUi()
        self.mainwindow.hide()
    def setupUi(self):
        self.mainwindow.resize(self.playerui_x,self.playerui_y)
        self.playerui=QtWidgets.QWidget(self.mainwindow)
        self.playerui.setGeometry(0,0,1400,900)
        self.background=QtWidgets.QLabel(self.playerui)
        self.background.setGeometry(0,0,1400,900)
        self.background.setStyleSheet('background:black;')

        self.backbutton=QtWidgets.QPushButton(self.playerui)
        self.backbutton.setGeometry(50,760,30,30)
        self.backbutton.setStyleSheet('background-image:url(previous.jpg);''border:1px solid black;')


        self.volumeslider=QtWidgets.QSlider(QtCore.Qt.Horizontal,self.playerui)
        self.volumeslider.setGeometry(350,760,80,30)
        self.volumeslider.setStyleSheet("QSlider::handle:horizontal {background-color: red;}")

        self.speaker=QtWidgets.QPushButton(self.playerui)
        self.speaker.setGeometry(300,760,30,30)
        self.speaker.setStyleSheet('background-image:url(speaker.png);''border:1px solid black;')

        self.pausebutton=QtWidgets.QPushButton(self.playerui)
        self.pausebutton.setGeometry(100,760,30,30)
        self.pausebutton.setStyleSheet('background-image:url(pause.jpg);''border:1px solid black;')

        self.playbutton=QtWidgets.QPushButton(self.playerui)
        self.playbutton.setGeometry(100,760,30,30)
        self.playbutton.setStyleSheet('background-image:url(play.jpg);''border:1px solid black;')
        self.playbutton.hide()

        self.nextbutton=QtWidgets.QPushButton(self.playerui)
        self.nextbutton.setGeometry(200,760,30,30)
        self.nextbutton.setStyleSheet('background-image:url(next.jpg);''border:1px solid black;')

        self.stopbutton=QtWidgets.QPushButton(self.playerui)
        self.stopbutton.setGeometry(150,760,30,30)
        self.stopbutton.setStyleSheet('background-image:url(stop.jpg);''border:1px solid black;')

        self.videolistlabel=QtWidgets.QLabel(self.playerui)
        self.videolistlabel.setGeometry(1100,50,250,600)
        self.videolistlabel.setStyleSheet('background:#1C1C1C;')

        self.videoframe = QtWidgets.QFrame(self.playerui)

        self.videoframe.setGeometry(QtCore.QRect(50, 50, 1000, 700))

        self.videoframe.setFrameShape(QtWidgets.QFrame.Box)

        self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)

        self.vboxlayout = QtWidgets.QVBoxLayout()

        self.vboxlayout.addWidget(self.videoframe)

        

        self.buttonlistlabel=QtWidgets.QLabel(self.playerui)
        self.buttonlistlabel.setGeometry(1100,680,250,200)
        self.buttonlistlabel.setStyleSheet('background:#1C1C1C;')
        
        self.previouspagebutton=QtWidgets.QPushButton(self.playerui)
        self.previouspagebutton.setGeometry(650,760,190,25)
        self.previouspagebutton.setStyleSheet('border-style:dashed;''border-width:2px;''border-color:red;''background:black;''color:white;')
        self.previouspagebutton.setText('재생목록으로 돌아가기')

        self.miniplayerbutton=QtWidgets.QPushButton(self.playerui)
        self.miniplayerbutton.setGeometry(860,760,190,25)
        self.miniplayerbutton.setStyleSheet('border-style:dashed;''border-width:2px;''border-color:red;''background:black;''color:white;')
        self.miniplayerbutton.setText('미니 플레이어 사용하기')

        

