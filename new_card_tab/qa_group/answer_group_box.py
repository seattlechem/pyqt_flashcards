import sys
import flash_cards_resource
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

        vbox = QVBoxLayout()
        vbox.addWidget(answer_label)
        vbox.addWidget(answer_textbox)
        self.setLayout(vbox)
