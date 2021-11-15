from random import randrange as rr
from Graphics import Graphui
from PyQt5.QtWidgets import QWidget, QApplication
from PIL import Image as img


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        Graphui(self).Graphinit()


a = QApplication([]), Main()
a[1].show(), a[0].exec()