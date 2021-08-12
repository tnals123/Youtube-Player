import sys

import vlc

from PyQt5 import QtCore, QtGui, QtWidgets


class Player(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Player, self).__init__(parent)
        self.setWindowTitle("Media Player")
        # creating a basic vlc instance
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        ##########video frame
        self.videoframe = QtWidgets.QFrame(
            frameShape=QtWidgets.QFrame.Box, frameShadow=QtWidgets.QFrame.Raised
        )

        if sys.platform.startswith("linux"):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.videoframe.winId())

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        lay.addWidget(self.videoframe)

        filename = "Zoom 2021-04-24 09-26-22.mp4"
        media = self.instance.media_new(filename)
        self.mediaplayer.set_media(media)
        self.mediaplayer.play()


