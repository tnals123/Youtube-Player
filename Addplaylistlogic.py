import videodata
from PyQt5 import QtCore, QtGui, QtWidgets

class AddLogic:


    def __init__(self):
        self.data=videodata.VideoData()
    
    def addplaylist(self,event,name,paper,name2):
        self.data.FindCount()
        print('함수작동')
        self.name=name
        self.name2=name2
        self.mypaper=paper
        self.name=QtWidgets.QPushButton(self.mypaper)
        self.name.setGeometry(self.data.result[0][0]*100,350,200,200)
        self.name.setStyleSheet('background:white;')
        self.name2.setGeometry(100+(300*self.data.result[0][0]),350,200,200)
        

    
