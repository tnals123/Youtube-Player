from PyQt5 import QtCore, QtGui, QtWidgets
import sys
class SearchVideoUi(object):
    def __init__(self):
        self.SetUpUi()
        self.mainwindow.resize(self.searchvideoui_x,self.searchvideoui_y)
        self.mainwindow.show()

    def SetUpUi(self):
        self.searchvideoui_x=700
        self.searchvideoui_y=800

        self.mainwindow=QtWidgets.QMainWindow()

        self.paper=QtWidgets.QWidget(self.mainwindow)
        self.paper.setGeometry(0,0,700,800)
        self.background=QtWidgets.QLabel(self.paper)
        self.background.setGeometry(0,0,700,800)
        self.background.setStyleSheet('background:black;')


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    asdf=SearchVideoUi()
    sys.exit(app.exec_())