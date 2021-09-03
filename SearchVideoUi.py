from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class SearchVideoUi(object):
    def __init__(self):
        self.SetUpUi()
        self.mainwindow.resize(self.searchvideoui_x,self.searchvideoui_y)
        self.mainwindow.move(1200,0)
        self.mainwindow.hide()

    def SetUpUi(self):
        self.searchvideoui_x=700
        self.searchvideoui_y=900

        self.mainwindow=QtWidgets.QMainWindow()

        self.paper=QtWidgets.QWidget(self.mainwindow)
        self.paper.setGeometry(0,0,700,900)

        self.background=QtWidgets.QLabel(self.paper)
        self.background.setGeometry(0,0,700,900)
        self.background.setStyleSheet('background:black;')

        self.backbutton=QtWidgets.QPushButton(self.paper)
        self.backbutton.setGeometry(300,830,100,30)
        self.backbutton.setText('돌아가기')
        self.backbutton.setStyleSheet('background:black;''border-color:red;''border-style:dashed;''border-width:2px;''color:white;')

        self.scrollarea=QtWidgets.QScrollArea(self.paper)
        self.scrollarea.setGeometry(0,0,700,780)

        self.videolist=QtWidgets.QWidget(self.scrollarea)
        self.videolist.setGeometry(0,0,698,1800)
        self.videolist.setStyleSheet('background: #1C1C1C;')

        self.scrollarea.setWidget(self.videolist)


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=SearchVideoUi()
    sys.exit(app.exec_())