import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection
from .qa_group.qa_group_box import QAGroupBox
from .source_group_box import SourceGroupBox


class NewCardTab(QWidget):
    def __init__(self):
        super().__init__()

        # Add GroupBox: QA & Source
        hbox = QHBoxLayout()
        qa_groupbox = QAGroupBox("Question and Answer")
        source_groupbox = SourceGroupBox("Source")

        hbox.addWidget(qa_groupbox)
        hbox.addWidget(source_groupbox)

        self.setLayout(hbox)
