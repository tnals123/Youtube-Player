from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import videodatabase
class VideoPlayer(object):
    def __init__(self):
        self.mainwindow=QtWidgets.QMainWindow()
        self.playerui_x=1450
        self.playerui_y=900
        
        self.setupUi()
        self.mainwindow.hide()
    def setupUi(self):
        self.mainwindow.resize(self.playerui_x,self.playerui_y)
        self.playerui=QtWidgets.QWidget(self.mainwindow)
        self.playerui.setGeometry(0,0,1500,900)
        

        self.background=QtWidgets.QLabel(self.playerui)
        self.background.setGeometry(0,0,1500,900)
        self.background.setStyleSheet('background:black;')

        

        self.backbutton=QtWidgets.QPushButton(self.playerui)
        self.backbutton.setGeometry(50,760,30,30)
        self.backbutton.setShortcut('Left')
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
        self.pausebutton.setShortcut('space')

        self.playbutton=QtWidgets.QPushButton(self.playerui)
        self.playbutton.setGeometry(100,760,30,30)
        self.playbutton.setStyleSheet('background-image:url(play.jpg);''border:1px solid black;')
        self.playbutton.setShortcut('space')
        self.playbutton.hide()

        self.nextbutton=QtWidgets.QPushButton(self.playerui)
        self.nextbutton.setGeometry(200,760,30,30)
        self.nextbutton.setShortcut('Right')
        self.nextbutton.setStyleSheet('background-image:url(next.jpg);''border:1px solid black;')

        self.stopbutton=QtWidgets.QPushButton(self.playerui)
        self.stopbutton.setGeometry(150,760,30,30)
        self.stopbutton.setStyleSheet('background-image:url(stop.jpg);''border:1px solid black;')

        self.videolistlabel=QtWidgets.QScrollArea(self.playerui)
        self.videolistlabel.setGeometry(1100,50,320,600)
        self.videolistlabel.horizontalScrollBar().setStyleSheet('height:0px;')
        
        self.videolistlabelarea=QtWidgets.QWidget(self.playerui)
        self.videolistlabelarea.setStyleSheet('background:black;')

        self.videolistlabel.setWidget(self.videolistlabelarea)

        self.videoframe = QtWidgets.QFrame(self.playerui)
        self.videoframe.setGeometry(QtCore.QRect(50, 50, 1000, 700))
        self.videoframe.setFrameShape(QtWidgets.QFrame.Box)
        self.videoframe.setFrameShadow(QtWidgets.QFrame.Raised)

        self.buttonlistlabel=QtWidgets.QLabel(self.playerui)
        self.buttonlistlabel.setGeometry(1100,680,310,200)
        self.buttonlistlabel.setStyleSheet('background:#1C1C1C;')

        self.editbutton=QtWidgets.QPushButton(self.playerui)
        self.editbutton.setGeometry(1180,700,150,25)
        self.editbutton.setText('????????????')

        self.cancelbutton=QtWidgets.QPushButton(self.playerui)
        self.cancelbutton.setGeometry(1180,700,150,25)
        self.cancelbutton.setText('????????????')
        self.cancelbutton.hide()

        self.onesongbutton=QtWidgets.QPushButton(self.playerui)
        self.onesongbutton.setGeometry(1180,740,150,25)
        self.onesongbutton.setText('?????? ??????')

        self.orderbutton=QtWidgets.QPushButton(self.playerui)
        self.orderbutton.setGeometry(1180,780,150,25)
        self.orderbutton.setText('?????? ??????')

        self.randombutton=QtWidgets.QPushButton(self.playerui)
        self.randombutton.setGeometry(1180,820,150,25)
        self.randombutton.setText('?????? ??????')
        
        
        self.previouspagebutton=QtWidgets.QPushButton(self.playerui)
        self.previouspagebutton.setGeometry(650,760,190,25)
        self.previouspagebutton.setStyleSheet('border-style:dashed;''border-width:2px;''border-color:red;''background:black;''color:white;')
        self.previouspagebutton.setText('?????????????????? ????????????')

        self.miniplayerbutton=QtWidgets.QPushButton(self.playerui)
        self.miniplayerbutton.setGeometry(860,760,190,25)
        self.miniplayerbutton.setStyleSheet('border-style:dashed;''border-width:2px;''border-color:red;''background:black;''color:white;')
        self.miniplayerbutton.setText('?????? ???????????? ????????????')

        self.positionslider = QtWidgets.QSlider(QtCore.Qt.Horizontal,self.playerui)
        self.positionslider.setMaximum(1000)
        self.positionslider.setGeometry(50,700,1000,30)

        self.timer = QtCore.QTimer(self.playerui)
        self.timer.setInterval(200)
        
        
       



        
        


        

