from PyQt5 import QtCore
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QFont


class MyQPlainTextEdit(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setStyleSheet("color: white; background-color: black;")
        # self.setStyleSheet(
            # """QPlainTextEdit:::focus {background-color: blue;}""")
        self.setCursorWidth(2)
        self.setFont(QFont('Consolas', 13))
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)
