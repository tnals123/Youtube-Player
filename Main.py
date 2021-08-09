
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import ConnectUi
import CheckAddUi
import Addplaylistlogic

class Mainlogic:
    def __init__(self):
        
        self.mainlogic=ConnectUi.Connect()
    
        
        self.mainlogic.show()
        self.mainlogic.playlist.addpushbutton.clicked.connect(self.CheckAddPlaylist)
        self.mainlogic.check.cancelbutton.clicked.connect(self.Uihide)
        self.mainlogic.check.addpushbutton.mousePressEvent=lambda event,name2=self.mainlogic.playlist.addpushbutton:self.AddPlaylist(event,name2)
        self.mainlogic.playlist.addpushbutton.enterEvent=lambda event:self.EnterAnimation(event)
        self.mainlogic.playlist.addpushbutton.leaveEvent=lambda event:self.LeaveAnimation(event)
        self.mainlogic.playlist.editbutton.clicked.connect(self.EditButton)

        for i in range(0,len(self.mainlogic.playlist.playlistlocate.buttonlist)):
            self.MyEvent(i)
        self.mainlogic.playlist.searchbutton.clicked.connect(self.SearchPage)
    
    #페이지 이동
    def SearchPage(self):
        self.mainlogic.mainwindow.resize(self.mainlogic.search.searchui_x,self.mainlogic.search.searchui_y)
        self.mainlogic.paper.setCurrentIndex(2)


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
        self.i=i
        self.mainlogic.videodata.StoreButtons()
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].enterEvent=lambda event,i=self.i:self.FolderAnimation(event,i)
        self.mainlogic.playlist.playlistlocate.buttonlist[self.i].leaveEvent=lambda event,i=self.i:self.FolderLeaveAnimation(event,i)

    #재생목록 편집 함수

    def CreateDeleteButton(self):
        self.deletelist=[]
        self.mainlogic.videodata.deletebutton[self.mainlogic.videodata.result[0][0]]=QtWidgets.QPushButton(self.mainlogic.playlist.playlistui)
        if 100+(300*self.mainlogic.videodata.result[0][0]<=700) :
            self.mainlogic.videodata.deletebutton[self.mainlogic.videodata.result[0][0]].setGeometry(100+(300*self.mainlogic.videodata.result[0][0]+180),200,30,30)
            self.mainlogic.videodata.deletebutton[self.mainlogic.videodata.result[0][0]].setStyleSheet('border-radius:15px;''background:red;')
            self.mainlogic.videodata.deletebutton[self.mainlogic.videodata.result[0][0]].hide()
            self.deletelist.append(self.mainlogic.videodata.deletebutton[self.mainlogic.videodata.result[0][0]])
            return self.mainlogic.videodata.deletebutton[self.mainlogic.videodata.result[0][0]]

    def EditButton(self):
        for i in range(0,len(self.mainlogic.videodata.deletebutton)):
            print(self.mainlogic.videodata.deletebutton[i])



    #재생목록 추가 관련 함수

    def CheckAddPlaylist(self):
        self.mainlogic.videodata.FindCount()
        self.mainlogic.check.mainwindow.show()
        self.mainlogic.check.lineedit.setText('재생목록'+str(self.mainlogic.videodata.result[0][0]))


    def Uihide(self):
        self.mainlogic.check.mainwindow.hide()

    def AddPlaylist(self,event,name2):
        self.name2=name2
        self.mainlogic.videodata.CreatePlaylist(self.mainlogic.check.lineedit.text())
        self.mainlogic.videodata.CreateDeleteButton(self.mainlogic.check.lineedit.text())
        self.mainlogic.videodata.StoreButtons()
        self.MakePlaylist()
        self.CreateDeleteButton()
        self.mainlogic.videodata.UpdateCount()
        self.mainlogic.videodata.FindCount()
        if 100+(300*self.mainlogic.videodata.result[0][0]<=700) :
            self.name2.setGeometry(100+(300*self.mainlogic.videodata.result[0][0]),350,200,200)
            if 100+(300*self.mainlogic.videodata.result[0][0])>1000:
                self.name2.setGeometry(100+(300*(self.mainlogic.videodata.result[0][0]-4)),350*2-100,200,200)
        self.mainlogic.check.mainwindow.hide()

    

    def MakePlaylist(self):
        self.mainlogic.videodata.FindCount()
        
        self.mainlogic.videodata.buttonlist[self.mainlogic.videodata.result[0][0]]=QtWidgets.QPushButton(self.mainlogic.playlist.playlistui)
  
        self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]]=QtWidgets.QLabel(self.mainlogic.playlist.playlistui)
        

        if 100+(300*self.mainlogic.videodata.result[0][0]<=700) :
            self.mainlogic.videodata.buttonlist[self.mainlogic.videodata.result[0][0]].setGeometry(100+(300*self.mainlogic.videodata.result[0][0]),350,200,200)
            self.mainlogic.videodata.buttonlist[self.mainlogic.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
    
            self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].setGeometry(100+(300*self.mainlogic.videodata.result[0][0])+40,450,200,200)
            self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
            self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].setStyleSheet('color:white;')

            self.mainlogic.videodata.buttonlist[self.mainlogic.videodata.result[0][0]].show()
            self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].show()

            if 100+(300*self.mainlogic.videodata.result[0][0])>1000:
                self.mainlogic.videodata.buttonlist[self.mainlogic.videodata.result[0][0]].setGeometry(100+(300*(self.mainlogic.videodata.result[0][0]-4)),350*2-100,200,200)
                self.mainlogic.videodata.buttonlist[self.mainlogic.videodata.result[0][0]].setStyleSheet('background:black;''background-image:url(folder.png)')
                self.mainlogic.videodata.buttonlist[self.mainlogic.videodata.result[0][0]].show()

                self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].setGeometry(100+(300*(self.mainlogic.videodata.result[0][0]-4))+40,350*2,200,200)
                self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].setText(self.mainlogic.check.lineedit.text())
                self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].setStyleSheet('color:white;')
                self.mainlogic.videodata.buttonlabellist[self.mainlogic.videodata.result[0][0]].show()

        
        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=Mainlogic()
    sys.exit(app.exec_())