import sys
import flash_cards_resource
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QDialog, QTabWidget, \
    QVBoxLayout, QDialogButtonBox, QLabel, QPlainTextEdit, QGroupBox, QHBoxLayout, \
    QPlainTextEdit, QLabel, QListWidget, QPushButton, QComboBox, QDialog

from PyQt5.QtGui import QIcon
from new_card_tab.new_card_tab import NewCardTab
from test_tab.test_tab import TestTab
from new_card_tab.new_card_tab import NewCardTab


class TabWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Flash Cards')
        self.setWindowIcon(QIcon(':/images/images/idle.ico'))

        tab_widget = QTabWidget()
        tab_widget.addTab(TestTab(), "Test")
        tab_widget.addTab(NewCardTab(), "New Card")

        vbox = QVBoxLayout()
        vbox.addWidget(tab_widget)
        self.setLayout(vbox)
        self.setFixedSize(640, 480)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tab_widget = TabWidget()
    tab_widget.show()
    app.exec_()
