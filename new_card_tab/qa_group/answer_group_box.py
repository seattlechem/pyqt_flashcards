import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QPlainTextEdit, QVBoxLayout
from common.my_group_box import MyGroupBox


answer_textbox = None


class AnswerGroupBox(MyGroupBox):
    def __init__(self):
        super().__init__()
        answer_label = QLabel()
        answer_label.setText("Answer  ")

        global answer_textbox
        answer_textbox = QPlainTextEdit()
        answer_textbox.setStyleSheet("color: rgb(242, 242, 242);\
            background-color: rgb(128, 128, 128);")
        answer_textbox.setStyleSheet(
            """QPlainTextEdit::focus {background-color: blue;}""")
        answer_textbox.setCursorWidth(2)
        answer_textbox.setFont(QFont('Consolas', 13))
        answer_textbox.viewport().setCursor(QtCore.Qt.ArrowCursor)
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
