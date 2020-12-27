import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection
from .question_group_box import QuestionGroupBox
from .answer_group_box import AnswerGroupBox


class QAGroupBox(QGroupBox):
    def __init__(self, title: str):
        super().__init__()
        self.setTitle(title)

        question_groupbox = QuestionGroupBox()
        # question_groupbox.setFlat(True)
        # question_groupbox.setStyleSheet("border:0;")
        answer_groupbox = AnswerGroupBox()

        vbox = QVBoxLayout()
        vbox.addWidget(question_groupbox)
        vbox.addWidget(answer_groupbox)
        self.setLayout(vbox)
        self.setFixedSize(300, 500)
