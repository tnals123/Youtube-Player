from PyQt5 import QtCore, QtGui, QtWidgets


class MiniplayerUi:
    def __init__(self):
        self.miniplayer_x=500
        self.miniplayer_y=150
        self.setupUi()
    def setupUi(self):
        self.miniplayer=QtWidgets.QWidget()

        self.background=QtWidgets.QLabel(self.miniplayer)
        self.background.setGeometry(0,0,500,150)
        self.background.setStyleSheet('background:black;')

        self.videotitle=QtWidgets.QLabel(self.miniplayer)
        self.videotitle.setGeometry(50,10,400,25)
        self.videotitle.setStyleSheet('background:black;''color:white;')
        self.videotitle.setText('asdfasdasdasdf')

        self.backbutton=QtWidgets.QPushButton(self.miniplayer)
        self.backbutton.setGeometry(50,50,30,30)
        self.backbutton.setShortcut('Left')
        self.backbutton.setStyleSheet('background-image:url(previous.jpg);''border:1px solid black;')


        self.volumeslider=QtWidgets.QSlider(QtCore.Qt.Horizontal,self.miniplayer)
        self.volumeslider.setGeometry(350,50,80,30)
        self.volumeslider.setStyleSheet("QSlider::handle:horizontal {background-color: red;}")

        self.speaker=QtWidgets.QPushButton(self.miniplayer)
        self.speaker.setGeometry(300,50,30,30)
        self.speaker.setStyleSheet('background-image:url(speaker.png);''border:1px solid black;')

        self.pausebutton=QtWidgets.QPushButton(self.miniplayer)
        self.pausebutton.setGeometry(100,50,30,30)
        self.pausebutton.setShortcut('space')
        self.pausebutton.setStyleSheet('background-image:url(pause.jpg);''border:1px solid black;')

        self.playbutton=QtWidgets.QPushButton(self.miniplayer)
        self.playbutton.setGeometry(100,50,30,30)
        self.playbutton.setShortcut('space')
        self.playbutton.setStyleSheet('background-image:url(play.jpg);''border:1px solid black;')
        self.playbutton.hide()

        self.nextbutton=QtWidgets.QPushButton(self.miniplayer)
        self.nextbutton.setGeometry(200,50,30,30)
        self.nextbutton.setShortcut('Right')
        self.nextbutton.setStyleSheet('background-image:url(next.jpg);''border:1px solid black;')

        self.stopbutton=QtWidgets.QPushButton(self.miniplayer)
        self.stopbutton.setGeometry(150,50,30,30)
        self.stopbutton.setStyleSheet('background-image:url(stop.jpg);''border:1px solid black;')

        self.backtovideobutton=QtWidgets.QPushButton(self.miniplayer)
        self.backtovideobutton.setGeometry(400,100,80,25)
        self.backtovideobutton.setStyleSheet('background:black;''border-color:red;''border-width:2px;''border-style:dashed;''color:white;')
        self.backtovideobutton.setText('돌아가기')