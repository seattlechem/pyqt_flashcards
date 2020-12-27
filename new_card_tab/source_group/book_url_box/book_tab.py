import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QListWidget, QPushButton, QComboBox, QDialog, QLineEdit, QGridLayout

from PyQt5.QtGui import QIcon
# from db.db_script import SqliteConnection
# from .qa_group_box import QAGroupBox
# from .source_group_box import SourceGroupBox


class BookTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):

        # title: QLabel, QLineEdit
        self.title_label = QLabel("Title")
        self.title_input = QLineEdit()

        # author
        self.author_label = QLabel("Author")
        self.author_input = QLineEdit()

        # year
        self.year_label = QLabel("Year")
        self.year_input = QLineEdit()

        # note QPlainTextEdit
        self.note_label = QLabel("Note")
        self.note_input = QPlainTextEdit()
        self.note_input.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.note_input.setMaximumHeight(100)

        #TO btn_search_book
        self.search_book_button = QPushButton("Search Book")
        self.search_book_button.setMinimumWidth(100)


        vbox = QVBoxLayout()
        vbox.addWidget(self.title_label)
        vbox.addWidget(self.title_input)
        vbox.addWidget(self.author_label)
        vbox.addWidget(self.author_input)
        vbox.addWidget(self.year_label)
        vbox.addWidget(self.year_input)
        vbox.addWidget(self.note_label)
        vbox.addWidget(self.note_input)
        vbox.addWidget(self.search_book_button)
        self.setLayout(vbox)