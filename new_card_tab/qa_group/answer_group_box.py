import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection
from common.my_group_box import MyGroupBox


class AnswerGroupBox(MyGroupBox):
    def __init__(self):
        super().__init__()
        answer_label = QLabel()
        answer_label.setText("Answer  ")
        answer_textbox = QPlainTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(answer_label)
        vbox.addWidget(answer_textbox)
        self.setLayout(vbox)
