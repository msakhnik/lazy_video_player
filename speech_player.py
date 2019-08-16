"""Player executer"""
import time
import sys
from argparse import ArgumentParser
from core.vlc_player import VlcPlayer
from PyQt5 import QtWidgets, QtGui, QtCore


def main() -> None:
    parser = ArgumentParser(description="Speech player.")
    parser.add_argument("--video", dest="video", help="Path to media file")
    options = parser.parse_args()
    app = QtWidgets.QApplication(sys.argv)
    player = VlcPlayer(options.video)
    player.resize(640, 480)
    player.show()
    player.play()
    counter = 0
    while True:
        app.sync()
        counter += 1
        time.sleep(0.1)
        # if player.media.is_playing() == 0:
        #     break
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
