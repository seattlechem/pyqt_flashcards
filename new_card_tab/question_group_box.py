import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection


class QuestionGroupBox(QGroupBox):
    def __init__(self):
        super().__init__()

        question_label = QLabel()
        question_label.setText("Question")
        question_textbox = QPlainTextEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(question_label)
        vbox.addWidget(question_textbox)
        self.setLayout(vbox)
