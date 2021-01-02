import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog, \
        QLineEdit

from PyQt5.QtGui import QIcon
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
        self.url_input = QPlainTextEdit()
        self.url_note_label = QLabel("Note")
        self.url_note_input = QPlainTextEdit()
        self.url_input.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.url_input.setMaximumHeight(120)
        self.url_note_input.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.url_note_input.setMaximumHeight(120)


        vbox = QVBoxLayout()
        vbox.addWidget(self.url_label)
        vbox.addWidget(self.url_input)
        vbox.addWidget(self.url_note_label)
        vbox.addWidget(self.url_note_input)
        self.setLayout(vbox)
