from PyQt5 import QtCore, QtGui, QtWidgets


class MiniplayerUi:
    def __init__(self):
        self.miniplayer_x=300
        self.miniplayer_y=200
        self.setupUi()
    def setupUi(self):
        self.miniplayer=QtWidgets.QWidget()
        self.label=QtWidgets.QLabel(self.miniplayer)
        self.label.setGeometry(0,0,200,200)
        self.label.setText('sdaf')