from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon, QFont

class MyQLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Consolas', 12))
