from PyQt5 import QtCore, QtGui, QtWidgets


class SearchUi:
    def __init__(self):
        self.searchui_x=600
        self.searchui_y=600
        self.setupUi()
    def setupUi(self):
        self.searchui=QtWidgets.QWidget()
        self.label=QtWidgets.QLabel(self.searchui)
        self.label.setGeometry(0,0,200,200)
        self.label.setText('seacifk')