import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog, \
        QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection
#from .subject_combobox import SubjectComboBox
#from .add_new_subject_dialog import AddNewSubjectDialog
from .source_group.subject_group_box import SubjectGroupBox
from .source_group.url_book_tab_group_box import URLBookTab


class SourceGroupBox(QGroupBox):
    def __init__(self, title: str):
        super().__init__()
        self.setTitle(title)
        self.setupUi()
        # self.add_new_card_button.clicked.connect(self.open_dialog)

    def setupUi(self):
        #self.subject_combo = SubjectComboBox()

        # TODO add subject button (push button)
        #self.add_new_card_button = QPushButton("Add New Subject")
        subject_group_box = SubjectGroupBox()
        url_book_group_box = URLBookTab()

        # self.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.buttonBox = QtWidgets.QDialogButtonBox()
        # self.buttonBox.addButton("Help", QtWidgets.QDialogButtonBox.HelpRole)
        self.buttonBox.addButton(
            "Submit", QtWidgets.QDialogButtonBox.AcceptRole)
        self.buttonBox.addButton(
            "Cancel", QtWidgets.QDialogButtonBox.RejectRole)

        gbox = QGridLayout()
        gbox.addWidget(subject_group_box)
        gbox.addWidget(url_book_group_box)
        gbox.addWidget(self.buttonBox)

        self.setLayout(gbox)

    def open_dialog(self):
        add_dialog = AddNewSubjectDialog()
        add_dialog.exec_()
