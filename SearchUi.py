from PyQt5 import QtCore, QtGui, QtWidgets


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