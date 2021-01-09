import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QVBoxLayout
from common.my_group_box import MyGroupBox
from common.my_qplaintextedit import MyQPlainTextEdit


answer_textbox = None


class AnswerGroupBox(MyGroupBox):
    def __init__(self):
        super().__init__()
        answer_label = QLabel()
        answer_label.setText("Answer  ")

        global answer_textbox
        answer_textbox = MyQPlainTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(answer_label)
        vbox.addWidget(answer_textbox)
        self.setLayout(vbox)

    # def cursor_event(self):
    #     if (answer_textbox.hasFocus()):
    #         # instance of QRect
    #         qrect = QtCore.QRect(QtGui.QTextCursor())
    #         qpainter = QtGui.QPainter(answer_textbox.viewport())
    #         qpainter.fillRect(qrect, QtGui.QColor(255, 0, 0, 255))
