import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection
from .subject_combobox import SubjectComboBox


class SourceGroupBox(QGroupBox):
    def __init__(self, title: str):
        super().__init__()
        self.setTitle(title)

        subject_combo = SubjectComboBox()
        hbox = QHBoxLayout()
        hbox.addWidget(subject_combo)

        self.setLayout(hbox)
