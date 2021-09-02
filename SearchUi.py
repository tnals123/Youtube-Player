from PyQt5 import QtCore, QtGui, QtWidgets
import videodatabase


class SearchUi:
    def __init__(self):
        
        self.searchui_x=600
        self.searchui_y=600
        self.setupUi()
    def setupUi(self):
        self.searchui=QtWidgets.QWidget()

        self.background=QtWidgets.QLabel(self.searchui)
        self.background.setGeometry(0,0,600,600)
        self.background.setStyleSheet('background:black;')

        self.searchlineedit=QtWidgets.QLineEdit(self.searchui)
        self.searchlineedit.setGeometry(50,50,500,25)
        self.searchlineedit.setStyleSheet('background:white;')

        self.backtoplaylist=QtWidgets.QPushButton(self.searchui)
        self.backtoplaylist.setGeometry(400,100,200,25)
        self.backtoplaylist.setStyleSheet('background:black;''border-color:red;''border-style:dashed;''border-width:2px;''color:white;')
        self.backtoplaylist.setText('재생목록으로 돌아가기')

        self.okbutton=QtWidgets.QPushButton(self.searchui)
        self.okbutton.setGeometry(260,550,50,25)
        self.okbutton.setStyleSheet('background:black;''border-color:red;''border-style:dashed;''border-width:2px;''color:white;')
        self.okbutton.setText('확인')

    def ChoicePlaylist(self):
        self.videodata=videodatabase.VideoData()
        self.videodata.StoreButtons()
        self.videodata.StoreButtons2()
        for i in range(0,len(self.videodata.buttonlist)):
            if i<=8:
                self.videodata.buttonlist[i]=QtWidgets.QPushButton(self.searchui)
                self.videodata.buttonlist[i].setGeometry(50,200+i*50,80,25)
                self.videodata.buttonlist[i].setText(self.videodata.strbutton[i])
                self.videodata.buttonlist[i].show()
            elif i>8 and i<=16:
                self.videodata.buttonlist[i]=QtWidgets.QPushButton(self.searchui)
                self.videodata.buttonlist[i].setGeometry(200,200+i*50,80,25)
                self.videodata.buttonlist[i].setText(self.videodata.strbutton[i])
                self.videodata.buttonlist[i].show()