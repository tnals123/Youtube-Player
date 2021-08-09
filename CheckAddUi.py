from PyQt5 import QtCore, QtGui, QtWidgets
import videodata
from PyQt5.QtWidgets import QMessageBox
class CheckAddPlaylist(object):
    def __init__(self):

        self.msg=QMessageBox()
        self.data=videodata.VideoData()
        self.data.FindCount()
        self.mainwindow=QtWidgets.QMainWindow()
        self.mainwindow.hide()
        self.SetupUi()

    def SetupUi(self):
        self.mainwindow.resize(500,500)

        self.paper=QtWidgets.QWidget(self.mainwindow)
        self.paper.setGeometry(0,0,500,500)
        self.paper.setStyleSheet('background:#1C1C1C;')

        self.label=QtWidgets.QLabel(self.paper)
        self.label.setGeometry(40,40,205,22)
        self.label.setText('재생목록 이름을 정해 주세요')
        self.label.setStyleSheet('color:white;''border: 1px solid red;')

        self.lineedit=QtWidgets.QLineEdit(self.paper)
        self.lineedit.setGeometry(40,80,300,22)
        self.lineedit.setText('재생목록'+str(self.data.result[0][0]))
        self.lineedit.setStyleSheet('background:white;')
        

        self.addpushbutton=QtWidgets.QPushButton(self.paper)
        self.addpushbutton.setGeometry(150,400,80,30)
        self.addpushbutton.setText('추가하기')
        self.addpushbutton.setStyleSheet('color:white;''background:black;''border: 1px solid red;')

        self.cancelbutton=QtWidgets.QPushButton(self.paper)
        self.cancelbutton.setGeometry(280,400,80,30)
        self.cancelbutton.setText('취소')
        self.cancelbutton.setStyleSheet('color:white;''background:black;''border: 1px solid red;')
    

    def openmessage4(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('재생목록 생성 실패!')
        self.msg.setText('재생목록 중 같은 이름이 있습니다.')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()
