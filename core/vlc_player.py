"""The module contains class that uses python-vlc to play video file"""
import vlc
from PyQt5 import QtWidgets


class VlcPlayer(QtWidgets.QMainWindow):
    """The class provides simple interface to control video stream"""
    def __init__(self, filepath: str) -> None:
        super().__init__()
        self.filepath = filepath
        self.instance = vlc.Instance([b"--fullscreen"])
        self.media = self.instance.media_player_new(self.filepath)
        # PyQt initialisation
        self.videoframe = QtWidgets.QFrame()
        self.videoframe.showFullScreen()
        # self.showMaximized()
        # self.showFullScreen()
        # self.media.set_fullscreen(True)
        self.widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.widget)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.videoframe)
        self.widget.setLayout(self.layout)
        self.media.toggle_fullscreen()

    def open(self, filepath: str) -> None:
        self.filepath = filepath
        media = self.instance.media_new(self.filepath)
        self.media.set_media(media)

    def play(self) -> None:
        self.media.set_xwindow(int(self.videoframe.winId()))
        self.media.play()

    def toggle_fullscreen(self) -> None:
        self.media.toggle_fullscreen()

    def pause(self) -> None:
        self.media.pause()

    def stop(self) -> None:
        self.media.stop()
