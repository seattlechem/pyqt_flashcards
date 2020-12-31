import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QListWidget, QPushButton, QComboBox, QDialog, QLineEdit, QGridLayout

from PyQt5.QtGui import QIcon
from .search_book_dialog import SearchBookDialog
# from db.db_script import SqliteConnection
# from .qa_group_box import QAGroupBox
# from .source_group_box import SourceGroupBox

book_title = None
book_author = None
book_year = None
book_note = None

class BookTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.search_book_button_action_connection()

    def setupUi(self):

        # title: QLabel, QLineEdit
        self.title_label = QLabel("Title")
        global book_title
        self.title_input = QLineEdit()
        book_title = self.title_input

        # author
        self.author_label = QLabel("Author")
        global book_author
        self.author_input = QLineEdit()
        book_author = self.author_input

        # year
        self.year_label = QLabel("Year")
        global book_year
        self.year_input = QLineEdit()
        book_year = self.year_input

        # note QPlainTextEdit
        self.note_label = QLabel("Note")
        global book_note
        self.note_input = QPlainTextEdit()
        self.note_input.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.note_input.setMaximumHeight(100)
        book_note = self.note_input

        # TO btn_search_book
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

    def search_book_button_action_connection(self):
        self.search_book_button.clicked.connect()

    def open_search_book_dialog(self):
        # TODO
        # add a logic to open a dialog where users can search for book
        # in db by title or author
        # if book exists users does not need to reenter the book info
        #
        add_dialog = SearchBookDialog()
        add_dialog.exec_()
