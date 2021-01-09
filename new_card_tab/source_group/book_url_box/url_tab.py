import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog, \
    QLineEdit

from PyQt5.QtGui import QIcon
from common.my_qplaintextedit import MyQPlainTextEdit
# from db.db_script import SqliteConnection
# from .qa_group_box import QAGroupBox
# from .source_group_box import SourceGroupBox


class URLTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):

        # url: QLabel, QLineEdit
        self.url_label = QLabel("URL")
        self.url_input = MyQPlainTextEdit()
        self.url_note_label = QLabel("Note")
        self.url_note_input = MyQPlainTextEdit()
        self.url_input.setMaximumHeight(120)
        self.url_note_input.setMaximumHeight(120)

        vbox = QVBoxLayout()
        vbox.addWidget(self.url_label)
        vbox.addWidget(self.url_input)
        vbox.addWidget(self.url_note_label)
        vbox.addWidget(self.url_note_input)
        self.setLayout(vbox)
