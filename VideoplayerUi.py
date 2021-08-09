from PyQt5 import QtCore, QtGui, QtWidgets


class Player:
    def __init__(self):
        self.setupUi()
    def setupUi(self):
        self.playerui=QtWidgets.QWidget()
        self.label=QtWidgets.QLabel(self.playerui)
        self.label.setGeometry(0,0,200,200)
        self.label.setText('asdfasdfasdf')