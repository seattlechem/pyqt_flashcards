import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from db.db_script import SqliteConnection
from .test_ui import TestUi


class TestTab(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.pushButton = QtWidgets.QPushButton()
        self.pushButton.setGeometry(QtCore.QRect(530, 120, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton()
        self.pushButton_2.setGeometry(QtCore.QRect(530, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.setGeometry(QtCore.QRect(160, 390, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton()
        self.pushButton_3.setGeometry(QtCore.QRect(260, 390, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(QtCore.QRect(476, 20, 101, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 60, 421, 291))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton_4 = QtWidgets.QPushButton()
        self.pushButton_4.setGeometry(QtCore.QRect(530, 330, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.comboBox_2 = QtWidgets.QComboBox()
        self.comboBox_2.setGeometry(QtCore.QRect(50, 390, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setGeometry(QtCore.QRect(180, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setGeometry(QtCore.QRect(110, 20, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setGeometry(QtCore.QRect(250, 20, 47, 13))
        self.label_5.setObjectName("label_5")

        hbox = QHBoxLayout()
        componenets = [
            self.pushButton,
            self.pushButton_2,
            self.pushButton_3,
            self.pushButton_4,
            self.comboBox,
            self.comboBox_2,
            self.label,
            self.label_2,
            self.label_3,
            self.label_4,
            self.label_5,
            self.plainTextEdit
        ]

        self.add_widgets_to_layout(hbox, componenets)

        self.setLayout(hbox)

        self.retranslateUi()

    def add_widgets_to_layout(self, layout_box, components: list):
        for item in components:
            layout_box.addWidget(item)

    def retranslateUi(self):
        self.pushButton.setText("Pass")
        self.pushButton_2.setText("Fail")
        self.pushButton_3.setText("Start")
        self.label.setText("URL")
        self.label_2.setText("Last Seen Date")
        self.pushButton_4.setText("Flip")
        self.label_3.setText("Pass Rate")
        self.label_4.setText("TextLabel")
        self.label_5.setText("TextLabel")
